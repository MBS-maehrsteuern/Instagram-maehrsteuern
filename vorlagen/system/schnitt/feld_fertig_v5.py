# Feld-Reel v5: KI-Hook + Premium-Stimme + KI-Schluss + Büro-Blur-Hintergrund
import json,subprocess,sys
from pathlib import Path
R=Path('/home/user/roh'); O=R/'out'; P='/home/user/Instagram-maehrsteuern/vorlagen/system/premium'
run=lambda *a: subprocess.run(list(a),check=True)
dur=lambda f: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(f)]))
run('python3',str(R/'schnitt5.py'))
for n,ziel in [('weihnachtsfeier','weihnachtsfeier_110'),('kundengeschenk','kundengeschenk_50')]:
    L=(O/f'{n}_v3.txt').read_text().splitlines(); L[-1]=f"file '{O}/cta_buero_teil.mov'"; (O/f'{n}_v5.txt').write_text('\n'.join(L))
    run('ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',str(O/f'{n}_v5.txt'),'-c','copy',str(O/f'{n}_schnitt.mov'))
    m=json.load(open(O/f'{n}_mapping.json')); d=dur(O/f'{n}_schnitt.mov'); c=int(round(m['cta']*30))
    z=m['zeiten'][:c]; a0=m['zeiten'][c]; z+=[round(min(a0+i/30,m['zeiten'][-1]),4) for i in range(int(d*30)-len(z))]
    m['zeiten']=z; m['dauer']=d; json.dump(m,open(O/f'{n}_mapping.json','w'))
    # Hintergrund für den Blur: Hook-Teile (KI) + Büro-Schleife (KI-Hook vor/zurück) + Schluss
    hook=[x for x in L if f'{n}_v3_0_' in x]; hd=sum(dur(x.split("'")[1]) for x in hook); mitte=m['cta']-hd
    # Loris 31.10.: echter Gang aus dem KI-Hook, nur vorwärts; weder Vor-/Zurück-Schleife noch Standbild noch KI-Sprechclip – KI-Bewegung (Runway Gen-4 Turbo aus dem letzten Hook-Bild, 10 s),
    # nur vorwärts, bei Bedarf mehrfach mit 1 s Überblendung aneinandergehängt
    src=O/f'hook_ki_{n[0]}.mp4'; L1=dur(src); k=max(1,int((mitte-1)//(L1-1))+1)
    ins=[]; [ins.extend(['-i',str(src)]) for _ in range(k)]
    f=';'.join(f'[{i}:v]scale=1080:1920,fps=30,setpts=PTS-STARTPTS[c{i}]' for i in range(k)); last='c0'
    for i in range(1,k):
        f+=f';[{last}][c{i}]xfade=transition=fade:duration=1:offset={i*(L1-1):.3f}[x{i}]'; last=f'x{i}'
    run('ffmpeg','-loglevel','error','-y',*ins,'-filter_complex',f,'-map',f'[{last}]','-t',f'{mitte:.3f}','-an','-c:v','libx264','-crf','20','-pix_fmt','yuv420p',str(O/f'{n}_buero_mitte.mov'))
    bl=[x for x in hook]+[f"file '{O}/{n}_buero_mitte.mov'",f"file '{O}/cta_buero_teil.mov'"]; (O/f'{n}_bg.txt').write_text('\n'.join(bl))
    run('ffmpeg','-loglevel','error','-y','-f','concat','-safe','0','-i',str(O/f'{n}_bg.txt'),'-an','-c:v','libx264','-crf','20','-pix_fmt','yuv420p',str(O/f'{n}_bg.mov'))
    run('rm','-rf',str(O/f'{n}_frames')); run('node',f'{P}/rendern_alpha.mjs',f'{P}/{n}_overlay.html','0',str(O/f'{n}_frames'),str(O/f'{n}_mapping.json'))
    run('python3',str(R/'zusammen2.py'),n,'1.5',str(m['cta']),ziel)
    print(n,'fertig',round(d,2),'Hook',round(hd,2),'Mitte',round(mitte,2))
