def prime_eratos(n):
    # nums: 0부터 n까지의 숫자들 리스트입니다.
    # prime: 소수 리스트
    nums =  [0] * (n+1)
    prime = []

    for i in range(2, n+1):
        # 소수인 경우 리스트에 추가
        if nums[i] == 0:
            prime.append(i)
        else:
            continue
        for j in range(i ** 2, n+1, i):
            nums[j] = 1

    return prime

m, n = map(int, input().split())
my_prime = prime_eratos(n)
for num in my_prime:
    if num >= m:
        print(num)
