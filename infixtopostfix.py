#infix to postfix
operator = {"*":2,"/":2,"+":1,"-":1}
exp = input("Enter any expression : ")
postfix = ""
stack = []
for i in exp:
    if i not in operator:
        postfix = postfix + i
    else:
        if stack==[]:
            stack.append(i)
        else:
            if operator[stack[-1]] < operator[i] or operator[stack[-1]] == operator[i]:
                stack.append(i)
            else:
                while(stack!=[]):
                    postfix = postfix + str(stack.pop())
                stack.append(i)
while(stack!=[]):
    postfix = postfix + str(stack.pop())
print("postfix expression : " +postfix)
#postfix = 'ABC*+DE*-'
for i in postfix:
    if not stack:
        stack.append(i)
    else:
        if i in operator:
            op2 = stack.pop()
            op1 = stack.pop()
            if i == "+":
                stack.append(int(op1)+int(op2))
            elif i=="-":
                stack.append(int(op1)-int(op2))
            elif i=="/":
                stack.append(int(op1)/int(op2))
            else:
                stack.append(int(op1)*int(op2))
        else:
            stack.append(i)
print("result : "+str(stack[-1]))
            

                    
            
    
    
    
            
