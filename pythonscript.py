def add_numbers (num1, num2):
    result = num1 + num2
    return result

def main():
    # Prompt input for two numbers
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter another number: "))
    
    # Prompt function and store results
    sum_result = add_numbers(number1, number2)
    
    #Display results
    print("The sum is: ", sum_result)
    

# Call the main function
if __name__ == "__main__":
    main()
        
# Test
def test_add_numbers():
    # Test case 1
    assert add_numbers(2, 3) == 5
    
    # Test case 2
    assert add_numbers(-10, 5) == -5
    
    # Test case 3
    assert add_numbers(0,0) == 0
    
    print("All test cases passed.")
    
# Call the unit test function
test_add_numbers()