#Author:Nathaniel Brown
#Date Created:August 8,2022
#Course: ITT103
#Purpose: <This is a program to calculate and print the commission received by a salesperson for JamEx Limited. The program will also process a number of salesperson and terminate by a predefined input appropriately.
#Declaring sales and Class as integer and SPN as input.
sales=int(input("sales written in dollars:"))
Class=int(input("types of class 1,2,3:"))
SPN=input("sales person numer is:")
#using if, elif statements to process a number of salesperson for class 1
if Class==1:
 if sales<= 1000:
  print(SPN,"should recieve",0.06*sales)
 elif 1000< sales <2000:
  print(SPN,"should recieve",0.07* sales)
 elif sales>=2000:
  print(SPN,"should recieve",0.1* sales)
#using if, elif statements to process a number of salesperson for class 2
elif Class==2:
 if sales<1000:
  print(SPN,"should recieve",0.04*sales)
 if sales>=1000:
   print(SPN,"should recieve",0.06*sales)
#using if, else, elif statements to process a number of salesperson for class 3
elif Class==3:
  print(SPN,"should recieve",0.045*sales)
else:
 print("Error Occurred")
