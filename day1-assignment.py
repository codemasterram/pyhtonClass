# Program to ask for a co-ordinate point (x,y).And
#  print in which quadrent it lies in. If it lies in any axis 
#  print the name of the axis instead. For eg: (5,0) 
# should print 'X-axis' but (5,-5) should print "4st quadrent".
x= int(input('Enter co-ordinate of x'))
y= int(input('Enter co-ordinate of y'))
if x==0 and y==0:
	print("Co-ordinate belongs to the origin")
elif x>0 and  y>0: 
	print("it lies in first quadrent")
elif x==0:
	print("it lies in y-axis")
elif y==0:
	print("It lies in x-axis")
elif x<0 and y>0:
	print('It lies in second quadrent')
elif x<0 and y<0:
	print('It lies in third quadrent')
elif x>0 and y<0:
	print('It lies in fourth quadrent')
