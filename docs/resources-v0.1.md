# 细胞周期从零学：资源清单与仓库结构 v0.1
核实日期：2026-10-27（PubMed E-utilities 核 PMID/DOI/年份/期刊；Unpaywall 核开放获取；GitHub API 核 star/最近推送/许可证；BioModels API 核模型条目）

## 结论先行
- 入门主线：Alberts《MBoC》第17章（第4版 NCBI Bookshelf 免费）→ Morgan《The Cell Cycle》（作者实验室官网免费 PDF，绝版）→ 按下方 22 篇路线读原文。
- OpenStax Biology 2e 第10章现为 CC BY-NC-SA 4.0，且明确禁止被大模型摄取；只放链接，不搬运图文。
- GitHub 没有高 star 的“细胞周期教学”专门仓库；最靠谱的模型来源是 BioModels 的 Tyson/Novak/Chen 经典 SBML，用 tellurium 运行。
- 可复用图库：Servier Medical Art（CC BY 4.0）、Reactome 图示与图标（CC BY 4.0）、Bioicons（逐图标看许可）。

## 一、书籍/教材
| 书 | 版本/年份 | 细胞周期章节 | 水平 | 免费合法版本 |
|---|---|---|---|---|
| Morgan, The Cell Cycle: Principles of Control | 2007, New Science Press（唯一版，已绝版） | 全书 | 进阶主教材 | 有：Morgan Lab (UCSF) 官网提供全书 PDF 下载 https://morganlab.ucsf.edu/cell-cycle-principles-control（只链接，不放进仓库） |
| Alberts 等, Molecular Biology of the Cell | 第7版 2022, W. W. Norton（作者含 Morgan） | Ch.17 The Cell Cycle（据课程大纲） | 入门→中级 | 第4版 2002（Garland）在 NCBI Bookshelf：NBK21054，Ch.17 The Cell Cycle and Programmed Cell Death（NBK21056） |
| Lodish 等, Molecular Cell Biology | 第9版 2021, Macmillan | Ch.19 The Eukaryotic Cell Cycle | 中级（实验逻辑强） | 第4版 2000 在 Bookshelf：NBK21475，Ch.13 Regulation of the Eukaryotic Cell Cycle（NBK21468） |
| Cooper, The Cell: A Molecular Approach | 第2版 2000, Sinauer | Ch.14 The Cell Cycle | 入门 | Bookshelf：NBK9839，Ch.14（NBK9876） |
| OpenStax, Biology 2e | 2018 起在线更新 | Ch.10 Cell Reproduction（10.2 周期、10.3 调控、10.4 癌症） | 零基础 | 免费在线，CC BY-NC-SA 4.0，禁止 LLM 摄取 |
| Nobel 2001 官网资料 | 2001 | 授奖理由与三位得主讲座 | 入门 | https://www.nobelprize.org/prizes/medicine/2001/summary/ |
注：Bookshelf 老版教材“只能检索、不能整本浏览”，用上面的 NBK 链接直达。旧版知识框架仍对，但 APC/C、SAC 分子细节以新版和近年综述为准。

## 二、经典文献阅读路线（22 站，配对文献同站读）
OA 列来自 Unpaywall（2026-10-27）；“未检出”不等于完全看不到，可走学校图书馆。难度 ★ 易 / ★★ 中 / ★★★ 难。

### 阶段0 地图
| # | 文献 | PMID | DOI | OA | 难度 | 核心问题 / 关键实验 / 为何经典 |
|---|---|---|---|---|---|---|
| 0 | Nurse PM. Nobel Lecture: Cyclin dependent kinases and cell cycle control. Biosci Rep 2002;22:487-99 | 12635846 | 10.1023/a:1022017701871 | 期刊版未检出；Nobel 官网有讲座资料 | ★ | 得主本人讲全景，先建立地图 |

