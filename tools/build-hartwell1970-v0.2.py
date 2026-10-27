exec(open('tools/shell-v0.2.py').read()); exec(open('tools/svgkit-v0.2.py').read())
FIG='../figures/'
def timeline_svg():
    p='tl'
    X={'bud':330,'dna':560,'mit':960,'sep':1350}
    o=[f'<svg viewBox="0 0 1680 500" style="max-height:430px;display:block;margin:auto" width="100%" font-family="Noto Sans SC,PingFang SC,sans-serif">',defs(p)]
    # 顶部周期轨道
    o.append(f'<rect x="200" y="148" width="1360" height="14" rx="7" fill="{BLUE3}"/>')
    o.append(f'<rect x="{X["bud"]}" y="148" width="{X["dna"]-X["bud"]+60}" height="14" rx="7" fill="{BLUE2}" opacity=".55"/>')
    icons=[(X['bud'],1,'m','出芽起始','周期起点'),(X['dna'],2,'m','DNA 复制','前 25% 完成'),(X['mit'],3,'neck','核分裂','约周期一半'),(X['sep'],None,None,'细胞分离','周期终点')]
    for x,b,n,t,s in icons:
        if b is None: o.append(yeast(p,x,80,sep=True,sc=.9))
        else: o.append(yeast(p,x-14,80,bud=b,nuc=n,sc=.9))
        o.append(f'<circle cx="{x}" cy="155" r="11" fill="#fff" stroke="{BLUE}" stroke-width="4"/>')
        o.append(f'<text x="{x}" y="200" font-size="22" font-weight="700" fill="{INK}" text-anchor="middle">{t}</text>')
        o.append(f'<text x="{x}" y="226" font-size="17" fill="{MUTE}" text-anchor="middle">{s}</text>')
    o.append(f'<text x="200" y="128" font-size="17" fill="{MUTE}">一个细胞周期（芽殖酵母，示意）→</text>')
    lanes=[('cdc-1','369D-1',X['bud'],'停在执行点：小芽、单核',EO,False),('cdc-2','370D-1',X['mit'],'停在有丝分裂：等大双联体，核卡在颈部',HE,False),('cdc-3','104D-1',X['sep'],'不分离，但出芽、核分裂继续 → 无确定终止点',WARN,True)]
    for i,(g,st,tx,desc,c,open_) in enumerate(lanes):
        y=272+i*84
        o.append(f'<rect x="20" y="{y-38}" width="1640" height="76" rx="22" fill="url(#{p}card)" stroke="#E3E9F2" filter="url(#{p}sh)"/>')
        o.append(f'<text x="50" y="{y-4}" font-size="26" font-weight="700" fill="{c}" font-style="italic">{g}</text>')
        o.append(f'<text x="50" y="{y+22}" font-size="16" fill="{MUTE}">{st}</text>')
        x0=X['bud']
        if tx>x0:
            dash=' stroke-dasharray="2 0"'
            o.append(f'<line x1="{x0}" y1="{y}" x2="{tx-18}" y2="{y}" stroke="{c}" stroke-width="7" stroke-linecap="round" opacity=".35"/>')
            if open_: pass
        if open_:
            o.append(f'<path d="M{tx+20},{y} q50,-30 100,0 t100,0" stroke="{c}" stroke-width="4" fill="none" stroke-dasharray="7 7"/>')
        # 执行点（空心菱形）
        o.append(f'<rect x="{x0-13}" y="{y-13}" width="26" height="26" transform="rotate(45 {x0} {y})" fill="#fff" stroke="{c}" stroke-width="4"/>')
        if not open_:
            o.append(f'<circle cx="{tx}" cy="{y}" r="22" fill="{c}" opacity=".18" filter="url(#{p}gl)"/>')
            o.append(f'<circle cx="{tx}" cy="{y}" r="14" fill="{c}"/>' if tx!=x0 else f'<circle cx="{tx}" cy="{y}" r="7" fill="{c}"/>')
        dx=tx+(40 if not open_ else 260)
        if tx==x0: dx=x0+40
        anchor='start'
        if dx>1300 and not open_: dx=tx-36; anchor='end'
        if open_:
            o.append(f'<rect x="{X["dna"]-10}" y="{y-20}" width="470" height="40" rx="20" fill="#fff" stroke="{c}" stroke-opacity=".35"/>')
            o.append(f'<text x="{X["dna"]+225}" y="{y+7}" font-size="20" fill="{INK2}" text-anchor="middle">{desc}</text>')
            o.append(f'<circle cx="{tx}" cy="{y}" r="14" fill="#fff" stroke="{c}" stroke-width="4"/><line x1="{tx-9}" y1="{y+9}" x2="{tx+9}" y2="{y-9}" stroke="{c}" stroke-width="4"/>')
        else:
            o.append(f'<text x="{dx}" y="{y+7}" font-size="20" fill="{INK2}" text-anchor="{anchor}">{desc}</text>')
    # 图例
    o.append(f'<rect x="{X["bud"]-160}" y="582" width="0" height="0"/>')
    o.append(f'<g transform="translate(1040,-130)"><rect x="0" y="-9" width="18" height="18" transform="translate(9,250) rotate(45 0 0)" fill="#fff" stroke="{INK2}" stroke-width="3"/><text x="30" y="257" font-size="17" fill="{INK2}">执行点：基因平时干活的时刻</text>'
             f'<circle cx="300" cy="250" r="9" fill="{INK2}"/><text x="316" y="257" font-size="17" fill="{INK2}">终止点</text></g>')
    o.append('</svg>');return ''.join(o)
