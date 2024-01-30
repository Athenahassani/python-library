# python-library
This is a math library for Python enthusiasts.

In this library, pre-built libraries are not used.

An attempt has been made not to use Python's default methods.

This library is for elementary math calculations.

We have 4 files called static, matrix, arithmetic and sorting.

In arithmetic, we come across Python codes for elementary mathematics.
 Such as addition and subtraction, multiplication and division, calculating logarithms, factorials, square roots, converting radians to degrees and vice versa, calculating remainders, recognizing primes, calculating the reverse of a number and recursive Fibonacci sequence, etc.

 In the matrix file, we have Python codes for addition, multiplication, transposition, matrix inverse and covariance matrix , etc.

 In sorting, we have methods for sorting numbers, such as insertion sorting, bubble sorting and merge sorting, etc.

 In the statistics file, we have codes for calculating sum of numbers, mean, variance, standard deviation, mode, median, percentile, covariance, correlation, finding maximum and minimum, calculating range, normal distribution and counting even and odd numbers, etc.

 In the following, I have given you how to calculate the variance using this library:
 
 from pymath import static

 
 x = [1,2,3,4]
 
 v = static.calculate_variance(x)
 
 print(v)
