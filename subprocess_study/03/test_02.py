def get_len(argv1):
    print(f"입력받은 글자의 길이는 {len(argv1)} 이다.")

import sys
if __name__ == '__main__':
    argv1 = str(sys.argv[1])
    get_len(argv1)