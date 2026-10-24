def fib(n):
    if n==1:
        return 1
    return n*fib(n-1)
num = int(input("Enter a num\n"))
print(fib(num))



#Strings

s="coding is \"fun\" "
print(s)

s='coding is \'fun\' ' 
print(s)

s='coding is "fun" ''
print(s)

s="coding is 'fun' "
print(s)

s= ''' coding is 'fun' '''
print(s)


