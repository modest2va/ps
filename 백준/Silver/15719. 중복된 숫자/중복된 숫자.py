import sys

def sol(n, nums):
    sum_nums = 0
    tmp_number = ''
    for number in nums:
        if number.isnumeric():
            tmp_number+=number
        else:
            sum_nums+=int(tmp_number)
            tmp_number = ''

    answer = n - (int(n*(n+1)/2) - sum_nums)
    return answer

if __name__ == '__main__':
    n = int(input())
    nums = sys.stdin.read()
    print(sol(n, nums))