### 阶段1 发现“控制系统”（1970–1976）
| # | 文献 | PMID | DOI | OA | 难度 | 核心问题 / 关键实验 / 为何经典 |
|---|---|---|---|---|---|---|
| 1 | Hartwell LH 等. Genetic control of the cell-division cycle in yeast. I. Detection of mutants. PNAS 1970;66:352-9 | 5271168 | 10.1073/pnas.66.2.352 | 是（PMC283051） | ★★ | 能否用遗传学拆解分裂？温度敏感 cdc 突变体筛选；开创细胞周期遗传学 |
| 2 | Masui Y, Markert CL. Cytoplasmic control of nuclear behavior during meiotic maturation of frog oocytes. J Exp Zool 1971;177:129-45 | 5106340 | 10.1002/jez.1401770202 | 未检出 | ★★ | 胞质里有无驱动成熟的因子？卵母细胞胞质显微注射；提出 MPF |
| 3 | Hartwell LH 等. Genetic control of the cell division cycle in yeast. Science 1974;183:46-51 | 4587263 | 10.1126/science.183.4120.46 | 未检出 | ★★ | 事件之间是否有依赖顺序？cdc 突变体排序；提出 Start 与依赖通路 |
| 4 | Pardee AB. A restriction point for control of normal animal cell proliferation. PNAS 1974;71:1286-90 | 4524638 | 10.1073/pnas.71.4.1286 | 是（PMC388211） | ★ | 哺乳动物细胞何时“下决心”分裂？营养/血清撤除实验；提出限制点 R |
| 5 | Nurse P. Genetic control of cell size at cell division in yeast. Nature 1975;256:547-51 | 1165770 | 10.1038/256547a0 | 未检出 | ★★ | 大小如何控制分裂时机？wee 突变体；把细胞大小与 G2/M 连起来 |
| 6 | Nurse P, Thuriaux P, Nasmyth K. Genetic control of the cell division cycle in the fission yeast S. pombe. Mol Gen Genet 1976;146:167-78 | 958201 | 10.1007/BF00268085 | 未检出 | ★★★ | 裂殖酵母 cdc 系统筛选；cdc2 登场 |

### 阶段2 找到分子本体（1983–1991）
| # | 文献 | PMID | DOI | OA | 难度 | 核心问题 / 关键实验 / 为何经典 |
|---|---|---|---|---|---|---|
| 7 | Evans T, …, Hunt T. Cyclin: a protein specified by maternal mRNA in sea urchin eggs that is destroyed at each cleavage division. Cell 1983;33:389-96 | 6134587 | 10.1016/0092-8674(83)90420-8 | 未检出 | ★ | 哪种蛋白随分裂周期升降？海胆卵 35S 标记电泳；发现 cyclin |
| 8 | Lee MG, Nurse P. Complementation used to clone a human homologue of the fission yeast cell cycle control gene cdc2. Nature 1987;327:31-5 | 3553962 | 10.1038/327031a0 | 未检出 | ★★ | 人类有没有同一个开关？人 cDNA 互补酵母突变；证明机制跨物种保守（CDK1） |
| 9 | Lohka MJ, Hayes MK, Maller JL. Purification of maturation-promoting factor… PNAS 1988;85:3009-13 | 3283736 | 10.1073/pnas.85.9.3009 | 是（PMC280132） | ★★ | MPF 是什么？爪蟾卵生化纯化 |
| 10 | Gautier J 等. Purified MPF contains the product of a Xenopus homolog of cdc2+. Cell 1988;54:433-9 | 3293803 | 10.1016/0092-8674(88)90206-1 | 未检出 | ★★ | 遗传学（cdc2）与生化（MPF）在此会师 |
| 11 | Murray AW, Kirschner MW. Cyclin synthesis drives the early embryonic cell cycle. Nature 1989;339:275-80 | 2566917 | 10.1038/339275a0 | 未检出 | ★★ | cyclin 合成是否足以驱动周期？无细胞卵提取物+mRNA 去除/回补；建立周期振荡器概念 |
| 12 | Glotzer M, Murray AW, Kirschner MW. Cyclin is degraded by the ubiquitin pathway. Nature 1991;349:132-8 | 1846030 | 10.1038/349132a0 | 未检出 | ★★ | cyclin 怎么被清掉？泛素化+destruction box |

