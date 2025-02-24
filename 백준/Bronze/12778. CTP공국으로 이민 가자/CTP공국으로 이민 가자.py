def sol(type_prob, probs):
    if type_prob == 'C':
        answer = [ord(i)-64 for i in probs]
    elif type_prob == 'N':
        answer = [chr(int(i) + 64) for i in probs]

    return answer

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m, type_prob = input().split()
        probs = list(input().split())
        print(*sol(type_prob, probs))
        