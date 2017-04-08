a = float(input('First Number: '))
b = float(input('Second Number: '))
try:
	result = (a / b)
except ZeroDivisionError: # ZeroDivisionError is a library defined error in python when any number is divided by zero
	print('Error: Division by Zero')