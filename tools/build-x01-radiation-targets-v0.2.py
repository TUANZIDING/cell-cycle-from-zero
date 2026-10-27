# 补充单元 X01：辐射到底打中了什么？  生成 units/x01-radiation-targets-v0.2.html
exec(open('tools/shell-v0.2.py').read()); exec(open('tools/svgkit-v0.2.py').read())
FIG='../figures/'
F='font-family="Noto Sans SC,PingFang SC,sans-serif"'
def pm(pmid,txt=None): return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{pmid}/">{txt or "PMID "+pmid}</a>'

def targets_svg():
    p='tg'
    o=[f'<svg viewBox="0 0 1660 470" width="100%" style="display:block;max-height:380px;margin:0 auto" {F}>',defs(p)]
    # 细胞
    cx,cy=330,240
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="250" ry="200" fill="url(#{p}cell)" stroke="{EO}" stroke-width="5" stroke-dasharray="14 8" filter="url(#{p}sh)"/>')
    o.append(f'<circle cx="{cx+10}" cy="{cy}" r="88" fill="url(#{p}nuc)" opacity=".92"/>')
    # DNA 断裂
    o.append(f'<path d="M{cx-40},{cy-40} q20,20 0,40 q-20,20 0,40" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M{cx-12},{cy-40} q-20,20 0,40 q20,20 0,40" stroke="#F0A3C0" stroke-width="6" fill="none" stroke-linecap="round"/>')
    o.append(f'<path d="M{cx+30},{cy-40} q20,20 0,32" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M{cx+30},{cy+8} q-20,16 0,32" stroke="#fff" stroke-width="6" fill="none" stroke-linecap="round"/>')
    o.append(f'<path d="M{cx+58},{cy-40} q-20,20 0,32" stroke="#F0A3C0" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M{cx+58},{cy+8} q20,16 0,32" stroke="#F0A3C0" stroke-width="6" fill="none" stroke-linecap="round"/>')
    o.append(f'<circle cx="{cx+44}" cy="{cy-4}" r="12" fill="{WARN}" opacity=".55" filter="url(#{p}gl)"/>')
    # 线粒体
    for (mx,my,r) in ((cx-170,cy-70,-20),(cx-150,cy+100,15),(cx+170,cy+110,-30)):
        o.append(f'<g transform="rotate({r} {mx} {my})"><ellipse cx="{mx}" cy="{my}" rx="38" ry="20" fill="#F4C2C9" stroke="#C9606E" stroke-width="3"/><path d="M{mx-26},{my} q7,-12 13,0 q7,12 13,0 q7,-12 13,0" stroke="#C9606E" stroke-width="2.5" fill="none"/></g>')
    # 射线
    for dy in (-150,40):
        o.append(f'<path d="M20,{cy+dy-60} L{cx+44},{cy-4}" stroke="{WARN}" stroke-width="4" stroke-dasharray="2 0" opacity=".85"/>')
    o.append(f'<path d="M60,30 l-22,44 h20 l-16,40 l44,-54 h-22 l18,-30z" fill="{WARN}"/>')
    o.append(f'<text x="30" y="182" font-size="22" font-weight="700" fill="{WARN}">电离辐射</text>')
    # 右侧四个靶点
    rows=[('细胞膜','鞘磷脂水解 → 神经酰胺 → 内皮凋亡','确切 · 细胞类型依赖',EO,'#FDECF3',(cx+160,cy-152),3,False),
          ('细胞核 DNA','双链断裂 → 克隆源性死亡、染色体畸变','证据最强 · 主靶',BLUE,'#EAF2FB',(cx+98,cy-4),5,True),
          ('线粒体','mtDNA / 电子传递链 → 持续 ROS','确切 · 权重待定',WARN,'#FFF1DD',(cx+205,cy+92),3,False),
          ('邻近细胞','旁观者效应：没被打中也出现损伤','确切 · 多见低剂量',HE,'#F3EEFA',(cx+120,cy+186),3,False)]
    for i,(t,s,lv,c,bg,(sx,sy),st,main) in enumerate(rows):
        y=30+i*108; ey=y+44
        o.append(f'<path d="M{sx},{sy} C{(sx+760)/2+40},{sy} {(sx+760)/2-40},{ey} 760,{ey}" stroke="{c}" stroke-width="{6 if main else 3}" fill="none" opacity=".85" marker-end="url(#{p}arg)"/>')
        o.append(f'<rect x="766" y="{y}" width="880" height="88" rx="44" fill="{bg}" stroke="{c}" stroke-width="{3 if main else 2}" {"filter=\"url(#%ssh)\"" % p if main else ""}/>')
        o.append(f'<text x="810" y="{y+40}" font-size="27" font-weight="800" fill="{c}">{t}</text>')
        o.append(f'<text x="810" y="{y+70}" font-size="18" fill="{INK2}">{s}</text>')
        for k in range(5):
            o.append(f'<rect x="{1440+k*34}" y="{y+22}" width="26" height="12" rx="6" fill="{c if k<st else "#E3E7EE"}"/>')
        o.append(f'<text x="1610" y="{y+66}" font-size="16" fill="{MUTE}" text-anchor="end">{lv}</text>')
    o.append('</svg>');return ''.join(o)

