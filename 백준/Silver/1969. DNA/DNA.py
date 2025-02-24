from collections import Counter
def cal_hamming(dna,target):
    hamming = 0
    for compared_dna in dna:
        for i in range(len(target)):
            if compared_dna[i]!= target[i]:
                hamming+=1
    return hamming

if __name__ == '__main__':
    n,m = map(int, input().split())
    dna=[input() for i in range(n)]
    answer =''
    for i in range(m):
        tmp=[]
        for j in range(n):
            tmp.append(dna[j][i])
        sorted_counter =sorted(Counter(tmp).items(), key=lambda x: (-x[1],x[0] ))
        answer+=sorted_counter[0][0]
    print(answer)
    print(cal_hamming(dna,answer))