import json,subprocess,os
w=json.load(open('woerter.json'))['sprechtexte_fach.mp3']
S=[];cur=[]
for x in w:
    cur.append(x)
    if x[0].endswith(('.','?','!')) or len(cur)>25: S.append(cur);cur=[]
if cur:S.append(cur)
# (satz, ab_wort_index)
R={
'30':[3,4,5,6,7,8,9,10],
'32':[38,39,40,41,31,32,33,34,35,36],
'33':[49,50,51,52,59,60,61,62],
'34':list(range(63,79)),
'36':[79,80,81,82,83,84,85,86,92,93,94],
'38':list(range(98,108)),
'39':list(range(109,121)),
'40':[122,123,124,125,126,127,(139,'und'),140,141,142],
'42':list(range(146,155)),
'43':list(range(159,166)),
'45':list(range(166,174)),
'47':list(range(192,206)),
'48':list(range(207,215)),
'49':list(range(216,225)),
'50':list(range(226,234))+[235,236,237,238],
'52':list(range(240,246)),
'53':[246,247,250,251,252,253],
'54':list(range(260,270)),
'55':list(range(273,282)),
'57':[(282,1)]+list(range(283,290)),
'58':list(range(290,299)),
}
SRC='/home/claude/instagram-maehrsteuern/aufnahmen/2026-10-21/sprechtexte_fach.mp3'
info={}
for nr,sel in R.items():
    spans=[];text=[];minp=[]
    for s in sel:
        if isinstance(s,tuple):
            i,k=s; ws=S[i]
            if isinstance(k,str): k=[j for j,t in enumerate(ws) if t[0].lower().startswith(k)][0]
            ws=ws[k:]
        else: ws=S[s]
        # split sentence on internal pauses > 0.6s to drop long gaps
        seg=[ws[0]]
        for a,b in zip(ws,ws[1:]):
            if b[1]-a[2]>0.6: spans.append((seg[0][1],seg[-1][2])); seg=[]
            seg.append(b)
        spans.append((seg[0][1],seg[-1][2]))
        text+= [t[0] for t in ws]; minp+=[t for t in ws if t[3]<0.5]
    f=[];parts=[]
    for j,(a,b) in enumerate(spans):
        a=max(0,a-0.06); b=b+0.14
        parts.append(f"[0:a]atrim={a:.2f}:{b:.2f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={b-a-0.03:.2f}:d=0.03,apad=pad_dur=0.16[p{j}]")
    fc=";".join(parts)+";"+"".join(f"[p{j}]" for j in range(len(spans)))+f"concat=n={len(spans)}:v=0:a=1,highpass=f=80,afftdn=nf=-30,loudnorm=I=-18:TP=-1.5:LRA=7[o]"
    out=f'cut/stimme_{nr}.wav'
    subprocess.run(['ffmpeg','-y','-v','error','-i',SRC,'-filter_complex',fc,'-map','[o]','-ar','48000','-ac','1',out],check=True)
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',out],capture_output=True,text=True).stdout)
    info[nr]={'dauer':round(d,1),'woerter':len(text),'text':" ".join(text),'unsicher':[t[0] for t in minp]}
    print(nr,round(d,1),len(text),"unsicher:",", ".join(t[0] for t in minp)[:120])
json.dump(info,open('cut/info.json','w'),ensure_ascii=False,indent=1)
