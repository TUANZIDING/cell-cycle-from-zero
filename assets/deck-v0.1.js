// cell-cycle-from-zero 翻页脚本 v0.1：←/→ 翻页，T 目录，R 阅读模式
(function(){
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const pages=$$('.page');let cur=0;
function fit(){if(document.body.classList.contains('read'))return;const s=Math.min(innerWidth/1920,innerHeight/1080),st=$('#stage');
st.style.transform=`scale(${s})`;st.style.left=(innerWidth-1920*s)/2+'px';st.style.top=(innerHeight-1080*s)/2+'px'}
function go(i){i=Math.max(0,Math.min(pages.length-1,i));pages[cur].classList.remove('cur');cur=i;pages[i].classList.add('cur');
$('#chap').textContent=String(i+1).padStart(2,'0')+' · '+pages[i].dataset.title;$('#idx').textContent=(i+1)+' / '+pages.length;
$('#prog .fill').style.width=(pages.length>1?i/(pages.length-1)*100:100)+'%';
$$('#toc button').forEach((b,j)=>b.classList.toggle('cur',j===i));history.replaceState(null,'','#'+(i+1))}
function setRead(on){document.body.classList.toggle('read',on);document.documentElement.classList.toggle('read',on);$('#bRead').textContent=on?'翻页模式':'阅读模式';
if(!on)fit();else{const st=$('#stage');st.style.left=st.style.top='0'};try{localStorage.setItem('ccRead',on?'1':'0')}catch(e){}}
$('#toc').innerHTML=pages.map((p,i)=>`<button data-i="${i}"><span class="n">${String(i+1).padStart(2,'0')}</span>${p.dataset.title}</button>`).join('');
$$('#toc button').forEach(b=>b.onclick=()=>{const i=+b.dataset.i;go(i);$('#toc').classList.remove('show')});
$('#bPrev').onclick=()=>go(cur-1);$('#bNext').onclick=()=>go(cur+1);$('#bToc').onclick=()=>$('#toc').classList.toggle('show');
$('#bRead').onclick=()=>setRead(!document.body.classList.contains('read'));
addEventListener('keydown',e=>{if(document.body.classList.contains('read')&&e.key!=='r'&&e.key!=='R')return;
if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();go(cur+1)}else if(['ArrowLeft','PageUp'].includes(e.key))go(cur-1);
else if(e.key==='t'||e.key==='T')$('#toc').classList.toggle('show');else if(e.key==='r'||e.key==='R')setRead(!document.body.classList.contains('read'))});
addEventListener('resize',fit);
const h=parseInt(location.hash.slice(1));go(isNaN(h)?0:h-1);
let pref=null;try{pref=localStorage.getItem('ccRead')}catch(e){}
setRead(pref==='1'||(pref===null&&innerWidth<1000));
})();
