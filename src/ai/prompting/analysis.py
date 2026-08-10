"""Prompt construction for profile-driven content analysis."""

from ...models import ContentItem, InterestConfig
from ...processing.profiles import LoadedProfile
from .common import EVIDENCE_RULES, UNTRUSTED_INPUT_RULE

ANALYSIS_RULES = f"""You are a content curator evaluating an item under the supplied processing profile.

- {UNTRUSTED_INPUT_RULE}
- Base the analysis only on the supplied item and its metadata.
{EVIDENCE_RULES}
- Apply the profile's evaluation policy consistently."""


def _interest_policy_prompt(interests: InterestConfig | None) -> str:
    if interests is None or not interests.enabled:
        return ""

    bucket_catalog = "\n".join(
        f"- `{bucket_id}` ({bucket.name}; target {bucket.target_count}): "
        f"{bucket.description} Priority topics: "
        f"{', '.join(bucket.priority_topics) or 'none specified'}."
        for bucket_id, bucket in interests.buckets.items()
    )
    include_topics = ", ".join(interests.include_topics) or "none specified"
    exclude_topics = ", ".join(interests.exclude_topics) or "none specified"
    hard_rejects = "\n".join(
        f"- {rule}" for rule in interests.hard_reject_rules
    ) or "- None configured."
    return f"""

# Personalized interest policy

Audience: {interests.audience or 'Not specified.'}
Priority topics: {include_topics}
Excluded topics: {exclude_topics}

Available interest buckets:
{bucket_catalog}

Hard rejection rules:
{hard_rejects}

Evaluate personal relevance separately from general news importance:
- `relevance_score`: direct fit for the configured audience and priority topics.
- `actionability_score`: how readily the reader can try, apply, build with, or make a decision from the item.
- `video_score`: suitability for a concise landscape explainer with concrete visuals and a clear takeaway.
- Set `rejection_reason` to a concise non-empty reason when an excluded topic or hard rejection rule applies; otherwise use null.
- For accepted items, choose exactly one configured `interest_bucket`. For rejected items, use null.
"""


def analysis_system_prompt(
    profile: LoadedProfile,
    interests: InterestConfig | None = None,
) -> str:
    interest_policy = _interest_policy_prompt(interests)
    interest_contract = ""
    if interests is not None and interests.enabled:
        interest_contract = """,
  "interest_bucket": "<configured bucket ID or null when rejected>",
  "relevance_score": <number from 0 to 10>,
  "actionability_score": <number from 0 to 10>,
  "video_score": <number from 0 to 10>,
  "rejection_reason": "<reason or null>\""""

    return f"""{ANALYSIS_RULES}

# Profile policy

{profile.analysis_prompt}
{interest_policy}

# Output contract

Return valid JSON only:
{{
  "score": <number from 0 to 10>,
  "reason": "<concise explanation>",
  "summary": "<one-sentence summary>",
  "tags": ["<tag>", "..."]{interest_contract}
}}"""


def analysis_user_prompt(
    item: ContentItem,
    content_section: str,
    discussion_section: str,
) -> str:
    return f"""Analyze the following content.

Title: {item.title}
Source: {item.source_type.value}
Author: {item.author or "Unknown"}
URL: {item.url}
{content_section}
{discussion_section}"""
