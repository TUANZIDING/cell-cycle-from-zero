import math
exec(open('tools/shell-v0.1.py').read())
def pt(frac,r,cx=330,cy=300):
    a=math.radians(-90+360*frac); return cx+r*math.cos(a), cy+r*math.sin(a)
def cycle_svg():
    o=['<svg viewBox="0 0 760 600" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans SC,PingFang SC,sans-serif">']
    o.append('<circle cx="330" cy="300" r="210" fill="none" stroke="#1B5FA8" stroke-width="10" opacity=".18"/>')
    # S phase arc 0-25%
    x1,y1=pt(0.02,210);x2,y2=pt(0.25,210)
    o.append(f'<path d="M{x1:.0f},{y1:.0f} A210,210 0 0 1 {x2:.0f},{y2:.0f}" stroke="#3F8BD6" stroke-width="10" fill="none"/>')
    labels=[(0.0,'出芽起始（周期起点）','#1B5FA8'),(0.13,'DNA 复制（前 25%）','#3F8BD6'),(0.5,'核分裂（约一半处）','#5B3F9E'),(0.9,'细胞分离','#2E9E7A')]
    for f,t,c in labels:
        x,y=pt(f,210);o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{c}"/>')
        lx,ly=pt(f,262);anchor='start' if lx>330 else ('end' if lx<330 else 'middle')
        if f==0.0: anchor='middle'; ly-=4
        o.append(f'<text x="{lx:.0f}" y="{ly+7:.0f}" font-size="21" fill="{c}" text-anchor="{anchor}" font-weight="600">{t}</text>')
    # execution point open box near bud initiation
    x,y=pt(0.02,170);o.append(f'<rect x="{x-11:.0f}" y="{y-11:.0f}" width="22" height="22" fill="#fff" stroke="#D9719C" stroke-width="4"/>')
    o.append(f'<text x="{x+18:.0f}" y="{y+30:.0f}" font-size="19" fill="#B04679">执行点（三个突变都在这里）</text>')
    # termination points
    x,y=pt(0.0,130);o.append(f'<rect x="{x-11:.0f}" y="{y-11:.0f}" width="22" height="22" fill="#D9719C"/>')
    o.append(f'<text x="{x:.0f}" y="{y+40:.0f}" font-size="18" fill="#3A4357" text-anchor="middle">cdc-1 终止：小芽、单核</text>')
    x,y=pt(0.5,170);o.append(f'<rect x="{x-11:.0f}" y="{y-11:.0f}" width="22" height="22" fill="#D9719C"/>')
    o.append(f'<text x="{x:.0f}" y="{y-24:.0f}" font-size="18" fill="#3A4357" text-anchor="middle">cdc-2 终止：有丝分裂</text>')
    o.append('<text x="330" y="318" font-size="18" fill="#667085" text-anchor="middle">cdc-3：无确定终止点</text>')
    o.append('<text x="330" y="342" font-size="16" fill="#667085" text-anchor="middle">（不分离，但出芽、核分裂照常）</text>')
    o.append('<path d="M600,140 a40,40 0 0 1 20,40" stroke="#667085" stroke-width="3" fill="none" marker-end="url(#ar)"/>')
    o.append('<defs><marker id="ar" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#667085"/></marker></defs>')
    o.append('<text x="630" y="130" font-size="16" fill="#667085">顺时针前进</text>')
    o.append('<rect x="560" y="470" width="20" height="20" fill="#fff" stroke="#D9719C" stroke-width="4"/><text x="590" y="487" font-size="17" fill="#3A4357">执行点</text>')
    o.append('<rect x="560" y="505" width="20" height="20" fill="#D9719C"/><text x="590" y="522" font-size="17" fill="#3A4357">终止点</text>')
    o.append('</svg>');return ''.join(o)
