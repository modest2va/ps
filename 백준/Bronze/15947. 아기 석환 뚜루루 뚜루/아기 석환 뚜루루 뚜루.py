def sol(n):
    n-=1
    song ='baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan'
    song= list(song.split())
    idx = n%14
    repeat = n//14
    if idx in [3,7,11]:
        answer =("tu+ru*%d"%(repeat+1) if repeat>=4 else "turu"+'ru'*repeat)
    elif idx in [2,6,10]:
        answer =("tu+ru*%d"%(repeat+2) if repeat>=3 else "tururu"+'ru'*repeat)
    else:
        answer = song[idx]
    return answer
if __name__ == '__main__':
    n=int(input())
    print(sol(n))