### 阶段3 检查点
| # | 文献 | PMID | DOI | OA | 难度 | 核心问题 / 关键实验 / 为何经典 |
|---|---|---|---|---|---|---|
| 13 | Weinert TA, Hartwell LH. The RAD9 gene controls the cell cycle response to DNA damage in S. cerevisiae. Science 1988;241:317-22 | 3291120 | 10.1126/science.3291120 | 未检出 | ★★ | 损伤后停顿是被动还是主动？rad9 突变体照射后不停顿而死亡；第一个检查点基因 |
| 14 | Hartwell LH, Weinert TA. Checkpoints: controls that ensure the order of cell cycle events. Science 1989;246:629-34 | 2683079 | 10.1126/science.2683079 | 未检出 | ★ | 概念性论文，提出 checkpoint 一词与框架 |
| 15 | Hoyt MA 等. S. cerevisiae genes required for cell cycle arrest in response to loss of microtubule function. Cell 1991;66:507-17 ＋ 配对 Li R, Murray AW. Feedback control of mitosis in budding yeast. Cell 1991;66:519-31 | 1651171 / 1651172 | 10.1016/0092-8674(81)90014-3 / 10.1016/0092-8674(81)90015-5（PubMed 原样记录的 DOI，前缀看似 1981 属出版商旧编码） | Hoyt 是（CC BY-NC-ND）；Li 未检出 | ★★★ | 纺锤体组装检查点：BUB 与 MAD 基因背靠背发表 |

### 阶段4 APC/C
| # | 文献 | PMID | DOI | OA | 难度 | 核心问题 |
|---|---|---|---|---|---|---|
| 16 | King RW 等. A 20S complex containing CDC27 and CDC16 catalyzes the mitosis-specific conjugation of ubiquitin to cyclin B. Cell 1995;81:279-88 ＋ 配对 Sudakin V 等. The cyclosome… Mol Biol Cell 1995;6:185-97 | 7736580 / 7787245 | 10.1016/0092-8674(95)90338-0 / 10.1091/mbc.6.2.185 | 均是 | ★★★ | 谁给 cyclin 打泛素标签？两组独立鉴定 APC/C（cyclosome） |

### 阶段5 哺乳动物 G1、肿瘤抑制
| # | 文献 | PMID | DOI | OA | 难度 | 核心问题 |
|---|---|---|---|---|---|---|
| 17 | el-Deiry WS 等. WAF1, a potential mediator of p53 tumor suppression. Cell 1993;75:817-25 ＋ 配对 Harper JW 等. The p21 Cdk-interacting protein Cip1… Cell 1993;75:805-16 | 8242752 / 8242751 | 10.1016/0092-8674(93)90500-p / 10.1016/0092-8674(93)90499-g | el-Deiry 是；Harper 未检出 | ★★ | p53 如何让细胞停？p21 作为 CDK 抑制剂，同期两篇 |
| 18 | Serrano M, Hannon GJ, Beach D. A new regulatory motif in cell-cycle control causing specific inhibition of cyclin D/CDK4. Nature 1993;366:704-7 | 8259215 | 10.1038/366704a0 | 未检出 | ★★ | p16INK4a 发现；INK4 家族 |
| 19 | Weinberg RA. The retinoblastoma protein and cell cycle control. Cell 1995;81:323-30（综述） | 7736585 | 10.1016/0092-8674(95)90385-2 | 是（bronze） | ★ | Rb 作为限制点的分子刹车 |
| 20 | Dyson N. The regulation of E2F by pRB-family proteins. Genes Dev 1998;12:2245-62 ＋ Sherr CJ, Roberts JM. CDK inhibitors: positive and negative regulators of G1-phase progression. Genes Dev 1999;13:1501-12 | 9694791 / 10385618 | 10.1101/gad.12.15.2245 / 10.1101/gad.13.12.1501 | 均是 | ★★ | Rb/E2F 与 CKI 两张网的标准综述 |

### 阶段6 现代视角
| # | 文献 | PMID | DOI | OA | 难度 | 核心问题 |
|---|---|---|---|---|---|---|
| 21 | Spencer SL 等. The proliferation-quiescence decision is controlled by a bifurcation in CDK2 activity at mitotic exit. Cell 2013;155:369-83 | 24075009 | 10.1016/j.cell.2013.08.062 | 是（PMC4001917） | ★★★ | 活细胞 CDK2 传感器；修正“限制点只在 G1 中段”的教科书图景 |
| 22 | Basu S, …, Nurse P. Core control principles of the eukaryotic cell cycle. Nature 2022;607:381-6 | 35676478 | 10.1038/s41586-022-04798-8 | 是（CC BY） | ★★★ | 单一 CDK 活性阈值能否解释周期顺序？ |

