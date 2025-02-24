def sol(start, end):
    cnt = (end - start)//60
    for i in range(cnt+1):
        print('All positions change in year %d'%(start+i*60))
        
if __name__ == '__main__':
    start = int(input())
    end = int(input())
    sol(start,end)