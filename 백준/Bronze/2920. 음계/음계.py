piano = list(map(int, input().split()))

if piano == sorted(piano):
    print('ascending')
elif piano == sorted(piano, reverse=True):
    print('descending')
else:
    print('mixed')
    