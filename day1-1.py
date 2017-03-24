# part one 

age = int(input('Enter your age in numbers.'))
if age <=0:
	print("Invalid input for age.")
elif age<=1:
	print("You're infant")
elif age>=2 and age<=12:
	print("You are just a kid")
elif age>=13 and age<=19:
	print("You're teenager")
elif age>=20 and age<=45:
	print("You're adult now")
elif age>=46 and age<=59:
	print("You're infant")
elif age>=60 and age<=119:
	print("You're old")
elif age>=120:
	print("You're too oldd to still be alive.")

#part two

age = int(input('Enter your age in numbers.'))
if age<=0:
	print("Invalid input for age.")
elif age<=1:
	print("You're infant")
elif age<=12:
	print("You are just a kid")
elif age<=19:
	print("You're teenager")
elif age<=45:
	print("You're adult now")
elif age<=59:
	print("You're infant")
elif age<=119:
	print("You're old")
elif age>=120:
	print("You're too oldd to still be alive.")

