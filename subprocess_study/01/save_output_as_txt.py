import subprocess
f=open('output.txt', 'w')
out=subprocess.check_output(['hello.py'], shell=True, encoding='utf-8')
f.write(out)
f.close()