def evidence_svg():
    p='ev'
    o=[f'<svg viewBox="0 0 1660 430" width="100%" {F}>',defs(p)]
    W=520
    titles=[('Munro 1970','只照胞质 vs 照细胞核'),('Warters 1978','¹²⁵I 放在哪里'),('Taylor 1975','AT 细胞的存活曲线')]
    for i,(t,s) in enumerate(titles):
        x=10+i*(W+30)
        o.append(f'<rect x="{x}" y="10" width="{W}" height="400" rx="28" fill="url(#{p}card)" stroke="#E3E9F2" stroke-width="2" filter="url(#{p}sh)"/>')
        o.append(f'<text x="{x+30}" y="56" font-size="26" font-weight="800" fill="{BLUE}">{t}</text><text x="{x+30}" y="88" font-size="18" fill="{INK2}">{s}</text>')
    # 面板1：两只细胞，针尖
    x=10
    for j,(lab,tx,col,h) in enumerate((('照胞质','需极大剂量',EO,60),('照细胞核','少量即致死',BLUE,230))):
        cx=x+140+j*240; cy=210
        o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="78" ry="62" fill="url(#{p}cell)" stroke="{BLUE}" stroke-width="2.5"/><circle cx="{cx}" cy="{cy}" r="26" fill="url(#{p}nuc)"/>')
        tx2,ty2=(cx-46,cy-14) if j==0 else (cx,cy)
        o.append(f'<line x1="{cx-40}" y1="{cy-110}" x2="{tx2}" y2="{ty2}" stroke="{INK2}" stroke-width="4" stroke-linecap="round"/><circle cx="{tx2}" cy="{ty2}" r="9" fill="{WARN}" opacity=".7" filter="url(#{p}gl)"/><circle cx="{tx2}" cy="{ty2}" r="4" fill="{WARN}"/>')
        o.append(f'<text x="{cx}" y="{cy+100}" font-size="20" font-weight="700" fill="{col}" text-anchor="middle">{lab}</text><text x="{cx}" y="{cy+128}" font-size="17" fill="{INK2}" text-anchor="middle">{tx}</text>')
    o.append(f'<text x="{x+30}" y="394" font-size="14" fill="{MUTE}">α 放射源针尖局部照射（示意）</text>')
    # 面板2：条形 致死效率
    x=10+W+30
    bars=[('掺入 DNA','¹²⁵IUdR',300,BLUE),('结合细胞膜','¹²⁵I-ConA',34,EO),('胞质蛋白','对照',22,WARN)]
    for j,(a,b,v,c) in enumerate(bars):
        y=130+j*82
        o.append(f'<text x="{x+30}" y="{y+22}" font-size="19" font-weight="700" fill="{INK}">{a}</text><text x="{x+30}" y="{y+46}" font-size="15" fill="{MUTE}">{b}</text>')
        o.append(f'<rect x="{x+170}" y="{y+6}" width="310" height="28" rx="14" fill="#EEF2F7"/><rect x="{x+170}" y="{y+6}" width="{v}" height="28" rx="14" fill="{c}"/>')
    o.append(f'<text x="{x+170}" y="384" font-size="15" fill="{MUTE}">相对致死效率（示意，非原始数据）</text>')
    # 面板3：存活曲线
    x=10+2*(W+30); ox,oy=x+80,350
    o.append(f'<line x1="{ox}" y1="{oy}" x2="{ox+390}" y2="{oy}" stroke="{INK2}" stroke-width="2"/><line x1="{ox}" y1="{oy}" x2="{ox}" y2="120" stroke="{INK2}" stroke-width="2"/>')
    o.append(f'<text x="{ox+390}" y="{oy+28}" font-size="15" fill="{MUTE}" text-anchor="end">剂量 →</text><text x="{ox-14}" y="132" font-size="15" fill="{MUTE}" text-anchor="end">存活</text><text x="{ox-14}" y="150" font-size="13" fill="{MUTE}" text-anchor="end">(对数)</text>')
    o.append(f'<path d="M{ox},130 C{ox+90},134 {ox+170},175 {ox+380},300" stroke="{OK}" stroke-width="5" fill="none"/>')
    o.append(f'<path d="M{ox},130 C{ox+40},160 {ox+90},280 {ox+150},{oy-6}" stroke="{EO}" stroke-width="5" fill="none"/>')
    o.append(f'<text x="{ox+300}" y="250" font-size="19" font-weight="700" fill="#1E6E52">正常细胞</text><text x="{ox+120}" y="245" font-size="19" font-weight="700" fill="#B04679">AT 细胞</text>')
    o.append(f'<text x="{x+30}" y="394" font-size="14" fill="{MUTE}">曲线形状为示意</text>')
    o.append('</svg>');return ''.join(o)

