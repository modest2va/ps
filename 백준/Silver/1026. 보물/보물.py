def sol(nums1,nums2):
    answer=0
    for i in range(len(nums1)):
        answer+=nums1[i]*nums2[i]
    return answer
n=int(input())
nums1=sorted(list(map(int,input().split())))
nums2=sorted(list(map(int,input().split())), reverse=True)

print(sol(nums1,nums2))