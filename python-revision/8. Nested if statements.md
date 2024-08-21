# Nested if statements
We can use if, if-else, elif statements inside other if statements as well.

``` python
Example:

a = int(input("Enter the number"))

if ( a < 0 ):
    print("its negative")
    
elif( a > 0 ):
    if ( a <= 9 ):
        print("number is less than 10")
    elif( a == 10):
        print('number is 10')
    elif( a > 10 and a <= 20 ):
        print("number is between 10 to 20")
    else :
        print("number is greater than 20")    
    
else:
    print("its zero")

Output:
number is 10

```

``` python
Example:

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

Output:
Number is between 11-20