def death_svg():
    p='dt'
    o=[f'<svg viewBox="0 0 1660 380" width="100%" {F}>',defs(p)]
    steps=[(30,'照射','DSB 形成',WARN,'#FFF1DD'),(330,'检查点停顿','ATM → p53 / Chk2',HE,'#F3EEFA'),(660,'修复','HR / NHEJ',OK,'#E3F4EC'),(990,'带伤进入分裂','染色体断片、桥、微核',EO,'#FDECF3'),(1320,'有丝分裂灾难','第 1 至数次分裂时死亡',EO,'#FDECF3')]
    for i,(x,t,s,c,bg) in enumerate(steps):
        o.append(f'<rect x="{x}" y="40" width="300" height="120" rx="30" fill="{bg}" stroke="{c}" stroke-width="2.5" filter="url(#{p}sh)"/>')
        o.append(f'<text x="{x+150}" y="92" font-size="27" font-weight="800" fill="{c}" text-anchor="middle">{t}</text><text x="{x+150}" y="128" font-size="18" fill="{INK2}" text-anchor="middle">{s}</text>')
    for x in (330,660,990,1320):
        if x==660: continue
        o.append(f'<line x1="{x-24}" y1="100" x2="{x-4}" y2="100" stroke="{MUTE}" stroke-width="3" marker-end="url(#{p}arg)"/>')
    o.append(f'<path d="M630,100 L656,100" stroke="{OK}" stroke-width="3" marker-end="url(#{p}arg)"/>')
    o.append(f'<path d="M810,162 C810,215 780,215 760,215" stroke="{OK}" stroke-width="3" fill="none" stroke-dasharray="7 6"/><text x="740" y="222" font-size="18" fill="#1E6E52" text-anchor="end">修好 → 继续周期，存活</text>')
    o.append(f'<path d="M960,100 L986,100" stroke="{MUTE}" stroke-width="3" marker-end="url(#{p}arg)"/>')
    # 分支
    o.append(f'<path d="M480,162 C480,250 560,290 640,290" stroke="{WARN}" stroke-width="3.5" fill="none" marker-end="url(#{p}arg)"/>')
    o.append(f'<rect x="646" y="254" width="420" height="72" rx="36" fill="#FFF1DD" stroke="{WARN}" stroke-width="2"/><text x="676" y="298" font-size="22" font-weight="700" fill="#9A5A16">持续 p53 → p21：衰老</text>')
    o.append(f'<path d="M420,162 C420,300 330,320 250,320" stroke="{HE}" stroke-width="3.5" fill="none" marker-end="url(#{p}arg)"/>')
    o.append(f'<text x="30" y="300" font-size="22" font-weight="700" fill="{HE}">凋亡</text><text x="30" y="330" font-size="17" fill="{INK2}">淋巴细胞等：数小时内</text>')
    o.append(f'<text x="1640" y="300" font-size="18" fill="{MUTE}" text-anchor="end">多数增殖中的实体细胞走这条路</text><path d="M1470,280 L1470,168" stroke="{MUTE}" stroke-width="2" stroke-dasharray="4 5"/>')
    o.append('</svg>');return ''.join(o)

