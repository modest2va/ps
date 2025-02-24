def cnt(nums):
    return nums[0]*6+nums[1]*3+nums[2]*2+nums[3]*1+nums[4]*2
nums1=list(map(int, input().split()))
nums2=list(map(int, input().split()))
print(cnt(nums1),cnt(nums2))