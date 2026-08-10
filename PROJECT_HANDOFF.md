# 📋 Horizon AI Daily - 项目完整交接文档 (Project Handoff Document)

> **目标**：本文档旨在为接手的 AI 助手（如 ChatGPT / GPT-4o）或人类开发者提供完整、严密、无缝的项目上下文，以便零成本接管开发。

---

## 1. 📌 项目背景与核心目标

* **项目名称**：`Horizon` (Horizon AI Daily)
* **核心定位**：全自动 AI 科技日报与 1080P 高清短视频生成系统。
* **每日自动化流程**：
  1. **数据抓取**：从 GitHub Trending、RSS（HuggingFace、V2EX、TechCrunch 等）抓取每日 AI 科技新闻。
  2. **智能摘要与配音**：使用 Gemini API 生成中文精简摘要，并使用 Edge-TTS (`zh-CN-YunxiNeural`) 制作立体声自然配音与 SRT 字幕。
  3. **博客发布**：自动生成 GitHub Pages (Jekyll) Markdown 文章并提交发布。
  4. **短视频合成**：全自动合成包含动效、声画同步、品牌 Logo、磨砂玻璃卡片的 1080P 高清短视频成品。

---

## 2. 🗂 代码库目录结构与模块说明

```
Horizon/
├── docs/                        # Jekyll 静态博客目录
│   └── _posts/                  # 自动生成的每日 Markdown 博客
├── data/                        # 运行数据与输出目录
│   └── videos/                  # 生成的视频、音频与素材
│       └── exports/             # 导出的单项素材、FCPXML 与成品 MP4
├── src/                         # 核心源码
│   ├── fetcher/                 # 新闻抓取模块 (GitHub Trending, RSS)
│   ├── summarizer/              # 摘要生成模块 (Gemini API / LLM)
│   ├── publisher/               # Jekyll 文章发布模块
│   └── video/                   # 视频合成引擎
│       ├── generator.py         # FFmpeg 原生 MP4 渲染引擎
│       ├── jianying_draft.py    # 剪映/CapCut 工程与 FCPXML 导出器
│       └── web_renderer.py      # Playwright + HTML5 60fps 极高颜值渲染器
├── tests/                       # 单元与集成测试
├── src/orchestrator.py          # 每日任务全自动调度入口
├── pyproject.toml               # Python 依赖配置文件 (uv)
└── PROJECT_HANDOFF.md           # 本交接文档
```

---

## 3. 🛠 运行环境与依赖配置

* **操作系统**：macOS (Apple Silicon / Intel)
* **Python 环境**：Python 3.12 (基于 `uv` 包管理器)
* **核心依赖库**：
  * `edge-tts`：微软 Edge 免费高保真 TTS 语音合成
  * `playwright`：Headless Chromium 60fps 网页级视频帧渲染
  * `pillow`：图像处理与图文 Overlay 渲染
  * `pyyaml` / `requests` / `aiofiles`
* **系统原生工具**：`ffmpeg` (已安装并配置至 PATH)

### 快速启动与测试指令
```bash
# 1. 安装与同步依赖
uv sync

# 2. 运行每日全自动流水线
uv run python src/orchestrator.py

# 3. 仅测试 Playwright 高颜值为短视频合成
uv run python -c "
import asyncio
from pathlib import Path
from src.video.web_renderer import WebVideoRenderer

async def test():
    renderer = WebVideoRenderer()
    # 传入新闻列表与音频，直接输出成品 MP4
    await renderer.render_video(..., Path('data/videos/exports/HORIZON_2026-08-10.mp3'), Path('data/videos/TEST.mp4'))

asyncio.run(test())
"
```

---

## 4. 🔑 关键技术踩坑总结与经验备忘（接手必读）

### ⚠️ 关于剪映 (Jianying) / CapCut 草稿箱导出的重要结论
1. **Mac 客户端防篡改校验**：在 macOS CapCut 9.1+ 与剪映 6.0+ 版本中，字节跳动增加了二进制签名与沙盒校验。直接通过外部 Python 脚本注入私有 `draft_content.json` 会触发软件弹窗：`“草稿使用异常：此草稿来自非常规路径，暂不支持使用”`。
2. **正确解法（工程文件导出）**：
   * 如果需要导入 CapCut/剪映，**不要硬写私有草稿格式**，请使用系统生成的 **FCPXML (`.fcpxml`)** 开放标准文件（位于 `data/videos/exports/HORIZON_YYYY-MM-DD.fcpxml`），在软件中通过 `File -> Import -> Final Cut Pro XML` 导入。
3. **最佳全自动解法（Web 60fps 原生渲染）**：
   * 采用 `src/video/web_renderer.py`，利用 HTML5 / CSS Glassmorphism + Playwright 录制 60fps 高清画面，再结合 FFmpeg 混音。**全过程 100% 自动、无需人工介入、外观极具现代科技感**。

---

## 5. 🚀 给接手 AI (GPT-4o) 的后续优化建议

1. **视频字幕细化 (Subtitles Sync)**：
   * 在 `src/video/web_renderer.py` 的 HTML 模板中，可进一步增强字幕动态逐字亮起（Karaoke 效果）或逐句卡点。
2. **背景音乐 (BGM) 自动混音**：
   * 在 `FFmpeg` 合成阶段加入一条无版权 Lo-Fi / Tech 背景音乐音轨，并通过 `-filter_complex` 设置 `-20dB` 压限（Sidechain ducking），使语音播报时音乐自动降音。
3. **GitHub Actions 自动化**：
   * 配置 `.github/workflows/daily.yml`，在云端定时触发 `orchestrator.py`，实现无人值守每日推送。

---
*文档生成时间：2026-08-10*
