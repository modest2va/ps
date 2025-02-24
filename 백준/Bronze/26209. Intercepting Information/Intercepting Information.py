def sol(nums):
    if 9 in nums :
        return False
    else:
        return True

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    if sol(nums):
        print('S')
    else:
        print('F')