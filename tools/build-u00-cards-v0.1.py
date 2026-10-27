# 由 cards/u00-map-anki-v0.1.txt 生成可翻面的思维卡片网页 cards/u00-cards-v0.1.html
import html, re, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, 'cards/u00-map-anki-v0.1.txt'), encoding='utf-8').read()
rows = [l.split('\t') for l in src.splitlines() if l.strip() and not l.startswith('#')]

TOPICS = {
 '01_周期引擎':   ('01', '周期引擎',     '#1B5FA8', '#DCE8F6'),
 '02_三个关口':   ('02', '三个关口',     '#5B3F9E', '#ECE5F7'),
 '03_DNA损伤应答':('03', 'DNA 损伤应答', '#C2477A', '#FBE7EF'),
 '04_细胞命运':   ('04', '细胞命运',     '#B88A3B', '#F6EEDC'),
 '05_有丝分裂':   ('05', '有丝分裂',     '#2E9E7A', '#E1F3EC'),
 '06_骨骼肌修复': ('06', '骨骼肌修复',   '#D4793A', '#FBEADD'),
 '07_周日自测':   ('07', '周日自测',     '#3A4357', '#E8EBF0'),
}
ICON = {
 '01': '<circle cx="40" cy="40" r="24" fill="none" stroke="C" stroke-width="5" stroke-dasharray="118 33" stroke-linecap="round"/><path d="M58 18l6 12-13 1z" fill="C"/><circle cx="40" cy="40" r="9" fill="L" stroke="C" stroke-width="3"/>',
 '02': '<rect x="12" y="20" width="10" height="44" rx="3" fill="C"/><rect x="58" y="20" width="10" height="44" rx="3" fill="C"/><rect x="22" y="34" width="36" height="7" rx="3.5" fill="C" opacity=".55"/><circle cx="40" cy="20" r="7" fill="none" stroke="C" stroke-width="3"/>',
 '03': '<path d="M22 10c22 12 14 24 0 30M58 10c-22 12-14 24 0 30" fill="none" stroke="C" stroke-width="4" stroke-linecap="round"/><path d="M22 52c22 6 14 14 0 20M58 52c-22 6-14 14 0 20" fill="none" stroke="C" stroke-width="4" stroke-linecap="round" opacity=".55"/><path d="M30 44l8-4 4 6 8-5" fill="none" stroke="#E0A32E" stroke-width="3.5" stroke-linecap="round"/>',
 '04': '<circle cx="18" cy="40" r="8" fill="C"/><path d="M26 40h12M38 40l20-20M38 40h22M38 40l20 20" stroke="C" stroke-width="4" stroke-linecap="round" fill="none"/><circle cx="62" cy="18" r="5" fill="C" opacity=".5"/><circle cx="64" cy="40" r="5" fill="C" opacity=".75"/><circle cx="62" cy="62" r="5" fill="C" opacity=".35"/>',
 '05': '<ellipse cx="26" cy="40" rx="16" ry="20" fill="L" stroke="C" stroke-width="4"/><ellipse cx="54" cy="40" rx="16" ry="20" fill="L" stroke="C" stroke-width="4"/><path d="M22 34l6 12M30 34l-6 12M50 34l6 12M58 34l-6 12" stroke="C" stroke-width="3" stroke-linecap="round"/>',
 '06': '<rect x="8" y="22" width="64" height="10" rx="5" fill="C"/><rect x="8" y="36" width="64" height="10" rx="5" fill="C" opacity=".7"/><rect x="8" y="50" width="64" height="10" rx="5" fill="C" opacity=".45"/><circle cx="46" cy="33.5" r="5" fill="#fff" stroke="C" stroke-width="2.5"/>',
 '07': '<circle cx="40" cy="40" r="26" fill="L" stroke="C" stroke-width="4"/><path d="M31 32a9 9 0 1 1 13 8c-3 2-4 3-4 7" fill="none" stroke="C" stroke-width="4.5" stroke-linecap="round"/><circle cx="40" cy="56" r="3" fill="C"/>',
}
def icon(no, c, l):
    return '<svg viewBox="0 0 80 80" aria-hidden="true">' + ICON[no].replace('"C"', f'"{c}"').replace('"L"', f'"{l}"') + '</svg>'

