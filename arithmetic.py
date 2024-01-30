# Sorting Functions
def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers



# Calculator Functions
def add(x, y):
    return x + y



def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y



def divide(x, y):
    if y == 0:
        return "خطا!تقسیم ممکن نیست."
    return x / y



def my_log(x):
    if x <= 0:
        return float('-inf')  # لگاریتم اعداد منفی یا صفر در پایتون برابر است با float('-inf')
    
    n = 1000000  # تعداد تکرارهای تقریب
    result = 0
    for i in range(1, n + 1):
        result += ((-1) ** (i + 1)) * ((x - 1) ** i) / i
    
    return result



def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)



def calculate_square_root(x):
    return x ** 0.5



def calculate_power(base, exponent):
    return base ** exponent



def radians_to_degrees(radians):
    degrees = radians * (180 / 3.141592653589793)
    return degrees




def degrees_to_radians(degrees):
    radians = degrees * (3.141592653589793 / 180)
    return radians



def calculate_remainder(dividend, divisor):
    if divisor == 0:
        return "خطا! تقسیم بر صفر ناممکن است."
    return dividend % divisor



def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True



def add_list(numbers):
    result = 0
    for num in numbers:
        result += num
    return result



def calculate_inverse(number):
    if number == 0:
        return "خطا! نمی‌توان معکوس صفر را محاسبه کرد."
    return 1 / number



def fibonacci_recursive(n):
    if n <= 0:
        return "خطا! عدد ورودی باید مثبت باشد."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

