# -*- coding: utf-8 -*-
'''
https://blog.naver.com/sagala_soske
29 OCT 2020
subprocess 예제
'''
import subprocess

p1 = subprocess.run(args=["type", "result.txt"], shell=True, capture_output=True, encoding='utf8')
p2 = subprocess.run(args=["findstr", "-n", "19"], shell=True, capture_output=True, encoding='utf8',
     text=True, input=p1.stdout)
print(p2.stdout)