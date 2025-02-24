w_university = [int(input()) for i in range(10)]
k_university = [int(input()) for i in range(10)]
w_university.sort(reverse= True)
k_university.sort(reverse= True)
print(sum(w_university[:3]), sum(k_university[:3]))