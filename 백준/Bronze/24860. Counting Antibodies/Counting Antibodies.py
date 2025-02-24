def sol(vk, jk, vl,jl,vh,dh,j):
    return (vk*jk+vl*+jl)*(vh*dh*j)

if __name__ == '__main__':
    vk, jk =map(int, input().split())
    vl, jl = map(int, input().split())
    vh, dh, j = map(int, input().split())

    print(sol(vk, jk, vl,jl,vh,dh,j))