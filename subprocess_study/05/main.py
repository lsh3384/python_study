# -*- coding: utf-8 -*-
'''
https://blog.naver.com/sagala_soske
29 OCT 2020
subprocess 예제
'''
import subprocess
import sys

# with open("result.txt", "w", encoding='utf-8') as result:
#     p1 = subprocess.run(args=[sys.executable, 'test_01.py'],
#                         capture_output=True, text=True, encoding='utf-8')
#     p2 = subprocess.run(args=[sys.executable, 'test_02.py', p1.stdout],
#                         capture_output=True, text=True, encoding='utf-8')
#     result.write(p2.stdout)
#

with open("result.txt", "w", encoding='CP949') as result:
    p1 = subprocess.run(args=[sys.executable, 'test_01.py'],
                        capture_output=True, text=True, encoding='CP949')
    p2 = subprocess.run(args=[sys.executable, 'test_02.py', 'get_len', p1.stdout],
                        text=True, encoding='utf-8', stdout=result)
    print('finished')