def logic_svg():
    p='lg'
    o=[f'<svg viewBox="0 0 860 430" width="100%" font-family="Noto Sans SC,PingFang SC,sans-serif">',defs(p)]
    o.append(f'<text x="20" y="34" font-size="20" font-weight="700" fill="{BLUE}">升温那一刻</text><text x="560" y="34" font-size="20" font-weight="700" fill="{EO}">36 °C 下的结局</text>')
    rows=[(130,'A 还没到执行点（无芽）',0,'m','停在 2 个大细胞'),(320,'B 已越过执行点（大芽）',3,'m','多走一圈，停在 4 个大细胞')]
    for y,t,b,n,end in rows:
        o.append(f'<rect x="10" y="{y-70}" width="840" height="150" rx="22" fill="url(#{p}card)" stroke="#E3E9F2" filter="url(#{p}sh)"/>')
        o.append(yeast(p,110,y-8,bud=b,nuc=n,sc=1.15))
        o.append(f'<text x="40" y="{y+58}" font-size="18" fill="{INK2}">{t}</text>')
        o.append(f'<line x1="270" y1="{y-8}" x2="470" y2="{y-8}" stroke="{HE}" stroke-width="4" marker-end="url(#{p}ar)"/>')
        if b==0:
            o.append(yeast(p,610,y-8,sep=True,sc=1.15))
        else:
            o.append(yeast(p,560,y-10,sep=True,sc=.95)+yeast(p,730,y-10,sep=True,sc=.95))
        o.append(f'<text x="830" y="{y+58}" font-size="18" fill="{EO}" font-weight="700" text-anchor="end">{end}</text>')
    o.append(f'<text x="20" y="420" font-size="16" fill="{MUTE}">以 cdc-2 为例：谁多走一圈，就说明执行点在 A 与 B 之间——约在出芽起始时。示意，自绘。</text>')
    o.append('</svg>');return ''.join(o)

