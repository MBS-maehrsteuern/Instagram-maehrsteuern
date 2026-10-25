import json, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
SRC='/root/.claude/uploads/7936d62e-f7e9-52a2-a372-a7a75a768708/1ccda3e8-18.10.2026_20.05.mp3'
tr=json.load(open('/tmp/claude-0/-home-claude/7936d62e-f7e9-52a2-a372-a7a75a768708/scratchpad/tr.json'))
W=[w for s in tr for w in s['words']]
SEG=[(141.10,143.95,"Deine Steuererklärung liest zuerst kein Mensch, sondern ein Code."),
(257.80,261.97,"Ich wurde auf der anderen Seite der Macht ausgebildet. In der Thüringer Steuerverwaltung."),
(262.75,267.12,"Mein Bild vorher: ein Sachbearbeiter liest jede Erklärung Zeile für Zeile."),
(176.60,180.92,"Die Realität ist aber: zuerst entscheidet ein System aus Code."),
(199.45,204.20,"Unauffällig heißt nicht ungeprüft. Das Gesetz verlangt zusätzlich eine Zufallsauswahl."),
(204.78,207.10,"Und alles im qualifizierten Freitextfeld"),
(212.10,213.68,"stoppt die Automatik und ihr landet"),
(215.85,217.98,"auf dem Tisch des Sachbearbeiters."),
(218.45,219.98,"Welcher Punkt war neu für dich?")]
GRUEN={"Code.","Mensch,","Macht","Thüringer","System","ungeprüft.","Zufallsauswahl.","Freitextfeld","Automatik","Sachbearbeiters.","neu"}
GAP=0.16; words=[]; t=0.15; parts=[]
for a,b,txt in SEG:
    ws=[w for w in W if a<= (w[1]+w[2])/2 < b]; tx=txt.split()
    assert len(ws)==len(tx),(txt,[w[0] for w in ws])
    for w,x in zip(ws,tx): words.append((x,t+w[1]-a,t+w[2]-a))
    parts.append((a,b)); t+=b-a+GAP
DUR=round(t+0.5,2)
# audio
fc=''.join(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={b-a-0.03}:d=0.03,apad=pad_dur={GAP}[s{i}];" for i,(a,b) in enumerate(parts))
fc+=''.join(f"[s{i}]" for i in range(len(parts)))+f"concat=n={len(parts)}:v=0:a=1,adelay=150|150,loudnorm=I=-16:TP=-1.5[v];[1:a]atrim=0:{DUR},volume=0.11,afade=t=out:st={DUR-1}:d=1[m];[v][m]amix=inputs=2:normalize=0,atrim=0:{DUR}[a]"
if 0: subprocess.run(['ffmpeg','-y','-loglevel','error','-i',SRC,'-i','/home/claude/instagram-maehrsteuern/musik/06_runway_lofi_ruhig.mp3','-filter_complex',fc,'-map','[a]','-ac','2','-ar','44100','ton.wav'],check=True)
# chunks of 2-3 words, break at punctuation
chunks=[];cur=[]
for w in words:
    cur.append(w)
    if len(cur)==3 or w[0][-1] in '.,:?' or (len(cur)>=2 and len(' '.join(z[0] for z in cur))>18): chunks.append(cur);cur=[]
if cur: chunks.append(cur)
base=Image.open('/home/claude/post/reel_frame.png').convert('RGB')
F=ImageFont.truetype('/home/claude/instagram-maehrsteuern/vorlagen/system/schriften/Outfit-Bold.ttf',80)
fps=30; N=int(DUR*fps)
p=subprocess.Popen(['ffmpeg','-y','-loglevel','warning','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r',str(fps),'-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','video.mp4'],stdin=subprocess.PIPE)
for f in range(N):
    tt=f/fps; z=1+0.06*tt/DUR
    cw,ch=2160/z,3840/z; x0=(2160-cw)/2; y0=(3840-ch)/2
    fr=base.resize((1080,1920),Image.BILINEAR,box=(x0,y0,x0+cw,y0+ch))
    d=ImageDraw.Draw(fr)
    for c in chunks:
        if c[0][1]-0.05<=tt< (c[-1][2]+0.25):
            # draw words with colour
            g=80; Fg=F
            tot0=sum(d.textlength(w[0]+' ',font=F) for w in c)-d.textlength(' ',font=F)
            if tot0>800: g=int(80*800/tot0); Fg=ImageFont.truetype('/home/claude/instagram-maehrsteuern/vorlagen/system/schriften/Outfit-Bold.ttf',g)
            sizes=[d.textlength(w[0]+' ',font=Fg) for w in c]; tot=sum(sizes)-d.textlength(' ',font=Fg)
            x=470-tot/2
            for w,s in zip(c,sizes):
                col=(83,195,162) if w[0] in GRUEN else (255,255,255)
                d.text((x,1440+(80-g)//2),w[0],font=Fg,fill=col,stroke_width=7,stroke_fill=(0,0,0))
                x+=s
            break
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait(); print('dauer',DUR)
