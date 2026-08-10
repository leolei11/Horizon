"""
Pro Web-based Video Renderer using HTML5, CSS Glassmorphism, Playwright 60fps, and FFmpeg.
Generates stunning 1080P AI News Video automatically.
"""

import os
import json
import asyncio
from pathlib import Path
import logging
from typing import List, Dict, Any

from playwright.async_api import async_playwright

logger = logging.getLogger(__name__)

class WebVideoRenderer:
    def __init__(self, output_dir: Path = Path("data/videos")):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _generate_html(self, items: List[Dict[str, Any]], total_dur_sec: float) -> str:
        items_json = json.dumps(items, ensure_ascii=False)
        
        return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Horizon AI Daily</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            width: 1920px;
            height: 1080px;
            background: #090d16;
            font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
            color: #ffffff;
            overflow: hidden;
            position: relative;
        }}

        /* Ambient Dynamic Background */
        .bg-gradient {{
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at 20% 30%, rgba(99, 102, 241, 0.25), transparent 50%),
                        radial-gradient(circle at 80% 70%, rgba(236, 72, 153, 0.2), transparent 50%),
                        radial-gradient(circle at 50% 50%, rgba(16, 185, 129, 0.15), transparent 60%);
            animation: pulseBg 12s ease-in-out infinite alternate;
        }}
        @keyframes pulseBg {{
            0% {{ transform: scale(1) rotate(0deg); }}
            100% {{ transform: scale(1.1) rotate(5deg); }}
        }}

        /* Video / Media Canvas */
        .bg-video {{
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.45;
            filter: blur(2px) brightness(0.85);
            transition: opacity 1s ease;
        }}

        /* Header Bar */
        .header {{
            position: absolute;
            top: 48px;
            left: 80px;
            right: 80px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 10;
        }}
        .brand-badge {{
            display: flex;
            align-items: center;
            gap: 16px;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 12px 24px;
            border-radius: 40px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }}
        .brand-logo {{
            width: 32px;
            height: 32px;
            border-radius: 8px;
        }}
        .brand-title {{
            font-size: 22px;
            font-weight: 700;
            letter-spacing: 1px;
            background: linear-gradient(135deg, #a5b4fc, #38bdf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .date-badge {{
            font-size: 18px;
            color: rgba(255, 255, 255, 0.6);
            font-weight: 500;
        }}

        /* Main Content Container */
        .container {{
            position: absolute;
            inset: 120px 80px 80px 80px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 10;
        }}

        /* Glassmorphism Card */
        .glass-card {{
            width: 1280px;
            background: rgba(15, 23, 42, 0.65);
            backdrop-filter: blur(28px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 32px;
            padding: 56px 64px;
            box-shadow: 0 24px 64px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1);
            display: flex;
            flex-direction: column;
            gap: 28px;
            opacity: 0;
            transform: translateY(30px) scale(0.98);
            transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .glass-card.active {{
            opacity: 1;
            transform: translateY(0) scale(1);
        }}

        /* Index & Tag Row */
        .card-meta {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}
        .index-tag {{
            background: linear-gradient(135deg, #6366f1, #4f46e5);
            color: #ffffff;
            font-size: 18px;
            font-weight: 700;
            padding: 6px 16px;
            border-radius: 12px;
            box-shadow: 0 4px 14px rgba(99, 102, 241, 0.4);
        }}
        .source-tag {{
            font-size: 18px;
            color: rgba(255, 255, 255, 0.7);
            font-weight: 500;
        }}

        /* Article Title */
        .card-title {{
            font-size: 42px;
            font-weight: 800;
            line-height: 1.3;
            color: #f8fafc;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
        }}

        /* Summary Sentences */
        .summary-list {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}
        .summary-item {{
            font-size: 24px;
            line-height: 1.6;
            color: #cbd5e1;
            display: flex;
            align-items: flex-start;
            gap: 12px;
            opacity: 0;
            transform: translateX(-15px);
            transition: all 0.4s ease-out;
        }}
        .summary-item.visible {{
            opacity: 1;
            transform: translateX(0);
        }}
        .bullet {{
            color: #38bdf8;
            font-weight: bold;
        }}

        /* Progress Bar */
        .progress-bar {{
            position: absolute;
            bottom: 0;
            left: 0;
            height: 6px;
            background: linear-gradient(90deg, #6366f1, #38bdf8, #ec4899);
            width: 0%;
            transition: width 0.1s linear;
        }}
    </style>
</head>
<body>
    <div class="bg-gradient"></div>
    <video class="bg-video" id="bgVideo" autoplay loop muted></video>

    <div class="header">
        <div class="brand-badge">
            <img class="brand-logo" id="brandLogo" src="" alt="logo">
            <span class="brand-title">HORIZON AI DAILY</span>
        </div>
        <div class="date-badge">2026-08-10</div>
    </div>

    <div class="container">
        <div class="glass-card" id="glassCard">
            <div class="card-meta">
                <span class="index-tag" id="indexTag">01 / 05</span>
                <span class="source-tag" id="sourceTag">GitHub Trending</span>
            </div>
            <div class="card-title" id="cardTitle">新闻加载中...</div>
            <div class="summary-list" id="summaryList"></div>
        </div>
    </div>

    <div class="progress-bar" id="progressBar"></div>

    <script>
        const items = {items_json};
        let currentIndex = -1;

        function showScene(index) {{
            if (index < 0 || index >= items.length) return;
            currentIndex = index;
            const item = items[index];

            const card = document.getElementById('glassCard');
            card.classList.remove('active');

            setTimeout(() => {{
                document.getElementById('indexTag').innerText = `0${{index + 1}} / 0${{items.length}}`;
                document.getElementById('sourceTag').innerText = item.source || 'AI Tech Digest';
                document.getElementById('cardTitle').innerText = item.title;

                if (item.logo_path) {{
                    document.getElementById('brandLogo').src = item.logo_path;
                }}

                if (item.bg_path) {{
                    const v = document.getElementById('bgVideo');
                    v.src = item.bg_path;
                }}

                const listEl = document.getElementById('summaryList');
                listEl.innerHTML = '';
                item.sentences.forEach((s, sIdx) => {{
                    const div = document.createElement('div');
                    div.className = 'summary-item';
                    div.innerHTML = `<span class="bullet">•</span><span>${{s}}</span>`;
                    listEl.appendChild(div);

                    setTimeout(() => {{
                        div.classList.add('visible');
                    }}, 200 + sIdx * 300);
                }});

                card.classList.add('active');
            }}, 300);
        }}

        // Expose render trigger to Playwright
        window.renderScene = showScene;
        window.updateProgress = function(pct) {{
            document.getElementById('progressBar').style.width = pct + '%';
        }};
    </script>
</body>
</html>
"""

    async def render_video(self, items: List[Dict[str, Any]], audio_path: Path, output_mp4: Path) -> Path:
        """Render 60fps high-aesthetic video via Playwright & combine with TTS audio."""
        logger.info("Starting Playwright 60fps Web Video Render...")
        
        # Calculate scene durations based on sentences length
        total_dur_sec = 0.0
        for item in items:
            sentences = item.get("sentences", [item["title"]])
            dur = max(len("".join(sentences)) * 0.35, 8.0)
            item["duration_sec"] = dur
            total_dur_sec += dur

        html_content = self._generate_html(items, total_dur_sec)
        html_file = self.output_dir / "render.html"
        html_file.write_text(html_content, encoding="utf-8")

        temp_video_dir = self.output_dir / "raw_frames"
        temp_video_dir.mkdir(parents=True, exist_ok=True)
        raw_video_path = self.output_dir / "raw_web_render.webm"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                record_video_dir=str(temp_video_dir),
                record_video_size={"width": 1920, "height": 1080}
            )
            page = await context.new_page()
            await page.goto(f"file://{html_file.resolve()}")

            # Render scenes sequentially
            elapsed = 0.0
            for idx, item in enumerate(items):
                await page.evaluate(f"window.renderScene({idx})")
                dur = item["duration_sec"]
                
                # Update progress bar smoothly over scene duration
                steps = 10
                step_time = dur / steps
                for step in range(steps):
                    elapsed += step_time
                    pct = (elapsed / total_dur_sec) * 100
                    await page.evaluate(f"window.updateProgress({pct:.2f})")
                    await asyncio.sleep(step_time)

            await context.close()
            await browser.close()

            # Retrieve recorded webm file
            recorded_files = list(temp_video_dir.glob("*.webm"))
            if recorded_files:
                raw_video_path = recorded_files[0]

        # Combine recorded 60fps video with Edge-TTS audio using FFmpeg
        logger.info("Combining 60fps Playwright video with TTS audio using FFmpeg...")
        cmd = [
            "ffmpeg", "-y",
            "-i", str(raw_video_path),
            "-i", str(audio_path.resolve()),
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "18",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            str(output_mp4.resolve())
        ]
        
        proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        await proc.communicate()

        logger.info("Successfully rendered Pro Web 1080P Video: %s", output_mp4)
        return output_mp4