P=[]
P.append(('封面','封面',f'''<div class="cover-ttl"><div class="k">补充单元 X01 · 承接 U00 的一个问题</div>
<h1>辐射到底<br><em class="hl">打中了什么？</em></h1>
<div class="sub">DNA 是主靶，但不是唯一靶点</div>
<div class="meta">约 2 × 45 分钟 · 读完能回答：辐射是不是“只靠打断 DNA”伤害细胞<br>文献 12 篇，均经 PubMed 核对</div></div>
<div class="cover-chips"><div><b>1 个主靶</b>细胞核 DNA，尤其双链断裂</div><div><b>3 条旁路</b>细胞膜、线粒体、旁观者效应</div><div><b>2 条线</b>研究骨骼肌照射损伤的拆法</div></div>
<div class="cover-eye"><img src="{FIG}x01-cover-v0.1.jpg" alt="射线穿过细胞、打断 DNA"><span class="lab">AI 生成示意图 · 射线穿过细胞</span></div>'''))
P.append(('一句话结论','结论',f'''<div class="hd"><div class="kick"><span class="no">01</span>先说结论</div><h2 class="t">“会不会死、还能不能分裂”主要看 DNA；“功能怎么变”还要看膜、线粒体和邻居</h2></div>
<div class="card box" data-b="1" style="padding:22px 26px">{targets_svg()}<p class="cap">示意图，自绘；右侧色条是本笔记对证据强度的主观评级，不是定量数据。</p></div>
<div class="g3" style="gap:20px;margin-top:12px">
<div class="pt bl" data-b="2"><h4>事实</h4><p>细胞致死（克隆源性死亡）的主靶是核 DNA，双链断裂最关键。</p></div>
<div class="pt eo" data-b="2"><h4 style="color:#B04679">事实</h4><p>非 DNA 靶点也确实存在：膜神经酰胺、胞质照射致突变、旁观者效应。</p></div>
<div class="pt wn" data-b="3"><h4 style="color:#9A5A16">推测</h4><p>不分裂的肌纤维，损伤可能更多来自非 DNA 和组织层面的通路。</p></div></div>'''))
P.append(('损伤长什么样','损伤',f'''<div class="hd"><div class="kick"><span class="no">02</span>DNA 被打成什么样</div><h2 class="t">数量最少的双链断裂，却最致命</h2></div>
<div class="fx" style="grid-template-columns:820px 1fr">
<div class="card box" data-b="1"><table class="t">
<tr><th style="width:30%">损伤类型</th><th style="width:28%">每细胞每 Gy（量级）</th><th>后果</th></tr>
<tr><td><b>碱基损伤</b></td><td>&gt; 1000</td><td>BER 修复，多数无害</td></tr>
<tr><td><b>单链断裂 SSB</b></td><td>约 1000</td><td>有互补链作模板，修得快</td></tr>
<tr><td><b>双链断裂 DSB</b></td><td><span class="tag eo">约 20–40</span></td><td>修错 → 染色体断片、易位、双着丝粒</td></tr>
<tr><td><b>簇集损伤</b></td><td>随 LET 增加</td><td>一两圈螺旋内多处损伤，最难修</td></tr></table>
<p class="cap" style="margin-top:12px">量级为放射生物学教材常用数值，不同测量方法差异较大；分类见 Ward 1988（{pm("3065826")}）、Lomax 2013（{pm("23849504")}）。</p></div>
<div class="pts" data-b="2">
<div class="pt bl"><h4>直接作用</h4><p>射线直接电离 DNA 分子本身。</p></div>
<div class="pt eo"><h4>间接作用</h4><p>射线先电离水，产生羟自由基 ·OH，再由 ·OH 攻击 DNA。X 线等低 LET 辐射以此为主（约 2/3）。</p></div>
<div class="pt wn"><h4>为什么 DSB 最致命</h4><p>两条链同时断，没有完整的一条当模板；G1 期只能靠易错的 NHEJ 直接接上。</p></div>
<div class="pt ok"><h4>怎么“看见”断裂</h4><p>γH2AX 焦点：一个焦点大致对应一个 DSB（Rogakou 1998，{pm("9488723")}）。</p></div></div></div>'''))
P.append(('三个关键证据','证据',f'''<div class="hd"><div class="kick"><span class="no">03</span>凭什么说 DNA 是主靶</div><h2 class="t">三类实验从三个方向指向同一个答案</h2></div>
<div class="card box" data-b="1" style="padding:18px 22px">{evidence_svg()}</div>
<div class="g3" style="gap:20px;margin-top:18px">
<div class="pt bl" data-b="2"><h4>定位</h4><p>Munro 1970：只照胞质要极大剂量才致死，照核则少量即可（{pm("5463516","Radiat Res 1970")}）。</p></div>
<div class="pt bl" data-b="2" style="border-left-color:var(--he)"><h4 style="color:var(--he)">内照射</h4><p>Warters 1978：¹²⁵I 掺入 DNA 时高效致死，结合在膜上几乎无毒（{pm("565271","Curr Top Radiat Res Q 1978")}）。</p></div>
<div class="pt eo" data-b="3"><h4 style="color:#B04679">遗传学</h4><p>Taylor 1975：AT 患者细胞对辐射异常敏感（{pm("1196376","Nature 1975")}），致病基因后来证实为 ATM。</p></div></div>'''))
P.append(('细胞怎么死','死法',f'''<div class="hd"><div class="kick"><span class="no">04</span>DNA 断了，细胞怎么死</div><h2 class="t">多数增殖细胞不是当场死，而是在分裂时“算总账”</h2></div>
<div class="card box" data-b="1" style="padding:22px 26px">{death_svg()}<p class="cap">示意图，自绘。</p></div>
<div class="g2" style="gap:20px;margin-top:20px">
<div class="card box" data-b="2" style="border-left:6px solid var(--blue2)"><p><b>和细胞周期的关系：</b>照射后的命运几乎全由检查点决定：停下修、永久停（衰老），还是带伤闯过去（有丝分裂灾难）。这正是 U00 第 05 页那五种结局。</p></div>
<div class="card box" data-b="3" style="border-left:6px solid var(--eo)"><p><b>“死亡”的定义：</b>放射生物学说的“杀死”通常是<b>克隆源性死亡</b>，即失去无限增殖能力。细胞可以还活着、还有功能。</p></div></div>'''))
P.append(('非 DNA 靶点','旁路',f'''<div class="dense"><div class="hd"><div class="kick"><span class="no">05</span>但 DNA 不是唯一靶点</div><h2 class="t">四个经典实验：膜、血管、邻居、胞质</h2></div>
<div class="g2" style="gap:20px">
<div class="card box" data-b="1"><h3><span class="tag eo">膜</span>Haimovitz-Friedman 1994</h3><p>照射使牛主动脉内皮细胞的鞘磷脂迅速水解为神经酰胺并凋亡；在<b>不含细胞核的膜制备物</b>上照射同样能激活（中性）鞘磷脂酶，说明信号可直接起于细胞膜。</p><p class="cap">J Exp Med · {pm("8046331")} · doi:10.1084/jem.180.2.525</p></div>
<div class="card box" data-b="2"><h3><span class="tag he">血管</span>Garcia-Barros 2003</h3><p>酸性鞘磷脂酶缺陷小鼠的肿瘤内皮照射后不凋亡，肿瘤也更耐照射：<b>内皮的膜通路</b>能左右组织层面的放射反应。</p><p class="cap">Science · {pm("12750523")} · doi:10.1126/science.1082504</p></div>
<div class="card box" data-b="3"><h3><span class="tag wn">邻居</span>Nagasawa & Little 1992</h3><p>极低剂量 α 粒子只打中约 1% 的细胞核，却有约 30% 的细胞出现姐妹染色单体交换增加：<b>旁观者效应</b>。</p><p class="cap">Cancer Res · {pm("1423287")}</p></div>
<div class="card box" data-b="4"><h3><span class="tag ok">胞质</span>Wu 1999</h3><p>微束 α 粒子<b>只照胞质</b>即可诱发核基因突变，细胞毒性很小，且可被自由基清除剂抑制：经 ROS 间接伤到 DNA。</p><p class="cap">PNAS · {pm("10220401")} · doi:10.1073/pnas.96.9.4959</p></div></div>
<div class="card box" data-b="4" style="margin-top:18px;border-left:6px solid var(--warn)"><p><b>注意：</b>Wu 1999 和旁观者效应里，最终受伤的往往还是 DNA，只是射线没直接打中它。所以更准确的说法是：<b>“DNA 损伤是核心读数，但损伤的来路不止一条”</b>。</p></div></div>'''))
P.append(('两类靶点对比','对比','''<div class="hd"><div class="kick"><span class="no">06</span>放在一起比</div><h2 class="t">哪种效应在什么情况下更重要</h2></div>
<div class="card box" data-b="1"><table class="t">
<tr><th style="width:18%"></th><th style="width:27%">DNA 直接/间接损伤</th><th style="width:27%">膜 · 神经酰胺</th><th>旁观者 / 胞质 / 线粒体</th></tr>
<tr><td><b>证据强度</b></td><td><span class="tag">最强</span> 定位、内照射、遗传学三线一致</td><td><span class="tag eo">确切</span> 细胞类型依赖</td><td><span class="tag he">确切</span> 机制与体内权重仍有争议</td></tr>
<tr><td><b>剂量</b></td><td>全剂量范围</td><td>较高单次剂量更显著</td><td>低剂量时相对更突出</td></tr>
<tr><td><b>最敏感的细胞</b></td><td>增殖中的细胞</td><td>内皮细胞</td><td>与细胞间通讯、代谢状态有关</td></tr>
<tr><td><b>主要后果</b></td><td>克隆源性死亡、衰老、突变</td><td>快速凋亡、微血管损伤</td><td>基因组不稳定、慢性氧化应激</td></tr>
<tr><td><b>U00 对应</b></td><td>检查点 → 五种结局</td><td>细胞命运：凋亡</td><td>微环境、SASP</td></tr></table>
<p class="cap" style="margin-top:12px">本页为综合整理（关联层面），“剂量”“最敏感细胞”两行是概括性描述，具体阈值因模型而异。</p></div>'''))
P.append(('骨骼肌','骨骼肌',f'''<div class="hd"><div class="kick"><span class="no">07</span>回到骨骼肌</div><h2 class="t">肌纤维不分裂；照射伤肌肉，很可能靠两条线</h2></div>
<div class="fx" style="grid-template-columns:860px 1fr">
<div class="card fig" data-b="1"><div class="pinwrap"><img src="{FIG}muscle-niche-v0.1.jpg" alt="肌肉干细胞龛示意">
<span class="pin" style="left:50%;top:17%"><i>1</i>卫星细胞：DNA 线</span><span class="pin eo" style="left:30%;top:47%"><i>2</i>肌纤维：不分裂</span>
<span class="pin wn" style="left:22%;top:93%"><i>3</i>内皮</span><span class="pin ok" style="left:57%;top:94%"><i>4</i>FAP：微环境线</span></div>
<p class="cap">AI 生成示意图，比例非真实；标注为本笔记添加。</p></div>
<div class="pts" data-b="2">
<div class="pt bl"><h4>事实 · 卫星细胞</h4><p>使卫星细胞丧失增殖能力的 γ 照射后，小鼠 EDL 不能代偿性肥大，但纤维类型的维持不受影响（Rosenblatt & Parry 1992，{pm("1490967")}）。</p></div>
<div class="pt ok"><h4>事实 · 微环境</h4><p>幼年小鼠单次 16 Gy 后：卫星细胞、内皮、FAP 减少；FAP 衰老、向成纤维分化，其分泌组损害卫星细胞分化与融合；56 天出现纤维化（Collao 2023，{pm("37671686")}）。</p></div>
<div class="pt wn"><h4>推测 · 两条线</h4><p>① 卫星细胞：DNA 损伤 → p53/p21 停滞或衰老 → 再生下降；② 微环境：FAP、内皮、线粒体与 ROS。待后续文献核实。</p></div></div></div>'''))
P.append(('今天的认识','认识','''<div class="hd"><div class="kick"><span class="no">08</span>今天的认识</div><h2 class="t">把“事实 / 关联 / 推测”分开放</h2></div>
<div class="g3" style="gap:22px">
<div class="card box" data-b="1" style="border-top:6px solid var(--blue)"><h3><span class="tag">事实</span></h3><ul>
<li>细胞致死的主靶是核 DNA，DSB 最关键</li><li>X 线损伤约 2/3 经 ·OH 间接作用</li><li>DSB 修复缺陷（如 AT）显著增加辐射敏感性</li><li>膜神经酰胺、胞质照射、旁观者效应均有实验证据</li></ul></div>
<div class="card box" data-b="2" style="border-top:6px solid var(--eo)"><h3><span class="tag eo">关联</span></h3><ul>
<li>增殖越活跃的细胞对 DNA 损伤越敏感</li><li>内皮丢失与晚期纤维化、萎缩相伴出现</li><li>FAP 衰老与照射后肌肉纤维化相关（Collao 2023）</li></ul></div>
<div class="card box" data-b="3" style="border-top:6px solid var(--warn)"><h3><span class="tag wn">推测</span></h3><ul>
<li>静息卫星细胞的 DNA 损伤可能在被唤醒时才暴露</li><li>肌纤维本身的损伤可能以线粒体 / ROS 为主</li><li>p21 可能是卫星细胞线的关键节点（与 U00 呼应）</li></ul></div></div>'''))
P.append(('自测','自测','''<div class="dense"><div class="hd"><div class="kick"><span class="no">09</span>费曼输出 + 自测</div><h2 class="t">能讲给实习生听，才算懂</h2></div>
<div class="g2" style="grid-template-columns:1fr 1.3fr">
<div class="card box" data-b="1"><h3><span class="tag eo">费曼开头</span></h3><p class="feyn">射线穿过细胞时会到处“打碎东西”，但真正决定细胞还能不能分裂的，是细胞核里的 DNA 有没有被整个打断……</p><p style="margin-top:12px">续写到“为什么肌纤维不太会被射线直接杀死”为止。配套 <a href="../cards/x01-cards-v0.1.html">26 张思维卡片</a>。</p></div>
<div class="card box" data-b="2">
<div class="q"><p><span class="lv">记忆</span>每 Gy 产生的 SSB 和 DSB 大约各多少？</p><details><summary>答案</summary><p>SSB 约 1000，DSB 约 20–40（教材量级）。</p></details></div>
<div class="q"><p><span class="lv">理解</span>Warters 为什么用 ¹²⁵I？</p><details><summary>答案</summary><p>¹²⁵I 衰变释放射程极短的俄歇电子，能量几乎只沉积在它所在的位置，可以分别“只照 DNA”或“只照膜”。</p></details></div>
<div class="q"><p><span class="lv">应用</span>照射后的细胞第二天看起来正常，能说明它没受伤吗？</p><details><summary>答案</summary><p>不能。它可能在之后第 1 到数次分裂时死于有丝分裂灾难，或已进入衰老。</p></details></div>
<div class="q"><p><span class="lv">分析</span>Garcia-Barros 2003 说明了什么？</p><details><summary>答案</summary><p>组织的放射反应不只取决于靶细胞自身 DNA，内皮细胞经膜神经酰胺的凋亡也能左右结局。</p></details></div>
<div class="q"><p><span class="lv">评价</span>“辐射损伤肌肉＝打断肌纤维 DNA”对吗？</p><details><summary>答案</summary><p>不全对。肌纤维不分裂，主要通过卫星细胞（DNA 线）和 FAP、内皮等微环境（非 DNA 线）受损。</p></details></div></div></div></div>'''))
refs=[('Munro TR. The relative radiosensitivity of the nucleus and cytoplasm of Chinese hamster fibroblasts. Radiat Res 1970;42:451–70.','5463516',''),
('Taylor AM, et al. Ataxia telangiectasia: a human mutation with abnormal radiation sensitivity. Nature 1975;258:427–9.','1196376','10.1038/258427a0'),
('Warters RL, et al. Radionuclide toxicity in cultured mammalian cells: elucidation of the primary site of radiation damage. Curr Top Radiat Res Q 1978;12:389–407.','565271',''),
('Ward JF. DNA damage produced by ionizing radiation in mammalian cells. Prog Nucleic Acid Res Mol Biol 1988;35:95–125.','3065826','10.1016/s0079-6603(08)60611-x'),
('Nagasawa H, Little JB. Induction of sister chromatid exchanges by extremely low doses of alpha-particles. Cancer Res 1992;52:6394–6.','1423287',''),
('Rosenblatt JD, Parry DJ. Gamma irradiation prevents compensatory hypertrophy of overloaded mouse EDL muscle. J Appl Physiol 1992;73:2538–43.','1490967','10.1152/jappl.1992.73.6.2538'),
('Haimovitz-Friedman A, et al. Ionizing radiation acts on cellular membranes to generate ceramide and initiate apoptosis. J Exp Med 1994;180:525–35.','8046331','10.1084/jem.180.2.525'),
('Rogakou EP, et al. DNA double-stranded breaks induce histone H2AX phosphorylation on serine 139. J Biol Chem 1998;273:5858–68.','9488723','10.1074/jbc.273.10.5858'),
('Wu LJ, et al. Targeted cytoplasmic irradiation with alpha particles induces mutations in mammalian cells. PNAS 1999;96:4959–64.','10220401','10.1073/pnas.96.9.4959'),
('Garcia-Barros M, et al. Tumor response to radiotherapy regulated by endothelial cell apoptosis. Science 2003;300:1155–9.','12750523','10.1126/science.1082504'),
('Lomax ME, et al. Biological consequences of radiation-induced DNA damage: relevance to radiotherapy. Clin Oncol 2013;25:578–85.','23849504','10.1016/j.clon.2013.06.007'),
('Collao N, et al. Radiation induces long-term muscle fibrosis and promotes a fibrotic phenotype in fibro-adipogenic progenitors. J Cachexia Sarcopenia Muscle 2023;14:2335–49.','37671686','10.1002/jcsm.13320')]
li=''.join(f'<li>{t} {pm(p)}{" · doi:"+d if d else ""}</li>' for t,p,d in refs)
P.append(('出处','出处',f'''<div class="dense"><div class="hd"><div class="kick"><span class="no">10</span>出处</div><h2 class="t">12 篇文献，PMID / DOI 均经 PubMed 核对（2026-10-27）</h2></div>
<div class="card box" data-b="1"><ol style="font-size:16px;line-height:1.55">{li}</ol>
<p class="cap" style="margin-top:10px">图均为自绘或 AI 生成；未收录任何原文图片。实验细节以原文为准。</p></div></div>'''))
secs='\n'.join(f'<section class="page" id="p{i+1}" data-title="{t}" data-mag="{m}">\n{b}\n</section>' for i,(t,m,b) in enumerate(P))
open('units/x01-radiation-targets-v0.2.html','w').write(wrap('补充单元 X01 · 辐射到底打中了什么 · 细胞周期从零学','补充单元 X01 · 辐射靶点',secs))
for i,s in enumerate([targets_svg(),evidence_svg(),death_svg()]): open(f'/workspace/work/x01-{i}.svg','w').write(s.replace('Noto Sans SC,PingFang SC,sans-serif','WenQuanYi Zen Hei'))
print('ok',len(P))
