# 共用外壳 v0.2：沿用个人精读笔记的翻页框架（品牌、徽章、底栏进度点、目录）
def wrap(title, brand_sub, sections, depth=1):
    up='../'*depth
    return f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{up}assets/deck-v0.2.css">
</head><body>
<div id="viewport"><div id="stage">
<div id="brand"><a href="{up}index.html"><span class="dot"></span><b>细胞周期从零学</b></a><span>· {brand_sub}</span></div>
<div id="magbadge"><span class="obj">封面</span><span class="idx">1 / 1</span></div>
<div id="pages">
{sections}
</div>
<div id="toc" class="card"><h4>目录</h4><div id="tocList"></div></div>
<div id="bar"><button class="ib" id="bToc" title="目录 T"><svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h10"/></svg></button>
<button class="ib" id="bPrev" title="上一页 ←"><svg viewBox="0 0 24 24"><path d="M15 6l-6 6 6 6"/></svg></button>
<button class="ib" id="bNext" title="下一页 →"><svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg></button>
<div id="chapName"></div><div id="prog"><div class="tr"></div><div class="fill"></div><div class="dots"></div></div>
<button class="ib" id="bRead" title="阅读模式 R">阅读模式</button>
<a class="ib" href="{up}index.html" title="总览"><svg viewBox="0 0 24 24"><path d="M3 11l9-7 9 7M5 10v10h14V10"/></svg></a>
<button class="ib" id="bPrint" title="打印 / 导出 PDF"><svg viewBox="0 0 24 24"><path d="M6 9V3h12v6M6 18H4v-7h16v7h-2M8 14h8v7H8z"/></svg></button></div>
</div></div>
<script src="{up}assets/deck-v0.2.js"></script>
</body></html>
'''
