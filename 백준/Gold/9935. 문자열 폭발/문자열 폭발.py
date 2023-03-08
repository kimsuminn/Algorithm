text = input()
string = input()
stack = []

for i in range(len(text)):
    stack.append(text[i])
    if ''.join(stack[-len(string):]) == string:
        for _ in range(len(string)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
