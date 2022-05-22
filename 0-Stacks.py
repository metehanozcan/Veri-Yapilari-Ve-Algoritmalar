
#*Basit Yığın Veri Yapısı
def create_stack():
    stack=[]
    return stack

def check_empty():
    return len(stack)==0


def push(stack,item):
    stack.append(item)
    return stack
    

def pop(stack):
    if (check_empty(stack)):
        return "Empty stack"
    
    return stack.pop()

stack = create_stack()
print(push(stack,1))
push(stack,2)
push(stack,3)
push(stack,4)
push(stack,5)

print(stack.pop())
print(stack)


