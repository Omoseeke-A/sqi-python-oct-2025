# Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.
 

# class NegativeNumberError(Exception):
#     def __init__(self,number):
#         self.number= number
#         super().__init__(self.number)
    
# def check_positive(number):
#          if number < 0 :
#               raise NegativeNumberError(" Number must not be negative")
#          print(f"{number} is positive")
# try:
#    check_positive(-5)
#    check_positive(5)

# except NegativeNumberError as e:
#      print(e)


# Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.
def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("You cannot divide by zero,Try Again")      
    except TypeError:
        print("Both values has to be numbers,Try Again!")
    except ValueError:
        print("DID YOU ENTER A STRING")
    else:
        print("Torr")
    

print(safe_divide(1,4))

print(safe_divide(1,0))

print(safe_divide(1,"4"))

# print(safe_divide(1+"a",2+"b"))