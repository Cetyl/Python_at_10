# if-else Statements

Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further classified into following types:

- if
- if-else
-  if-else-elif
-  nested if-else-elif.

### An if……else statement evaluates like this:
#### if the expression evaluates True:
Execute the block of code inside if statement. After execution return to the code out of the if……else block.\

#### if the expression evaluates False:
Execute the block of code inside else statement. After execution return to the code out of the if……else block.

```python
Example:

applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

Output:
Alexa, do not add Apples to the cart.

```

```python
Example:

a = int(input ("whats your age ?" ) )
print("your age is",a)

# conditional inputs 
print(a > 21)
print(a < 21)
print(a == 21)
print(a != 21)

if ((a) > 21): 
    print("you can drink")
else:
    print("go home")

Output:
your age is 81
True
False
False
True
you can drink
```