def cells_svg():
    # 三种终止形态示意
    def cell(cx,cy,r,fill='#DCE8F6'): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="#1B5FA8" stroke-width="3"/>'
    o=['<svg viewBox="0 0 1500 330" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans SC,PingFang SC,sans-serif">']
    # wt
    o+= [cell(110,140,52),cell(185,140,34),'<text x="140" y="250" font-size="22" text-anchor="middle" fill="#1C2333" font-weight="600">野生型</text>','<text x="140" y="282" font-size="18" text-anchor="middle" fill="#667085">芽持续长大，约 2.5 h 一代</text>']
    # cdc-1
    o+= [cell(470,140,58),cell(532,92,11),'<circle cx="465" cy="145" r="13" fill="#5B3F9E"/>','<text x="480" y="250" font-size="22" text-anchor="middle" fill="#1C2333" font-weight="600">cdc-1（369D-1）</text>','<text x="480" y="282" font-size="18" text-anchor="middle" fill="#667085">单细胞 + 不再长大的小芽，单核</text>']
    # cdc-2
    o+= [cell(790,140,55),cell(898,140,52),'<ellipse cx="845" cy="140" rx="34" ry="11" fill="#5B3F9E"/>','<text x="845" y="250" font-size="22" text-anchor="middle" fill="#1C2333" font-weight="600">cdc-2（370D-1）</text>','<text x="845" y="282" font-size="18" text-anchor="middle" fill="#667085">两个等大细胞，核卡在颈部（哑铃形）</text>']
    # cdc-3
    o+= [cell(1230,140,50),'<path d="M1270,110 q60,-40 110,-30" stroke="#1B5FA8" stroke-width="16" stroke-linecap="round" fill="none" opacity=".55"/>','<path d="M1275,160 q70,30 120,20" stroke="#1B5FA8" stroke-width="16" stroke-linecap="round" fill="none" opacity=".55"/>','<path d="M1210,92 q-20,-50 10,-80" stroke="#1B5FA8" stroke-width="16" stroke-linecap="round" fill="none" opacity=".55"/>','<circle cx="1220" cy="150" r="10" fill="#5B3F9E"/><circle cx="1245" cy="125" r="10" fill="#5B3F9E"/>','<text x="1260" y="250" font-size="22" text-anchor="middle" fill="#1C2333" font-weight="600">cdc-3（104D-1）</text>','<text x="1260" y="282" font-size="18" text-anchor="middle" fill="#667085">多个长突起、多核，最终裂解</text>']
    o.append('</svg>');return ''.join(o)

