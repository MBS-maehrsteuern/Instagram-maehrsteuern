import numpy as np, json, subprocess
C=json.load(open('chunks.json'))
SRC='/home/claude/instagram-maehrsteuern/aufnahmen/2026-10-21/sprechtexte_fach.mp3'
SR=48000
r=subprocess.run(['ffmpeg','-v','error','-i',SRC,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True)
X=np.frombuffer(r.stdout,np.float32).copy()
rg=lambda a,b:list(range(a,b+1))
R={'30':rg(8,23),'32':rg(63,66)+rg(53,59),'33':rg(76,84)+rg(96,102),'34':rg(105,113),
'36':rg(116,124)+rg(133,136),'38':rg(141,150),'39':rg(153,161),'40':rg(163,171)+rg(203,204),
'42':rg(210,218),'43':rg(223,230),'45':rg(232,241)+rg(244,245),'48':rg(284,292),'49':rg(294,305),
'50':rg(308,313)+rg(316,319),'52':rg(322,331)+rg(336,337),'53':rg(339,341)+rg(347,355),'54':rg(362,373),
'55':rg(380,390),'57':rg(392,400),'58':rg(402,414)}
PRE,POST,MAXGAP,XF=0.09,0.22,0.42,0.025
def seg(a,b): return X[int(a*SR):int(b*SR)]
def xcat(parts):
    out=parts[0]; n=int(XF*SR); w=np.sin(np.linspace(0,np.pi/2,n))**2
    for p in parts[1:]:
        out=np.concatenate([out[:-n], out[-n:]*(1-w)+p[:n]*w, p[n:]])
    return out
info={}
for nr,sel in R.items():
    parts=[]
    for k,i in enumerate(sel):
        a,b=C[i][0],C[i][1]
        prv=C[i-1][1] if i>0 else 0; nxt=C[i+1][0] if i+1<len(C) else b+1
        nxt_sel = k+1<len(sel) and sel[k+1]==i+1
        prv_sel = k>0 and sel[k-1]==i-1
        s=a-min(PRE,(a-prv)/2) if not prv_sel else a
        if nxt_sel:
            gap=nxt-b
            if gap<=MAXGAP: e=nxt   # keep whole natural gap
            else: e=b+min(POST,gap/2); # shorten: tail here, head of next added via its own pre
        else: e=b+min(POST,(nxt-b)/2)
        if prv_sel:
            gap=a-prv
            s = a if gap<=MAXGAP else a-min(PRE+0.1,gap/2)
        parts.append(seg(s,e))
    y=xcat(parts)
    y=y/np.max(np.abs(y))*0.5
    raw=f'bau/r_{nr}.f32'; y.astype(np.float32).tofile(raw)
    out=f'bau/stimme_{nr}.wav'
    subprocess.run(['ffmpeg','-y','-v','error','-f','f32le','-ar',str(SR),'-ac','1','-i',raw,'-af','highpass=f=70,loudnorm=I=-18:TP=-1.5:LRA=9',out,'-ar','48000'],check=True)
    info[nr]=round(len(y)/SR,1)
print(info)
json.dump(info,open('bau/dauer.json','w'))
