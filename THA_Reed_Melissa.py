
#While Loop and Math#
numberlist= [1, 2, 4, 5 , 6, 7, 9, 10, 13, 14, 15, 16]
i=0 
while i < len(numberlist):
    if numberlist[i] % 2 == 0:
        print("Printing the value of i " + str(numberlist[i]))
    i +=1

#Funtions and Parameters
def my_function(one, two, number):
#================================
# This function written by Melissa Reed
    if len(one) == len(two):
        print ("Equal Lengths")
    else:
        print ("Unequal Lenths")
    print (len(one)+number)

my_function("hello", "bye", 3)




#Lambda Function
x = lambda one, two, number : len(one) + len(two) - number

x ("hello", "bye", 3)