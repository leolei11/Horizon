---
layout: default
title: "Horizon Summary: 2026-11-01 (ZH)"
date: 2026-11-01
lang: zh
---

> 从 55 条内容中筛选出 20 条重要资讯。

---

**科技新闻**
1. [Memdoor：由 5 个 Qwen3.8-27B 模型组成的团队在 LiveCodeBench Hard 上击败 Fable 5](#item-tech-news-1) ⭐️ 8.0/10
2. [HackerTube：基于 Hacker News 历年评论推荐视频构建的 YouTube 替代前端](#item-tech-news-2) ⭐️ 8.5/10
3. [JavaScript 框架的 AI 成本](#item-tech-news-3) ⭐️ 6.5/10
4. [巴西法院因法律文书中的提示词注入对律师实施制裁](#item-tech-news-4) ⭐️ 5.0/10

**科技博客**
1. [简历小节标题：ATS 解析器究竟能识别哪些？](#item-tech-blog-1) ⭐️ 8.2/10
2. [你能解释一下你刚 shipped 的代码吗？](#item-tech-blog-2) ⭐️ 8.0/10
3. [自定义 Python 类中的操作符与函数重载](#item-tech-blog-3) ⭐️ 7.5/10
4. [我们是如何接管 ChatGPT 账号的：一则沙箱漏洞剖析](#item-tech-blog-4) ⭐️ 8.5/10
5. [datasette-llm 0.1a9 版本发布](#item-tech-blog-5) ⭐️ 8.5/10
6. [从 600 万到 6000 万美元：软件咨询公司规模化的 7 条核心经验](#item-tech-blog-6) ⭐️ 7.0/10
7. [高级远程软件工程师职位精选：4 个岗位年薪超 15 万美元（11 月 1 日）](#item-tech-blog-7) ⭐️ 7.0/10
8. [Socket Programming in Python \(Guide\)](#item-tech-blog-8) ⭐️ 6.0/10
9. [Freelance Taxes Feel Random Until You Do This One Calculation Every Quarter](#item-tech-blog-9) ⭐️ 7.2/10
10. [How to Get Your First Opportunity Without Work Experience](#item-tech-blog-10) ⭐️ 6.5/10
11. [Only 12% of executives expect AI to raise wages. That number is a choice.](#item-tech-blog-11) ⭐️ 6.0/10
12. [How to Build a Python GUI Application With wxPython](#item-tech-blog-12) ⭐️ 5.5/10
13. [Using the Python zip\(\) Function for Parallel Iteration](#item-tech-blog-13) ⭐️ 5.0/10
14. [Generating Random Data in Python \(Guide\)](#item-tech-blog-14) ⭐️ 5.0/10
15. [Documenting Python Code: A Complete Guide](#item-tech-blog-15) ⭐️ 5.0/10
16. [Recursion in Python: An Introduction](#item-tech-blog-16) ⭐️ 5.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Memdoor：由 5 个 Qwen3.8-27B 模型组成的团队在 LiveCodeBench Hard 上击败 Fable 5](https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve) ⭐️ 8.0/10

Memdoor 展示了如何通过一个由多个本地 Qwen 模型组成的团队在 LiveCodeBench 上击败传统基准，并提供了完整的解题工作流源码。它解决了单模型在复杂编程基准中泛化能力不足的问题，通过多模型协作来提升本地 AI 的代码解题表现。对于希望探索本地 Agent 架构和多模型工作流的独立开发者而言，该项目具备极高的参考价值。项目通过开源代码直观展示了如何构建轻量级的多模型解题协作团队。

hackernews · guregodevo · 10月31日 22:46 · [社区讨论](https://news.ycombinator.com/item?id=50320995)

**「背景」** 本地模型在应对复杂基准测试时，往往难以与闭源的超大规模模型相抗衡，社区一直在积极探索如何让便宜的本地模型通过组合达到高阶水平。

**「实际影响」** 该项目为开发者提供了一个具体的开源多模型协作解题范例，证明了通过合理的工作流编排，本地模型也能在硬核编程测试中取得亮眼成绩。

**「下一步」** 前往 GitHub 的 memdoor 仓库查看 team-solve 工作流示例，了解具体的提示词与编排逻辑。

**「社区讨论」** Hacker News 评论者讨论了构建本地模型蜂群（swarms）的挑战，指出虽然调整 harness 优化单一 eval 比较容易，但要实现跨任务的通用泛化则非常困难；同时也有人质疑评测样本规模以及是否借助了 Claude 进行文本编写。

**标签**: `#Agent`, `#GitHub 开源`, `#API 集成`

---

<a id="item-tech-news-2"></a>
### [HackerTube：基于 Hacker News 历年评论推荐视频构建的 YouTube 替代前端](https://karpathy.bearblog.dev/hacker-tube/) ⭐️ 8.5/10

HackerTube 是一个仿 YouTube 界面布局的视频聚合平台，收录了自 2007 年以来在 Hacker News 评论中被推荐的 6,000 多个视频。它解决了传统视频平台过度依赖算法、充斥着互动陷阱和成瘾优化的痛点，为用户提供了一个高信噪比、能够真正开阔视野的内容浏览空间。对于独立开发者和产品设计爱好者而言，该项目展示了如何通过社区高质量的文本数据倒逼出独特的前端产品。用户可以通过清爽的聚合界面直接发现那些真正令人惊叹的优质视频内容。

hackernews · karpathy · 10月31日 19:56 · [社区讨论](https://news.ycombinator.com/item?id=50319510)

**「背景」** 互联网上的主流视频平台大多围绕用户的点击率和互动时长进行算法优化，导致信息茧房和低质量诱饵泛滥。

**「实际影响」** 该项目为广大用户提供了一个清爽的、基于人工高质量推荐的替代浏览体验，激发了社区对去中心化与防成瘾产品设计的思考。

**「下一步」** 访问 hackertube.org 亲自体验由 Hacker News 评论精选出来的视频流内容。

**「社区讨论」** Hacker News 评论者对这种没有算法焦虑、摆脱成瘾优化的浏览体验给予了高度评价，认为它找回了互联网早期用于拓展视野和启发思考的初心。

**标签**: `#独立开发`, `#产品设计`, `#SaaS架构`

---

<a id="item-tech-news-3"></a>
### [JavaScript 框架的 AI 成本](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/) ⭐️ 6.5/10

本文探讨了在 AI 辅助编程（vibe-coding）时代，使用现代 JavaScript 框架所带来的实际维护成本与隐性影响。它剖析了框架在企业和工程团队中如何被用于简化招聘或规避深度培训，并指出在 AI 时代依然可以通过实证来指导技术选型而非单纯依靠直觉。对于前端开发者和技术决策者来说，它提供了一个审视现代前端框架复杂性的全新视角。文章倡导在面对繁杂的前端生态时，应当基于具体的证据进行理性评估。

hackernews · luu · 11月1日 06:06 · [社区讨论](https://news.ycombinator.com/item?id=50323088)

**「背景」** 随着 AI 编码工具的普及，开发者生产代码的速度大幅提升，但随之而来的框架复杂性和维护成本也逐渐浮出水面。

**「实际影响」** 促使开发者和工程团队反思现代前端框架带来的真实回报，避免盲目追逐技术潮流而引入不必要的维护负担。

**「下一步」** 阅读原文，了解作者在 AI 时代评估和选择前端框架的具体衡量维度。

**「社区讨论」** Hacker News 社区就框架存在的意义展开了热烈讨论，部分评论指出框架在很大程度上是为了降低企业的招聘和候选人筛选门槛，缓解“非我所创”（Invented Here）综合征。

**标签**: `#前端`, `#AI 编码`

---

<a id="item-tech-news-4"></a>
### [巴西法院因法律文书中的提示词注入对律师实施制裁](https://jetstream.security/insights/brazilian-court-sanctions-prompt-injection-filing/) ⭐️ 5.0/10

该安全热点报道了巴西法院因法律文书内包含提示词注入（Prompt Injection）而对涉事律师进行制裁的事件。它直观展现了将不受信任的外部文档直接喂给 AI 系统所带来的安全风险，对 AI 应用安全及 API 注入防御具有重要的现实参考意义。相关安全建议指出，在处理具有对抗意图的内容时，可通过将文档转为照片并运行 OCR 来清除潜在的隐性元数据。对于构建 AI 工作流的开发者和法务技术人员而言，这是一个必须重视的安全警示。

hackernews · doodlesdev · 11月1日 02:19 · [社区讨论](https://news.ycombinator.com/item?id=50322173)

**「背景」** 随着生成式 AI 被广泛应用于各行各业，如何防范恶意提示词注入攻击已成为亟待解决的法律与技术难题。

**「实际影响」** 该案件为 AI 在司法及其他合规场景中的安全性敲响了警钟，促使开发者与机构重新审视文档输入管道的安全性。

**「下一步」** 在处理外部不可信来源的文本或文件时，排查并增强应用程序的输入验证与清洗管道，防止隐式提示词注入。

**「社区讨论」** 社区评论讨论了广告和社交媒体行业如何通过微妙的操纵影响人类行为，并将此与提示词注入进行了类比。同时，有安全建议指出可以通过将文档转换为照片并运行 OCR 的方式来剥离不可见的元数据。

**标签**: `#AI 安全`, `#Prompt Injection`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [简历小节标题：ATS 解析器究竟能识别哪些？](https://dev.to/muhammadalimughal/resume-section-headings-what-ats-parsers-recognize-4jgn) ⭐️ 8.2/10

本文分析了 ATS（简历自动解析系统）如何识别简历中的各个模块，并指出了创意型、带样式修饰的标题容易引发解析失败的问题。它直接解决了求职者精心排版的简历在进入系统时被错误归类或字段丢失的痛点。文章通过对标准、创意和加粗间距三种标题样式的实际测试，给出了明确的避坑建议与常规命名指南。任何希望通过自动化招聘系统高效筛选的求职者和求职开发者都应该关注此文。

rss · Dev.to Career \(Resume &amp; Interview\) · 11月1日 14:16

**「背景」** ATS 解析器在提取具体的工作经历、学历或技能之前，必须先根据标题文本将文本流切分为不同的段落和小节。

**「实际影响」** 采用传统的常规标题（如 Work Experience、Education、Skills）能显著降低解析错误率，确保候选人的履历数据能够准确映射到招聘者的后台表单中。

**「下一步」** 检查个人简历的小节标题，将花哨的自定义命名（如“Where I Made an Impact”）替换为标准的“Work Experience”等传统名称。

**标签**: `#AI 求职`, `#职业发展`

---

<a id="item-tech-blog-2"></a>
### [你能解释一下你刚 shipped 的代码吗？](https://dev.to/kayashaolu/can-you-explain-what-you-shipped-mfc) ⭐️ 8.0/10

本文探讨了在使用 AI 代理（Agent）辅助编程时，开发者容易失去对代码理解的隐性风险，并提出了通过主动询问 AI 原理与测试来保持代码掌控力的实操建议。它解决了在 vibe-coding 时代“测试虽通过、却对底层原理一无所知”的效率陷阱。文章结合最新的学术研究成果，给出了让 AI 解释原因、展示测试并在接受方案前进行严格复核的具体工作流。对于每天重度依赖 AI 编写代码、希望确保自己能独立答辩并掌握架构的全栈开发者与工程师来说，这篇文章非常值得一读。

rss · Dev.to Career \(Resume &amp; Interview\) · 11月1日 14:01

**「背景」** 一项由 Anthropic 研究人员进行的随机对照试验显示，使用 AI 助手编程的开发者在随后关于代码的测验中得分低了 17 个百分点。

**「实际影响」** 盲目接受 AI 生成的代码会导致工程理解力退化，而通过强制要求 AI 给出解释和测试，则能有效兼顾开发速度与技术掌控力。

**「下一步」** 挑选最近由 AI 辅助构建的一个功能模块，尝试向队友大声复述并解释其背后的架构逻辑与原理。

**标签**: `#AI Agent`, `#全栈开发`, `#工程实践`, `#AI求职`

---

<a id="item-tech-blog-3"></a>
### [自定义 Python 类中的操作符与函数重载](https://realpython.com/operator-function-overloading/) ⭐️ 7.5/10

本文介绍了如何在自定义 Python 类中运用操作符重载，让用户自定义的对象能够无缝支持内置函数和标准运算符。它解决了自定义类在直接与其他 Python 内置类型交互时语法不够直观、代码复用率低的问题。文章详细讲解了相关魔术方法的具体实现，帮助开发者编写出更符合 Pythonic 风格的高质量代码。任何希望深入掌握 Python 面向对象高级特性的后端和全栈开发人员都应当阅读此文。

rss · Real Python \(Python &amp; Backend\) · 11月1日 14:00

**「背景」** Python 允许开发者通过定义特定的特殊方法（俗称魔术方法），赋予自定义类拦截和响应内置运算符及函数的能力。

**「实际影响」** 通过规范的操作符重载，自定义类的接口可以变得与 Python 内置类型高度一致，从而大幅提升代码的可读性与易用性。

**「下一步」** 尝试在自己的 Python 类中实现如 \`\_\_add\_\_\` 或 \`\_\_repr\_\_\` 等常见的魔术方法。

**标签**: `#Python`, `#后端开发`, `#代码规范`

---

<a id="item-tech-blog-4"></a>
### [我们是如何接管 ChatGPT 账号的：一则沙箱漏洞剖析](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/) ⭐️ 8.5/10

Parameter Labs 详细披露了一起针对 ChatGPT 的 Canvas/HTML 预览沙箱、MathLive 虚拟键盘及 YouTube oEmbed 漏洞链的攻击细节。它揭示了沙箱 iframe 之间未受限制的 \`postMessage\(\)\` 通信和 \`innerHTML\` 注入如何组合成复杂的跨站脚本（XSS）漏洞。通过这一攻击链，恶意构造的分享链接能够在不知情的情况下读取受害者的私有 API 数据并进行越权操作。对于关注 Web 安全、前端沙箱机制和 SaaS 架构防护的安全工程师及全栈开发者而言，这是一篇极其震撼的复盘警示。

rss · Simon Willison \(AI &amp; Tools\) · 10月31日 23:15

**「背景」** ChatGPT 允许通过沙箱化的 iframe 运行交互式自定义 HTML 应用（即早期的 Canvas、最新的 HTML 预览模式），而严密的沙箱隔离是确保其安全的核心防线。

**「实际影响」** 该漏洞展示了多重微小缺陷（如未受限的 \`postMessage\` 和宽松的 CSP 脚本域）如何被组合利用以实现完全的账号接管。

**「下一步」** 阅读 Parameter Labs 的原文报告，排查自身项目中 iframe 沙箱及 \`postMessage\` 接收逻辑是否存在类似的安全隐患。

**标签**: `#Web安全`, `#Frontend`, `#SaaS架构`

---

<a id="item-tech-blog-5"></a>
### [datasette-llm 0.1a9 版本发布](https://simonwillison.net/2026/Oct/31/datasette-llm/) ⭐️ 8.5/10

Simon Willison 推出了 datasette-llm 插件的 0.1a9 小幅更新，核心改进是自动捕获 LLM 工具包中配置的默认模型。它解决了以往在启动 Datasette Agent 时必须显式通过命令行参数指定模型名称的繁琐配置痛点。通过这一升级，开发者现在可以直接利用 \`uvx\` 一键拉起并运行 Datasette Agent。对于使用 Python、LLM 插件生态以及进行轻量级 AI 数据集探索的独立开发者而言，这提升了日常开发体验。

rss · Simon Willison \(AI &amp; Tools\) · 10月31日 22:10

**「背景」** Datasette Agent 依托底层的 LLM 插件生态，此前在初始化时需要用户手动传入默认的大模型标识符才能正常运行。

**「实际影响」** 简化了命令行启动流程，使得本地通过临时环境快速拉起 Agent 的工作流变得更加顺畅。

**「下一步」** 运行更新后的 \`uvx --with datasette-agent datasette ...\` 命令，体验免显式指定默认模型的便捷启动。

**标签**: `#开源项目`, `#Agent`, `#API 集成`, `#Python`

---

<a id="item-tech-blog-6"></a>
### [从 600 万到 6000 万美元：软件咨询公司规模化的 7 条核心经验](https://dev.to/ashkan/from-6m-to-60m-7-lessons-from-scaling-a-software-consulting-firm-2iai) ⭐️ 7.0/10

本文总结了一位合伙人在三年内将软件咨询公司营收从 600 万美元推高至 6000 万美元的七条实战经验。它直接解决了咨询公司和早期 SaaS 团队在盲目扩张时常遇到的利润率下降、交付能力跟不上销售以及定位模糊等核心痛点。文章涵盖了及早选择细分垂直定位、转向价值定价、将交付能力作为销售硬约束以及提前招聘管理者等关键决策。对于独立黑客（Indie Hacker）和正准备扩大业务规模的技术团队主管来说，这具有极高的参考价值。

rss · Dev.to Career \(Resume &amp; Interview\) · 11月1日 14:52

**「背景」** 在软件咨询和外包服务行业的快速增长期，如果没有规范的系统和明确的定位，企业很容易陷入交付危机和人才断层。

**「实际影响」** 这套经验帮助管理者建立起可重复的业务增长闭环，避免了盲目接单带来的信誉损耗和组织崩溃。

**「下一步」** 审视当前的业务管道，检查定位是否足够清晰并确保销售与交付团队的步调保持一致。

**标签**: `#saas`, `#business`, `#consulting`, `#indie-hacking`

---

<a id="item-tech-blog-7"></a>
### [高级远程软件工程师职位精选：4 个岗位年薪超 15 万美元（11 月 1 日）](https://dev.to/crackr/senior-remote-swe-roles-hiring-now-4-pay-150k-nov-1-3hf4) ⭐️ 7.0/10

本文汇总了多条面向海内外资深工程师的远程软件开发和 DevOps 岗位，包含具体的薪资范围与技术栈要求。它解决了求职者在海量招聘信息中搜寻高质量高薪远程岗位的痛点，提供了精准的岗位速递。文中涉及的公司涵盖 Wagmo、Klardaten、Lemon.io 及 DuckDuckGo 等，技术栈横跨 React、Python、Go、Java 与 AWS。对于正在积极寻找远程全栈或后端高薪机会的资深开发者来说，这是一份实用的招聘速览。

rss · Dev.to Career \(Resume &amp; Interview\) · 11月1日 15:00

**「背景」** 全球远程招聘市场高度分散，资深开发人员往往需要花费大量时间筛选匹配自身技术栈和薪资期望的真实岗位。

**「实际影响」** 为求职者直接对齐了薪资预期、地区限制以及主流技术栈（如 Python、Go、TypeScript 等），节省了搜寻时间。

**「下一步」** 访问 Crackr.dev 的远程岗位页面，查看感兴趣的具体公司并提交符合要求的简历申请。

**标签**: `#求职`, `#远程开发`

---

<a id="item-tech-blog-8"></a>
### [Socket Programming in Python \(Guide\)](https://realpython.com/python-sockets/) ⭐️ 6.0/10

介绍如何使用 Python 从零构建支持多连接的 socket 服务器与客户端。 来源内容补充：Build a Python socket server and client from scratch, then extend it to handle multiple connections at once without blocking.

rss · Real Python \(Python &amp; Backend\) · 10月31日 14:00

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#python`, `#backend`, `#networking`

---

<a id="item-tech-blog-9"></a>
### [Freelance Taxes Feel Random Until You Do This One Calculation Every Quarter](https://dev.to/jartan/freelance-taxes-feel-random-until-you-do-this-one-calculation-every-quarter-3hkb) ⭐️ 7.2/10

介绍了一种帮助自由职业者进行季度税务估算与规避罚款的四步计算法。 来源内容补充：&lt;p&gt;Freelance income is lumpy, but the IRS payment schedule is not. Four dates a year: April 15, June 15, September 15 and January 15. If you earn money without an employer withholding tax, you are the withholding department, and most of us run that department with a guess.&lt;/p&gt; &lt;p&gt;I used to guess like this: take last quarter&\#x27;s number, add a cushion, and hope. It works until a big invoice lands in one month, or a slow

rss · Dev.to Career \(Resume &amp; Interview\) · 11月1日 14:12

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#自由职业`, `#独立开发`

---

<a id="item-tech-blog-10"></a>
### [How to Get Your First Opportunity Without Work Experience](https://dev.to/ladipo_samuel_7cfaa827bf5/how-to-get-your-first-opportunity-without-work-experience-2aip) ⭐️ 6.5/10

分享了开发者在没有工作经验的情况下，如何通过聚焦垂直领域、持续产出和借助 AI 来争取职业机会。 来源内容补充：&lt;p&gt;Yesterday, I was a panelist at a tech event, and I was asked some questions which I was able to answer, but due to time constraints, I couldn&\#x27;t say everything. After the event, I had multiple people reach out asking different questions. Then I thought, instead of answering 30 people individually, let me actually write about this. I believe this will really help you, as it comes from what I have experienced, not ju

rss · Dev.to Career \(Resume &amp; Interview\) · 11月1日 14:52

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#求职`, `#职业发展`

---

<a id="item-tech-blog-11"></a>
### [Only 12% of executives expect AI to raise wages. That number is a choice.](https://dev.to/ganesh_sivakumar_359edfcd/only-12-of-executives-expect-ai-to-raise-wages-that-number-is-a-choice-3a02) ⭐️ 6.0/10

结合 WEF 与 OECD 报告分析高管对 AI 薪资与就业的预期，指出技能短缺与分配不均问题。 来源内容补充：&lt;p&gt;Ask ten executives what AI will do to their business and you get optimism. Ask the same executives what it will do to pay, and the optimism vanishes. In the World Economic Forum&\#x27;s annual survey of more than 10,000 executives globally, 54% expect AI to displace existing jobs, more than four in ten expect it to increase profit margins - and only 12% expect it to have a positive impact on wages. That gap between the

rss · Dev.to Career \(Resume &amp; Interview\) · 11月1日 14:59

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#AI 求职`

---

<a id="item-tech-blog-12"></a>
### [How to Build a Python GUI Application With wxPython](https://realpython.com/python-gui-with-wxpython/) ⭐️ 5.5/10

使用 wxPython 构建跨平台 Python 桌面图形界面应用及 MP3 标签编辑器的教程。 来源内容补充：Build a cross-platform Python GUI with wxPython in this tutorial, from buttons and sizers to a working MP3 tag editor application.

rss · Real Python \(Python &amp; Backend\) · 10月31日 14:00

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#Python`, `#后端`

---

<a id="item-tech-blog-13"></a>
### [Using the Python zip\(\) Function for Parallel Iteration](https://realpython.com/python-zip-function/) ⭐️ 5.0/10

介绍 Python zip\(\) 函数用于并行迭代、解包和构建字典的基础用法。 来源内容补充：Learn how to use the Python zip\(\) function to iterate over multiple iterables in parallel, unzip sequences, and build dictionaries with less code.

rss · Real Python \(Python &amp; Backend\) · 10月31日 14:00

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#后端`

---

<a id="item-tech-blog-14"></a>
### [Generating Random Data in Python \(Guide\)](https://realpython.com/python-random/) ⭐️ 5.0/10

对比 Python 内置 random 模块与其他生成随机数据方案的安全性与速度。 来源内容补充：Compare the Python random module with its alternatives for generating random data, on security, versatility, purpose, and speed.

rss · Real Python \(Python &amp; Backend\) · 10月31日 14:00

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#Python`, `#后端`

---

<a id="item-tech-blog-15"></a>
### [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/) ⭐️ 5.0/10

本文介绍了为小型脚本到大型项目编写高质量 Python 代码文档的完整指南。 来源内容补充：A complete guide to documenting Python code. Whether you&\#x27;re documenting a small script or a large project, this guide covers what you need to know.

rss · Real Python \(Python &amp; Backend\) · 11月1日 14:00

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#Python`, `#开发规范`

---

<a id="item-tech-blog-16"></a>
### [Recursion in Python: An Introduction](https://realpython.com/python-recursion/) ⭐️ 5.0/10

介绍 Python 中的递归原理、应用场景及与迭代的对比。 来源内容补充：Get to grips with Python recursion: what it is, how it works, when to reach for it, and how recursive and iterative solutions compare.

rss · Real Python \(Python &amp; Backend\) · 11月1日 14:00

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#Python`, `#后端`

---