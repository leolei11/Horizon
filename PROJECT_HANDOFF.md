# Horizon 项目交接

更新日期：2026-08-10

## 1. 产品目标

Horizon 是 Neo 的个人信息雷达，不是通用科技新闻聚合器。它每天应产生两个版本：

1. 完整日报：必须恰好 20 条，帮助判断当天值得试用、学习、写作或跟进的内容。
2. 横屏视频版：从日报中再次选择最多 5 条，输出 1920×1080 的中文 MP4。

当前兴趣边界：

- 优先：可直接试用的 AI 应用、Agent 工作流、Codex/Antigravity 提效、AI 视频与内容生产、AI 产品编辑与求职、GitHub 开源、SaaS/全栈工程实践。
- 明确排除：Claude Code。
- 硬拒绝：纯论文/跑分、泛科技社会新闻、重复或无可靠来源的宣传。

这套规则定义在 `data/config.json -> interests`，并真正进入分析 Prompt、质量门槛和配额逻辑，不再是无效配置文字。

## 2. 当前运行链路

```text
GitHub / HN / RSS / OSS Insight
        ↓
跨源去重 + 历史去重
        ↓
Profile 分析 + 兴趣评分
        ↓
硬拒绝 + relevance/actionability 质量优先排序
        ↓
规范化 URL/标题去重 + DeepSeek 最终同事件审计
        ↓
applied-ai / builder-stack 目标配额（10 + 10，可交叉补位）
        ↓
正文补全（失败可降级）
        ├── 完整 Markdown 日报
        └── video_score 二次筛选
                 ↓
             Edge TTS
                 ↓
        Remotion 确定性逐帧渲染
                 ↓
          H.264 + AAC 横屏 MP4
```

关键原则：

- `digest.require_exact_count: true` 将 20 条设为发布硬契约；不足 20 条时中止，不发布残缺日报。
- 高质量门槛决定优先顺序；不足时只从仍属于兴趣桶、未被硬拒绝的候选补位。
- 兴趣桶的 `target_count` 是 10 + 10 的优先目标；某一桶不足时允许另一桶补位，确保总数恰好 20。
- `digest.require_unique_items: true` 会先做规范化 URL/标题去重，再用 DeepSeek 审计相同事件；审计失败会重试三次，仍失败则阻止发布。
- 视频只接受达到 `min_video_score` 且存在目标语言正文补全的条目；宁可少发，也不混入英文或低质量条目。
- 补全失败不会让日报整体失败；系统保留分析摘要并明确记录部分失败。

## 3. API 与运行时

当前 `data/config.json` 使用 SiliconFlow 的 OpenAI 兼容接口与 `deepseek-ai/DeepSeek-V3`，密钥从 `SILICONFLOW_API_KEY` 读取。

稳定性配置：

- `request_timeout_sec: 45`
- `max_retries: 1`
- 最终重复审计最多尝试 3 次。
- 外部资料搜索硬超时 15 秒，超时只降级为空结果，不再无限卡住整批补全。
- 已移除分析层和补全层额外的三次指数重试，避免故障时等待被成倍放大。
- 稳定来源都显式绑定 Profile，省去无意义的 AI 分类调用。
- 每完成 10 条分析会输出一次进度。

安装与运行：

```bash
uv sync --extra dev
npm install --prefix video --no-audit --no-fund

# 正式日报 + 配置启用时的视频
uv run horizon --hours 48

# 重新渲染已有视频清单
uv run horizon-video data/videos/manifests/horizon-YYYY-MM-DD-zh.json

# 验证
uv run --extra dev pytest -q
npm --prefix video run typecheck
```

## 4. 视频实现

默认视频实现：

- Python 编排：`src/video/pipeline.py`
- Remotion 视觉组件：`video/src/HorizonDaily.tsx`
- Node 渲染入口：`video/render.mjs`
- CLI：`horizon-video`

设计方向为“信号台”：

