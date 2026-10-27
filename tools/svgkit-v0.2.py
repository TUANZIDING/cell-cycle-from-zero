# 自绘示意图工具 v0.2：统一的渐变、阴影和配色
BLUE,BLUE2,BLUE3,HE,EO,OK,WARN,INK,INK2,MUTE='#1B5FA8','#3F8BD6','#DCE8F6','#5B3F9E','#D9719C','#2E9E7A','#D4793A','#1C2333','#3A4357','#667085'
def defs(p):
    return f'''<defs>
<filter id="{p}sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#1C2850" flood-opacity=".13"/></filter>
<filter id="{p}gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
<radialGradient id="{p}cell" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#E4EEFA"/><stop offset="1" stop-color="#BCD3EE"/></radialGradient>
<radialGradient id="{p}nuc" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#A88BE0"/><stop offset="1" stop-color="#5B3F9E"/></radialGradient>
<linearGradient id="{p}bp" x1="0" x2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset=".6" stop-color="#8E6BC8"/><stop offset="1" stop-color="{EO}"/></linearGradient>
<linearGradient id="{p}card" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#F4F7FC"/></linearGradient>
<marker id="{p}ar" markerUnits="userSpaceOnUse" markerWidth="18" markerHeight="18" refX="16" refY="9" orient="auto"><path d="M1,2 L17,9 L1,16 Q5,9 1,2z" fill="{HE}"/></marker>
<marker id="{p}arg" markerUnits="userSpaceOnUse" markerWidth="18" markerHeight="18" refX="16" refY="9" orient="auto"><path d="M1,2 L17,9 L1,16 Q5,9 1,2z" fill="{MUTE}"/></marker>
</defs>'''
def yeast(p,cx,cy,bud=0,nuc='m',sc=1.0,sep=False):
    """bud: 0 无芽, 1 小芽, 2 中芽, 3 大芽；nuc: m 母细胞内, neck 颈部哑铃, two 两核"""
    o=[]
    rx,ry=34*sc,29*sc
    if sep:
        o.append(f'<ellipse cx="{cx-30*sc}" cy="{cy}" rx="{rx*.92}" ry="{ry*.92}" fill="url(#{p}cell)" stroke="{BLUE}" stroke-width="2.5"/>')
        o.append(f'<ellipse cx="{cx+34*sc}" cy="{cy}" rx="{rx*.92}" ry="{ry*.92}" fill="url(#{p}cell)" stroke="{BLUE}" stroke-width="2.5"/>')
        o.append(f'<circle cx="{cx-30*sc}" cy="{cy}" r="{10*sc}" fill="url(#{p}nuc)"/><circle cx="{cx+34*sc}" cy="{cy}" r="{10*sc}" fill="url(#{p}nuc)"/>')
        return ''.join(o)
    br={0:0,1:8,2:18,3:27}[bud]*sc
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="url(#{p}cell)" stroke="{BLUE}" stroke-width="2.5"/>')
    if br:
        bx=cx+rx+br*.75
        o.append(f'<circle cx="{bx}" cy="{cy}" r="{br}" fill="url(#{p}cell)" stroke="{BLUE}" stroke-width="2.5"/>')
    if nuc=='m': o.append(f'<circle cx="{cx-4*sc}" cy="{cy+2*sc}" r="{11*sc}" fill="url(#{p}nuc)"/>')
    elif nuc=='neck':
        bx=cx+rx+br*.75
        o.append(f'<path d="M{cx+4*sc},{cy} Q{cx+rx},{cy-5*sc} {bx-4*sc},{cy}" stroke="{HE}" stroke-width="{9*sc}" stroke-linecap="round" fill="none" opacity=".9"/>')
        o.append(f'<circle cx="{cx+2*sc}" cy="{cy}" r="{9*sc}" fill="url(#{p}nuc)"/><circle cx="{bx-2*sc}" cy="{cy}" r="{8*sc}" fill="url(#{p}nuc)"/>')
    return ''.join(o)
