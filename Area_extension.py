""" Your task now is to write a Python program which accepts the radius of a circle from the user and computes area.
Your Input and Output should look something like this

Input the radius of the circle : 1.1 The area of the circle with radius 1.1 is: 3.8013271108436504 """



from math import pi
radius = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius**2))



""" Your second task now is to write a Python program to accept a filename from the user and print the extension of that.
Your Input and Output should look something like this

Input the Filename: abc.py The extension of the file is : 'python'

Let's start coding ! """


filename = input("Input the Filename: ")
f_ext = filename.split(".")
print ("The extension of the file is : " + repr(f_ext[-1]))