### 近年高质量综述（按需查）
| 文献 | PMID | DOI | OA |
|---|---|---|---|
| Matthews HK, Bertoli C, de Bruin RAM. Cell cycle control in cancer. Nat Rev Mol Cell Biol 2022;23:74-88 | 34508254 | 10.1038/s41580-021-00404-3 | 未检出 |
| Musacchio A. The molecular biology of spindle assembly checkpoint signaling dynamics. Curr Biol 2015;25:R1002-18 | 26485365 | 10.1016/j.cub.2015.08.051 | 是 |
| Swaffer MP 等. CDK substrate phosphorylation and ordering the cell cycle. Cell 2016;167:1750-61 | 27984725 | 10.1016/j.cell.2016.11.034 | 是（CC BY） |
| Pines J. Cubism and the cell cycle: the many faces of the APC/C. Nat Rev Mol Cell Biol 2011;12:427-38 | 21633387 | 10.1038/nrm3132 | 未检出 |
| Musacchio A, Salmon ED. The spindle-assembly checkpoint in space and time. Nat Rev Mol Cell Biol 2007;8:379-93 | 17426725 | 10.1038/nrm2163 | 未检出 |
| Morgan DO. Cyclin-dependent kinases: engines, clocks, and microprocessors. Annu Rev Cell Dev Biol 1997;13:261-91 | 9442875 | 10.1146/annurev.cellbio.13.1.261 | 未检出 |
| Kastan MB, Bartek J. Cell-cycle checkpoints and cancer. Nature 2004;432:316-23 | 15549093 | 10.1038/nature03097 | 未检出 |
| Massagué J. G1 cell-cycle control and cancer. Nature 2004;432:298-306 | 15549091 | 10.1038/nature03094 | 未检出 |
| Malumbres M, Barbacid M. Cell cycle, CDKs and cancer: a changing paradigm. Nat Rev Cancer 2009;9:153-66 | 19238148 | 10.1038/nrc2602 | 未检出 |
| Yang HW 等. Competing memories of mitogen and p53 signalling control cell-cycle entry. Nature 2017;549:404-8 | 28869970 | 10.1038/nature23880 | 是 |
| Coudreuse D, Nurse P. Driving the cell cycle with a minimal CDK control network. Nature 2010;468:1074-9 | 21179163 | 10.1038/nature09543 | 未检出 |

### 数学模型论文（配合 models/ 目录）
| 文献 | PMID | DOI | OA | BioModels |
|---|---|---|---|---|
| Tyson JJ. Modeling the cell division cycle: cdc2 and cyclin interactions. PNAS 1991;88:7328-32 | 1831270 | 10.1073/pnas.88.16.7328 | 是 | BIOMD0000000005（Tyson1991 - Cell Cycle 6 var） |
| Novak B, Tyson JJ. Numerical analysis of a comprehensive model of M-phase control in Xenopus… J Cell Sci 1993;106:1153-68 | 8126097 | 10.1242/jcs.106.4.1153 | 未检出 | BIOMD0000000107 |
| Chen KC 等. Integrative analysis of cell cycle control in budding yeast. Mol Biol Cell 2004;15:3841-62 | 15169868 | 10.1091/mbc.e03-11-0794 | 是 | BIOMD0000000056 |
| Ferrell JE Jr 等. Modeling the cell cycle: why do certain circuits oscillate? Cell 2011;144:874-85 | 21414480 | 10.1016/j.cell.2011.03.006 | 是 | — |

