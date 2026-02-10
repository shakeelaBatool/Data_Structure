stack=[]
def push(x):
    stack.append(x)
def pop():
    if len(stack)== 0:
        print("Stack is empty")
    else:
        print(stack.pop())

push(9)
push(11)
push(12)
push(14)
pop()
pop()
pop()

pop()

