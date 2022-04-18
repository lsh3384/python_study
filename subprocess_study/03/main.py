# -*- coding: utf-8 -*-
'''
https://blog.naver.com/sagala_soske
29 OCT 2020
subprocess 예제
'''
import subprocess
import sys

p1 = subprocess.run(args=[sys.executable, 'test_01.py'], capture_output=True, text=True)
p2 = subprocess.run(args=[sys.executable, 'test_02.py', p1.stdout])