cards = []
for i, (front, back, tags) in enumerate(rows, 1):
    key = [t for t in tags.split() if t in TOPICS][0]
    no, name, c, l = TOPICS[key]
    kind = '术语'
    m = re.match(r'【(.+?)】(.*)', front)
    if m:
        kind, front = m.group(1).replace('·', ' · '), m.group(2)
    # 术语正面：主名 + 括号里的全称/中文
    m2 = re.match(r'(.+?)\s*[（(](.+)[)）]\s*$', front)
    main, sub = (m2.group(1), m2.group(2)) if (m2 and kind == '术语') else (front, '')
    cards.append(dict(i=i, no=no, name=name, c=c, l=l, kind=kind, main=main, sub=sub, back=back, spec='推测' in back))

def card_html(k):
    q = ' q' if k['kind'] != '术语' else ''
    sub = f'<div class="sub">{html.escape(k["sub"])}</div>' if k['sub'] else ''
    spec = '<span class="spec">含推测</span>' if k['spec'] else ''
    return f'''<div class="fc{q}" data-t="{k['no']}" data-i="{k['i']}" style="--c:{k['c']};--l:{k['l']}" tabindex="0">
<div class="in"><div class="face front">
<div class="top"><span class="chip">{k['no']} · {k['name']}</span><span class="num">#{k['i']:02d}</span></div>
<div class="ic">{icon(k['no'], k['c'], k['l'])}</div>
<div class="kind">{html.escape(k['kind'])}</div><div class="main">{html.escape(k['main'])}</div>{sub}
<div class="hint">点击翻面 ↻</div></div>
<div class="face back"><div class="top"><span class="chip">{html.escape(k['main'][:22] if not q else k['kind'])}</span>{spec}</div>
<div class="ans">{k['back']}</div>
<div class="bot"><button class="ok" data-act="ok">✓ 已掌握</button><span class="hint">再点翻回</span></div></div></div></div>'''

chips = ''.join(f'<button class="f" data-f="{v[0]}" style="--c:{v[2]};--l:{v[3]}">{v[0]} {v[1]}<i>{sum(1 for k in cards if k["no"]==v[0])}</i></button>' for v in TOPICS.values())

