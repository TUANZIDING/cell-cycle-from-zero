# 共用外壳：把各页 <section> 包进统一的翻页框架
def wrap(title, brand_sub, sections, depth=1):
    up = '../' * depth
    return f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{up}assets/deck-v0.1.css">
</head><body>
<div id="viewport"><div id="stage">
<div id="brand"><a href="{up}index.html"><span class="dot"></span><b>细胞周期从零学</b></a><span>· {brand_sub}</span></div>
<div id="badge"><span id="idx">1 / 1</span></div>
{sections}
<div id="toc" class="card"></div>
<div id="prog"><div class="fill"></div></div>
<div id="nav"><button id="bPrev">← 上一页</button><span id="chap"></span><button id="bNext">下一页 →</button><button id="bToc">目录</button><button id="bRead">阅读模式</button><a class="btn" href="{up}index.html">总览</a></div>
</div></div>
<script src="{up}assets/deck-v0.1.js"></script>
</body></html>
'''
