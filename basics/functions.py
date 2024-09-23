jan_exp = [2300, 3456, 39990, 23]
feb_exp = [3344, 211, 98, 78765]

total=0
for i in jan_exp:
    total = total + i
print("Jan expense total:", total)

total=0
for i in feb_exp:
    total = total + i
print("Feb expense total:", total)

#Instead of writing 2 for loops with same functionality, we can create a function

exp_total=0
def calculate_expenses(exp):
    exp_total=0
    for i in exp:
        exp_total = exp_total+ i
    print("Exp Total inside function", exp_total)
    return exp_total

jan_total = calculate_expenses(jan_exp)
feb_total = calculate_expenses(feb_exp)

print("Jan expense total:", jan_total)
print("Feb expense total:", feb_total)

"""
print(exp_total) -> cannot call exp_total here as the variable is local variable inside
the function and hence cannot be called outside
Also if exp_total was defined globally outside the function, the value of it inside 
function will be different from outside as shown below
"""
print("Exp total outside function", exp_total)

def sum(a,b=0):
    """
    in case second number isnt passed while calling the function, it will default the
    second number as 0
    """
    sum_total=a+b
    return sum_total

check_sum1 = sum(9,5)
#Positional Arguement - where a and b takes value as per their position while passing the
#parameter
print(check_sum1)

check_sum2 = sum(6)
print(check_sum2)

check_sum3 = sum(b=8,a=3)
#Named Arguement - where the values to variables are mentioned explicitly
print(check_sum3)