## 三、开源项目与可视化资源（GitHub 数据 2026-10-27）
| 项目 | 用途 | ★ | 最近推送 | 许可证 | 备注 |
|---|---|---|---|---|---|
| scverse/scanpy | 单细胞分析（含细胞周期打分） | 2595 | 2026-10-26 | BSD-3 | 进阶，做组学时用 |
| duerrsimon/bioicons | 科学插图图标库 | 1778 | 2026-10-23 | 仓库 MIT | 图标逐个有各自许可，用前看单个图标 |
| MathCancer/PhysiCell | 多细胞模拟（内置周期模型） | 217 | 2026-10-02 | GitHub 未识别 | 用前看仓库内 LICENSE |
| SchmollerLab/Cell_ACDC | 显微图像分割追踪+周期注释 | 204 | 2026-10-26 | BSD-3 | 进阶 |
| pysb/pysb | 规则建模框架 | 201 | 2026-05-19 | BSD-2 | 进阶 |
| sys-bio/tellurium | Python 运行 SBML/Antimony 模型 | 148 | 2026-08-29 | Apache-2.0 | 首选：跑 Tyson1991 |
| copasi/COPASI | 图形化生化网络模拟 | 132 | 2026-10-26 | Artistic-2.0 | 不写代码也能跑模型 |
| CompuCell3D/CompuCell3D | 多细胞仿真 | 84 | 2026-10-11 | MIT | 进阶 |
| sys-bio/roadrunner | SBML 高速模拟引擎 | 64 | 2026-10-24 | GitHub 未识别 | tellurium 的底层 |
| andreariba/DeepCycle | scRNA-seq 推断周期 | 52 | 2023-04-25 | GPL-3.0 | 停更 3 年 |
| LoLab-MSM/pyvipr | Jupyter 中可视化模型 | 28 | 2023-03-13 | MIT | 停更 |
| YangLab-um/interactive-cell-cycle | 交互式周期模型网页 | 0 | 2023-10-31 | MIT | star 低但正对主题，可参考 |
模型库：BioModels（上表三个条目已核实存在）。

可复用图示：
| 来源 | 许可 | 仓库里能怎么用 |
|---|---|---|
| Servier Medical Art（smart.servier.com） | CC BY 4.0 | 可放入、可改，须署名 |
| Reactome 通路图示/图标库 | CC BY 4.0（数据 CC0） | 可放入，须署名并注明修改 |
| Bioicons | 逐图标许可（CC0/CC BY/BSD 等） | 只用 CC0/CC BY 的，逐个记录 |
| Wikimedia Commons | 逐文件许可 | 只用 CC BY/CC0/公有领域，记录作者 |
| OpenStax Biology 2e | CC BY-NC-SA 4.0＋禁止 LLM 摄取 | 只放链接 |
| 教材/论文原图、Bookshelf 图 | 出版社版权 | 不放；用 Mermaid/SVG 自绘“示意” |

## 四、公开仓库版权规则
1. 不放出版社 PDF（含 Morgan 免费 PDF，只给官网链接）、不放论文原图、不放教材截图。
2. 关键图解读用自己的话＋自绘示意图，并标注“据 X 文献 Fig.N 重绘示意，非原图”。
3. 引用原文每处不超过一两句，标出处。
4. 第三方 CC BY 素材集中登记在 figures/credits-v0.1.md。
5. 建议许可：笔记与图 CC BY 4.0，代码 MIT（双许可写在 README）。

## 五、仓库结构草案
```
cell-cycle-from-zero/
├── README.md                     # 项目说明、学习路线入口、许可说明
├── LICENSE                       # 约定俗成文件名（需你确认是否豁免版本号）
├── docs/
│   ├── roadmap-v0.1.md           # 学习路线与进度
│   ├── resources-v0.1.md         # 本资源清单
│   ├── glossary-v0.1.md          # 中英术语表
│   └── copyright-policy-v0.1.md  # 版权规则
├── chapters/
│   ├── 00-overview/cell-cycle-overview-v0.1.md
│   ├── 01-g1-phase/
│   ├── 02-s-phase/
│   ├── 03-g2-phase/
│   ├── 04-m-phase/
│   ├── 05-cdk-cyclin-network/
│   ├── 06-checkpoints/
│   ├── 07-cell-cycle-and-cancer/
│   └── 08-history-and-nobel/
├── papers/
│   ├── paper-template-v0.1.md
│   ├── reading-list-v0.1.md
│   └── 1970-hartwell-cdc-mutants-v0.1.md
├── figures/
│   ├── mermaid/
│   ├── svg/
│   └── credits-v0.1.md
├── models/
│   ├── README.md
│   └── tyson1991/                # 后续：tellurium 运行 BIOMD0000000005
└── quizzes/
    └── chapter00-quiz-v0.1.md
```

## 六、文献拆解模板
元信息（引用、PMID、DOI、OA、难度、阅读日期）→ 一句话结论 → 背景（当时不知道什么）→ 核心问题 → 实验设计（模型系统、对照、读出指标）→ 关键图解读（逐图：问了什么、看到什么、说明什么；自绘示意）→ 作者结论 → 今天的认识（事实 / 关联 / 推测 分开写）→ 自测题 5 道（答案折叠）→ 延伸阅读。
