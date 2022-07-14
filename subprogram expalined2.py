#subprograms explained 2
#this subprogram is an example of a "function"
#A functionm contains a return statement value
a = int(input("enter a number >"))
b = input(input("enter another number>"))

def adding(a,b): #parameters arse used a and b
    answer = 0
    answer = a+b
    print(answer)
    return answer

adding(a,b)#call with parameters

x = adding(a,b)
print(x)


   
                     
