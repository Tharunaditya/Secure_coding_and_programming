# Type Casting Exercise

a = 7

# 1. print the type of the variable
print(type(a))
#   Convert integer variable to float and confirm the type cast worked (print it out)
float_a = float(a)
print(type(float_a))

# 2. Now, Convert your float variable to string and print out the type

str_a=str(float_a)
print(type(str_a))
# 3. Finally, Convert your string variable back to integer and print it out (the type)

int_a= str_a
again=int(float(int_a))
print(type(again))