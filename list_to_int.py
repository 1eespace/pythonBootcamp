# Task 1: Given a list of digits, determine the integer that it represents
# TypeError: 'list' object cannot be interpreted as an integer

# Step1. Make a function
def determine_int(x):
    # Step2. Set variable as local (Inside the function scope)
    result = 0
    # Using "for loop" for iteration
    for number in x:  
        # Step3. Using the math expression: 
        # 1111 => 1 + (10 * 1) + 1 + (10 * 10) + 1 + (10 * 10 * 10) + 1
        result = result * 10 + number  
    
    # Step4. Using "print" function to show value in the Terminal
    print(result)
        
# Test
x = [8, 3, 5, 1]
determine_int(x)