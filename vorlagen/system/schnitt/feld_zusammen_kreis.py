# Komposit v2 (Loris 30.10.): Gesicht nur kurz im Hook, danach durchgehend unscharf; im CTA rundes Gesichts-Fenster.
# python3 zusammen2.py <name> <blur_ab> <cta_ab>
import subprocess,sys
from pathlib import Path
R=Path('/home/user/roh'); name,a,c=sys.argv[1],float(sys.argv[2]),float(sys.argv[3])
musik='/home/user/Instagram-maehrsteuern/musik/06_runway_lofi_ruhig.mp3'
d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(R/f'out/{name}_schnitt.mov')]))
K=400; X,Y=340,1090   # Kreis: 400 px, über der CTA-Karte
fc=(f"[0:v]split=2[s][k];[6:v]gblur=sigma=38,eq=brightness=-0.10:saturation=0.75,format=yuva420p,fade=t=in:st={a}:d=0.35:alpha=1[bl];"
    f"[s][bl]overlay=shortest=1[bg];"
    f"[k]crop=1080:1080:0:470,scale={K}:{K},format=rgba[kk];[4:v]format=gray[m];[kk][m]alphamerge,fade=t=in:st={c}:d=0.3:alpha=1[kreis];"
    f"[5:v]format=rgba,fade=t=in:st={c}:d=0.3:alpha=1[ring];"
    f"[bg][ring]overlay={X-10}:{Y-10}:shortest=1[b2];[b2][kreis]overlay={X}:{Y}[b3];[b3][1:v]overlay=format=auto[v];"
    f"[2:a]volume=0.07,afade=t=in:d=0.8,afade=t=out:st={d-1.5}:d=1.5[mu];[0:a][mu]amix=inputs=2:duration=first:normalize=0,"
    f"atempo=1.1,loudnorm=I=-18:TP=-1.5:LRA=11[a];[v]setpts=PTS/1.1,fps=30[vs]")
ziel=f'/home/user/Instagram-maehrsteuern/aufnahmen/2026-10-30/reels/{sys.argv[4]}.mp4'
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',str(R/f'out/{name}_schnitt.mov'),'-framerate','30','-i',str(R/f'out/{name}_frames/f%05d.png'),
   '-stream_loop','-1','-i',musik,'-f','lavfi','-i','anullsrc','-loop','1','-i',str(R/'out/kreis_maske.png'),'-loop','1','-i',str(R/'out/kreis_ring.png'),'-i',str(R/f'out/{name}_bg.mov'),
   '-filter_complex',fc,'-map','[vs]','-map','[a]','-c:v','libx264','-crf','18','-pix_fmt','yuv420p',
   '-c:a','aac','-b:a','192k','-ar','48000','-t',f'{d/1.1:.3f}','-movflags','+faststart',ziel],check=True)
print('✓',ziel)
