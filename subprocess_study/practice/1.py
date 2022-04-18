import subprocess

subprocess.call('ffmpeg -re -i C:\\Users\\User\\Downloads\\ffmpeg-2022-03-21-git-505a7d39cd-full_build\\bin\\test1.mkv -c copy -f rtp_mpegts rtp://localhost:8554/visual', shell=True)