P=[]
P.append(('封面','封面',f'''<div class="cover-ttl"><div class="k">经典文献拆解 · 第 1 站</div>
<h1>用“温度开关”<br>找出控制细胞分裂的<em class="hl">基因</em></h1>
<div class="sub">Hartwell LH, Culotti J, Reid B<br><i>Proc Natl Acad Sci USA</i> 1970; 66(2): 352–359</div>
<div class="meta">PMID 5271168 · doi:10.1073/pnas.66.2.352 · PMC283051 开放获取<br>华盛顿大学遗传学系 · 笔记整理：2026 年 10 月</div></div>
<div class="cover-chips"><div><b>~100 株</b>温度敏感突变株做延时摄影</div><div><b>15 株</b>整群细胞停在周期同一处</div><div><b>2 个概念</b>执行点与终止点，全篇的灵魂</div></div>
<div class="cover-eye"><img src="{FIG}hartwell-cover-v0.1.jpg" alt="出芽酵母示意"><span class="lab">AI 生成示意图 · 出芽酵母</span></div>'''))
P.append(('一页速览','速览','''<div class="hd"><div class="kick"><span class="no">01</span>一页速览</div><h2 class="t">一句话：把突变酵母从 23 °C 换到 36 °C，看它们“卡”在哪，就能把基因钉到周期的具体时刻</h2></div>
<div class="g2" style="grid-template-columns:1.3fr 1fr">
<div class="card box" data-b="1"><h3>三个基因的表现（36 °C）</h3><table class="t">
<tr><th style="width:20%">基因</th><th style="width:22%">执行点</th><th>终止点与形态</th></tr>
<tr><td><b><i>cdc-1</i></b><br><span class="src">369D-1</span></td><td>出芽起始前后</td><td>停在执行点：单细胞带一个不再长大的小芽、单核（压片后 <span class="num">≥75%</span> 可见小芽）</td></tr>
<tr><td><b><i>cdc-2</i></b><br><span class="src">370D-1</span></td><td>出芽起始前后</td><td>停在有丝分裂：两个近等大细胞，核位于颈部，常呈哑铃形</td></tr>
<tr><td><b><i>cdc-3</i></b><br><span class="src">104D-1</span></td><td>与前两者同期</td><td>无确定终止点：不再分离，但出芽和核分裂继续，形成多突起、多核细胞，最终裂解</td></tr></table></div>
<div style="display:flex;flex-direction:column;gap:20px">
<div class="card box" data-b="2"><h3><span class="tag ok">值得学</span></h3><ul><li>把“芽的大小”当成周期时钟</li><li>一个读数给出两个参数：执行点、终止点</li><li>每株追踪 100 个以上细胞，再用核染色、大小分布、显微操作补证</li></ul></div>
<div class="card box" data-b="3"><h3><span class="tag wn">要注意</span></h3><ul><li>停留在表型层面，不知道基因编码什么</li><li>1970 年的基因名与后来通用名不一一对应</li></ul></div></div></div>'''))
P.append(('背景与问题','背景','''<div class="hd"><div class="kick"><span class="no">02</span>背景与科学问题</div><h2 class="t">事件的顺序早已知道，但“谁在安排顺序”完全是空白</h2></div>
<div class="g3">
<div class="card box" data-b="1"><span class="tag">已知</span><h3 style="margin-top:12px">芽殖酵母的时间表</h3><ul><li>出芽起始 = 周期起点</li><li>DNA 复制在前 <span class="num">25%</span> 内完成</li><li>核分裂约在周期一半处，历时很短</li><li>最后细胞分离；芽一路长到与母细胞差不多大</li></ul></div>
<div class="card box" data-b="2"><span class="tag eo">空白</span><h3 style="margin-top:12px">基因与产物未知</h3><p>保证事件有序推进的基因、产物和功能“基本未知”。生化方法只能看到事件本身，看不到背后的开关。</p></div>
<div class="card box" data-b="3"><span class="tag he">切入点</span><h3 style="margin-top:12px">为什么用温度敏感突变</h3><p>分裂基因是必需基因，直接敲掉细胞就死了。温度敏感突变在 23 °C 正常、36 °C 失灵，等于给基因装上一个随时可按的开关。</p></div></div>
<div class="card box" data-b="4" style="margin-top:24px"><p><b>临床类比：</b>像在手术流程里逐个“暂停”某个岗位——手术停在哪一步，就知道这个岗位在哪一步不可缺；如果停在更后面，说明这个岗位提前做了后面要用的准备。</p></div>'''))
P.append(('实验设计','设计','''<div class="dense"><div class="hd"><div class="kick"><span class="no">03</span>实验设计</div><h2 class="t">诱变 → 遗传学确认单基因 → 升温后延时摄影 → 三种补充测量</h2></div>
<div class="fx" style="grid-template-columns:560px 1fr">
<div class="pts" data-b="1">
<div class="pt bl"><h4>① 诱变</h4><p>亲本 A364A 经亚硝基胍诱变，得到温敏单倍体 ts-369、ts-370、ts-104。</p></div>
<div class="pt bl"><h4>② 遗传分析</h4><p>与非温敏株杂交、四分体解剖，缺陷均 2:2 分离（单个核基因）；再配成纯合二倍体。对照：A364A D-4。</p></div>
<div class="pt eo"><h4>③ 延时摄影</h4><p>23 °C 对数期细胞点到预热 36 °C 平板，网格定位同一视野连续拍照；每株观察 <span class="num">100+</span> 个细胞。</p></div>
<div class="pt ok"><h4>④ 三种补证</h4><p>液体培养后测大小分布（Fig. 3）、Giemsa 染核（Fig. 4）、显微操作拆分 44 个细胞。</p></div></div>
<div class="card box" data-b="2"><table class="t">
<tr><th style="width:24%">项目</th><th>细节</th></tr>
<tr><td>菌株</td><td>369D-1（<i>cdc-1</i>）、370D-1（<i>cdc-2</i>）、104D-1（<i>cdc-3</i>），均为纯合二倍体</td></tr>
<tr><td>温度</td><td>许可 23 °C；限制 36 °C</td></tr>
<tr><td>对照生长</td><td>野生型二倍体 36 °C 下约 <b>2.5 h</b> 一代；三个突变株 23 °C 生长速度与之相近</td></tr>
<tr><td>筛选规模</td><td>约 100 株温敏突变株做延时摄影，<b>15 株</b>整群表现一致</td></tr>
<tr><td>大小分布</td><td>36 °C 液体培养至全部到达终止点，轻度超声，按芽/母体积比分 6 类</td></tr>
<tr><td>核染色</td><td>Helly 固定 + Giemsa，部分用核糖核酸酶替代盐酸水解</td></tr>
<tr><td>显微操作</td><td>104D-1 取 44 个带小芽细胞，36 °C 6 h 后拆开计数</td></tr></table></div></div></div>'''))
P.append(('核心概念图','概念',f'''<div class="dense"><div class="hd"><div class="kick"><span class="no">04</span>核心概念</div><h2 class="t">执行点 = 基因平时“干活”的时刻；终止点 = 不干活时细胞停下的地方</h2></div>
<div class="card box" data-b="1" style="padding:18px 22px">{timeline_svg()}<p class="cap">据原文正文与 Fig. 5 思路重绘的示意图，非原图；时间位置为示意。</p></div>
<div class="g2" style="margin-top:18px">
<div class="card box" data-b="2"><h3>三个执行点都在出芽附近</h3><p>作者推想：从上次分裂到出芽之间，可能完成了“为后面整个周期编程”的许多功能——这正是后来 Start 概念的雏形。</p></div>
<div class="card box" data-b="3"><h3>两点不重合，意味着依赖</h3><p><i>cdc-2</i>、<i>cdc-3</i> 早早起作用，缺陷却在后面才暴露：早期事件是后期事件的前提。</p></div></div></div>'''))
P.append(('执行点怎么判断','逻辑',f'''<div class="hd"><div class="kick"><span class="no">05</span>执行点怎么判断</div><h2 class="t">升温那一刻，越过执行点的细胞能多走完一整圈</h2></div>
<div class="fx" style="grid-template-columns:900px 1fr">
<div class="card box" data-b="1" style="padding:20px">{logic_svg()}</div>
<div class="pts" data-b="2">
<div class="pt bl"><h4>不同步培养是关键</h4><p>细胞分散在周期各处，相当于一次升温同时“采样”了所有时刻。</p></div>
<div class="pt eo"><h4>cdc-2 的原文观察</h4><p>无芽或极小芽的细胞停在 2 个大细胞；芽较大的细胞完成本轮、再出芽，停在 4 个大细胞。</p></div>
<div class="pt eo"><h4>cdc-1 的原文观察</h4><p>升温后 1 h 内新出的少数芽还能长大，之后出的芽都停在小芽。</p></div>
<div class="pt ok"><h4>作者的一般化</h4><p>“更靠前的细胞比更靠后的细胞少走一圈”——这个判据适用于任何只在一个阶段起作用的基因。</p></div></div></div>'''))
P.append(('Fig. 1–2 延时摄影','Fig 1–2',f'''<div class="hd"><div class="kick"><span class="no">06</span>逐图解读 · 原文 Fig. 1–2</div><h2 class="t">芽的大小就是周期时钟；三个突变株在 36 °C 下各自停成一种形状</h2></div>
<div class="card box" data-b="1" style="padding:16px 20px"><div class="pinwrap" style="max-width:1080px;margin:auto"><img src="{FIG}yeast-stages-v0.1.jpg" alt="出芽周期示意"></div>
<div class="steps" style="max-width:1180px;margin:8px auto 0"><div><b>无芽</b>G1</div><div><b>小芽</b>出芽起始 · <i>cdc-1</i> 停这里</div><div><b>中芽</b>核移向颈部</div><div><b>大芽 · 核在颈部</b><i>cdc-2</i> 停这里</div><div><b>分离</b><i>cdc-3</i> 过不去</div></div>
<p class="cap">AI 生成的出芽周期示意，非原文照片；原文 Fig. 1–2 为延时显微照片，见 PMC 全文。</p></div>
<div class="g3" style="margin-top:20px">
<div class="card box" data-b="2"><h3><i>cdc-1</i></h3><p>已有芽的细胞把芽养大；之后新出的芽全部停在小芽。→ 出芽前有一步必须在许可温度下完成。</p></div>
<div class="card box" data-b="3"><h3><i>cdc-2</i></h3><p>终态只有大细胞，没有小芽：两个或四个大细胞，取决于升温时芽的大小。</p></div>
<div class="card box" data-b="4"><h3><i>cdc-3</i></h3><p>升温后新出的芽都异常，长成长突起，约每一代时间再长一个；最终裂解。</p></div></div>'''))
P.append(('Fig. 3–4 补充证据','Fig 3–4','''<div class="hd"><div class="kick"><span class="no">07</span>逐图解读 · 原文 Fig. 3–4 与显微操作</div><h2 class="t">形态之外，再量“分开没有”和“核分了没有”</h2></div>
<div class="g3">
<div class="card box" data-b="1"><span class="tag">Fig. 3 · 大小分布</span><h3 style="margin-top:12px">分开没有</h3><ul><li>369D-1：几乎全是单个细胞（可带小芽）</li><li>370D-1：几乎全是近等大双联体 → 停在分离之前</li><li>104D-1：单细胞带 1–5 个长突起，多数 3 个</li></ul></div>
<div class="card box" data-b="2"><span class="tag he">Fig. 4 · Giemsa 染核</span><h3 style="margin-top:12px">核分了没有</h3><ul><li>野生型约 500 个细胞中 <span class="num">7%</span> 在核分裂，此时芽约为母细胞体积的 <span class="num">50%</span></li><li>369D-1：每个细胞 1 个核</li><li>370D-1：核在颈部，常呈哑铃形</li><li>104D-1：可见多核 → 核分裂照常</li></ul></div>
<div class="card box" data-b="3"><span class="tag eo">显微操作</span><h3 style="margin-top:12px"><i>cdc-3</i> 分离几次</h3><p>44 个带小芽细胞在 36 °C 6 h 后：</p><p style="margin-top:10px"><span class="num" style="font-size:44px">40</span> 个分成 2 个细胞<br><span class="num" style="font-size:30px">3</span> 个仍是 1 个 · <span class="num" style="font-size:30px">1</span> 个分成 3 个</p><p style="margin-top:10px">→ 多数完成当轮分离后，再也不分离。</p></div></div>
<div class="card box" data-b="4" style="margin-top:22px"><p><b>读图要点：</b>延时摄影只能看形态；作者用三种独立读数分别回答“停在哪”“分开没有”“核分了没有”，三者一致才下结论。这是“多读数交叉验证”的早期范例。</p></div>'''))
P.append(('作者结论','结论','''<div class="hd"><div class="kick"><span class="no">08</span>作者结论</div><h2 class="t">方法可推广；执行点集中在出芽附近；早期基因能决定晚期事件</h2></div>
<div class="g2">
<div class="card box" data-b="1"><h3><span class="tag">1</span>一种通用的筛选方法</h3><p>只要某基因只在周期的一个阶段起作用，就能被这种方法捕获；判据只是“越过某阶段的细胞多走一圈”。</p></div>
<div class="card box" data-b="2"><h3><span class="tag">2</span>执行点集中在出芽起始附近</h3><p>从上次分裂到出芽之间，可能完成了为后面整个周期“编程”的许多功能。</p></div>
<div class="card box" data-b="3"><h3><span class="tag">3</span>早执行、晚终止</h3><p>有些基因早早起作用，用来保证后面事件的完成，这可能是周期有序推进的关键。</p></div>
<div class="card box" data-b="4"><h3><span class="tag">4</span>事件之间可以拆开</h3><p>从 <i>cdc-3</i> 看，细胞分离不是出芽和核分裂的前提。这类突变可以用来解析事件间的依赖关系。</p></div></div>'''))
P.append(('今天的认识','今天','''<div class="hd"><div class="kick"><span class="no">09</span>今天的认识</div><h2 class="t">这篇开了“细胞周期遗传学”的头；结论 2 后来发展成 Start 概念</h2></div>
<div class="fx" style="grid-template-columns:1fr 1fr 1fr;display:grid">
<div class="pts" data-b="1"><div class="pt ok"><h4>事实</h4><p>Hartwell 与 Hunt、Nurse 因发现细胞周期关键调控因子，分享 2001 年诺贝尔生理学或医学奖。</p></div>
<div class="pt ok"><h4>事实</h4><p>同一系列筛选后来找到 <i>CDC28</i>——芽殖酵母的 CDK，与裂殖酵母 <i>cdc2</i>、人 CDK1 同源。</p></div>
<div class="pt ok"><h4>事实</h4><p>Hartwell 1974 年 <i>Science</i> 综述用这些突变排出事件顺序，提出 Start（PMID 4587263）。</p></div></div>
<div class="pts" data-b="2"><div class="pt bl"><h4>关联</h4><p>“出芽前完成编程”与哺乳动物限制点（Pardee 1974）思路相通：过点之后，周期基本自动走完。</p></div>
<div class="pt bl"><h4>关联</h4><p>“早期事件是后期前提”为后来检查点概念（Hartwell & Weinert 1989）埋下伏笔。</p></div></div>
<div class="pts" data-b="3"><div class="pt wn"><h4>命名陷阱</h4><p>芽殖酵母 <i>CDC2</i> ≠ 裂殖酵母 <i>cdc2</i>：前者编码 DNA 聚合酶 III（今称 δ）大亚基（Boulet 1989，PMID 2670563）——所以 <i>cdc-2</i> 停在有丝分裂前。</p></div>
<div class="pt wn"><h4>后续鉴定</h4><p><i>CDC3</i> 产物定位在母芽颈部，属隔膜蛋白（septin）家族（Kim 1991，PMID 1993729）——解释了“不能分离”。</p></div></div></div>'''))
P.append(('与课题的关系','关联','''<div class="hd"><div class="kick"><span class="no">10</span>与辐射骨骼肌课题的关系</div><h2 class="t">“扰动后看细胞停在哪”的逻辑，可以直接搬到照射实验里</h2></div>
<div class="g2">
<div class="card box" data-b="1"><h3><span class="tag ok">可以借的思路</span></h3><ul><li>照射就像升温：一个时间点上的统一扰动</li><li>问题从“细胞少了多少”变成“停在哪个时期、能不能多走一圈”</li><li>读数：DNA 含量流式、EdU 掺入、p21 免疫染色，对应芽大小和核位置</li></ul></div>
<div class="card box" data-b="2"><h3><span class="tag wn">需要分清的地方</span></h3><ul><li>肌纤维不分裂，周期问题主要在卫星细胞、FAP 等单个核细胞</li><li>静息卫星细胞处于 G0，与增殖期细胞不同</li><li>细胞对射线的敏感性随周期时相变化，G2/M 较敏感，S 期后段较耐受（Terasima & Tolmach，<i>Biophys J</i> 1963，PMID 13980635）</li></ul></div></div>
<div class="card box" data-b="3" style="margin-top:24px;border-left:6px solid var(--warn)"><p><b>一个可检验的小问题（推测）：</b>照射后 24 h，激活中的卫星细胞主要堆在 G1 还是 G2/M？如果 p21 升高为主，预期更多停在 G1——需要实验回答。</p></div>'''))
P.append(('核心概念','概念表','''<div class="dense"><div class="hd"><div class="kick"><span class="no">11</span>读懂这篇需要的 10 个概念</div><h2 class="t">中英对照，先背定义，再用自己的话复述</h2></div>
<div class="card box" data-b="1"><table class="t">
<tr><th style="width:23%">术语</th><th style="width:27%">一句话</th><th style="width:23%">术语</th><th>一句话</th></tr>
<tr><td><b>温度敏感突变</b><br><span class="en">temperature-sensitive, ts</span></td><td>许可温度下正常，限制温度下失灵</td><td><b>许可 / 限制温度</b><br><span class="en">permissive / restrictive</span></td><td>本文为 23 °C / 36 °C</td></tr>
<tr><td><b>执行点</b><br><span class="en">execution point</span></td><td>基因功能平时被完成的时刻</td><td><b>终止点</b><br><span class="en">termination point</span></td><td>功能缺失时细胞停下的阶段</td></tr>
<tr><td><b>cdc 突变</b><br><span class="en">cell division cycle</span></td><td>阻断周期特定步骤的突变</td><td><b>出芽</b><br><span class="en">budding</span></td><td>芽殖酵母的分裂方式，芽大小反映周期进度</td></tr>
<tr><td><b>延时摄影</b><br><span class="en">time-lapse photomicroscopy</span></td><td>同一视野按时间连续拍照</td><td><b>四分体分析</b><br><span class="en">tetrad analysis</span></td><td>解剖孢子，看性状是否 2:2 分离</td></tr>
<tr><td><b>不同步培养</b><br><span class="en">asynchronous culture</span></td><td>细胞分散在周期各个位置</td><td><b>Start</b></td><td>后来命名的芽殖酵母 G1 晚期承诺点</td></tr></table></div></div>'''))
P.append(('费曼与自测','自测','''<div class="dense"><div class="hd"><div class="kick"><span class="no">12</span>费曼一段话 + 自测题</div><h2 class="t">讲给实习生听，再按布鲁姆层级检验自己</h2></div>
<div class="g2" style="grid-template-columns:1fr 1.25fr">
<div class="card box" data-b="1"><h3><span class="tag eo">费曼一段话</span></h3><p class="feyn">每个酵母细胞身上长着一个芽，芽越大，说明它在分裂流程里走得越远。Hartwell 找到一些坏了开关的酵母，一加热某一步就失灵。他把加热后的细胞一直拍下来，看它们最后停成什么样，就知道这个开关管哪一步；再看哪些细胞还能多走一圈，就知道这个开关平时什么时候打开。</p>
<div class="lvl"><span>记忆</span><span>理解</span><span>应用</span><span>分析</span><span>评价</span></div></div>
<div class="card box" data-b="2">
<div class="q"><p><span class="lv">记忆</span>执行点和终止点分别指什么？</p><details><summary>答案</summary><p>执行点：基因功能平时完成的时刻；终止点：功能缺失时细胞停下的阶段。</p></details></div>
<div class="q"><p><span class="lv">理解</span>为什么必须用温度敏感突变？</p><details><summary>答案</summary><p>周期基因是必需基因，普通缺失突变无法存活；ts 突变能在许可温度保种，再按需关掉。</p></details></div>
<div class="q"><p><span class="lv">应用</span>无芽细胞停在“两个大细胞”，大芽细胞停在“四个大细胞”，执行点在哪？</p><details><summary>答案</summary><p>约在出芽起始：大芽细胞已越过它，多走了一圈（即 cdc-2 的表现）。</p></details></div>
<div class="q"><p><span class="lv">分析</span><i>cdc-3</i> 说明了哪两类事件互不依赖？</p><details><summary>答案</summary><p>细胞分离与出芽、核分裂：不分离时后两者照常进行。</p></details></div>
<div class="q"><p><span class="lv">评价</span>只凭形态判断终止点，最大漏洞是什么？作者怎么补的？</p><details><summary>答案</summary><p>分不清“分开没有”“核分了没有”；作者补了大小分布、Giemsa 染核和显微操作。</p></details></div></div></div></div>'''))
P.append(('出处与延伸','出处','''<div class="hd"><div class="kick"><span class="no">13</span>出处与延伸阅读</div><h2 class="t">原文开放获取；下一站读 Hartwell 1974 和 Pardee 1974</h2></div>
<div class="g2">
<div class="card box" data-b="1"><h3>本文</h3><p>Hartwell LH, Culotti J, Reid B. Genetic control of the cell-division cycle in yeast, I. Detection of mutants. <i>Proc Natl Acad Sci USA</i> 1970;66(2):352–359.</p><p style="margin-top:10px">PMID <a href="https://pubmed.ncbi.nlm.nih.gov/5271168/">5271168</a> · doi:<a href="https://doi.org/10.1073/pnas.66.2.352">10.1073/pnas.66.2.352</a> · <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC283051/">PMC283051 全文</a></p>
<p class="src" style="margin-top:14px">本页数字均取自原文正文。示意图为自绘或 AI 生成，未复制原文图片。</p></div>
<div class="card box" data-b="2"><h3>延伸</h3><ul>
<li>Hartwell LH 等. Genetic control of the cell division cycle in yeast. <i>Science</i> 1974. PMID <a href="https://pubmed.ncbi.nlm.nih.gov/4587263/">4587263</a></li>
<li>Pardee AB. A restriction point for control of normal animal cell proliferation. <i>PNAS</i> 1974. PMID <a href="https://pubmed.ncbi.nlm.nih.gov/4524638/">4524638</a></li>
<li>Hartwell LH, Weinert TA. Checkpoints. <i>Science</i> 1989. PMID <a href="https://pubmed.ncbi.nlm.nih.gov/2683079/">2683079</a></li>
<li>Boulet A 等. <i>EMBO J</i> 1989. PMID <a href="https://pubmed.ncbi.nlm.nih.gov/2670563/">2670563</a></li>
<li>Kim HB 等. <i>J Cell Biol</i> 1991. PMID <a href="https://pubmed.ncbi.nlm.nih.gov/1993729/">1993729</a></li></ul></div></div>'''))
secs='\n'.join(f'<section class="page" id="p{i+1}" data-title="{t}" data-mag="{m}">\n{b}\n</section>' for i,(t,m,b) in enumerate(P))
open('papers/p01-hartwell1970-cdc-mutants-v0.2.html','w').write(wrap('Hartwell 1970 · cdc 突变体 · 文献拆解','文献 01 · Hartwell 1970',secs))
for i,s in enumerate([timeline_svg(),logic_svg()]): open(f'/workspace/work/hv2-{i}.svg','w').write(s)
print('ok',len(P))
