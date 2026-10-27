# 细胞周期从零学 · cell-cycle-from-zero

面向初学者的中文学习库：从细胞分裂周期出发，经 DNA 损伤应答、细胞命运，走到照射后骨骼肌的修复。

- **在线阅读**：<https://tuanziding.github.io/cell-cycle-from-zero/>（U00 思维卡片：<https://tuanziding.github.io/cell-cycle-from-zero/cards/u00-cards-v0.1.html>）
- **本地阅读**：直接用浏览器打开 `index.html`
- **操作**：←/→ 翻页，T 目录，R 切换阅读模式（手机默认阅读模式）

## 目录

```
index.html                 总览首页
assets/                    共用样式与翻页脚本（deck-v0.2.css / deck-v0.2.js）
units/                     学习单元（u00 总地图 …）
papers/                    经典文献拆解（p01 Hartwell 1970 …）
cards/                     思维卡片网页 + Anki 卡组
figures/                   AI 生成插图（无文字，标注在网页上叠加）
docs/                      资源清单、术语表、学习计划、版权约定
tools/                     生成单元页面的 Python 脚本
```

## 学习方法

工作日 45 分钟（读 25 → 闭卷回忆 10 → 卡片复习 10），周六 2 小时拆解文献，周日 1 小时费曼输出与自测。每个单元按同一页序：一页速览 → 背景与问题 → 机制图解 → 关键实验 → 今天的认识（事实 / 关联 / 推测）→ 与课题的关系 → 核心概念 → 费曼一段话 → 自测（按布鲁姆层级）→ 出处。

## 版权与许可

- 笔记与自绘图：CC BY 4.0；代码：MIT（见 `LICENSE`）
- 不收录出版社 PDF、论文原图、教材截图；示意图注明“自绘”或“AI 生成”；不复制原文图
- 详见 `docs/copyright-policy-v0.1.md`


## 思维卡片

`cards/u00-cards-v0.1.html`：单元 00 的可翻面思维卡片（按主题筛选、打乱、专注模式、本机记录掌握进度、可打印），由 `tools/build-u00-cards-v0.1.py` 从下方 Anki 文件生成。

`cards/u00-map-anki-v0.1.txt`：单元 00 的 30 个核心术语 + 6 道问答卡。Anki 桌面版“文件 → 导入”选择该文件即可，分隔符、HTML 与标签列（第 3 列）已在文件头声明。
