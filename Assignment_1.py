#Q.3. Write a Python program to find the volume of a sphere with diameter 12 cm.

from math import pi

d = 12 #diameter = 12
r = d/2 #radius = diameter/2
print(r)
volume = (4/3) * pi * (r**3)
print(f'Volume of the sphere is {volume:.3f}')


#Q.2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

first_name = str(input("Enter your First Name : "))
last_name = str(input("Enter your Last Name : "))

print(f'{first_name[::-1]} {last_name[::-1]}')

#Q.1.  Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

for i in range(2000, 3201) :
    if i % 7 == 0 and i % 5 != 0 :
        print(i, end=',')