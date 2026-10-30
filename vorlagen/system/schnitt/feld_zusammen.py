# Komposit: geschnittenes Video (scharf) -> Mitte unscharf+abgedunkelt -> transparente Overlay-Frames -> Ton mit Musik, -18 LUFS
# python3 zusammen.py <name> <blur_von> <blur_bis> [musik]
import subprocess,sys,json
from pathlib import Path
R=Path('/home/user/roh'); name,a,b=sys.argv[1],float(sys.argv[2]),float(sys.argv[3])
musik=sys.argv[4] if len(sys.argv)>4 else '/home/user/Instagram-maehrsteuern/musik/06_runway_lofi_ruhig.mp3'
d=json.load(open(R/f'out/{name}_woerter.json'))['dauer']; d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(R/f'out/{name}_schnitt.mov')]))
frames=R/f'out/{name}_frames'
fc=(f"[0:v]split[s][u];[u]gblur=sigma=38,eq=brightness=-0.10:saturation=0.75,format=yuva420p,"
    f"fade=t=in:st={a-0.15}:d=0.35:alpha=1,fade=t=out:st={b-0.2}:d=0.35:alpha=1[bl];[s][bl]overlay=shortest=1[bg];"
    f"[bg][1:v]overlay=format=auto[v];"
    f"[2:a]volume=0.07,afade=t=in:d=0.8,afade=t=out:st={d-1.5}:d=1.5[m];[0:a][m]amix=inputs=2:duration=first:normalize=0,"
    f"loudnorm=I=-18:TP=-1.5:LRA=11[a]")
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',str(R/f'out/{name}_schnitt.mov'),'-framerate','30','-i',f'{frames}/f%05d.png',
   '-stream_loop','-1','-i',musik,'-filter_complex',fc,'-map','[v]','-map','[a]','-c:v','libx264','-crf','18','-pix_fmt','yuv420p',
   '-c:a','aac','-b:a','192k','-ar','48000','-t',f'{d:.3f}','-movflags','+faststart',str(R/f'out/{name}_reel.mp4')],check=True)
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',str(R/f'out/{name}_reel.mp4'),'-frames:v','1',str(R/f'out/{name}_titelbild.png')],check=True)
print('✓',R/f'out/{name}_reel.mp4')
