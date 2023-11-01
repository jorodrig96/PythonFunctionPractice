"""
1.
A function named hello() that prints a greeting to the user. 
This function should accept no arguments and returns nothing.
"""

def hello():
    print("Greetings Friend")

hello()

"""
2.
A function named pack() that accepts three arguments
and returns a single list with the three arguments inside as list elements.
"""

def pack (cookies, ice_cream, pizza):
    return[cookies, ice_cream, pizza]

print(pack("chocalte chip cookies", "oreo ice cream", "pepporoni pizza"))



"""
3. 
A function called eat_lunch(). 
This function should accept a list of any length, and print out a series of strings that say:
"First I eat __" (the first element of the list)
and "Next I eat ___" (for the following elements in the list). 
If the list is empty, print "My lunchbox is empty!". The function should not return anything.
"""

def eat_lunch(lunch_menu):
    if len(lunch_menu) == 0: 
        print("My lunchbox is empty!")
    elif len(lunch_menu) == 1:
        print(f"First I'll eat {lunch_menu[0]}.")
    else:
        for i in range(len(lunch_menu)):
            print(f"Next I'll eat some {lunch_menu[i]}.")
            

eat_lunch([])
eat_lunch(["chicken and rice."]) 
eat_lunch(["pizza","fries","chips","cookies"])



