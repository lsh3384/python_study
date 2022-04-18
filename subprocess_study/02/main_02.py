# -*- coding: utf-8 -*-
'''
https://blog.naver.com/sagala_soske
29 OCT 2020
subprocess 예제
'''
import subprocess
import sys


# 변수에 담아서 사용하는 방법
p2 = subprocess.run(args=[sys.executable, 'test_02.py'], capture_output=True, text=True)

print(p2.stdout)