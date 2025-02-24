import sys
s_price,s_weight=map(int,sys.stdin.readline().split())
n_price,n_weight=map(int,sys.stdin.readline().split())
u_price,u_weight=map(int,sys.stdin.readline().split())
if s_price*10>=5000: s_gsb= (s_weight*10)/(s_price*10 - 500)
else : s_gsb=(s_weight*10)/(s_price*10 )
if n_price*10>=5000: n_gsb= (n_weight*10)/(n_price*10 - 500)
else : n_gsb=(n_weight*10)/(n_price*10 )
if u_price*10>=5000: u_gsb= (u_weight*10)/(u_price*10 - 500)
else : u_gsb=(u_weight*10)/(u_price*10 )

if s_gsb > n_gsb and s_gsb > u_gsb: print("S")
if n_gsb > s_gsb and n_gsb > u_gsb: print("N")
if u_gsb > n_gsb and u_gsb > s_gsb: print("U")