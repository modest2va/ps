a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
c1,c2=map(int,input().split())

if abs(b1-c1)+abs(b2-c2)> max(abs(a1-c1),abs(a2-c2)):
    print("bessie")
if abs(b1-c1)+abs(b2-c2)< max(abs(a1-c1),abs(a2-c2)):
    print("daisy")
if abs(b1-c1)+abs(b2-c2)== max(abs(a1-c1),abs(a2-c2)):
    print("tie")