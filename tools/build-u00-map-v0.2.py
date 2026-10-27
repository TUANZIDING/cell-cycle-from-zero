import math
exec(open('tools/shell-v0.2.py').read()); exec(open('tools/svgkit-v0.2.py').read())
FIG='../figures/'
def map_svg():
    p='mp'
    o=[f'<svg viewBox="0 0 1660 430" width="100%" font-family="Noto Sans SC,PingFang SC,sans-serif">',defs(p)]
    cards=[(20,'细胞周期','G1 → S → G2 → M',BLUE,'#EAF2FB'),(440,'DNA 损伤应答','感受 → 传递 → 执行',HE,'#F3EEFA'),(860,'细胞命运','停顿后的五种结局',EO,'#FDECF3'),(1280,'骨骼肌修复','卫星细胞 · FAP · 巨噬',OK,'#E3F4EC')]
    for i,(x,t,s,c,bg) in enumerate(cards):
        o.append(f'<rect x="{x}" y="140" width="360" height="190" rx="28" fill="{bg}" stroke="{c}" stroke-width="2.5" filter="url(#{p}sh)"/>')
        o.append(f'<circle cx="{x+70}" cy="235" r="44" fill="#fff" stroke="{c}" stroke-width="2"/>')
        cx,cy=x+70,235
        if i==0:
            o.append(f'<path d="M{cx},{cy-26} A26,26 0 1 1 {cx-25},{cy-7}" stroke="{c}" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M{cx-34},{cy-14} L{cx-25},{cy-2} L{cx-14},{cy-12}" stroke="{c}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
        elif i==1:
            for k in range(2):
                ox=cx-22+k*26
                o.append(f'<path d="M{ox},{cy-24} q10,12 0,24 q-10,12 0,24" stroke="{c}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M{ox+12},{cy-24} q-10,12 0,24 q10,12 0,24" stroke="{EO}" stroke-width="5" fill="none" stroke-linecap="round" opacity=".7"/>')
            o.append(f'<line x1="{cx-30}" y1="{cy+4}" x2="{cx+30}" y2="{cy-4}" stroke="#fff" stroke-width="7"/>')
        elif i==2:
            o.append(f'<circle cx="{cx-18}" cy="{cy}" r="8" fill="{c}"/>'+''.join(f'<path d="M{cx-10},{cy} Q{cx+4},{cy} {cx+18},{cy+d}" stroke="{c}" stroke-width="4" fill="none"/><circle cx="{cx+20}" cy="{cy+d}" r="6" fill="#fff" stroke="{c}" stroke-width="3"/>' for d in (-22,0,22)))
        else:
            o.append(f'<rect x="{cx-30}" y="{cy-16}" width="60" height="32" rx="16" fill="#F4C2C9" stroke="#C9606E" stroke-width="2.5"/>'+''.join(f'<line x1="{cx-22+k*9}" y1="{cy-12}" x2="{cx-22+k*9}" y2="{cy+12}" stroke="#C9606E" stroke-width="2"/>' for k in range(6))+f'<ellipse cx="{cx}" cy="{cy-18}" rx="11" ry="6" fill="{BLUE2}"/>')
        o.append(f'<text x="{x+134}" y="226" font-size="31" font-weight="700" fill="{c}">{t}</text>')
        o.append(f'<text x="{x+134}" y="264" font-size="19" fill="{INK2}">{s}</text>')
        o.append(f'<text x="{x+134}" y="300" font-size="15" fill="{MUTE}">第 {["1–5","6–7","6–8","9–12"][i]} 周</text>')
    for x in (380,800,1220):
        o.append(f'<line x1="{x+6}" y1="235" x2="{x+56}" y2="235" stroke="{HE}" stroke-width="4" marker-end="url(#{p}ar)"/>')
    # 辐射
    o.append(f'<path d="M640,18 l-22,44 h20 l-16,40 l44,-54 h-22 l18,-30z" fill="{WARN}"/>')
    o.append(f'<line x1="620" y1="104" x2="620" y2="134" stroke="{WARN}" stroke-width="4" stroke-dasharray="6 5" marker-end="url(#{p}arg)"/>')
    o.append(f'<text x="680" y="58" font-size="24" font-weight="700" fill="{WARN}">电离辐射</text><text x="680" y="88" font-size="19" fill="{INK2}">DNA 双链断裂是起点</text>')
    # 反馈
    o.append(f'<path d="M620,334 C620,400 200,400 200,340" stroke="{HE}" stroke-width="3" fill="none" stroke-dasharray="8 6" marker-end="url(#{p}ar)"/>')
    o.append(f'<text x="410" y="414" font-size="18" fill="{HE}" text-anchor="middle">检查点让周期停下：p53 → p21，Chk1 / Chk2</text>')
    o.append('</svg>');return ''.join(o)
def wheel_svg():
    p='wh'
    cx,cy,r=360,330,200
    segs=[(0,.40,'G1','#1B5FA8','#4C8FD8'),(.40,.72,'S','#3F8BD6','#7FB4EA'),(.72,.90,'G2','#5B3F9E','#8E6BC8'),(.90,1.0,'M','#D9719C','#F0A3C0')]
    o=[f'<svg viewBox="0 0 820 600" width="100%" font-family="Noto Sans SC,PingFang SC,sans-serif">',defs(p)]
    gr=''
    for i,(a,b,t,c1,c2) in enumerate(segs): gr+=f'<linearGradient id="{p}g{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/></linearGradient>'
    o.append(f'<defs>{gr}<radialGradient id="{p}in" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#EEF3FA"/></radialGradient></defs>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r+40}" fill="#fff" opacity=".6" filter="url(#{p}sh)"/>')
    def P(f,rr): a=math.radians(-90+360*f); return cx+rr*math.cos(a), cy+rr*math.sin(a)
    for i,(a,b,t,c1,c2) in enumerate(segs):
        x1,y1=P(a+.004,r);x2,y2=P(b-.004,r);large=1 if b-a>.5 else 0
        o.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 1 {x2:.1f},{y2:.1f}" stroke="url(#{p}g{i})" stroke-width="58" fill="none"/>')
        mx,my=P((a+b)/2,r);o.append(f'<text x="{mx:.0f}" y="{my+11:.0f}" font-size="32" font-weight="800" fill="#fff" text-anchor="middle">{t}</text>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r-46}" fill="url(#{p}in)" stroke="#E3E9F2"/>')
    # 中心：小细胞 + DNA 含量
    o.append(f'<text x="{cx}" y="{cy-52}" font-size="18" fill="{MUTE}" text-anchor="middle" letter-spacing="3">DNA 含量</text>')
    o.append(f'<text x="{cx}" y="{cy-10}" font-size="40" font-weight="800" fill="{BLUE}" text-anchor="middle">2C → 4C</text>')
    o.append(f'<text x="{cx}" y="{cy+24}" font-size="19" fill="{INK2}" text-anchor="middle">S 期复制，M 期平分</text>')
    o.append(f'<text x="{cx}" y="{cy+56}" font-size="17" fill="{MUTE}" text-anchor="middle">驱动：CDK–cyclin</text>')
    # 检查点
    cps=[(.40,'1','限制点 / G1–S','条件够不够、要不要开始'),(.90,'2','G2 / M','DNA 复制完、没损伤才分裂'),(.985,'3','纺锤体检查点','染色体都挂好才分开')]
    for f,n,t,s in cps:
        x,y=P(f,r)
        o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="21" fill="#fff" stroke="{WARN}" stroke-width="4" filter="url(#{p}sh)"/><text x="{x:.0f}" y="{y+7:.0f}" font-size="20" font-weight="800" fill="{WARN}" text-anchor="middle">{n}</text>')
    o.append(f'<g transform="translate(590,470)"><text font-size="20" font-weight="700" fill="#9A5A16"><tspan x="0" y="0">① 限制点 / G1–S</tspan></text><text font-size="16" fill="{MUTE}"><tspan x="0" y="24">条件够不够、要不要开始</tspan></text></g>')
    o.append(f'<g transform="translate(20,64)"><text font-size="20" font-weight="700" fill="#9A5A16"><tspan x="0" y="0">② G2 / M</tspan></text><text font-size="16" fill="{MUTE}"><tspan x="0" y="24">复制完、没损伤才分裂</tspan></text></g>')
    o.append(f'<g transform="translate(250,20)"><text font-size="20" font-weight="700" fill="#9A5A16"><tspan x="0" y="0">③ 纺锤体检查点</tspan></text><text font-size="16" fill="{MUTE}"><tspan x="0" y="24">染色体都挂好才分开</tspan></text></g>')
    # G0
    gx,gy=P(.12,r+30)
    o.append(f'<path d="M{gx:.0f},{gy:.0f} C{gx+60:.0f},{gy-40:.0f} 640,150 690,150" stroke="{OK}" stroke-width="4" fill="none" stroke-dasharray="8 6"/>')
    o.append(f'<path d="M{gx+8:.0f},{gy+10:.0f} C{gx+80:.0f},{gy-10:.0f} 650,190 700,196" stroke="{OK}" stroke-width="3" fill="none" stroke-dasharray="4 6" opacity=".6"/>')
    o.append(f'<circle cx="730" cy="160" r="54" fill="#E3F4EC" stroke="{OK}" stroke-width="3" filter="url(#{p}sh)"/><text x="730" y="172" font-size="34" font-weight="800" fill="#1E6E52" text-anchor="middle">G0</text>')
    o.append(f'<text x="730" y="244" font-size="18" fill="#1E6E52" text-anchor="middle">静息（可逆）</text><text x="730" y="268" font-size="16" fill="{MUTE}" text-anchor="middle">卫星细胞的默认状态</text>')
    o.append('</svg>');return ''.join(o)
def fate_svg():
    p='ft'
    o=[f'<svg viewBox="0 0 1660 420" width="100%" font-family="Noto Sans SC,PingFang SC,sans-serif">',defs(p)]
    o.append(f'<rect x="20" y="150" width="330" height="120" rx="26" fill="#fff" stroke="{HE}" stroke-width="3" filter="url(#{p}sh)"/>')
    o.append(f'<text x="185" y="203" font-size="28" font-weight="700" fill="{HE}" text-anchor="middle">检查点停顿</text><text x="185" y="238" font-size="18" fill="{INK2}" text-anchor="middle">p53 → p21 / Chk1 · Chk2</text>')
    outs=[('修复后恢复','损伤修好，继续周期','干细胞池保住',OK,'#E3F4EC'),('静息 G0','可逆退出周期','卫星细胞的默认状态',BLUE,'#EAF2FB'),('衰老','永久停止 · p21/p16 ↑ · SASP','少了干细胞，还改变微环境',WARN,'#FFF1DD'),('凋亡','有序自杀，p53 可触发','细胞数量直接下降',HE,'#F3EEFA'),('有丝分裂灾难','带伤硬进分裂后死亡','多见于增殖中的细胞',EO,'#FDECF3')]
    for i,(t,s,m,c,bg) in enumerate(outs):
        y=14+i*80
        o.append(f'<path d="M352,210 C470,210 470,{y+33} 600,{y+33}" stroke="{c}" stroke-width="3.5" fill="none" marker-end="url(#{p}arg)" opacity=".85"/>')
        o.append(f'<rect x="606" y="{y}" width="1040" height="66" rx="33" fill="{bg}" stroke="{c}" stroke-width="2"/>')
        o.append(f'<circle cx="640" cy="{y+33}" r="12" fill="{c}"/>')
        o.append(f'<text x="668" y="{y+42}" font-size="25" font-weight="700" fill="{c}">{t}</text>')
        o.append(f'<text x="900" y="{y+41}" font-size="19" fill="{INK2}">{s}</text>')
        o.append(f'<text x="1626" y="{y+41}" font-size="17" fill="{MUTE}" text-anchor="end">{m}</text>')
    o.append('</svg>');return ''.join(o)

P=[]
P.append(('封面','封面',f'''<div class="cover-ttl"><div class="k">第 1 周 · 单元 00 · 总地图</div>
<h1>从细胞分裂到<br><em class="hl">照射后的肌肉修复</em></h1>
<div class="sub">先看清四个层次怎么连在一起，再逐层填细节</div>
<div class="meta">5 个工作日 × 45 分钟（读 25 · 回忆 10 · 卡片 10）<br>周六文献拆解 · 周日费曼输出与自测</div></div>
<div class="cover-chips"><div><b>4 层</b>细胞周期 → DNA 损伤应答 → 细胞命运 → 骨骼肌修复</div><div><b>3 个关口</b>限制点、G2/M、纺锤体检查点</div><div><b>30 个术语</b>本周只求能用一句话说清</div></div>
<div class="cover-eye"><img src="{FIG}u00-cover-v0.1.jpg" alt="分裂中的细胞与肌纤维"><span class="lab">AI 生成示意图 · 分裂细胞与肌纤维</span></div>'''))
P.append(('总地图','地图',f'''<div class="hd"><div class="kick"><span class="no">01</span>总地图</div><h2 class="t">一句话：辐射打断 DNA，检查点让周期停下，停下后的结局决定组织能不能修好</h2></div>
<div class="card box" data-b="1" style="padding:22px 26px">{map_svg()}<p class="cap">示意图，自绘。</p></div>
<div class="g3" style="grid-template-columns:repeat(4,1fr);gap:20px;margin-top:20px">
<div class="pt bl" data-b="2"><h4>细胞周期</h4><p>“先复制、再平分”的有序流程，由 CDK–cyclin 驱动。</p></div>
<div class="pt bl" data-b="2" style="border-left-color:var(--he)"><h4 style="color:var(--he)">DNA 损伤应答</h4><p>发现断裂、拉响警报、暂停周期、调修复工具。</p></div>
<div class="pt eo" data-b="3"><h4 style="color:#B04679">细胞命运</h4><p>修好就继续；修不好就衰老、凋亡或在分裂中崩溃。</p></div>
<div class="pt ok" data-b="3"><h4 style="color:#1E6E52">骨骼肌</h4><p>肌纤维不再分裂，修复靠 G0 里的卫星细胞重新进入周期。</p></div></div>'''))
P.append(('Day 1 细胞周期','Day 1',f'''<div class="hd"><div class="kick"><span class="no">02</span>Day 1 · 细胞周期骨架</div><h2 class="t">四个时期、一个旁路（G0）、三个关口</h2></div>
<div class="fx" style="grid-template-columns:820px 1fr">
<div class="card box" data-b="1" style="padding:14px 18px">{wheel_svg()}<p class="cap">示意图，自绘；各期长短为示意，不同细胞差别很大。</p></div>
<div class="pts" data-b="2">
<div class="pt bl"><h4>发动机：CDK + cyclin</h4><p>CDK 本身没活性，结合 cyclin 才开动；不同时期换不同 cyclin，所以周期能一段一段往前推。</p></div>
<div class="pt eo"><h4>熄火：APC/C</h4><p>给 cyclin 贴泛素标签送去降解，CDK 活性落下，细胞才能退出有丝分裂。</p></div>
<div class="pt wn"><h4>刹车：CDK 抑制蛋白</h4><p>p21、p16 等直接压住 CDK。p21 是本库后面反复出现的主角。</p></div>
<div class="pt ok"><h4>手术室类比</h4><p>三个关口 ≈ 手术安全核对的三个时点：麻醉前核对、切皮前暂停、离室前核对。前一步没过，不进下一步。</p></div></div></div>'''))
P.append(('Day 2 警报链','Day 2',f'''<div class="hd"><div class="kick"><span class="no">03</span>Day 2 · DNA 损伤应答</div><h2 class="t">感受 → 传递 → 执行：一条从断裂到“暂停周期”的警报链</h2></div>
<div class="fx" style="grid-template-columns:860px 1fr">
<div class="card fig" data-b="1"><div class="pinwrap"><img src="{FIG}dna-break-v0.1.jpg" alt="DNA 双链断裂示意">
<span class="pin wn" style="left:17%;top:9%"><i>1</i>电离辐射</span><span class="pin eo" style="left:55%;top:16%"><i>2</i>双链断裂</span><span class="pin he" style="left:64%;top:84%"><i>3</i>修复蛋白聚集</span></div>
<p class="cap">AI 生成示意图：双链断裂与修复蛋白；标注为本笔记添加。</p></div>
<div class="pts" data-b="2">
<div class="pt bl"><h4>感受器</h4><p>MRN 复合物发现双链断裂；RPA 包裹单链 DNA。断裂处组蛋白 H2AX 被磷酸化成 γH2AX，是常用的损伤读数。</p></div>
<div class="pt bl" style="border-left-color:var(--he)"><h4 style="color:var(--he)">传递</h4><p>ATM（双链断裂为主）→ Chk2；ATR（单链、复制压力为主）→ Chk1。</p></div>
<div class="pt eo"><h4>执行 · G1 停顿</h4><p>p53 稳定 → p21 抑制 CDK → 停在 G1。</p></div>
<div class="pt eo"><h4>执行 · G2 停顿</h4><p>Cdc25 失活 → CDK1 无法激活 → 停在 G2。</p></div></div></div>'''))
P.append(('Day 2 修复工具','Day 2',f'''<div class="dense"><div class="hd"><div class="kick"><span class="no">04</span>Day 2 · 五套修复工具</div><h2 class="t">修哪种损伤用哪套工具，而且受周期时相限制</h2></div>
<div class="g2" style="grid-template-columns:1.35fr 1fr">
<div class="card box" data-b="1"><table class="t">
<tr><th style="width:26%">通路</th><th>修什么</th><th style="width:30%">周期限制</th></tr>
<tr><td><b>BER</b> 碱基切除</td><td>单个氧化或受损碱基</td><td>全周期</td></tr>
<tr><td><b>NER</b> 核苷酸切除</td><td>使 DNA 变形的大损伤（如紫外线二聚体）</td><td>全周期</td></tr>
<tr><td><b>MMR</b> 错配修复</td><td>复制中产生的错配</td><td>主要在复制后</td></tr>
<tr><td><b>HR</b> 同源重组</td><td>双链断裂，按姐妹染色单体精确修</td><td><span class="tag">S / G2</span> 需要姐妹染色单体</td></tr>
<tr><td><b>NHEJ</b> 非同源末端连接</td><td>双链断裂，直接接上，可能出错</td><td><span class="tag eo">全周期</span> G1 主力</td></tr></table></div>
<div style="display:flex;flex-direction:column;gap:18px">
<div class="card box" data-b="2"><h3><span class="tag">HR</span>像照着原图补</h3><p>拿复制好的姐妹染色单体当模板，补得准；但只有 S/G2 才有模板。</p></div>
<div class="card box" data-b="3"><h3><span class="tag eo">NHEJ</span>像直接缝合</h3><p>断端修整后直接接起来，快、随时可用，但可能丢失或插入几个碱基。</p></div>
<div class="card box" data-b="4" style="border-left:6px solid var(--blue2)"><p><b>关联：</b>同一个双链断裂，在 G1 多走 NHEJ，在 S/G2 可以走 HR，所以“照射时细胞处在哪一期”会影响修复质量。第 6–8 周重点展开。</p></div></div></div></div>'''))
P.append(('Day 3 细胞命运','Day 3',f'''<div class="hd"><div class="kick"><span class="no">05</span>Day 3 · 细胞命运</div><h2 class="t">停下之后有五种结局，组织层面的后果完全不同</h2></div>
<div class="card box" data-b="1" style="padding:24px 26px">{fate_svg()}<p class="cap">示意图，自绘；右侧灰字为对肌肉修复的含义（关联）。</p></div>
<div class="card box" data-b="2" style="margin-top:22px;border-left:6px solid var(--eo)"><p><b>先记住一条：</b>p21 一头连着检查点（暂停），一头连着衰老（永久停）。它是从细胞周期走到辐射骨骼肌课题的第一座桥。</p></div>'''))
P.append(('Day 4 骨骼肌','Day 4',f'''<div class="hd"><div class="kick"><span class="no">06</span>Day 4 · 骨骼肌里的细胞周期</div><h2 class="t">肌纤维不分裂；修复靠卫星细胞从 G0 重新进入周期</h2></div>
<div class="fx" style="grid-template-columns:900px 1fr">
<div class="card fig" data-b="1"><div class="pinwrap"><img src="{FIG}muscle-niche-v0.1.jpg" alt="肌肉干细胞龛示意">
<span class="pin" style="left:50%;top:17%"><i>1</i>卫星细胞（Pax7⁺）</span><span class="pin he" style="left:83%;top:20%"><i>2</i>基膜</span><span class="pin eo" style="left:30%;top:47%"><i>3</i>肌纤维：多核、不分裂</span>
<span class="pin wn" style="left:22%;top:93%"><i>4</i>毛细血管</span><span class="pin ok" style="left:57%;top:94%"><i>5</i>FAP</span><span class="pin he" style="left:83%;top:93%"><i>6</i>巨噬细胞</span></div>
<p class="cap">AI 生成示意图，比例非真实；标注为本笔记添加。</p></div>
<div class="pts" data-b="2">
<div class="pt ok"><h4>事实 · 谁会分裂</h4><p>肌纤维是有丝分裂后细胞；卫星细胞位于基膜与肌膜之间、表达 Pax7、平时处于 G0；FAP、内皮、巨噬等单个核细胞也会分裂。</p></div>
<div class="pt bl"><h4>流程 · 损伤后的再生</h4><p>① 卫星细胞激活、离开 G0 → ② 增殖扩增 → ③ 分化、融合修补肌纤维 → ④ 一部分回到 G0 补充干细胞池。</p></div>
<div class="pt wn"><h4>推测 · 带着这个问题读</h4><p>照射时卫星细胞多在 G0，DNA 损伤可能“潜伏”到被唤醒、进入周期时才暴露。留到第 9–12 周用文献检验。</p></div></div></div>'''))
P.append(('Day 5 术语','Day 5','''<div class="dense"><div class="hd"><div class="kick"><span class="no">07</span>Day 5 · 30 个核心术语</div><h2 class="t">本周目标：每个都能用一句话说清（完整中英表见 docs/glossary-v0.1.md）</h2></div>
<div class="card box" data-b="1"><table class="t" style="font-size:17px">
<tr><th>术语</th><th>一句话</th><th>术语</th><th>一句话</th><th>术语</th><th>一句话</th></tr>
<tr><td><b>CDK</b></td><td>周期发动机，需 cyclin</td><td><b>cyclin</b></td><td>随时期升降的 CDK 搭档</td><td><b>APC/C</b></td><td>给 cyclin 等贴降解标签</td></tr>
<tr><td><b>MPF</b></td><td>即 CDK1–cyclin B</td><td><b>限制点 R</b></td><td>哺乳动物 G1 不回头点</td><td><b>Start</b></td><td>酵母的 G1 承诺点</td></tr>
<tr><td><b>检查点</b></td><td>前一步没完成不进下一步</td><td><b>SAC</b></td><td>纺锤体组装检查点</td><td><b>Rb</b></td><td>扣住 E2F 的刹车蛋白</td></tr>
<tr><td><b>E2F</b></td><td>启动 S 期基因的转录因子</td><td><b>p53</b></td><td>损伤后的“总安全官”</td><td><b>p21</b></td><td>p53 下游的 CDK 抑制蛋白</td></tr>
<tr><td><b>p16</b></td><td>抑制 CDK4/6 的刹车</td><td><b>Wee1</b></td><td>给 CDK1 加抑制性磷酸化</td><td><b>Cdc25</b></td><td>去掉该磷酸化、启动 CDK1</td></tr>
<tr><td><b>ATM</b></td><td>双链断裂的主警报激酶</td><td><b>ATR</b></td><td>单链/复制压力警报激酶</td><td><b>Chk1/Chk2</b></td><td>把警报传给执行者</td></tr>
<tr><td><b>γH2AX</b></td><td>断裂处的磷酸化组蛋白</td><td><b>HR</b></td><td>同源重组，精确修复</td><td><b>NHEJ</b></td><td>直接连接，可能出错</td></tr>
<tr><td><b>cohesin</b></td><td>把姐妹染色单体绑在一起</td><td><b>separase</b></td><td>剪开 cohesin 的酶</td><td><b>securin</b></td><td>separase 的抑制蛋白</td></tr>
<tr><td><b>动粒</b></td><td>染色体上挂纺锤丝处</td><td><b>G0</b></td><td>可逆退出周期</td><td><b>衰老</b></td><td>永久停止分裂</td></tr>
<tr><td><b>SASP</b></td><td>衰老细胞的分泌表型</td><td><b>卫星细胞</b></td><td>肌肉干细胞，Pax7⁺</td><td><b>FAP</b></td><td>纤维脂肪祖细胞</td></tr></table></div></div>'''))
P.append(('本周安排','安排','''<div class="hd"><div class="kick"><span class="no">08</span>本周 45 分钟 × 5 + 周末 3 小时</div><h2 class="t">每天：读 25 分钟 → 合上回忆 10 分钟 → 卡片复习 10 分钟</h2></div>
<div class="g2" style="grid-template-columns:1.4fr 1fr">
<div class="card box" data-b="1"><table class="t">
<tr><th style="width:16%">时间</th><th style="width:34%">读（25 分钟）</th><th>闭卷回忆（10 分钟）</th></tr>
<tr><td><b>Day 1</b></td><td>第 02 页 + Cooper 第 14 章开头</td><td>默画周期圈：四期、G0、三个关口</td></tr>
<tr><td><b>Day 2</b></td><td>第 03–04 页</td><td>警报链三层；五套修复各修什么</td></tr>
<tr><td><b>Day 3</b></td><td>第 05 页</td><td>p21 为什么是“桥”？两句话说清</td></tr>
<tr><td><b>Day 4</b></td><td>第 06 页</td><td>卫星细胞从静息到融合的四步</td></tr>
<tr><td><b>Day 5</b></td><td>第 07 页</td><td>遮住右列，逐个说出定义</td></tr></table></div>
<div style="display:flex;flex-direction:column;gap:18px">
<div class="card box" data-b="2"><h3><span class="tag he">周六 2 h</span></h3><p>文献 01：Hartwell 1970 拆解页。读原文 Fig. 1–2，对照拆解页自己先说结论。</p></div>
<div class="card box" data-b="3"><h3><span class="tag eo">周日 1 h</span></h3><p>写一段“讲给实习生听”的总地图，再做第 09 页自测。卡住的地方就是下周要补的。</p></div>
<div class="card box" data-b="4"><h3><span class="tag ok">卡片</span></h3><p>30 个术语做成正反面卡片，按 1、3、7、14 天间隔复习。</p></div></div></div>'''))
P.append(('费曼与自测','自测','''<div class="dense"><div class="hd"><div class="kick"><span class="no">09</span>周日 · 费曼输出 + 自测</div><h2 class="t">讲得出来才算懂；卡住的地方就是下周要补的地方</h2></div>
<div class="g2" style="grid-template-columns:1fr 1.3fr">
<div class="card box" data-b="1"><h3><span class="tag eo">费曼开头</span></h3><p class="feyn">细胞想分裂，就要先把 DNA 抄一遍再平分。整个过程靠一台叫 CDK 的发动机推着走，路上有三个安检站。辐射把 DNA 打断后，安检站会把细胞拦下来修……</p><p style="margin-top:12px">接着往下写，写到肌肉为止。需要用术语糊弄过去的地方标红，下周查。</p></div>
<div class="card box" data-b="2">
<div class="q"><p><span class="lv">记忆</span>G1、S、G2、M 各做什么？DNA 含量怎么变？</p><details><summary>答案</summary><p>G1 生长准备（2C）；S 复制 DNA（2C→4C）；G2 检查并准备分裂（4C）；M 分裂（回到 2C）。</p></details></div>
<div class="q"><p><span class="lv">理解</span>为什么 HR 主要在 S/G2？</p><details><summary>答案</summary><p>HR 需要姐妹染色单体当模板，复制之后才有。</p></details></div>
<div class="q"><p><span class="lv">应用</span>敲掉 p53 的细胞受照射后，最可能失去哪个关口？</p><details><summary>答案</summary><p>G1/S 停顿（p53→p21），细胞更容易带伤进入 S 期。</p></details></div>
<div class="q"><p><span class="lv">分析</span>肌纤维不分裂，为什么照射仍会损害肌肉再生？</p><details><summary>答案</summary><p>再生依赖卫星细胞重新进入周期；它们以及 FAP、内皮等细胞受损或衰老，都会影响修复。</p></details></div>
<div class="q"><p><span class="lv">评价</span>“衰老细胞不分裂，所以无害”对吗？</p><details><summary>答案</summary><p>不对：衰老细胞会通过 SASP 分泌炎症和促纤维化因子，改变微环境。</p></details></div></div></div></div>'''))
P.append(('出处与延伸','出处','''<div class="hd"><div class="kick"><span class="no">10</span>出处与延伸</div><h2 class="t">本周只读入门材料；文献从周六开始</h2></div>
<div class="g2">
<div class="card box" data-b="1"><h3>免费合法教材</h3><ul>
<li>Cooper《The Cell》第 2 版第 14 章：<a href="https://www.ncbi.nlm.nih.gov/books/NBK9876/">NCBI Bookshelf</a></li>
<li>Alberts《Molecular Biology of the Cell》第 4 版第 17 章：<a href="https://www.ncbi.nlm.nih.gov/books/NBK21056/">NCBI Bookshelf</a></li>
<li>Morgan《The Cell Cycle: Principles of Control》2007：<a href="https://morganlab.ucsf.edu/cell-cycle-principles-control">作者实验室页面</a></li>
<li>2001 年诺贝尔奖：<a href="https://www.nobelprize.org/prizes/medicine/2001/summary/">nobelprize.org</a></li></ul></div>
<div class="card box" data-b="2"><h3>本库约定</h3><ul><li>示意图为自绘或 AI 生成，已注明；不收录原文图</li><li>“事实 / 关联 / 推测”分开标注</li><li>文献信息均经 PubMed 核对</li><li>下一单元：U01 细胞周期总览（第 2 周）</li></ul></div></div>'''))
secs='\n'.join(f'<section class="page" id="p{i+1}" data-title="{t}" data-mag="{m}">\n{b}\n</section>' for i,(t,m,b) in enumerate(P))
open('units/u00-map-v0.2.html','w').write(wrap('单元 00 · 总地图 · 细胞周期从零学','单元 00 · 总地图',secs))
for i,s in enumerate([map_svg(),wheel_svg(),fate_svg()]): open(f'/workspace/work/uv2-{i}.svg','w').write(s.replace('font-family="Noto Sans SC,PingFang SC,sans-serif"','font-family="WenQuanYi Zen Hei"'))
print('ok',len(P))
