// cell-cycle-from-zero 翻页脚本 v0.2：←/→ 翻页、T 目录、R 阅读模式、P 打印；点进度条跳页；手机滑动
(function(){
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const pages=$$('.page');let cur=0;
const isRead=()=>document.body.classList.contains('read');
function fit(){if(isRead())return;const s=Math.min(innerWidth/1920,innerHeight/1080),st=$('#stage');st.style.transform=`scale(${s})`;st.style.left=(innerWidth-1920*s)/2+'px';st.style.top=(innerHeight-1080*s)/2+'px'}
const dots=$('#prog .dots');pages.forEach(()=>dots.appendChild(document.createElement('i')));
$('#tocList').innerHTML=pages.map((p,i)=>`<button data-i="${i}"><span class="n">${String(i).padStart(2,'0')}</span>${p.dataset.title}</button>`).join('');
$$('#tocList button').forEach(b=>b.onclick=()=>{go(+b.dataset.i);$('#toc').classList.remove('show')});
function go(i){i=Math.max(0,Math.min(pages.length-1,i));pages[cur].classList.remove('cur');cur=i;const p=pages[i];void p.offsetWidth;p.classList.add('cur');
$('#chapName').textContent=String(i).padStart(2,'0')+' · '+p.dataset.title;$('#magbadge .obj').textContent=p.dataset.mag||'';$('#magbadge .idx').textContent=(i+1)+' / '+pages.length;
$('#prog .fill').style.width=(pages.length>1?i/(pages.length-1)*100:100)+'%';$$('#prog .dots i').forEach((d,j)=>d.classList.toggle('done',j<=i));$$('#tocList button').forEach((b,j)=>b.classList.toggle('cur',j===i));history.replaceState(null,'','#'+(i+1))}
function setRead(on){document.body.classList.toggle('read',on);document.documentElement.classList.toggle('read',on);$('#bRead').textContent=on?'翻页模式':'阅读模式';
if(on){const st=$('#stage');st.style.left=st.style.top='0'}else fit();try{localStorage.setItem('ccRead',on?'1':'0')}catch(e){}}
$('#bPrev').onclick=()=>go(cur-1);$('#bNext').onclick=()=>go(cur+1);$('#bToc').onclick=()=>$('#toc').classList.toggle('show');
$('#bPrint').onclick=()=>print();$('#bRead').onclick=()=>setRead(!isRead());
$('#prog').onclick=e=>{const r=e.currentTarget.getBoundingClientRect();go(Math.round((e.clientX-r.left)/r.width*(pages.length-1)))};
addEventListener('keydown',e=>{if(e.target.tagName==='SUMMARY')return;
if(e.key==='r'||e.key==='R'){setRead(!isRead());return}if(isRead())return;
if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();go(cur+1)}else if(['ArrowLeft','PageUp'].includes(e.key))go(cur-1);
else if(e.key==='t'||e.key==='T')$('#toc').classList.toggle('show');else if(e.key==='p'||e.key==='P')print();else if(e.key==='Escape')$('#toc').classList.remove('show')});
let tx=null;addEventListener('touchstart',e=>tx=e.touches[0].clientX);addEventListener('touchend',e=>{if(tx===null||isRead())return;const d=e.changedTouches[0].clientX-tx;if(Math.abs(d)>50)go(cur+(d<0?1:-1));tx=null});
addEventListener('resize',fit);
go(Math.max(0,(parseInt(location.hash.slice(1))||1)-1));
let pref=null;try{pref=localStorage.getItem('ccRead')}catch(e){}
setRead(pref==='1'||(pref===null&&innerWidth<1000));
})();
