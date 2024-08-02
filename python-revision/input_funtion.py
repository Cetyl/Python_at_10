# create a calculator with input function which gives an output of the mul, div, add,sub, with two numbers ---- you can use variable
a = input("choose the number :")
b = input ("choose the number :")
print("answer of addition is ", int(a) + int(b) ,sep = '~ ' )
print("answer for subtraction is ", int(a) - int(b) ,sep = '~ ' )
print("answer for division is ", int(a) / int(b) ,sep = '~ ' )
print("answer for multiplication is ", int(a) * int(b) ,sep = '~ ' )

# second way
print("addition of", a,"+", b, "is", int(a) + int(b))
print("subtraction of", a,"+", b, "is", int(a) - int(b))
print("multiplication of", a,"+", b, "is", int(a) * int(b))
print("division of", a,"+", b, "is", int(a) / int(b))
