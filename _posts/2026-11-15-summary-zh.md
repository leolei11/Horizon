---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15
lang: zh
---

> 从 52 条内容中筛选出 20 条重要资讯。

---

**科技新闻**
1. [理解现代大模型中的位置嵌入](#item-tech-news-1) ⭐️ 7.0/10
2. [法院驳回针对 DRAM 价格操纵案的撤诉动议](#item-tech-news-2) ⭐️ 7.0/10
3. [Lovable 应用暴露护照详情及超 20 万条私密消息](#item-tech-news-3) ⭐️ 8.5/10
4. [A family tree of software job titles](#item-tech-news-4) ⭐️ 5.0/10
5. [All AI-generated code should be Open Source](#item-tech-news-5) ⭐️ 5.0/10

**科技博客**
1. [从零使用 Python 构建和训练 GLM-5.3-Flash 模型](#item-tech-blog-1) ⭐️ 7.0/10
2. [datasette-llm 0.1a11 发布](#item-tech-blog-2) ⭐️ 9.0/10
3. [XYBench：解决问题背后的问题](#item-tech-blog-3) ⭐️ 7.0/10
4. [2026 年夏季实习机会汇总：三星、Postman 等公司正在招募](#item-tech-blog-4) ⭐️ 7.2/10
5. [8 个可随时随地申请的全球远程软件工程师岗位](#item-tech-blog-5) ⭐️ 7.0/10
6. [中国计算机科学全英文项目：7 个值得考虑的学位选择](#item-tech-blog-6) ⭐️ 7.0/10
7. [400 美元规则：副业收入何时转化为纳税自雇收入](#item-tech-blog-7) ⭐️ 7.2/10
8. [信息流应当缓存什么，不应当缓存什么？](#item-tech-blog-8) ⭐️ 7.0/10
9. [Datasette-vega 0.7 发布](#item-tech-blog-9) ⭐️ 7.5/10
10. [Scientific Python: Using SciPy for Optimization](#item-tech-blog-10) ⭐️ 6.5/10
11. [10 Technical Interview Questions That Test How You Think, Not Just How You Code](#item-tech-blog-11) ⭐️ 6.0/10
12. [41% of cybersecurity job postings are remote: by specialty, country and pay \(Nov 2026\)](#item-tech-blog-12) ⭐️ 0.0/10
13. [EP233: Kubernetes Explained for Busy Engineers](#item-tech-blog-13) ⭐️ 5.0/10
14. [How to Do a Binary Search in Python](#item-tech-blog-14) ⭐️ 5.0/10
15. [Project Manager phần mềm thực chiến: Một cuốn sách miễn phí bằng cho người Việt](#item-tech-blog-15) ⭐️ 4.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [理解现代大模型中的位置嵌入](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings) ⭐️ 7.0/10

这篇文章深入探讨了现代大模型中位置嵌入（Positional Embeddings）的工作原理和核心机制。通过剖析不同类型的位置编码，它帮助读者理解模型如何感知文本中词语的相对与绝对顺序。对于关注大模型底层架构和原理的 AI 开发者来说，这是一篇极具价值的技术科普内容。

hackernews · vismit2000 · 11月15日 12:14 · [社区讨论](https://news.ycombinator.com/item?id=50506376)

**「下一步」** 阅读原文以了解现代大模型中位置嵌入的具体实现方式。

---

<a id="item-tech-news-2"></a>
### [法院驳回针对 DRAM 价格操纵案的撤诉动议](https://litnews.ai/articles/garciaguirre-samsung-sk-hynix-micron-dram-conspiracy-suit-survives-dismissal) ⭐️ 7.0/10

美国法院近期驳回了一起针对三星、SK 海力士和美光等 DRAM 制造商的价格操纵诉讼的撤诉动议。这起反垄断阴谋诉讼将继续推进，引发了业界对内存市场竞争状况的密切关注。对于硬件采购预算受到高昂内存成本挤压的计算研究人员和开发者而言，这一案件具有重要的行业影响。

hackernews · ybathaee · 11月15日 01:18 · [社区讨论](https://news.ycombinator.com/item?id=50502988)

**「下一步」** 关注后续审判进展以了解 DRAM 行业的潜在市场格局变化。

**「社区讨论」** 社区讨论指出，由于高昂的 RAM 和 VRAM 价格，构建本地 AI 计算工作站的预算压力巨大。有评论认为该市场呈现出类似囚徒困境的三方寡头格局，常规的市场竞争机制在这一细分领域面临失效。

---

<a id="item-tech-news-3"></a>
### [Lovable 应用暴露护照详情及超 20 万条私密消息](https://www.crissyfield.de/research/lovable-en/) ⭐️ 8.5/10

一项最新的安全研究揭示，由于 Lovable 应用及 Supabase 后端配置不当，导致海量用户的私密数据和敏感信息发生泄露。该问题集中暴露了前端直接对接后端时，若未能正确实施行级安全（RLS）策略所带来的严重安全隐患。文章引发了社区对“全栈低代码/无代码工具”以及缺乏后端经验的开发者在安全配置上的广泛讨论。对于使用类似现代化全栈工具的开发者和构建者而言，这是一记必须高度警惕的安全警钟。

hackernews · armcat · 11月14日 17:43 · [社区讨论](https://news.ycombinator.com/item?id=50499017)

**「背景」** 许多独立开发者在构建应用时，常采用前端直接连接 Supabase 等后端服务的现代架构，但若漏配行级安全策略，极易造成数据库裸奔。

**「实际影响」** 大量用户的护照详情和超过 20 万条私密消息面临公开暴露风险，凸显了安全配置在现代独立开发中的关键性。

**「下一步」** 立即检查你所使用项目的 Supabase 后端与行级安全（RLS）配置，确保敏感数据不会因前端直连而意外暴露。

**「社区讨论」** 评论区指出，许多使用现代全栈工具的“vibe coders”由于缺乏后端经验，常常忽略行级安全策略。部分网友还指出 Supabase 在防范和提示数据库未配置 RLS 方面也负有一定责任。

**标签**: `#SaaS架构`, `#后端安全`, `#独立开发`

---

<a id="item-tech-news-4"></a>
### [A family tree of software job titles](https://zwischenzugs.com/2026/11/03/a-family-tree-of-software-job-titles/) ⭐️ 5.0/10

探讨软件工程职位头衔的演变及 AI 时代带来的身份定义变化。 来源内容补充：A family tree of software job titles

hackernews · umerf · 11月14日 17:45 · [社区讨论](https://news.ycombinator.com/item?id=50499038)

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#职业发展`, `#软件工程`

---

<a id="item-tech-news-5"></a>
### [All AI-generated code should be Open Source](https://jakub.jankiewicz.org/blog/ai-code-open-source/) ⭐️ 5.0/10

探讨所有 AI 生成代码是否应当开源的观点及法律背景。 来源内容补充：All AI-generated code should be Open Source

hackernews · jcubic · 11月15日 14:46 · [社区讨论](https://news.ycombinator.com/item?id=50507303)

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#AI 法律`, `#开源`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [从零使用 Python 构建和训练 GLM-5.3-Flash 模型](https://www.freecodecamp.org/news/build-and-train-a-glm-53-flash-model-from-scratch-with-python/) ⭐️ 7.0/10

该教程介绍了如何使用 Python 从头构建和训练包含线性与稀疏注意力、专家混合（MoE）设计以及流形约束超连接的 GLM-5.3-Flash 模型。文章以一个拥有 2500 万参数的缩减版本为例，手把手带领开发者进行实现。对于希望深入理解大模型内部架构与动手构建小型前沿模型的开发者极具参考价值。

rss · freeCodeCamp News \(Tutorials &amp; Career\) · 11月14日 16:02

**「下一步」** 访问 freeCodeCamp 原文并尝试在本地运行该 Python 脚本。

---

<a id="item-tech-blog-2"></a>
### [datasette-llm 0.1a11 发布](https://simonwillison.net/2026/Nov/14/datasette-llm/) ⭐️ 9.0/10

datasette-llm 发布了 0.1a11 版本，正式引入对 OpenAI 兼容 API 端点的支持。通过这一更新，开发者可以配置 Datasette 使用任何遵循 OpenAI 协议的本地或托管大模型，如通过 LM Studio、Ollama 或 llama.cpp 运行的模型。借助该工具，全栈开发者能够快速配合 \`uvx\` 运行强大的 Datasette Agent 实例。

rss · Simon Willison \(AI &amp; Tools\) · 11月14日 23:59

**「下一步」** 通过命令行使用 uvx 配合本地大模型尝试运行 datasette-llm 0.1a11。

**标签**: `#ai-applications`, `#agent`, `#api-integration`, `#opensource`

---

<a id="item-tech-blog-3"></a>
### [XYBench：解决问题背后的问题](https://huggingface.co/blog/allenai/xybench) ⭐️ 7.0/10

Hugging Face 博客介绍了 XYBench，这是一个旨在帮助解决“问题背后的真正问题”的评测与研究工具。它通过更深入的视角来评估大模型在理解复杂用户意图时的表现。适合对大模型评测基准和意图对齐感兴趣的研究人员阅读。

rss · Hugging Face Blog \(Open-Source AI\) · 11月13日 17:02

**「下一步」** 阅读 Hugging Face 的 XYBench 博客了解详细设计思路。

---

<a id="item-tech-blog-4"></a>
### [2026 年夏季实习机会汇总：三星、Postman 等公司正在招募](https://dev.to/crackr/these-companies-want-interns-this-summer-nov-15-2a27) ⭐️ 7.2/10

本文汇总了三星、Postman、Rambus 等多家知名科技企业针对 2026 年夏季开放的实习岗位。其中包含圣何塞的三星 ML 编译器实习生、AI 系统性能工程师实习生，以及旧金山的 Postman AI 工程师实习生等岗位。对于寻找科技行业特别是 AI 与系统方向实习机会的学生和求职者提供了及时的信息聚合。

rss · Dev.to Career \(Resume &amp; Interview\) · 11月15日 15:00

**「下一步」** 访问 Crackr.dev 浏览具体的职位投递链接。

**标签**: `#AI求职`, `#实习信息`

---

<a id="item-tech-blog-5"></a>
### [8 个可随时随地申请的全球远程软件工程师岗位](https://dev.to/crackr/8-remote-swe-jobs-you-can-apply-to-from-anywhere-nov-15-53gm) ⭐️ 7.0/10

本文汇总了来自 Silver.dev、Lemon.io 等平台的 8 个全球远程软件工程师职位，免去了搬迁的烦恼。其中包括专注于 Node.js/TypeScript 的职位以及 Feltsense 的 AI 工程师岗位。对于寻求远程工作和全球化发展机会的开发者来说，这是一个高效的岗位信息来源。

rss · Dev.to Career \(Resume &amp; Interview\) · 11月15日 15:00

**「下一步」** 通过 Crackr.dev 查看这些远程岗位的具体薪资与技术栈要求。

**标签**: `#AI 求职`, `#远程工作`

---

<a id="item-tech-blog-6"></a>
### [中国计算机科学全英文项目：7 个值得考虑的学位选择](https://dev.to/joyousfuture/computer-science-in-china-7-english-taught-programs-worth-your-tuition-5f9o) ⭐️ 7.0/10

本文整理了中国高校中 7 个面向国际学生的优质全英文授课计算机科学、软件工程和数据科学学位项目。涵盖了北京交通大学、北京邮电大学、北京大学、中山大学、东北大学、四川大学和浙江大学等知名学府。对于希望在无需精通中文的情况下深入中国科技生态系统学习的国际学生提供了实用的指南。

rss · Dev.to Career \(Resume &amp; Interview\) · 11月15日 14:41

**「下一步」** 查阅 Joyous Future 的学位项目目录以对比不同院校的课程设置与申请要求。

---

<a id="item-tech-blog-7"></a>
### [400 美元规则：副业收入何时转化为纳税自雇收入](https://dev.to/ledgerlinehq/the-400-rule-when-your-side-income-becomes-taxable-self-employment-1ao6) ⭐️ 7.2/10

本文向独立开发者和自由职业者科普了美国税法中关于 400 美元净自雇收入的门槛规定。只要年净利润超过 400 美元，即使副业只是兴趣爱好或仅有一个客户，也必须缴纳 15.3% 的自雇税。文章同时提供了费用抵扣建议和税务计算表格，帮助自由职业者规避税务风险。

rss · Dev.to Career \(Resume &amp; Interview\) · 11月15日 14:16

**「下一步」** 使用免费的税收计算器估算副业收入的预留税款。

**标签**: `#独立开发`, `#SaaS架构`, `#求职与副业`

---

<a id="item-tech-blog-8"></a>
### [信息流应当缓存什么，不应当缓存什么？](https://dev.to/kayashaolu/what-should-a-feed-cache-and-what-shouldnt-it-24nd) ⭐️ 7.0/10

这篇文章针对高并发的 feed 流、视频网站或搜索框系统设计，探讨了合理的缓存策略。通过简单的三步判断法（所有人一致且允许旧数据则缓存；因人而异则按人缓存；必须绝对实时则不缓存），帮助开发者厘清系统设计中的缓存边界。对于后端和系统架构设计感兴趣的工程师具有很好的指导意义。

rss · Dev.to Career \(Resume &amp; Interview\) · 11月15日 14:00

**「下一步」** 阅读 System Thinking Lab 的相关课程了解更多系统架构基本构建块。

---

<a id="item-tech-blog-9"></a>
### [Datasette-vega 0.7 发布](https://simonwillison.net/2026/Nov/14/datasette-vega/) ⭐️ 7.5/10

Datasette-vega 0.7 是该项目自 2018 年 7 月以来的首次重大版本更新，主要用于在 Datasette 表格或自定义查询中借助 Vega-Lite 渲染交互式图表。新版本完成了对最新 Datasette 核心 alpha 版本的兼容，并带来了针对 Datasette Lite 的视觉外观优化。由于 Datasette Lite 现已支持加载 JavaScript 插件，用户可以直接在浏览器端实现轻量级的数据可视化。该项目非常适合需要快速探索、可视化表格数据的开发者与数据分析师。

rss · Simon Willison \(AI &amp; Tools\) · 11月14日 17:09

**「背景」** Datasette 是 Simon Willison 开发的用于探索和发布数据的开源工具，而 datasette-vega 是其历史最悠久的图表渲染插件。

**「实际影响」** 通过新版本与 Datasette Lite 的结合，用户无需复杂的后端配置即可在浏览器内直接将 CSV 或表格数据转化为精美的条形图、折线图或散点图。

**「下一步」** 访问 GitHub 上的 datasette-vega 0.7 或 README 中的 Datasette Lite 链接，尝试在浏览器中拖入 CSV 数据并体验其图表渲染功能。

**标签**: `#前端实战`, `#数据可视化`, `#开源项目`

---

<a id="item-tech-blog-10"></a>
### [Scientific Python: Using SciPy for Optimization](https://realpython.com/python-scipy-cluster-optimize/) ⭐️ 6.5/10

学习如何使用 Python 的 SciPy 生态系统进行聚类与优化。 来源内容补充：Learn how the SciPy ecosystem differs from the SciPy library, then install SciPy and use its clustering and optimization modules in Python.

rss · Real Python \(Python &amp; Backend\) · 11月15日 14:00

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#Python`, `#后端`

---

<a id="item-tech-blog-11"></a>
### [10 Technical Interview Questions That Test How You Think, Not Just How You Code](https://dev.to/aburayhanalif/10-technical-interview-questions-that-test-how-you-think-not-just-how-you-code-4ppl) ⭐️ 6.0/10

盘点 10 个测试开发者工程思维和设计抉择的技术面试跟进问题。 来源内容补充：&lt;p&gt;Solving a coding problem is one thing. Explaining why your solution makes sense is another.&lt;/p&gt; &lt;p&gt;You might write a working solution, pass the test cases, and still struggle when the interviewer asks:&lt;/p&gt; &lt;p&gt;Why did you choose this approach?&lt;/p&gt; &lt;p&gt;What alternatives did you consider?&lt;/p&gt; &lt;p&gt;What happens if the requirements change?&lt;/p&gt; &lt;p&gt;How would you improve this under different constraints?&lt;/p&gt; &lt;p&gt;These follow-

rss · Dev.to Career \(Resume &amp; Interview\) · 11月15日 14:37

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#career`, `#system-design`

---

<a id="item-tech-blog-12"></a>
### [41% of cybersecurity job postings are remote: by specialty, country and pay \(Nov 2026\)](https://dev.to/cyberjobscc/41-of-cybersecurity-job-postings-are-remote-by-specialty-country-and-pay-nov-2026-obo) ⭐️ 0.0/10

分析 2026 年 11 月网络安全职位的远程办公比例、细分领域与地域分布。 来源内容补充：&lt;p&gt;Remote security work is not rare. Of the 3,033 open cybersecurity roles at 696 employers that we read on 15 November 2026, 1,240 \(41%\) are remote, posted by 532 different employers. That is a lot of choice, but it is not spread evenly: some specialties are close to half remote, others closer to a third, and most remote roles are still tied to one country.&lt;/p&gt; &lt;h2&gt; Remote share by specialty &lt;/h2&gt; &lt;div class=&quot;table-

rss · Dev.to Career \(Resume &amp; Interview\) · 11月15日 15:19

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#职业发展`, `#远程办公`

---

<a id="item-tech-blog-13"></a>
### [EP233: Kubernetes Explained for Busy Engineers](https://blog.bytebytego.com/p/ep233-kubernetes-explained-for-busy) ⭐️ 5.0/10

为繁忙工程师准备的 Kubernetes 容器编排平台原理解析与应用指南。 来源内容补充：Kubernetes is an orchestration platform that manages the deployment and maintenance of containerized applications, particularly on multiple machines.

rss · ByteByteGo \(System Design &amp; Architecture\) · 11月14日 16:30

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#Kubernetes`, `#DevOps`, `#后端`

---

<a id="item-tech-blog-14"></a>
### [How to Do a Binary Search in Python](https://realpython.com/binary-search-python/) ⭐️ 5.0/10

本文介绍了如何在 Python 中使用 bisect 模块以及如何手写迭代和递归版本的二分查找算法。 来源内容补充：Use the bisect module to do a binary search in Python, then implement this classic algorithm yourself, both iteratively and recursively.

rss · Real Python \(Python &amp; Backend\) · 11月14日 14:00

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#Python`, `#算法`

---

<a id="item-tech-blog-15"></a>
### [Project Manager phần mềm thực chiến: Một cuốn sách miễn phí bằng cho người Việt](https://dev.to/phamtuanchip/project-manager-phan-mem-thuc-chien-mot-cuon-sach-mien-phi-bang-cho-nguoi-viet-1naa) ⭐️ 4.0/10

介绍一本面向软件开发者的免费中文软件项目管理实战书籍与案例研究。 来源内容补充：&lt;p&gt;Nếu bạn là dev lâu năm được &quot;đẩy lên&quot; làm PM, hoặc người mới muốn chuyển sang quản lý dự án phần mềm, có thể bạn từng gặp cảnh này: đọc xong vài bài về Scrum, Gantt, PMBOK, nhưng vào dự án thật vẫn không biết bắt đầu từ đâu — ai duyệt thay đổi, báo cáo cho sếp thế nào, khách đòi thêm tính năng thì trả lời ra sao, và tại sao dự án &quot;đang xanh&quot; bỗng nhiên trễ ba tháng.&lt;/p&gt; &lt;p&gt;Bài này nói ngắn gọn về vị trí PM, rồi gi

rss · Dev.to Career \(Resume &amp; Interview\) · 11月15日 14:53

**「下一步」** 查看原始来源，并按官方文档或项目说明核验后再试用。

**标签**: `#项目管理`, `#职业发展`

---