page = f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>U00 思维卡片 · 细胞周期从零学</title>
<link rel="stylesheet" href="../assets/deck-v0.2.css">
<style>
html,body{{overflow:auto;height:auto;background:radial-gradient(1200px 700px at 85% -10%,rgba(63,139,214,.10),transparent 60%),radial-gradient(900px 600px at -5% 105%,rgba(217,113,156,.09),transparent 60%),var(--bg)}}
body::before{{content:"";position:fixed;inset:0;pointer-events:none;opacity:.45;background-image:radial-gradient(rgba(27,95,168,.10) 1px,transparent 1.2px);background-size:28px 28px}}
.wrap{{position:relative;max-width:1320px;margin:0 auto;padding:40px 28px 80px}}
.topbar{{display:flex;align-items:center;gap:14px;color:var(--ink2);font-size:17px}}
.topbar a{{color:var(--blue);text-decoration:none}}
.topbar .dot{{width:32px;height:32px;border-radius:50%;border:2px solid var(--blue);position:relative}}
.topbar .dot::after{{content:"";position:absolute;inset:7px;border-radius:50%;background:var(--eo)}}
h1{{font-family:var(--serif);font-size:46px;margin:28px 0 8px}}h1 em{{font-style:normal;color:var(--eo)}}
.intro{{font-size:17px;line-height:1.7;color:var(--ink2);max-width:880px}}
.bar{{position:sticky;top:0;z-index:20;margin:24px -12px 22px;padding:12px;border-radius:18px;background:rgba(246,245,241,.86);backdrop-filter:blur(14px);display:flex;flex-wrap:wrap;gap:8px;align-items:center}}
.bar button{{padding:7px 14px;border-radius:30px;font-size:15px;background:var(--glass);border:1px solid var(--glassb);box-shadow:0 2px 8px rgba(28,40,80,.06)}}
.bar .f{{border-left:5px solid var(--c)}}.bar .f i{{font-style:normal;margin-left:6px;color:var(--mute);font-size:13px}}
.bar .f.on{{background:var(--l);color:var(--c);font-weight:700}}
.bar .sp{{flex:1}}.bar .act.on{{background:var(--ink);color:#fff}}
#prog{{flex-shrink:0;min-width:max-content;white-space:nowrap;font-size:14px;color:var(--mute);font-variant-numeric:tabular-nums}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:22px}}
.fc.q{{grid-column:span 2}}
.fc{{min-height:360px;perspective:1400px;cursor:pointer;outline:none}}
.fc .in{{position:relative;display:grid;width:100%;min-height:360px;transition:transform .7s cubic-bezier(.2,.8,.2,1);transform-style:preserve-3d}}
.fc.flip .in{{transform:rotateY(180deg)}}
.face{{grid-area:1/1;position:relative;min-height:360px;border-radius:22px;padding:20px 22px;backface-visibility:hidden;-webkit-backface-visibility:hidden;display:flex;flex-direction:column;
background:var(--glass);backdrop-filter:blur(18px);border:1px solid var(--glassb);box-shadow:var(--sh);overflow:hidden}}
.face::before{{content:"";position:absolute;left:0;top:0;right:0;height:6px;background:linear-gradient(90deg,var(--c),transparent)}}
.front{{background:radial-gradient(260px 200px at 100% 0%,var(--l),transparent 70%),var(--glass)}}
.back{{transform:rotateY(180deg);background:linear-gradient(180deg,var(--l),rgba(255,255,255,.85) 38%)}}
.top{{display:flex;justify-content:space-between;align-items:center;gap:8px}}
.chip{{font-size:13px;font-weight:700;letter-spacing:.06em;color:var(--c);background:#fff;padding:3px 10px;border-radius:20px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.num{{font-family:var(--serif);color:var(--mute);font-size:15px}}
.ic{{width:76px;height:76px;margin:22px 0 10px}}.ic svg{{width:100%;height:100%}}
.kind{{font-size:13px;letter-spacing:.2em;color:var(--mute)}}
.main{{font-family:var(--serif);font-size:30px;font-weight:600;line-height:1.3;margin-top:6px;color:var(--ink)}}
.q .main{{font-size:22px;line-height:1.45}}
.sub{{margin-top:8px;font-size:15px;line-height:1.5;color:var(--ink2)}}
.hint{{margin-top:auto;font-size:13px;color:var(--mute)}}
.ans{{margin-top:14px;font-size:16.5px;line-height:1.75;color:var(--ink);overflow:auto}}
.ans b{{color:var(--c)}}.q .ans{{font-size:15px;line-height:1.7}}
.spec{{font-size:12px;font-weight:700;color:#9A5B12;background:#FCEFD9;padding:2px 8px;border-radius:12px}}
.bot{{flex-shrink:0;margin-top:auto;padding-top:10px;display:flex;justify-content:space-between;align-items:center}}
.ok{{font-size:14px;padding:5px 12px;border-radius:20px;background:#fff;border:1px solid var(--line)}}
.fc.done .ok{{background:var(--ok);color:#fff}}
.fc.done .front::after{{content:"✓ 已掌握";position:absolute;right:18px;bottom:16px;font-size:13px;font-weight:700;color:var(--ok)}}
.hide{{display:none}}
/* 专注模式 */
#focus{{position:fixed;inset:0;z-index:50;background:rgba(233,236,241,.94);backdrop-filter:blur(8px);display:none;align-items:center;justify-content:center;flex-direction:column;gap:18px}}
#focus.on{{display:flex}}#focus .slot .fc{{width:min(620px,92vw);max-height:84vh;overflow:auto}}#focus .slot .fc .in,#focus .slot .face{{min-height:min(560px,70vh)}}
#focus .slot .main{{font-size:42px}}#focus .slot .q .main{{font-size:30px}}#focus .slot .ans{{font-size:21px}}#focus .slot .q .ans{{font-size:19px}}
#focus .slot .ic{{width:110px;height:110px}}
#focus .nav{{display:flex;gap:12px;align-items:center;font-size:15px;color:var(--ink2)}}
#focus .nav button{{padding:8px 16px;border-radius:30px;background:#fff;border:1px solid var(--line)}}
.foot{{margin-top:44px;font-size:14px;color:var(--mute);line-height:1.7}}
@media(max-width:680px){{.fc.q{{grid-column:auto}}}}
@media print{{
 .fc.q{{grid-column:auto}}
 .bar,#focus,.topbar,.hint,.ok{{display:none!important}}html,body{{background:#fff}}body::before{{display:none}}
 .grid{{grid-template-columns:1fr 1fr;gap:10px}}.fc{{height:auto;break-inside:avoid;perspective:none}}
 .fc .in{{transform:none!important;display:grid;grid-template-columns:1fr 1.5fr}}
 .face{{position:relative;transform:none;backface-visibility:visible;box-shadow:none;border:1px solid #ddd;backdrop-filter:none;min-height:200px}}
 .ic{{width:44px;height:44px;margin:10px 0 4px}}.main{{font-size:20px}}.q .main{{font-size:15px}}.ans{{font-size:12px;overflow:visible}}
}}
</style></head><body><div class="wrap">
<div class="topbar"><span class="dot"></span><a href="../index.html"><b style="font-family:var(--serif)">细胞周期从零学</b></a><span>· U00 思维卡片</span><span style="flex:1"></span><a href="../units/u00-map-v0.2.html">← 回到 U00 讲义</a></div>
<h1>U00 总地图 · <em>{len(cards)} 张思维卡片</em></h1>
<p class="intro">先看正面，在心里说出答案，再点卡片翻面核对。答对点“已掌握”，进度存在本机浏览器里。按 1、3、7、14 天间隔回来复习；“专注模式”一次只看一张（空格翻面，←/→ 换卡，K 标记掌握）。同一套内容的 Anki 导入版：<a href="u00-map-anki-v0.1.txt">u00-map-anki-v0.1.txt</a>。</p>
<div class="bar"><button class="f on" data-f="all" style="--c:var(--ink);--l:#fff">全部<i>{len(cards)}</i></button>{chips}
<span class="sp"></span><span id="prog"></span>
<button class="act" id="bTodo">只看未掌握</button><button class="act" id="bShuf">打乱</button><button class="act" id="bFlip">全部翻面</button><button class="act" id="bFocus">专注模式</button><button class="act" id="bReset">清空进度</button></div>
<div class="grid" id="grid">
{''.join(card_html(k) for k in cards)}
</div>
<p class="foot">卡片内容为个人学习笔记；“含推测”标签表示该卡有尚待文献证实的推断，与讲义中“事实 / 关联 / 推测”的标注一致。打印（⌘P）时自动排成正反面并排的两栏讲义。CC BY 4.0。</p>
</div>
<div id="focus"><div class="slot"></div><div class="nav"><button id="fPrev">← 上一张</button><span id="fIdx"></span><button id="fNext">下一张 →</button><button id="fClose">关闭 Esc</button></div></div>
<script>
(function(){{
const KEY='ccfz-u00-cards-done';let done=new Set(JSON.parse(localStorage.getItem(KEY)||'[]'));
const grid=document.getElementById('grid'),all=[...grid.querySelectorAll('.fc')];
let filt='all',todo=false;
function save(){{localStorage.setItem(KEY,JSON.stringify([...done]));}}
function paint(){{all.forEach(c=>c.classList.toggle('done',done.has(c.dataset.i)));
 all.forEach(c=>c.classList.toggle('hide',(filt!=='all'&&c.dataset.t!==filt)||(todo&&done.has(c.dataset.i))));
 document.getElementById('prog').textContent='已掌握 '+done.size+' / '+all.length;}}
function vis(){{return [...grid.querySelectorAll('.fc:not(.hide)')];}}
function toggleDone(c){{const i=c.dataset.i;done.has(i)?done.delete(i):done.add(i);save();paint();}}
grid.addEventListener('click',e=>{{const c=e.target.closest('.fc');if(!c)return;
 if(e.target.closest('[data-act=ok]')){{e.stopPropagation();toggleDone(c);return;}}c.classList.toggle('flip');}});
grid.addEventListener('keydown',e=>{{if(e.key===' '||e.key==='Enter'){{e.preventDefault();e.target.closest('.fc')?.classList.toggle('flip');}}}});
document.querySelectorAll('.bar .f').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.bar .f').forEach(x=>x.classList.remove('on'));b.classList.add('on');filt=b.dataset.f;paint();}});
bTodo.onclick=()=>{{todo=!todo;bTodo.classList.toggle('on',todo);paint();}};
bShuf.onclick=()=>{{const a=[...all];for(let i=a.length-1;i>0;i--){{const j=Math.random()*(i+1)|0;[a[i],a[j]]=[a[j],a[i]];}}a.forEach(c=>grid.appendChild(c));all.splice(0,all.length,...a);}};
bFlip.onclick=()=>{{const v=vis();const any=v.some(c=>!c.classList.contains('flip'));v.forEach(c=>c.classList.toggle('flip',any));}};
bReset.onclick=()=>{{if(confirm('清空本机的掌握进度？')){{done.clear();save();paint();}}}};
// 专注模式
const F=document.getElementById('focus'),slot=F.querySelector('.slot');let fi=0,fl=[];
function show(){{slot.innerHTML='';if(!fl.length)return;const c=fl[fi].cloneNode(true);c.classList.remove('flip','hide');slot.appendChild(c);
 c.onclick=e=>{{if(e.target.closest('[data-act=ok]')){{e.stopPropagation();toggleDone(fl[fi]);c.classList.toggle('done',done.has(c.dataset.i));return;}}c.classList.toggle('flip');}};
 fIdx.textContent=(fi+1)+' / '+fl.length;}}
bFocus.onclick=()=>{{fl=vis();fi=0;F.classList.add('on');show();}};
fPrev.onclick=()=>{{fi=(fi-1+fl.length)%fl.length;show();}};fNext.onclick=()=>{{fi=(fi+1)%fl.length;show();}};fClose.onclick=()=>F.classList.remove('on');
document.addEventListener('keydown',e=>{{if(!F.classList.contains('on'))return;const c=slot.querySelector('.fc');
 if(e.key==='ArrowRight')fNext.onclick();else if(e.key==='ArrowLeft')fPrev.onclick();else if(e.key==='Escape')fClose.onclick();
 else if(e.key===' '){{e.preventDefault();c&&c.classList.toggle('flip');}}else if(e.key.toLowerCase()==='k'&&c){{toggleDone(fl[fi]);c.classList.toggle('done',done.has(c.dataset.i));}}}});
paint();
}})();
</script></body></html>'''
open(os.path.join(ROOT, 'cards/u00-cards-v0.1.html'), 'w', encoding='utf-8').write(page)
print('cards', len(cards))
