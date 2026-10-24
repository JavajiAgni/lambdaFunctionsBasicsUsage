def get_quotient(num,den):
    return num/den

fun = lambda num, den : num/den
res = fun(10,2)
print(res)

print(get_quotient(10,2))

#sum of even numbers and odd numbers in series

even_sum, odd_sum = 0,0
n=int(input("Enter the values\n"))
for i in range(1,n+1):
    if i%2==0:
        even_sum+=i
        continue
    odd_sum+=i
    
print("sum of all even numbers",even_sum)
print("sum of all odd numbers",odd_sum)


#power of a number using lambda
res = (lambda  base, power: base**power)(2,5)
print(res)


#lambda functions inside def functions
#multiplication table
def fun1(num):
    return lambda x: x*num
num = int(input("Enter a number\n"))
math_table = fun1(num)
for i in range(1,11):
    print(num," X ",i," = ",math_table(i))


def fun1(num):
    return lambda x: x*num
num = int(input("Enter a number\n"))
math_table = fun1(num)
for i in range(1,11):
    print(num," X ",i," = ",math_table(i))
lst = [10,13,14,15,18]
def fun(x):
    if x%2==0:
        return True
    else:
        return False
res = list(filter(fun,lst))
print(res)
#filter function

result = list(filter(lambda x : (x%2==0), lst))
print(result)
#reduce function
lst1 = [1,2,3,4,5]
def fun1(x,y):
    return x+y 
res1 = reduce(fun1,lst)
print(res1)


res2 = reduce(lambda x,y : x+y, lst)
print(res2)
#map fuction

res3 = list(map(lambda x : x**2,lst))
print(res3)


def fun2(num):
    return lambda x : x*num
res4  = fun2(5)
print(res4(2))
