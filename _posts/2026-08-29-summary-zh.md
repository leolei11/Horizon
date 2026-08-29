---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29
lang: zh
---

> 从 81 条内容中筛选出 20 条重要资讯。

---

**科技新闻**
1. [StemDeck：一款免费、开源且支持本地运行的 AI 音轨分离工具](#item-tech-news-1) ⭐️ 10.0/10
2. [把 LLM 内存转为程序分析的技术探索与架构思考](#item-tech-news-2) ⭐️ 7.0/10
3. [Orbify 推出受《盗梦空间》启发的弯曲地图导航演示](#item-tech-news-3) ⭐️ 6.8/10
4. [OpenAI 关于 Cursor 被 SpaceX 收购后的决策与影响探讨](#item-tech-news-4) ⭐️ 6.0/10
5. [diffusionstudio/editor：将你的 AI Agent 转化为专业视频编辑器的开源工具](#item-tech-news-5) ⭐️ 9.0/10
6. [avoid-ai-writing：用于审计和消除 AI 写作痕迹的开源技能脚本](#item-tech-news-6) ⭐️ 10.0/10
7. [利用 Apple Virtualization.framework 启动虚拟 iPhone 的开源工具](#item-tech-news-7) ⭐️ 5.0/10
8. [TurboKV：超快的 Rust 键值存储库](#item-tech-news-8) ⭐️ 7.5/10
9. [vorssaintapp-utils：免费开源的 macOS 菜单栏工具集](#item-tech-news-9) ⭐️ 7.0/10
10. [address：基于真实开放数据的自托管跨国地址与测试资料生成器](#item-tech-news-10) ⭐️ 8.2/10
11. [dYm：抖音视频下载与 AI 智能分析管理工具](#item-tech-news-11) ⭐️ 8.0/10
12. [luvus：面向 AI Agent 的任务控制中心](#item-tech-news-12) ⭐️ 8.0/10
13. [reverse-skill：面向逆向与安全渗透的 AI 技能路由包](#item-tech-news-13) ⭐️ 7.1/10
14. [make-interfaces-feel-better：优化界面交互质感的 Agent 技能库](#item-tech-news-14) ⭐️ 8.0/10
15. [agentconnect：将 AI Agent 无缝嵌入团队协作的开源项目](#item-tech-news-15) ⭐️ 6.0/10

**科技博客**
1. [仅凭一个漏洞传闻便能引发自动化安全攻击的行业新挑战](#item-tech-blog-1) ⭐️ 7.5/10
2. [回归职场的简历策略：停止隐藏那些 ATS 早已解析出的断层](#item-tech-blog-2) ⭐️ 7.5/10
3. [前置部署 AI 工程师（FDE）：企业级 AI 真正急需的角色](#item-tech-blog-3) ⭐️ 8.0/10
4. [面向 AI 代码审查候选人的“诱饵 PR”测试方案：提示词与参考框架](#item-tech-blog-4) ⭐️ 8.2/10
5. [如何在 Express 中使用 Vitest 自动化测试](#item-tech-blog-5) ⭐️ 7.5/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [StemDeck：一款免费、开源且支持本地运行的 AI 音轨分离工具](https://github.com/stemdeckapp/stemdeck) ⭐️ 10.0/10

StemDeck 是一个免费、开源且支持本地运行的 AI 音轨分离工具，主要解决了用户在多媒体处理、视频剪辑以及本地音频提取时需要高效工具的实际痛点。它基于 htdemucs 模型，支持在本地设备上独立完成复杂的音轨拆分工作，无需依赖外部云端服务。对于需要处理视频音频、提取特定人声或乐器的创作者而言，这是一款非常实用且注重隐私的应用。用户可以在 GitHub 仓库查看项目源码并开始在本地部署使用。

hackernews · thclpr · 8月29日 01:24 · [社区讨论](https://news.ycombinator.com/item?id=49486081)

**「下一步」** 前往 GitHub 仓库查看项目源码并在本地环境中进行部署测试。

**「社区讨论」** 评论区有用户指出它本质上是对 htdemucs 的封装，也有人感叹这项技术让获取人声变得异常简单，甚至有人提及 Audacity 的 OpenVINO 插件也能实现类似功能。

**标签**: `#AI 应用`, `#开源项目`, `#音频处理`

---

<a id="item-tech-news-2"></a>
### [把 LLM 内存转为程序分析的技术探索与架构思考](https://pwning.systems/posts/llm-memory-program-analysis/) ⭐️ 7.0/10

这篇文章分享了将大语言模型（LLM）的内存或知识库处理转化为程序分析与形式化结构的架构探索。它针对的是传统大模型在处理复杂且易变的实体事实时容易遗忘、出错或缺乏可靠推理的痛点。文章的思路是将自然语言请求和结果解释放在终端，而中间的推理和状态存储则交由更为严谨的程序逻辑或知识图谱来处理。对于全栈开发者、系统架构师以及构建复杂 Agent 的技术人员来说，这种设计思路提供了很好的参考。

hackernews · matt\_d · 8月28日 23:27 · [社区讨论](https://news.ycombinator.com/item?id=49485416)

**「下一步」** 阅读原文博客，深入理解 LLM 与形式化知识库结合的安全分析与状态维护架构。

**「社区讨论」** 评论区网友结合选举候选人变动的实际案例展开了讨论，赞同将大模型作为终端接口，而中间推理交由知识图谱或 Datalog 等形式化结构进行机械推理的做法。

**标签**: `#LLM`, `#Agent`, `#系统架构`

---

<a id="item-tech-news-3"></a>
### [Orbify 推出受《盗梦空间》启发的弯曲地图导航演示](https://www.orbify.eu/demo/) ⭐️ 6.8/10

Orbify 推出了一个受电影《盗梦空间》视觉风格启发、用于逐向导航的 3D 弯曲地图概念演示。它通过将前方道路弯曲呈现的 UI 界面，尝试为用户提供一种新颖的视觉空间导航体验。该项目作为一个前端概念验证，非常适合前端开发者和 UI 设计师作为视觉灵感与交互创新的参考。有兴趣的读者可以通过其官方链接直接体验这个独特的地图演示。

hackernews · smoser · 8月28日 12:29 · [社区讨论](https://news.ycombinator.com/item?id=49477564)

**「下一步」** 访问 Orbify 的 demo 页面亲自体验这种创新的 3D 弯曲地图 UI 效果。

**「社区讨论」** Hacker News 评论区指出这种灵感类似于 2009 年的“Here and There”海报，但也有人指出这种投影方式在处理连续急弯时会导致前方路况信息缺失，存在一定的视觉干扰。

**标签**: `#前端开发`, `#UI 创意`, `#地图应用`

---

<a id="item-tech-news-4"></a>
### [OpenAI 关于 Cursor 被 SpaceX 收购后的决策与影响探讨](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 6.0/10

这篇文章讨论了 OpenAI 针对知名 AI 编程工具 Cursor 被 SpaceX 收购后所作出的相关决策及其可能带来的影响。随着竞争对手和模型提供商之间的资本变动，这一事件引发了开发工具生态、API 调用政策以及用户工作流可能发生变动的广泛关注。对于日常依赖 Cursor 或同类 AI 辅助编程工具的开发者来说，了解这一动向有助于及时评估开发环境的潜在风险。

hackernews · OpenAI News · 8月29日 01:47 · [社区讨论](https://news.ycombinator.com/item?id=49486172)

**「下一步」** 关注 OpenAI 与相关工具提供商的后续官方公告，评估开发环境可能受到的影响。

**「社区讨论」** 评论区讨论了 Anthropic 此前针对同类条款违规的封禁先例，并探讨了在失去首选工具后开发者寻找高效替代方案的可能性。

**标签**: `#AI 应用`, `#开发工具`

---

<a id="item-tech-news-5"></a>
### [diffusionstudio/editor：将你的 AI Agent 转化为专业视频编辑器的开源工具](https://github.com/diffusionstudio/editor) ⭐️ 9.0/10

diffusionstudio/editor 是一个基于 TypeScript 开发的开源项目，旨在将你的 AI 代理（Agent）转化为专业的视频编辑工具。它解决了多媒体开发者希望让 AI 自动化完成复杂视频剪辑、拼接与处理的需求。通过提供强大的开发接口，它能让各种智能体直接具备视频制作与处理能力。对于致力于开发 AI 视频应用和自动化工作流的开发者来说，这是一个值得关注的开源仓库。

ossinsight · diffusionstudio · 8月29日 13:50

**「下一步」** 访问 GitHub 仓库查看 diffusionstudio/editor 的 TypeScript 源码与文档，尝试将其集成到你的 AI 代理工作流中。

**标签**: `#TypeScript`, `#AI Video`, `#Open Source`, `#Agent`

---

<a id="item-tech-news-6"></a>
### [avoid-ai-writing：用于审计和消除 AI 写作痕迹的开源技能脚本](https://github.com/conorbronsdon/avoid-ai-writing) ⭐️ 10.0/10

avoid-ai-writing 是一个基于 JavaScript 开发的开源技能脚本，专门用于审计和重写内容以消除明显的 AI 写作模式与痕迹。它完美适配多种主流的 AI 辅助工具和代理，如 Claude Code、OpenClaw、Codex 以及 Hermes。该工具解决了创作者和开发者在使用 AI 生成初稿后，需要人工介入去除套话、机械化句式并使文风更加自然流畅的痛点。对于希望提升 AI 生成文本质量、让内容更具人类真实表达质感的写作者和技术人员来说，这是一个极其实用的辅助脚本。

ossinsight · conorbronsdon · 8月29日 13:50

**「下一步」** 在 GitHub 上获取 avoid-ai-writing 脚本，并将其配置到你常用的 AI 代理或编辑器中以优化文本输出质量。

**标签**: `#AI 产品编辑`, `#Agent`, `#开源项目`

---

<a id="item-tech-news-7"></a>
### [利用 Apple Virtualization.framework 启动虚拟 iPhone 的开源工具](https://github.com/Lakr233/vphone-cli) ⭐️ 5.0/10

开源项目 vphone-cli 允许开发者在 macOS 的虚拟化框架中运行 iOS 内核与用户空间。该工具主要解决了在虚拟环境中测试相关功能的底层需求，提供了方便的命令行控制手段。它非常适合需要进行应用测试或研究 Apple 系统架构的技术人员与全栈开发者。需要注意的是，该项目并非真正的模拟器，而是通过组合 iOS 内核与补丁来运行。

hackernews · hentrep · 8月28日 23:02 · [社区讨论](https://news.ycombinator.com/item?id=49485267)

**「背景」** Apple 提供的 iOS 内核常用于 PCC 或 cloudOS 镜像，该项目将其与用户空间及补丁进行配对。

**「实际影响」** 部分用户经常使用它来测试应用，并有配合的模型上下文协议（MCP）允许 AI 代理对其进行控制。

**「下一步」** 查看相关 GitHub 仓库以了解其详细的脚本及前置设置要求。

**「社区讨论」** 评论指出这并不是在模拟 iPhone，应用程序很容易将其与真机区分开；且部分脚本需要 root 权限运行，需注意安全性。

**标签**: `#GitHub 开源`, `#系统底层`, `#iOS`

---

<a id="item-tech-news-8"></a>
### [TurboKV：超快的 Rust 键值存储库](https://github.com/kingroryg/turbokv) ⭐️ 7.5/10

TurboKV 是一个用 Rust 编写的高性能嵌入式键值存储库，旨在提供极致的数据读写速度。它通过内存映射等技术应对高性能场景，但其在处理超出内存容量的数据集时可能会面临挑战。该项目适合对后端存储、高性能数据结构及 Rust 语言感兴趣的开发者和工程师了解与研究。

hackernews · rgbimbochamp · 8月29日 02:23 · [社区讨论](https://news.ycombinator.com/item?id=49486334)

**「背景」** 项目在早期曾就标志设计等内容进行过提交。

**「实际影响」** 在部分测试中展现了极高的速度，但也引发了关于其持久化模式（如未做每写同步）是否真正满足传统“持久”定义的讨论。

**「下一步」** 访问其 GitHub 仓库查阅基准测试和具体的代码实现。

**「社区讨论」** 社区讨论集中在其基准测试仅在小数据集上运行、内存映射在大数据集上的性能回退，以及所谓的 durable 模式是否能抵御断电风险等方面。

**标签**: `#Rust`, `#后端`, `#数据库`, `#开源`

---

<a id="item-tech-news-9"></a>
### [vorssaintapp-utils：免费开源的 macOS 菜单栏工具集](https://github.com/vorssaintapp/vorssaint-utils) ⭐️ 7.0/10

vorssaintapp/vorssaint-utils 是一个免费且开源的 macOS 菜单栏实用工具集。它为开发者提供了一个现成的菜单栏应用框架，解决了在 macOS 上快速开发轻量级系统小工具的痛点。对于喜欢定制 macOS 体验或希望参考 Swift 编写菜单栏应用的独立开发者来说具有不错的参考价值。

ossinsight · vorssaintapp · 8月29日 13:50

**「背景」** 基于 Swift 开发，近期在 GitHub 上获得了持续的关注。

**「实际影响」** 为 macOS 开发者提供了一个简洁的开源菜单栏工具实现模板。

**「下一步」** 前往 GitHub 仓库查看源码并尝试在本地构建运行。

**标签**: `#GitHub开源`, `#macOS`, `#Swift`

---

<a id="item-tech-news-10"></a>
### [address：基于真实开放数据的自托管跨国地址与测试资料生成器](https://github.com/daimon3332/address) ⭐️ 8.2/10

address 是一个基于真实开放数据的自托管地址和合成测试资料生成器，覆盖 27 个国家和地区。它解决了开发和测试过程中缺乏真实、多语言合规测试地址数据的痛点，支持多语言输出、IP 附近生成、地图预览和 API 调用。对于需要进行全球化产品测试、表单验证或数据构造的开发和测试人员非常实用。

ossinsight · daimon3332 · 8月29日 13:50

**「背景」** 项目由真实开放数据的街道、行政区域、坐标和邮编构建而成，使用 TypeScript 编写。

**「实际影响」** 提供自托管和 API 访问能力，能够极大地简化跨国业务场景下的测试数据准备工作。

**「下一步」** 访问 GitHub 了解自托管部署方式以及 API 的具体调用方法。

**标签**: `#GitHub 开源`, `#TypeScript`, `#API 集成`, `#测试数据`

---

<a id="item-tech-news-11"></a>
### [dYm：抖音视频下载与 AI 智能分析管理工具](https://github.com/Everless321/dYm) ⭐️ 8.0/10

dYm 是一个使用 TypeScript 构建的开源抖音视频下载与 AI 智能分析管理工具。它旨在解决短视频内容下载后的归档、检索和智能化分析难题，提供了集成化的管理能力。该工具适合内容创作者、AI 视频剪辑师以及对多媒体数据处理感兴趣的开发者。

ossinsight · Everless321 · 8月29日 13:50

**「背景」** 采用 TypeScript 编写，专注于短视频及 AI 分析场景。

**「实际影响」** 为处理抖音平台视频资产提供了一个开源的自动化下载与智能分析一体化方案。

**「下一步」** 查阅 GitHub 仓库的说明文档来配置和试用该工具。

**标签**: `#GitHub`, `#AI 视频`, `#TypeScript`

---

<a id="item-tech-news-12"></a>
### [luvus：面向 AI Agent 的任务控制中心](https://github.com/RizRiyz/luvus) ⭐️ 8.0/10

RizRiyz/luvus 是一个使用 Rust 构建的 AI Agent 任务控制中心开源项目。它解决了在复杂应用场景中对多个 AI Agent 进行统一调度、监控与管理的痛点，提供了类似任务控制面板的功能。对于构建和管理多 Agent 工作流的开发者以及 Rust 爱好者来说具有极高的探索价值。

ossinsight · RizRiyz · 8月29日 13:50

**「背景」** 项目基于 Rust 语言开发，聚焦于 AI 智能体的运行控制。

**「实际影响」** 为开发者在本地或服务端集中管控 AI 代理行为提供了一个新兴的架构选择。

**「下一步」** 前往 GitHub 查看项目源码，了解其 Agent 调度机制。

**标签**: `#GitHub`, `#Agent`, `#Rust`

---

<a id="item-tech-news-13"></a>
### [reverse-skill：面向逆向与安全渗透的 AI 技能路由包](https://github.com/zhaoxuya520/reverse-skill) ⭐️ 7.1/10

reverse-skill 是一个专为逆向工程、授权渗透测试和安全研究设计的 AI 技能路由包。它解决了在安全领域中 AI 编码助手缺乏专业工具链支持的问题，提供了 AI 自动路由、按需自举工具链和自动进化经验库。它支持 Claude Code、Kiro、Cursor、Cline 等多种主流 AI 编码客户端，适合从事安全研究或逆向工程的技术人员。

ossinsight · zhaoxuya520 · 8月29日 13:50

**「背景」** 使用 PowerShell 编写，旨在增强主流 AI 编程客户端在安全领域的专业能力。

**「实际影响」** 能够让主流 AI 客户端按需加载安全渗透工具链，提升安全研究场景下的自动化辅助效率。

**「下一步」** 在 GitHub 上查看其技能路由包配置并将其集成到你的 AI 编码客户端中。

**标签**: `#GitHub 开源`, `#Agent 工作流`, `#逆向安全`

---

<a id="item-tech-news-14"></a>
### [make-interfaces-feel-better：优化界面交互质感的 Agent 技能库](https://github.com/jakubkrehel/make-interfaces-feel-better) ⭐️ 8.0/10

jakubkrehel/make-interfaces-feel-better 是一个旨在帮助开发者优化界面交互质感的 Agent 技能开源项目。它解决了前端开发和产品设计中界面显得生硬、缺乏细节打磨的痛点，通过 Agent 技能提供优化建议。对于希望提升应用前端用户体验的全栈开发者和设计人员而言非常实用。

ossinsight · jakubkrehel · 8月29日 13:50

**「背景」** 基于 Markdown 编写的 Agent 技能定义，专注于 UI 交互的微调与打磨。

**「实际影响」** 为 AI 辅助前端开发提供了直接指导界面视觉与动效优化的落地方法。

**「下一步」** 阅读该 Markdown 技能文件的具体内容并将其应用到你的 AI 开发工作流中。

**标签**: `#Agent`, `#前端`, `#UI`, `#开源`

---

<a id="item-tech-news-15"></a>
### [agentconnect：将 AI Agent 无缝嵌入团队协作的开源项目](https://github.com/agentconnect-md/agentconnect) ⭐️ 6.0/10

agentconnect 是一个用 TypeScript 编写的开源项目，允许将任意 AI Agent 标记并嵌入到团队的日常工作流中。它解决了 AI 与人类团队协同割裂的问题，让代理能够与团队成员及其他代理并肩工作并持续学习。对于探索多 Agent 协同办公以及团队自动化流程的开发者来说具有很高价值。

ossinsight · agentconnect-md · 8月29日 13:50

**「背景」** 采用 TypeScript 开发，聚焦于团队日常协作与 Agent 的结合。

**「实际影响」** 为团队工作流引入 AI 智能体提供了轻量级的连接方案，使代理能够随团队共同成长。

**「下一步」** 访问 GitHub 仓库了解如何将代理接入你的团队协作场景。

**标签**: `#GitHub 开源`, `#Agent`, `#TypeScript`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [仅凭一个漏洞传闻便能引发自动化安全攻击的行业新挑战](https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/) ⭐️ 7.5/10

Simon Willison 在文章中探讨了由于现代 AI 编码助手和自动化 Agent 的普及，软件安全领域正在面临的严峻新挑战。文章指出，安全漏洞的修补讨论和补丁刚一公开，自动化工具和攻击代理便能在数分钟内利用这些信息进行扫描与探测，导致传统的开源漏洞缓冲期失效。这给开源项目维护者带来了巨大的漏洞排查压力，促使社区必须重新思考漏洞披露与安全通告的应对流程。对于所有开源维护者和技术团队来说，都需要警惕这种由 AI 带来的安全防御节奏失衡。

rss · Simon Willison \(AI &amp; Tools\) · 8月28日 22:12

**「下一步」** 审视自身项目的安全漏洞披露流程，防范自动化代码扫描与代理带来的潜在快速攻击风险。

**标签**: `#AI 安全`, `#开源维护`, `#编码 Agent`

---

<a id="item-tech-blog-2"></a>
### [回归职场的简历策略：停止隐藏那些 ATS 早已解析出的断层](https://dev.to/cvpilot/the-returner-cv-stop-hiding-the-gap-your-ats-already-parsed-55j3) ⭐️ 7.5/10

这篇文章深入剖析了求职者如何通过诚实的简历排版策略来应对 ATS（简历解析系统）的解析，解决职业断层带来的焦虑。文章指出，试图用复杂的功能性布局来掩盖多 years 的职业断层毫无意义，因为 ATS 可以在毫秒内解析出时间线，而隐藏的断层往往会被读作遮掩。正确的做法是在简历靠前的位置用简明的一行坦然说明断层原因，随后聚焦于断层前的过往成就与真实数据。对于正在准备重返职场的专业人士来说，这提供了一种更加自信和高效的简历优化策略。

rss · Dev.to Career \(Resume &amp; Interview\) · 8月29日 13:00

**「下一步」** 检查自己的简历，采用坦诚清晰的排版方式来处理职业断层，避免使用容易引起误解的隐藏技巧。

**标签**: `#求职`, `#简历优化`, `#ATS`

---

<a id="item-tech-blog-3"></a>
### [前置部署 AI 工程师（FDE）：企业级 AI 真正急需的角色](https://dev.to/trendwise/forward-deployed-ai-engineer-the-role-enterprise-ai-actually-needs-2f9i) ⭐️ 8.0/10

这篇文章深度解析了企业 AI 落地中长期存在的“构建与部署脱节”痛点，并提出了“前置部署 AI 工程师（FDE）”这一核心职能。FDE 并不是单纯的数据科学家或提示词工程师，而是能够独立串联需求发现、系统架构设计、代码编写、评估流水线、合规部署以及后期用户采纳全流程的关键角色。随着智能体（Agent）技术的大规模普及，企业对能够打通技术与实际生产环境的全栈 AI 人才需求正在急剧增长。对于希望在 AI 时代转型全栈或寻求高级技术职位的工程师来说，这是一个极具潜力的发展方向。

rss · Dev.to Career \(Resume &amp; Interview\) · 8月29日 12:55

**「下一步」** 评估并学习企业级 AI 部署、RAG 架构评估以及运维监控等相关技能，向复合型的部署工程方向发展。

**标签**: `#AI求职`, `#Agent工作流`, `#全栈开发`

---

<a id="item-tech-blog-4"></a>
### [面向 AI 代码审查候选人的“诱饵 PR”测试方案：提示词与参考框架](https://dev.to/appjs_3979/a-decoy-pr-test-for-ai-reviewer-candidates-prompt-rubric-and-a-free-server-reference-setup-3062) ⭐️ 8.2/10

这篇文章介绍了一种用于评估 AI 代码审查（Code Review）工具或候选人能力的“诱饵 PR 测试”方法。它通过在测试仓库中巧妙植入真实漏洞、看似危险但有防护的诱饵以及指令注入评论，来测试 AI 审查工具的克制度与防注入抗干扰能力。整套方案包含明确的提示词、加权的评分标准以及参考实现框架，无需昂贵的 API 密钥或独立 GPU 即可在笔记本上运行。对于需要构建、测试 AI 代码审查流水线或在面试中筛选 AI 工程师的技术团队而言，这是一个极具实操价值的现成方案。

rss · Dev.to Career \(Resume &amp; Interview\) · 8月29日 10:35

**「下一步」** 参考文章提供的提示词与加权评分标准，在本地测试环境中尝试部署并运行这套诱饵 PR 评审测试。

**标签**: `#AI 工作流`, `#Code Review`, `#提示词工程`

---

<a id="item-tech-blog-5"></a>
### [如何在 Express 中使用 Vitest 自动化测试](https://www.freecodecamp.org/news/how-to-automate-your-tests-in-express-using-vitest/) ⭐️ 7.5/10

本文介绍了如何在 Express 应用中使用 Vitest 编写和自动化 API 集成测试。它主要解决了开发者在手动切换标签页测试应用逻辑时效率低下的问题，提供了一套清晰的测试编写与自动化工作流。对于希望提升后端代码质量、减少手动测试时间的全栈开发者来说非常实用。

rss · freeCodeCamp News \(Tutorials &amp; Career\) · 8月28日 15:33

**「背景」** 开发者在处理 API 逻辑时，经常面临在应用和测试之间反复切换的繁琐过程。

**「实际影响」** 通过编写自动化测试，可以显著节省时间和精力，降低集成阶段出错的概率。

**「下一步」** 阅读 FreeCodeCamp 上的原文以获取完整的代码示例和配置步骤。

**标签**: `#后端`, `#测试`, `#Express`, `#Vitest`

---