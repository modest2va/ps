import sys


if __name__ == '__main__':
    # 사용 예시
    n = int(sys.stdin.readline())
    my_list = []
    for i in range(n):
        user_age, user_name = sys.stdin.readline().split()
        user_age = int(user_age)
        my_list.append((user_age, user_name))
    for age, name in sorted(my_list, key= lambda x: x[0]):
        print(age, name)