P=[]
P.append(('封面',f'''<div class="cover"><div class="k">经典文献拆解 · 第 1 站</div>
<h1>用“温度开关”<br>找出控制细胞分裂的<em>基因</em></h1>
<div class="sub">Hartwell LH, Culotti J, Reid B. Genetic control of the cell-division cycle in yeast, I. Detection of mutants.<br><i>Proc Natl Acad Sci USA</i> 1970; 66(2): 352–359 · PMID 5271168 · doi:10.1073/pnas.66.2.352 · PMC283051（开放获取）</div>
<div class="chips"><div><b>约 100 株</b>温度敏感突变株做了延时摄影</div><div><b>15 株</b>整群细胞停在周期的同一处</div><div><b>3 个基因</b>cdc-1、cdc-2、cdc-3 详细描述</div><div><b>2 个概念</b>执行点、终止点——全篇的灵魂</div></div></div>'''))
P.append(('一页速览','''<div class="hd"><div class="kick"><span class="no">01</span>一页速览</div><h2 class="t">一句话：把突变酵母从 23 °C 换到 36 °C，看它们“卡”在哪一步，就能把基因钉到细胞周期的具体时刻上</h2></div>
<div class="g2" style="grid-template-columns:1.35fr 1fr">
<div class="card box"><h3>三个突变的表现（36 °C）</h3><table class="t">
<tr><th style="width:22%">基因（株）</th><th style="width:26%">执行点</th><th>终止点与形态</th></tr>
<tr><td><b>cdc-1</b><br>369D-1</td><td>出芽起始前后</td><td>停在执行点：单细胞带一个不再长大的小芽、单核（压片后 ≥75% 可见小芽）</td></tr>
<tr><td><b>cdc-2</b><br>370D-1</td><td>出芽起始前后</td><td>停在有丝分裂：两个近等大细胞，核位于颈部，常呈哑铃形</td></tr>
<tr><td><b>cdc-3</b><br>104D-1</td><td>与前两者同期</td><td>无确定终止点：细胞不再分离，但出芽和核分裂继续，形成多突起、多核细胞，最终裂解</td></tr></table></div>
<div style="display:flex;flex-direction:column;gap:20px">
<div class="card box"><h3><span class="tag ok">值得学</span></h3><ul><li>用“芽的大小”当周期时钟，把形态变成时间读数</li><li>一个读数给出两个参数：执行点、终止点</li><li>每株追踪 100 个以上细胞，再用核染色、大小分布、显微操作补证</li></ul></div>
<div class="card box"><h3><span class="tag wn">要注意</span></h3><ul><li>只做到“表型”层面，不知道基因编码什么</li><li>1970 年的基因名与后来通用的名字不一一对应（见第 9 页）</li></ul></div></div></div>'''))
P.append(('背景与问题','''<div class="hd"><div class="kick"><span class="no">02</span>背景与科学问题</div><h2 class="t">事件的顺序早已知道，但“谁在安排顺序”完全是空白</h2></div>
<div class="g3">
<div class="card box"><span class="tag">已知</span><h3 style="margin-top:12px">芽殖酵母周期的时间表</h3><ul><li>出芽起始 = 周期起点</li><li>DNA 复制在周期前 25% 内完成</li><li>核分裂约在周期一半处、历时很短</li><li>最后细胞分离</li></ul></div>
<div class="card box"><span class="tag eo">空白</span><h3 style="margin-top:12px">基因与产物未知</h3><p>作者原话大意：保证事件有序推进的基因、它们的产物和功能“基本未知”。生化方法只能看到事件，看不到“开关”。</p></div>
<div class="card box"><span class="tag he">切入点</span><h3 style="margin-top:12px">为什么是温度敏感突变</h3><p>控制分裂的基因是必需基因，直接敲掉细胞就死了，没法研究。温度敏感突变在 23 °C 正常、36 °C 失灵，等于给基因装了一个可以随时按下的开关。</p></div></div>
<div class="card box" style="margin-top:22px"><p><b>临床类比：</b>像在手术流程里逐个“暂停”某个岗位——暂停器械护士，手术停在哪一步，就知道这个岗位在哪一步不可缺；如果手术停在更后面，说明这个岗位提前做了后面要用的准备。</p></div>'''))
P.append(('实验设计','''<div class="hd"><div class="kick"><span class="no">03</span>实验设计</div><h2 class="t">诱变 → 遗传学确认单基因 → 升温后延时摄影 → 三种补充测量</h2></div>
<div class="card box"><table class="t">
<tr><th style="width:18%">步骤</th><th>做法</th><th style="width:28%">回答的问题</th></tr>
<tr><td>诱变</td><td>亲本株 A364A，亚硝基胍诱变，得到单倍体温度敏感株 ts-369、ts-370、ts-104</td><td>有没有“卡周期”的突变</td></tr>
<tr><td>遗传分析</td><td>与非温敏株杂交、产孢、四分体解剖，每个缺陷 2:2 分离；再配成纯合二倍体 369D-1、370D-1、104D-1；对照二倍体 A364A D-4</td><td>是不是单个核基因</td></tr>
<tr><td>延时摄影</td><td>23 °C 对数生长的不同步细胞点到预热 36 °C 的平板，用不锈钢网格定位同一视野，36 °C 恒温下多时间点拍照；每株观察 100 个以上细胞</td><td>细胞在哪里停、从哪里开始受影响</td></tr>
<tr><td>大小分布</td><td>液体培养至全部到终止点，轻度超声后拍照，按芽/母细胞体积比分 6 类（原文 Fig. 3）</td><td>细胞分开了没有</td></tr>
<tr><td>核染色</td><td>Helly 固定，Giemsa 染核（原文 Fig. 4）</td><td>核分裂做了没有</td></tr>
<tr><td>显微操作</td><td>104D-1 取 44 个带小芽细胞，36 °C 6 h 后拆开数个体</td><td>cdc-3 能完成几次分离</td></tr></table></div>'''))
P.append(('核心概念图',f'''<div class="hd"><div class="kick"><span class="no">04</span>核心概念</div><h2 class="t">执行点 = 基因平时“干活”的时刻；终止点 = 不干活时细胞停下的地方</h2></div>
<div class="g2" style="grid-template-columns:1.2fr 1fr">
<div class="card fig">{cycle_svg()}<p class="cap">据原文 Fig. 5 的思路重绘示意，非原图。时间位置为示意。</p></div>
<div style="display:flex;flex-direction:column;gap:20px">
<div class="card box"><h3>判断执行点的逻辑</h3><p>升温那一刻，已经越过执行点的细胞能多走完一整圈再停；还没到执行点的细胞直接停在第一个终止点。看“谁多走了一圈”，就能反推出执行点的位置。</p></div>
<div class="card box"><h3>两点不重合的意义</h3><p>cdc-2 在周期早期“干活”，却在有丝分裂才表现出缺陷：早期做的事是后期事件的前提。这是“事件依赖关系”思想的起点。</p></div></div></div>'''))
P.append(('Fig.1–2 延时摄影',f'''<div class="hd"><div class="kick"><span class="no">05</span>逐图解读 · 原文 Fig. 1–2</div><h2 class="t">同一视野连续拍照：三个突变株在 36 °C 下各自停成一种形状</h2></div>
<div class="card fig">{cells_svg()}<p class="cap">据原文 Fig. 1–2 描述重绘的形态示意，非原图；紫色为细胞核。</p></div>
<div class="g3" style="margin-top:20px">
<div class="card box"><h3>cdc-1</h3><p>升温时已有芽的细胞把芽养大；升温后 1 h 内新出的少数芽也能长大，之后出的芽全部停在小芽。→ 出芽前有一步必须在许可温度下完成。</p></div>
<div class="card box"><h3>cdc-2</h3><p>无芽或极小芽的细胞停在“两个大细胞”；芽较大的细胞完成本轮、再出芽，停在“四个大细胞”。→ 执行点约在出芽起始时。</p></div>
<div class="card box"><h3>cdc-3</h3><p>已有芽的细胞正常发育；升温后新出的芽都异常，长成长突起，约每一代时间再长出一个。</p></div></div>'''))
P.append(('Fig.3–4 补充证据','''<div class="hd"><div class="kick"><span class="no">06</span>逐图解读 · 原文 Fig. 3–4 与显微操作</div><h2 class="t">形态之外，再量“分开没有”和“核分了没有”</h2></div>
<div class="g3">
<div class="card box"><span class="tag">Fig. 3 大小分布</span><h3 style="margin-top:12px">分开没有</h3><ul><li>369D-1：几乎全是单个细胞（可带小芽）</li><li>370D-1：几乎全是近等大的双联体 → 停在分离之前</li><li>104D-1：单个细胞带 1–5 个长突起，多数 3 个</li></ul></div>
<div class="card box"><span class="tag he">Fig. 4 Giemsa 核染色</span><h3 style="margin-top:12px">核分了没有</h3><ul><li>野生型约 500 个不同步细胞中 7% 处于核分裂，此时芽约为母细胞体积的 50%</li><li>369D-1：每个细胞 1 个核</li><li>370D-1：核在颈部，常呈哑铃形 → 停在有丝分裂</li><li>104D-1：可见多核 → 核分裂照常</li></ul></div>
<div class="card box"><span class="tag eo">显微操作</span><h3 style="margin-top:12px">cdc-3 分离几次</h3><p>44 个带小芽细胞在 36 °C 6 h 后：40 个分成 2 个细胞，3 个仍是 1 个，1 个分成 3 个。</p><p style="margin-top:8px">→ 多数完成当轮分离后，再也不分离。</p></div></div>'''))
P.append(('作者结论','''<div class="hd"><div class="kick"><span class="no">07</span>作者结论</div><h2 class="t">方法可推广，三个基因都在出芽附近执行，而且早期基因能决定晚期事件</h2></div>
<div class="g2">
<div class="card box"><h3>1. 一种通用的筛选方法</h3><p>只要某基因只在周期的一个阶段起作用，就能用这种方法找到；判据只是“越过某阶段的细胞比没越过的多走一圈”。</p></div>
<div class="card box"><h3>2. 执行点集中在出芽起始附近</h3><p>作者推想：从上次分裂到出芽之间，可能完成了“为后面整个周期编程”的许多功能。</p></div>
<div class="card box"><h3>3. 早执行、晚终止</h3><p>cdc-2、cdc-3 说明有些基因早早起作用，用来保证后面事件的完成——作者认为这可能对周期的有序推进很重要。</p></div>
<div class="card box"><h3>4. 事件之间可以拆开</h3><p>从 cdc-3 看，细胞分离不是出芽和核分裂的前提。这种突变可以用来解析事件之间的依赖关系。</p></div></div>'''))
P.append(('今天的认识','''<div class="hd"><div class="kick"><span class="no">08</span>今天的认识</div><h2 class="t">这篇开了“细胞周期遗传学”的头；结论 2 后来发展成 Start 概念</h2></div>
<div class="g3">
<div class="card box fact"><span class="tag ok">事实</span><ul style="margin-top:12px"><li>Hartwell 因细胞周期关键调控因子的发现，与 Hunt、Nurse 分享 2001 年诺贝尔生理学或医学奖</li><li>同一系列筛选后来找到 CDC28，即芽殖酵母的 CDK，与裂殖酵母 cdc2、人 CDK1 同源</li><li>Hartwell 1974 年在 <i>Science</i> 综述中用这些突变排出事件顺序，提出 Start（PMID 4587263）</li></ul></div>
<div class="card box assoc"><span class="tag">关联</span><ul style="margin-top:12px"><li>“出芽前完成编程”与哺乳动物的限制点（Pardee 1974）思路相通：过点之后，周期基本自动走完</li><li>“早期事件是后期前提”是后来检查点概念（Hartwell & Weinert 1989）的伏笔</li></ul></div>
<div class="card box spec"><span class="tag wn">命名陷阱与后续</span><ul style="margin-top:12px"><li>芽殖酵母的 CDC2 ≠ 裂殖酵母的 cdc2：后者才是 CDK</li><li>芽殖酵母 CDC2 编码 DNA 聚合酶 III（今称 δ）大亚基（Boulet 1989，PMID 2670563）——难怪 cdc-2 停在有丝分裂前：DNA 没复制完</li><li>CDC3 产物定位在母芽颈部，属隔膜蛋白（septin）家族（Kim 1991，PMID 1993729）——解释了“不能分离”</li></ul></div></div>'''))
P.append(('与课题的关系','''<div class="hd"><div class="kick"><span class="no">09</span>与辐射骨骼肌课题的关系</div><h2 class="t">“扰动后看细胞停在哪”的逻辑，可以直接搬到照射实验里</h2></div>
<div class="g2">
<div class="card box"><h3>可以借的思路</h3><ul><li>照射就像升温：一个时间点上的统一扰动</li><li>问题从“照射后细胞少了多少”变成“停在哪个时期、能不能多走一圈”</li><li>读数：DNA 含量流式、EdU 掺入、p21 免疫染色，对应形态学里的芽大小和核位置</li></ul></div>
<div class="card box"><h3>需要分清的地方</h3><ul><li>肌纤维已经不分裂，周期问题主要在卫星细胞和 FAP 等单个核细胞</li><li>静息卫星细胞处于 G0，照射时“在周期哪一点”与增殖期细胞不同</li><li>放射生物学经典结论：细胞对射线的敏感性随周期时相变化，G2/M 较敏感，S 期后段较耐受（Terasima & Tolmach，<i>Biophys J</i> 1963，PMID 13980635）</li></ul></div></div>
<div class="card box" style="margin-top:22px"><p><b>一个可检验的小问题：</b>照射后 24 h，激活中的卫星细胞主要堆在 G1 还是 G2/M？如果 p21 升高为主，预期更多停在 G1——这属于推测，需要实验回答。</p></div>'''))
P.append(('核心概念','''<div class="hd"><div class="kick"><span class="no">10</span>读懂这篇需要的 10 个概念</div><h2 class="t">中英对照，先背定义，再用自己的话复述</h2></div>
<div class="card box"><table class="t">
<tr><th style="width:24%">术语</th><th>一句话</th><th style="width:24%">术语</th><th>一句话</th></tr>
<tr><td>温度敏感突变 temperature-sensitive (ts)</td><td>许可温度下正常，限制温度下失灵</td><td>许可/限制温度 permissive / restrictive</td><td>本文为 23 °C / 36 °C</td></tr>
<tr><td>执行点 execution point</td><td>基因功能平时被完成的时刻</td><td>终止点 termination point</td><td>功能缺失时细胞停下的阶段</td></tr>
<tr><td>cdc 突变 cell division cycle</td><td>阻断周期特定步骤的突变</td><td>出芽 budding</td><td>芽殖酵母的分裂方式，芽大小反映周期进度</td></tr>
<tr><td>延时摄影 time-lapse photomicroscopy</td><td>同一视野按时间连续拍照</td><td>四分体分析 tetrad analysis</td><td>解剖孢子看性状是否 2:2 分离</td></tr>
<tr><td>不同步培养 asynchronous culture</td><td>细胞分散在周期各个位置</td><td>Start</td><td>后来命名的芽殖酵母 G1 晚期承诺点</td></tr></table></div>'''))
P.append(('费曼与自测','''<div class="hd"><div class="kick"><span class="no">11</span>费曼一段话 + 自测题</div><h2 class="t">讲给实习生听：先说比喻，再按布鲁姆层级检验</h2></div>
<div class="g2" style="grid-template-columns:1fr 1.25fr">
<div class="card box"><h3>费曼一段话</h3><p>“每个酵母细胞身上长着一个芽，芽越大说明它在分裂流程里走得越远。Hartwell 找到一些坏了开关的酵母，一加热某个步骤就失灵。他把加热后的细胞一直拍下来，看它们最后都停成什么样，就知道这个开关管哪一步；再看哪些细胞还能多走一圈，就知道这个开关平时在什么时候打开。”</p></div>
<div class="card box"><h3>自测</h3>
<p><span class="lv">记忆</span>执行点和终止点分别指什么？</p><details><summary>答案</summary><p>执行点：基因功能平时完成的时刻；终止点：功能缺失时细胞停下的阶段。</p></details>
<p style="margin-top:8px"><span class="lv">理解</span>为什么必须用温度敏感突变？</p><details><summary>答案</summary><p>周期基因是必需基因，普通功能缺失突变无法存活；ts 突变能在许可温度下保种，再按需关掉。</p></details>
<p style="margin-top:8px"><span class="lv">应用</span>某突变株升温后，无芽细胞停在“两个大细胞”，大芽细胞停在“四个大细胞”。执行点在哪？</p><details><summary>答案</summary><p>约在出芽起始时：大芽细胞已越过它，多走了一圈（即 cdc-2 的表现）。</p></details>
<p style="margin-top:8px"><span class="lv">分析</span>cdc-3 说明了哪两个事件互不依赖？</p><details><summary>答案</summary><p>细胞分离与出芽、核分裂：不分离时后两者照常进行。</p></details>
<p style="margin-top:8px"><span class="lv">评价</span>仅凭形态判断终止点，最大的漏洞是什么？作者怎么补的？</p><details><summary>答案</summary><p>形态分不清“分开没有”“核分了没有”；作者补了液体培养大小分布、Giemsa 核染色和显微操作。</p></details></div></div>'''))
P.append(('出处与延伸','''<div class="hd"><div class="kick"><span class="no">12</span>出处与延伸阅读</div><h2 class="t">原文开放获取；下一站读 Hartwell 1974 和 Pardee 1974</h2></div>
<div class="g2">
<div class="card box"><h3>本文</h3><p>Hartwell LH, Culotti J, Reid B. <i>Proc Natl Acad Sci USA</i> 1970;66(2):352–359.<br>PMID <a href="https://pubmed.ncbi.nlm.nih.gov/5271168/">5271168</a> · doi:<a href="https://doi.org/10.1073/pnas.66.2.352">10.1073/pnas.66.2.352</a> · <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC283051/">PMC283051 全文</a></p>
<p class="src">本页所有数字均取自原文正文；图为据原文描述重绘的示意图，未复制原图。</p></div>
<div class="card box"><h3>延伸</h3><ul>
<li>Hartwell LH 等. Genetic control of the cell division cycle in yeast. <i>Science</i> 1974. PMID <a href="https://pubmed.ncbi.nlm.nih.gov/4587263/">4587263</a></li>
<li>Pardee AB. A restriction point for control of normal animal cell proliferation. <i>PNAS</i> 1974. PMID <a href="https://pubmed.ncbi.nlm.nih.gov/4524638/">4524638</a></li>
<li>Hartwell LH, Weinert TA. Checkpoints. <i>Science</i> 1989. PMID <a href="https://pubmed.ncbi.nlm.nih.gov/2683079/">2683079</a></li>
<li>2001 年诺贝尔奖：<a href="https://www.nobelprize.org/prizes/medicine/2001/summary/">nobelprize.org</a></li></ul></div></div>'''))
secs=[]
for i,(t,body) in enumerate(P):
    secs.append(f'<section class="page" data-title="{t}">\n{body}\n</section>')
open('papers/p01-hartwell1970-cdc-mutants-v0.1.html','w').write(wrap('Hartwell 1970 · cdc 突变体 · 文献拆解','文献 01 · Hartwell 1970','\n'.join(secs)))
print('ok',len(P))
