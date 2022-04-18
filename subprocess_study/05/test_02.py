def get_len(argv1):
    print(f"입력받은 글자의 길이는 {len(argv1)} 이다.")

import sys
if __name__ == '__main__':
    if sys.argv[1] == 'get_len':
        get_len(sys.argv[2])