"""Original geometric drawings for the Zamurek icon system. No icon library."""
import math, html

PALETTE={'g':'#005C45','o':'#FF8A1E','m':'#D21868','p':'#F8F7EA','d':'#003B2D'}
def esc(s):return html.escape(str(s),quote=True)
class Canvas:
    def __init__(self,slug,mode):self.slug=slug;self.mode=mode;self.items=[]
    def shape(self,tag,attrs,tone='g',line=True):
        a=dict(attrs)
        if self.mode=='couleur':
            a.update(fill=f'url(#{self.slug}-{tone})' if tone in ['g','o','m'] else PALETTE.get(tone,tone),stroke=('#8BB5AA' if tone=='p' else '#E3F0D9') if line else 'none',**{'stroke-width':2.4,'stroke-opacity':.88})
            if tone=='p':a['data-paper-edge']='true'
        else:a.update(fill='none',stroke='currentColor',**{'stroke-width':4,'stroke-opacity':1})
        a.update({'stroke-linecap':'round','stroke-linejoin':'round'})
        self.items.append('<'+tag+' '+' '.join(f'{k}="{esc(v)}"' for k,v in a.items())+'/>')
    def path(self,d,t='g'):self.shape('path',{'d':d},t)
    def rect(self,x,y,w,h,r=7,t='g'):self.shape('rect',dict(x=x,y=y,width=w,height=h,rx=r),t)
    def circle(self,x,y,r,t='g'):self.shape('circle',dict(cx=x,cy=y,r=r),t)
    def ellipse(self,x,y,rx,ry,t='g'):self.shape('ellipse',dict(cx=x,cy=y,rx=rx,ry=ry),t)
    def line(self,d,t='p',w=4):
        data=f' data-solid-tone="{t}" data-paint="stroke"' if self.mode=='couleur' and t in ['g','o','m'] else ''
        self.items.append(f'<path d="{esc(d)}" fill="none" stroke="{PALETTE.get(t,t) if self.mode=="couleur" else "currentColor"}" stroke-width="{w if self.mode=="couleur" else 4}" stroke-linecap="round" stroke-linejoin="round"{data}/>')
    def dot(self,x,y,r=2.5,t='p'):
        data=f' data-solid-tone="{t}" data-paint="fill"' if self.mode=='couleur' and t in ['g','o','m'] else ''
        self.items.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{PALETTE.get(t,t) if self.mode=="couleur" else "currentColor"}"{data}/>')
    def glow(self,d):
        if self.mode=='couleur':self.items.append(f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-opacity=".22" stroke-width="3" stroke-linecap="round"/>')

def badge(c,b):
    if not b:return
    t='m' if b in ['minus','cancel','lock','alert'] else 'o'
    c.circle(76,76,13,t)
    if b in ['plus','minus']:c.line('M70 76H82'+(' M76 70V82' if b=='plus' else ''),w=3.5)
    elif b in ['check','approve']:c.line('M70 76L74 80L82 72',w=3.5)
    elif b=='cancel':c.line('M71 71L81 81M81 71L71 81',w=3.5)
    elif b=='clock':c.line('M76 69V76L81 79',w=3)
    elif b=='lock':c.rect(71,75,10,8,2,'p');c.line('M72 75V72A4 4 0 0 1 80 72V75',w=2.5)
    elif b=='alert':c.line('M76 69V77',w=3);c.dot(76,82,1.6)
    elif b=='arrow':c.line('M69 76H82M77 71L82 76L77 81',w=3)
    elif b=='star':star(c,76,76,8,'p')

def star(c,x=48,y=46,r=28,t='o'):
    ps=[]
    for i in range(10):
        a=-math.pi/2+i*math.pi/5;rr=r if i%2==0 else r*.46;ps.append((round(x+math.cos(a)*rr,2),round(y+math.sin(a)*rr,2)))
    c.path('M'+'L'.join(f'{x} {y}' for x,y in ps)+'Z',t)

def petal(c):
    c.circle(48,21,10,'g');c.path('M30 30Q48 36 66 30L54 45Q48 51 42 45Z')
    for d,t in [('M27 39L42 54Q45 58 41 62L29 74Q25 78 21 74L9 62Q5 58 9 54L21 42Q24 39 27 39Z','g'),('M69 39L84 54Q88 58 84 62L72 74Q68 78 64 74L52 62Q48 58 52 54L64 42Q67 39 69 39Z','o'),('M48 64L63 79Q66 82 63 85L51 94Q48 96 45 93L33 82Q30 79 33 76L44 66Q46 64 48 64Z','m')]:c.path(d,t)

def draw(c,k,t='g',arg=None):
    if k=='star':star(c,48,48,35,t)
    elif k=='home':
        c.path('M14 43L42 17Q48 12 54 17L82 43V77Q82 83 76 83H58V61H38V83H20Q14 83 14 77Z',t);c.glow('M20 43L45 21')
    elif k in ['search','zoom-in','zoom-out']:
        c.circle(40,39,25,t);c.circle(40,39,15,'p');c.path('M57 60L66 54L85 74Q89 79 83 84Q79 88 74 83Z','o')
        if k!='search':c.line('M32 39H48'+('M40 31V47' if k=='zoom-in' else ''),'g',3)
    elif k in ['grid','categories']:
        for x,y,tt in [(15,15,'o'),(53,15,'g'),(15,53,'g'),(53,53,'m')]:c.rect(x,y,28,28,8,tt)
    elif k=='bag':
        c.path('M21 32H75L81 78Q82 84 75 84H21Q14 84 15 78Z',t);c.line('M34 35V27C34 8 62 8 62 27V35','p',5);c.glow('M24 39L20 72')
    elif k=='cart':
        c.path('M24 29H84L75 63H32Z',t);c.line('M13 16H21L34 72H75','o',6);c.circle(38,82,6,'g');c.circle(70,82,6,'m');c.glow('M31 35H75')
    elif k=='heart':c.path('M48 83L15 51C-2 25 24 7 43 26L48 32L53 26C73 7 99 25 81 51Z',t)
    elif k=='person':c.circle(48,28,17,t);c.path('M17 83C17 48 79 48 79 83Z',t);c.glow('M23 75C26 63 36 59 43 59')
    elif k=='people':
        c.circle(31,30,12,'g');c.circle(66,33,11,'o');c.path('M10 79C10 51 53 51 53 79Z');c.path('M53 57C73 50 88 61 87 79H59','m')
    elif k=='menu':
        for y in [24,45,66]:c.rect(15,y,66,12,6,t)
    elif k=='document':
        c.path('M23 12H60L77 30V82H23Z',t);c.path('M60 12V30H77','p');c.line('M34 42H64M34 54H64M34 66H55')
    elif k=='clipboard':
        c.rect(22,20,53,65,8,t);c.rect(35,11,27,16,6,'o');c.line('M34 42H63M34 55H63M34 68H55')
    elif k=='receipt':
        c.path('M23 12H75V85L67 79L59 85L51 79L43 85L35 79L23 85Z',t);c.line('M35 29H63M35 42H63M35 56H52M35 69H61')
    elif k=='bell':
        c.path('M19 69L25 60V40C25 10 71 10 71 40V60L77 69Z',t);c.path('M38 75C38 88 58 88 58 75','o');c.glow('M32 48V39Q32 26 42 24')
    elif k=='shop':
        c.rect(18,40,60,43,5,t);c.rect(40,58,19,25,3,'o');c.path('M16 21H80L87 44C80 55 69 48 67 44C60 54 51 50 48 44C42 54 31 49 29 44C22 53 13 49 9 44Z','m');c.glow('M21 26H72')
    elif k=='fork':
        c.path('M20 14V35Q20 43 32 43V82H40V43Q51 43 51 35V14H45V31H38V14H31V31H26V14Z',t);c.path('M68 14Q81 14 81 31V82H70V52H62V30Q62 18 68 14Z','o')
    elif k=='scissors':
        c.circle(25,70,13,'m');c.circle(69,70,13,'m');c.path('M32 60L69 15Q76 9 78 17Q79 29 66 42L44 64Z',t);c.path('M62 60L25 15Q18 9 16 17Q15 29 28 42L50 64Z','o');c.dot(47,48,3)
    elif k=='wrench':c.path('M58 16C79 4 88 29 75 42C68 49 59 48 53 45L27 80Q17 90 10 80Q5 73 14 64L45 36C40 24 45 13 56 10L60 12L52 26L60 34L74 25L79 26Z',t);c.dot(21,74,3,'p')
    elif k=='sofa':
        c.rect(24,18,49,45,13,t);c.rect(12,43,17,32,7,'o');c.rect(69,43,17,32,7,'o');c.rect(24,57,49,21,7,'o');c.line('M23 79V85M74 79V85','g',6);c.glow('M33 25H62')
    elif k=='pill':
        c.path('M20 62L57 18C76-1 98 21 81 40L44 82C25 100 4 78 20 62Z','m');c.path('M20 62L39 40L63 60L44 82C25 100 4 78 20 62Z','p');c.line('M41 40L62 59','g',2.5)
    elif k=='basket':
        c.path('M13 38H83L74 82H23Z',t);c.line('M25 38L40 15M71 38L56 15','o',6);c.rect(9,32,78,12,6,'m');c.line('M31 52L34 70M48 52V70M65 52L62 70')
    elif k=='scale':
        c.rect(23,12,50,12,6,t);c.path('M31 30H65L80 82H16Z','o');c.circle(48,56,13,'p');c.line('M48 56L55 47','g',3);c.dot(48,56,2,'g')
    elif k=='building':
        c.rect(20,21,56,64,8,t);c.rect(34,9,28,16,4,'o');c.rect(41,65,14,20,2,'p')
        for x in [32,49,65]:
            for y in [37,52]:c.dot(x,y,3,'p')
    elif k=='truck':
        c.rect(10,25,47,47,7,t);c.path('M57 40H73L87 56V72H57Z','o');c.path('M65 46H72L80 56H65Z','p');c.circle(27,77,9,'m');c.circle(73,77,9,'g');c.glow('M17 33V59')
    elif k=='calendar':
        c.rect(15,22,66,62,10,t);c.rect(15,22,66,17,8,'m');c.line('M30 12V28M66 12V28','p',6)
        for x,y in [(30,51),(48,51),(66,51),(30,68),(48,68)]:c.rect(x-4,y-4,8,8,2,'p')
    elif k=='scan':
        c.line('M15 33V19Q15 14 21 14H34M62 14H76Q82 14 82 20V33M82 63V77Q82 82 76 82H63M34 82H20Q15 82 15 76V63',t,7)
        for x in [28,37,46,57,67]:c.line(f'M{x} 32V64','m',4 if x%2 else 3)
    elif k=='qr':
        for x,y in [(15,15),(57,15),(15,57)]:c.rect(x,y,24,24,3,t);c.rect(x+7,y+7,10,10,1,'p')
        c.rect(57,57,10,10,1,'m');c.rect(72,72,10,10,1,'o');c.line('M76 57V64H68V79H57','g',5)
    elif k=='wallet':
        c.path('M17 31L65 13L76 37Z','o');c.rect(13,29,70,51,10,t);c.rect(60,47,25,21,7,'m');c.dot(71,57,3)
    elif k in ['ticket','percent']:
        c.path('M19 22H77V36C62 36 62 60 77 60V76H19V60C34 60 34 36 19 36Z',t);c.line('M37 64L59 34');c.circle(38,36,5,'p');c.circle(58,62,5,'p')
    elif k=='chat':
        c.path('M14 28Q14 15 29 15H68Q83 15 83 31V57Q83 71 67 71H39L20 84V70Q14 67 14 57Z',t)
        for x in [33,49,65]:c.dot(x,44,3.5)
    elif k=='spark':
        c.path('M48 13Q53 40 79 47Q54 52 48 80Q42 53 16 47Q42 40 48 13Z',t);c.glow('M48 27L42 40')
    elif k=='pin':c.path('M48 86C40 75 20 54 20 36C20 1 76 1 76 36C76 54 56 75 48 86Z',t);c.circle(48,35,10,'p')
    elif k=='camera':
        c.path('M17 30H30L37 19H59L66 30H79Q85 30 85 38V76Q85 83 77 83H19Q11 83 11 75V38Q11 30 17 30Z',t);c.circle(48,55,18,'p');c.circle(48,55,11,'o');c.dot(73,39,3)
    elif k=='sliders':
        c.line('M16 26H80M16 49H80M16 72H80',t,6)
        for x,y,tt in [(35,26,'g'),(64,49,'o'),(41,72,'m')]:c.circle(x,y,8,tt)
    elif k=='sort':c.line('M28 81V16L15 30M28 16L41 30M68 15V80L55 66M68 80L81 66',t,7)
    elif k=='pencil':c.path('M17 62L64 15Q69 10 75 16L82 23Q87 29 82 34L35 81L13 86Z',t);c.line('M58 23L75 40M17 62L35 81','o',4)
    elif k=='trash':
        c.path('M23 31H73L68 83H28Z',t);c.rect(15,20,66,11,5,'o');c.line('M36 20V13H60V20M39 43V69M57 43V69','p',4)
    elif k=='share':
        c.line('M27 48L68 25M27 48L68 73',t,7);c.circle(23,48,11,t);c.circle(73,23,11,t);c.circle(73,76,11,'o')
    elif k=='bookmark':c.path('M25 13H71V85L48 68L25 85Z',t);c.glow('M32 21H62')
    elif k=='circle':c.circle(48,48,33,t)
    elif k in ['check','cross','info','warning','clock','help','minus','plus']:
        if k=='warning':c.path('M42 16Q48 6 54 16L86 74Q91 84 79 84H17Q5 84 11 74Z','o');c.line('M48 33V54',w=6);c.dot(48,68,3)
        else:
            c.circle(48,48,33,t)
            if k=='check':c.line('M29 49L42 62L68 34',w=6)
            if k=='cross':c.line('M35 35L61 61M61 35L35 61',w=6)
            if k=='info':c.dot(48,29,3);c.line('M48 43V65',w=6)
            if k=='help':c.line('M37 34C37 20 63 20 62 37C62 46 48 45 48 55',w=5);c.dot(48,68,3)
            if k=='clock':c.line('M48 27V49L63 59',w=5)
            if k in ['plus','minus']:c.line('M31 48H65'+('M48 31V65' if k=='plus' else ''),w=6)
    elif k=='loader':c.line('M48 15A33 33 0 1130 20',t,8);c.dot(31,20,4,'o')
    elif k=='wifi':c.line('M13 34Q48 3 83 34M25 49Q48 28 71 49M37 64Q48 54 59 64',t,7);c.dot(48,78,5,'g')
    elif k=='box':
        c.path('M13 29L48 11L83 29V68L48 87L13 68Z','o');c.path('M13 29L48 48L83 29M48 48V87',t);c.path('M36 17L69 35V49L59 55V40L25 23Z','p')
    elif k=='layers':
        for y,tt in [(57,'g'),(40,'m'),(22,t)]:c.path(f'M13 {y+8}L48 {y-8}L83 {y+8}L48 {y+25}Z',tt)
    elif k=='image':
        c.rect(14,18,68,62,9,t);c.circle(63,35,7,'o');c.path('M20 68L38 43L54 60L63 50L76 68Z','p')
    elif k=='tag':c.path('M14 51L51 14H78Q85 14 85 21V48L48 85Z',t);c.circle(69,29,6,'p')
    elif k=='flame':c.path('M48 10C64 31 72 30 67 44L77 35C97 76 65 94 44 85C9 76 20 42 30 30L32 48C44 42 48 30 48 10Z','o');c.path('M48 53C63 70 63 82 48 84C34 81 35 68 48 53Z','p')
    elif k=='diamond':c.path('M24 20H72L87 42L48 85L9 42Z',t);c.line('M9 42H87M34 20L27 42L48 85L68 42L62 20','p',2.5)
    elif k=='leaf':c.path('M45 67C10 70 9 37 15 24C40 24 54 39 45 67Z',t);c.path('M45 67C43 30 68 14 84 13C89 47 75 70 45 67Z','g');c.line('M45 84V61L66 37','p',4)
    elif k=='crown':c.path('M17 30L34 48L48 17L63 48L81 30L74 79H24Z','o');c.line('M28 69H70');c.circle(15,27,5,'o');c.circle(48,15,5,'o');c.circle(83,27,5,'o')
    elif k=='gift':
        c.rect(20,38,56,47,6,t);c.rect(13,28,70,17,5,'o');c.path('M43 29C15 23 28 3 42 16L48 28C53 6 75 9 64 23L52 29Z','m');c.rect(43,29,11,56,2,'p')
    elif k=='card':
        c.rect(13,22,70,53,9,t);c.rect(14,33,68,9,1,'p');c.line('M25 60H42','o',5);c.dot(66,60,3,'o')
    elif k=='return':c.line('M19 36C37 5 83 16 82 49C82 82 36 90 20 65',t,12);c.path('M11 17L12 44L38 41Z','o')
    elif k=='headset':
        c.line('M21 55V40C21 5 75 5 75 40V65Q75 81 57 81',t,7);c.rect(12,44,20,30,9,'m');c.rect(65,44,20,30,9,'m');c.rect(44,76,17,10,5,'o')
    elif k=='shield':c.path('M48 11L80 24V49Q79 71 48 87Q17 71 16 49V24Z',t);c.line('M35 35L61 61M61 35L35 61' if arg=='deny' else 'M32 47L43 59L65 34',w=5)
    elif k=='gear':
        ps=[]
        for i in range(32):
            a=i*math.pi/16;r=36 if i%4 in [0,1] else 29;ps.append(f'{48+math.cos(a)*r:.2f} {48+math.sin(a)*r:.2f}')
        c.path('M'+'L'.join(ps)+'Z',t);c.circle(48,48,13,'p');c.circle(48,48,6,'g')
    elif k=='chart':
        for x,y,h,tt in [(16,52,30,'m'),(39,35,47,'o'),(62,14,68,'g')]:c.rect(x,y,16,h,5,tt)
    elif k=='logout':
        c.rect(19,14,43,70,7,t);c.path('M19 14L48 22V84L19 76Z','o');c.line('M57 48H85M74 37L85 48L74 59','p',5);c.dot(39,50,3)
    elif k=='lock':c.rect(21,39,54,46,10,t);c.line('M32 40V28C32 6 64 6 64 28V40','o',7);c.dot(48,58,5);c.line('M48 61V71','p',4)
    elif k=='key':c.circle(31,32,19,t);c.circle(31,32,7,'p');c.path('M43 44L79 80L87 72L79 64L73 70L65 62L71 56L55 40Z','o')
    elif k=='mail':c.rect(12,22,72,55,9,t);c.path('M13 25L48 53L83 25','p');c.line('M16 72L36 52M80 72L60 52','g',3)
    elif k=='phone':c.rect(28,11,40,75,9,t);c.rect(33,20,30,50,3,'p');c.dot(48,78,3,'o')
    elif k=='desktop':c.rect(11,17,74,50,7,t);c.rect(18,24,60,35,3,'p');c.path('M43 68H54L57 81H39Z','o');c.line('M30 84H67','g',5)
    elif k=='printer':c.rect(14,33,68,39,9,t);c.rect(28,12,40,30,3,'p');c.path('M27 56H69V85H27Z','p');c.line('M35 65H60M35 74H57','g',3);c.dot(71,45,3,'o')
    elif k=='cash':c.rect(11,26,74,47,7,t);c.circle(48,49,13,'o');c.line('M48 38V60M55 42C44 34 36 48 49 49C62 50 55 64 41 56','p',3);c.dot(23,49,3);c.dot(73,49,3)
    elif k=='coins':
        for y in [67,56,45]:c.ellipse(36,y,23,10,'o')
        c.circle(64,40,22,t);c.line('M64 26V54M71 30C54 22 52 40 65 40C79 40 73 57 57 48','p',3)
    elif k=='register':c.rect(23,12,50,32,6,t);c.rect(29,18,38,17,3,'p');c.path('M23 47H73L85 78H11Z','o');c.rect(13,75,70,12,4,t);c.line('M35 55H61M39 64H66','p',4)
    elif k=='bank':c.path('M11 31L48 10L85 31Z','o');c.rect(15,76,66,10,3,t);c.line('M25 37V69M48 37V69M71 37V69','g',10)
    elif k=='arrows':c.line('M13 31H79M66 18L79 31L66 44','o',7);c.line('M83 65H17M30 52L17 65L30 78',t,7)
    elif k=='ruler':c.path('M12 65L65 12L84 31L31 84Z','o');c.line('M28 52L35 59M39 41L46 48M50 30L57 37M61 19L68 26','p',3)
    elif k=='table':c.ellipse(48,32,34,17,'o');c.line('M20 38V79M76 38V79M47 49V81','g',7)
    elif k=='pizza':c.path('M48 12L84 79Q49 93 13 79Z','o');c.path('M14 72Q48 84 81 72L84 80Q48 95 11 80Z','m');c.circle(43,49,6,'m');c.circle(57,67,5,'m');c.circle(33,67,4,'g')
    elif k=='cup':c.path('M21 29H69V65Q69 82 45 82Q21 82 21 65Z',t);c.line('M69 37C96 35 91 65 69 64','o',7);c.line('M34 12V19M48 8V19M61 12V19','m',3)
    elif k=='plate':c.circle(48,49,34,'p');c.circle(48,49,24,t);c.line('M34 35Q48 24 63 37','p',3)
    elif k=='chef':c.path('M24 49C4 42 16 13 36 23C39 4 66 6 66 24C86 13 96 44 73 50L69 80H27Z','p');c.line('M29 64H68','g',4)
    elif k=='pot':c.rect(17,35,62,43,12,t);c.path('M13 31Q48 8 83 31Z','o');c.line('M39 17H57M9 47H17M79 47H87','g',6);c.glow('M25 43V63')
    elif k=='cake':c.path('M17 42H79V80H17Z','o');c.path('M17 42Q25 24 34 40Q44 25 54 41Q67 25 79 42V54Q68 66 61 51Q48 64 40 51Q26 65 17 52Z','m');c.line('M34 18V33M61 18V33','g',5);c.dot(34,13,3,'o');c.dot(61,13,3,'o')
    elif k=='bottle':c.rect(35,9,26,12,4,t);c.path('M35 22H61V32L72 46V80Q72 86 65 86H31Q24 86 24 80V46L35 32Z',t);c.rect(27,50,42,23,4,'p');c.line('M42 61H54M48 55V67','o',4)
    elif k=='chocolate':c.path('M21 12H75V81H21Z','m');c.path('M21 12H75V51H21Z','o');c.line('M39 14V49M57 14V49M23 32H73','p',3);c.path('M21 52L48 65L75 52V84H21Z',t)
    elif k=='bread':c.path('M21 77V43C-1 25 30 3 48 20C68 3 99 25 77 43V77Z','o');c.line('M34 35V52M48 31V52M62 35V52','p',3)
    elif k=='fruit':c.path('M48 34C20 12 6 43 21 69C33 91 43 80 48 80C61 89 76 79 81 59C90 27 63 19 48 34Z','o');c.path('M48 29C49 13 64 10 74 12C70 26 61 30 48 29Z',t);c.line('M48 33V19','g',4)
    elif k=='chair':c.rect(29,12,38,40,8,t);c.rect(22,53,53,17,6,'o');c.line('M29 70V85M68 70V85','g',6)
    elif k=='bed':c.rect(12,44,72,29,6,t);c.rect(18,30,25,21,6,'p');c.rect(48,30,29,21,6,'o');c.line('M13 24V84M83 24V84','g',6)
    elif k=='lamp':c.path('M31 13H65L79 53H17Z','o');c.line('M48 54V79M29 83H67','g',6)
    elif k=='brush':c.path('M60 15Q72 10 79 20L55 56L42 46Z','o');c.path('M42 44Q23 43 22 61Q23 76 12 81C37 92 58 73 55 57Z',t)
    elif k=='comb':c.rect(13,27,72,13,6,t);c.line('M19 40V70M29 40V65M39 40V70M49 40V65M59 40V70M69 40V65M79 40V70','m',4)
    elif k=='dryer':c.path('M20 24H63Q83 24 83 43Q83 61 63 61H20Z','o');c.rect(11,30,13,25,4,t);c.path('M48 61H65L58 85H45Z',t);c.line('M71 34V50','p',3)
    elif k=='device':c.rect(25,9,46,78,9,t);c.rect(31,19,34,51,4,'p');c.path('M47 30L40 47L52 49L46 62','m');c.dot(48,79,3)
    elif k=='tools':draw(c,'gear',t);c.line('M48 45L78 78','m',12);c.circle(48,44,9,'o')
    elif k=='test':c.rect(16,16,49,67,7,t);c.line('M28 33H49M28 46H49');c.line('M40 66L49 76L77 45','o',7)
    elif k=='barcode':
        for i,x in enumerate([16,25,33,46,55,63,75,82]):c.line(f'M{x} 20V76',t,3+(i%3))
    elif k=='fingerprint':c.line('M22 62V42C22 5 76 5 76 42V64M32 72V41C32 18 65 18 65 41V73M43 81V42C43 34 54 34 54 42V81',t,4)
    elif k=='eye':c.path('M10 48Q48 3 86 48Q48 93 10 48Z',t);c.circle(48,48,14,'p');c.circle(48,48,6,'g')
    elif k=='globe':c.circle(48,48,35,t);c.ellipse(48,48,15,35,'g');c.line('M16 35H80M16 61H80','p',3)
    elif k=='map':c.path('M11 23L34 13L61 25L85 14V74L62 85L35 73L11 84Z',t);c.line('M35 14V73M61 25V83','p',3);c.circle(61,48,10,'m')
    elif k=='route':c.line('M22 22C83 13 11 68 64 71','g',6);c.circle(22,22,9,'o');c.path('M65 89C36 61 66 43 80 60C90 73 65 89 65 89Z','m');c.dot(66,69,3)
    elif k=='stairs':c.path('M13 80V61H33V43H53V25H74V13H85V84H13Z',t);c.glow('M20 68H40V51H60V33H78')
    elif k=='floor':c.path('M12 31L48 12L84 31L48 52Z',t);c.path('M12 51L48 72L84 51M12 69L48 89L84 69','o')
    elif k=='door':c.rect(21,12,54,73,6,t);c.path('M29 19L64 26V77L29 85Z','o');c.dot(56,51,3)
    elif k=='parking':c.rect(17,12,62,74,12,t);c.line('M36 71V28H53C73 28 73 52 53 52H36','p',7)
    elif k=='accessibility':c.circle(48,18,8,'o');c.line('M20 35H76M48 35V58M48 58L29 81M48 58L68 81','g',8)
    elif k=='network':c.line('M48 18V44M22 75L48 44L76 74',t,5);c.circle(48,18,10,'o');c.circle(48,46,13,t);c.circle(20,77,10,t);c.circle(78,77,10,'m')
    elif k=='database':
        c.path('M18 27V73C18 92 78 92 78 73V27Z',t);c.ellipse(48,26,30,13,'o');c.line('M19 49C25 65 72 65 77 49','p',3)
    elif k=='cloud':c.path('M26 74C-3 72 8 37 29 39C30 8 73 9 72 39C94 37 99 74 73 74Z',t);c.glow('M31 37Q34 22 47 23')
    elif k=='link':c.line('M42 27L49 20C76-1 100 30 76 50L66 59M54 69L47 77C22 96-2 66 20 46L30 36M34 61L63 34',t,10)
    elif k=='branch':c.line('M27 18V78M27 59C68 59 71 42 71 22',t,7);c.circle(27,18,9,'o');c.circle(71,20,9,'m');c.circle(27,79,9,'g')
    elif k=='toggle':c.rect(10,28,76,40,20,t);c.circle(31 if arg=='off' else 65,48,15,'p')
    elif k=='upload':c.path('M15 59V82H81V59',t);c.line('M48 66V15L31 32M48 15L65 32','o',6)
    elif k=='download':c.path('M15 59V82H81V59',t);c.line('M48 15V66L31 49M48 66L65 49','o',6)
    elif k=='arrow':
        d={'right':'M15 48H80M62 28L82 48L62 68','left':'M81 48H16M34 28L14 48L34 68','up':'M48 81V16M28 34L48 14L68 34','down':'M48 15V80M28 62L48 82L68 62'}[arg or 'right'];c.line(d,t,8)
    elif k=='chevron':
        d={'right':'M35 20L65 48L35 76','left':'M61 20L31 48L61 76','up':'M20 61L48 31L76 61','down':'M20 35L48 65L76 35'}[arg or 'right'];c.line(d,t,8)
    elif k=='dots':
        for x,y in ([(25,48),(48,48),(71,48)] if arg!='vertical' else [(48,25),(48,48),(48,71)]):c.circle(x,y,6,t)
    elif k=='play':c.path('M29 14L83 48L29 82Z',t)
    elif k=='pause':c.rect(22,15,18,68,5,t);c.rect(57,15,18,68,5,t)
    elif k=='stop':c.rect(20,20,56,56,10,t)
    elif k=='microphone':c.rect(34,11,28,48,14,t);c.line('M23 44C23 80 73 80 73 44M48 72V85M34 85H62','o',5)
    elif k=='sound':c.path('M13 36H31L52 17V79L31 60H13Z',t);c.line('M64 32Q80 48 64 64M75 20Q101 48 75 76','o',4)
    elif k=='flag':c.line('M24 11V85',t,6);c.path('M26 14H76L64 35L76 55H26Z','m')
    elif k=='crop':c.line('M27 12V69H84M12 27H69V84',t,8)
    elif k=='copy':c.rect(15,12,52,61,8,'o');c.rect(30,27,52,61,8,t);c.line('M42 45H69M42 58H69M42 71H61','p',3)
    elif k=='paperclip':c.line('M32 57L61 27C78 10 95 30 79 46L46 80C25 101-3 74 18 52L53 17',t,6)
    elif k=='spark-document':draw(c,'document',t);star(c,75,74,14,'o')
    elif k=='ai':
        c.path('M48 10Q53 37 80 45Q53 51 48 82Q42 53 13 45Q41 38 48 10Z',t);c.path('M77 15L87 25L77 35L67 25Z','m');c.glow('M48 23L42 38')
    elif k=='lightning':c.path('M52 8L17 54H42L36 88L81 35H54Z','o')
    elif k=='timer':c.circle(48,53,30,t);c.rect(36,9,24,10,4,'o');c.line('M48 23V18M48 53L61 40','p',4)
    elif k=='percent-bars':draw(c,'chart',t);c.line('M20 28L35 13','o',4);c.dot(20,15,3,'o');c.dot(36,28,3,'o')
    elif k=='package-open':c.path('M25 35L48 45L72 35L82 65L49 83L15 66Z',t);c.path('M25 35L10 20L35 11L48 27L61 11L86 20L72 35L48 45Z','o');c.line('M48 45V81','p',3)
    elif k=='empty':c.path('M17 39L31 19H66L80 39V79H17Z',t);c.path('M17 39H36L41 51H57L63 39H80','p');c.line('M39 67H58','g',4)
    elif k=='balance':c.line('M48 15V81M25 84H71M17 31H79','g',6);c.path('M25 31L11 59H39Z','o');c.path('M71 31L57 59H85Z','m')
    else:raise KeyError('No drawing for '+k)

def render(entry,mode):
    slug='zi-'+entry['id']+'-'+('c' if mode=='couleur' else 'i');c=Canvas(slug,mode)
    draw(c,entry['recipe'],entry.get('tone','g'),entry.get('arg'))
    knockout=''
    if mode=='interface' and entry.get('badge'):
        knockout=f'<mask id="{slug}-clear" maskUnits="userSpaceOnUse" x="0" y="0" width="96" height="96"><rect width="96" height="96" fill="#FFFFFF"/><circle cx="76" cy="76" r="16" fill="#000000"/></mask>'
        c.items=[f'<g mask="url(#{slug}-clear)">'+''.join(c.items)+'</g>']
    badge(c,entry.get('badge'))
    if entry.get('slash'):c.line('M18 16L80 80','m',6)
    defs=knockout
    if mode=='couleur':
        for tone,colors in {'g':['#259F7C','#005C45','#003B2D'],'o':['#FFBE67','#FF8A1E','#DA580C'],'m':['#F4599C','#D21868','#940B47']}.items():
            defs+=f'<linearGradient id="{slug}-{tone}" x1=".1" y1="0" x2=".85" y2="1"><stop offset="0" stop-color="{colors[0]}" data-tone="{tone}"/><stop offset=".48" stop-color="{colors[1]}" data-tone="{tone}"/><stop offset="1" stop-color="{colors[2]}" data-tone="{tone}"/></linearGradient>'
        defs+=f'<filter id="{slug}-shadow" x="-15%" y="-15%" width="130%" height="140%" color-interpolation-filters="sRGB"><feDropShadow dx="0" dy="1.4" stdDeviation=".9" flood-color="#003B2D" flood-opacity=".2"/></filter>'
    title=esc(entry['label']);desc=esc(entry['purpose'])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96" fill="none" role="img" aria-labelledby="{slug}-title {slug}-desc">
  <title id="{slug}-title">{title}</title><desc id="{slug}-desc">{desc}</desc>
  {('<defs>'+defs+'</defs>') if defs else ''}
  <g id="{slug}-drawing" data-icon="{entry['id']}" data-layer="drawing" {('filter="url(#'+slug+'-shadow)"') if mode=='couleur' else ''}>
    {''.join(c.items)}
  </g>
</svg>'''
