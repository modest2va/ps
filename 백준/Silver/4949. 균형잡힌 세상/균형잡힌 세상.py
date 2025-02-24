while True:
    answer = 'yes'
    s=input()
    if s=='.':
        break
    stack=[]
    for i in s:
        if i=='(' or i=='[':
            stack.append(i)
        if i==')':
            if len(stack) != 0 and stack[-1] =='(':
                stack.pop()
            else:
                stack.append(i)
        elif i==']':
            if len(stack) != 0 and stack[-1] =='[':
                stack.pop()
            else:
                stack.append(i)

    if len(stack) != 0:
        answer ="no"
    print(answer)