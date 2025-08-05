def add(num1, num2):
    return (num1 + num2)

def sub(num1, num2):
    return (num1 - num2)

def mul(num1, num2):
    return (num1 * num2)

def div(num1, num2):
    return (num1 / num2)

while not False:
    opr = str(input("Enter operation to perform (add/ sub/ mul/ div)"))

    if opr == 'exit':
        print("No operation performed! ")
        break
    
    elif opr == 'add' or opr == 'sub'or  opr =='mul'or opr == 'div':
        num1= int(input("enter first number: "))
        num2 = int(input("enter second number"))
        if opr == 'add':
            print("Additon is : ", add(num1,num2))
        if opr == 'sub':
            print("sub is : ", sub(num1,num2))
        if opr =='mul':
            print("mul is : ", mul(num1,num2))
        if opr == 'div':
            print("div is : ", div(num1,num2))
    else:
        print("Invalid output ")
    