- 不使用随机 Pexels 科技素材拼贴。
- 不使用泛滥的玻璃拟态卡片。
- 每条只表达标题、当前解释、来源、个人相关度，以及有证据时的下一步/影响。
- Horizon 信号线贯穿全片，节点对应真正入选的条目。
- 输出帧率由 Remotion composition 与 renderer 明确控制，目前为 30fps。

首次渲染优先复用系统 Google Chrome；若需要自定义浏览器，可设置 `HORIZON_BROWSER_EXECUTABLE`。

## 5. 关于 CapCut / 剪映

项目不再声称能够控制 CapCut 或剪映。

- 日报默认链路不会写入剪映/CapCut 私有草稿目录，也不会自动打开应用。
- `src/video/jianying_draft.py` 仅作为旧实验代码保留；显式调用仍可能写私有草稿目录，不属于受支持的自动化方案。
- FCPXML 只能被描述为“导出交换文件”，不能承诺 CapCut 一定接受，更不能等同于控制 CapCut。
- `src/video/web_renderer.py` 是旧 Playwright 实时录屏兼容层。Playwright 的视频 API 没有确定性 FPS 合约，因此不再宣称 60fps。

相关依据：

- [Playwright 视频文档](https://playwright.dev/python/docs/videos)
- [Remotion renderMedia 文档](https://www.remotion.dev/docs/renderer/render-media)
- [Remotion Composition 文档](https://www.remotion.dev/docs/composition)

## 6. 开源方案取舍

调研后采用的结论：

- [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)：学习其“文案 → TTS → 字幕时间轴 → 素材/镜头 → 合成”的分层流水线；不照搬随机库存素材审美。
- [MoneyPrinter](https://github.com/FujiwaraChoki/MoneyPrinter)：适合 Shorts 自动拼装的参考，不适合 Horizon 的信息密度与横屏编辑定位。
- [OpenCut](https://github.com/OpenCut-app/OpenCut)：项目正在重写，Editor API/MCP/headless automation 仍属路线图，不作为当前生产依赖。
- [Remotion](https://github.com/remotion-dev/remotion)：用于确定性尺寸、帧率、时长、音频和字幕编排。
- [FFmpeg filters](https://ffmpeg.org/ffmpeg-filters.html)：用于最终媒体检查和必要的音视频处理。

## 7. 已验证结果与边界

2026-08-10 的完整 DeepSeek API 隔离验证：

- 使用 SiliconFlow `deepseek-ai/DeepSeek-V3`，抓取 72 条，跨源合并后 71 条。
- 质量优先线以上 40 条；硬拒绝、确定性去重和最终同事件审计后保留 42 个唯一候选。
- 最终重复审计移除 3 条，按两个兴趣方向精确选择 20 条。
- 20 个 URL、规范化标题和内容事件均完成复核，无重复。
- 中文正文补全成功 20/20，无降级。
- 中文视频质量门槛最终保留 1 条，没有把补全失败的英文条目混入。
- 实际 MP4：H.264 + AAC、1920×1080、30fps、56.98 秒。

定时工作流使用 48 小时来源窗口并依靠历史记录排除已发布链接；每天上海时间 04:00 运行，通过后部署原 GitHub Pages。候选不足 20 条或最终重复审计失败时，任务会失败关闭，不会发布不足或未经审计的日报。

## 8. 仍可继续优化

优先级从高到低：

1. 为抓取结果增加便宜、可解释的模型前预筛，减少明显无关条目的 API 调用。
2. 将 AI 产品编辑/求职源从通用 Dev.to Career 换成更可靠、地域更匹配的职位与行业源。
3. 给视频加入按句级 TTS 时间戳，而不是按字符比例切换字幕。
4. 建立 30–50 条人工标注的兴趣黄金集，量化漏选、误选和 Claude Code 排除准确率。
5. 视频达到 3–5 条高质量内容后，再评估 BGM、项目截图或产品录屏；不要用随机库存视频填空。
