n='9780921418'
for _ in range(3):
    n+=input()
returnSum=0
for i in range(len(n)):
    if i%2==0: returnSum+=int(n[i])*1
    else: returnSum+=int(n[i])*3
print("The 1-3-sum is %d"%returnSum)