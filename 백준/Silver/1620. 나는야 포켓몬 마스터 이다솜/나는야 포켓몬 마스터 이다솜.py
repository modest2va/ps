import sys
n , m =map(int,sys.stdin.readline().split())
pokemon = dict()
for i in range(1,n+1):
    name = sys.stdin.readline().rstrip()
    pokemon[name] = i
pokemon_reversed = dict(map(reversed, pokemon.items()))
for i in range(m):
    target=sys.stdin.readline().rstrip()
    if target.isnumeric():
        print(pokemon_reversed[int(target)])
    else:
        print(pokemon[target])