import turtle

x = 5
y = 'string'


'''

<class 'int'>, means x is an instance of int class
<class 'str'>, means y is an instance of str class 

This classes allow us to have built in functionality 
Even functions are typically built into a class of a certain type 

Just understand that whenever you create anything in Python it is 
actually an object without you really knowing it or not. 
'''
print(type(x))

print(type(y))

tim = turtle.Turtle() #This is the constructor, when you call it you're actually creating a new turtle object
# and you're just naming it tim or storing it in the variable tim. 
tim.color("black", "red") 
tim.begin_fill() 
tim.circle(60) 
tim.end_fill()


#A function everyone here should know is created with the defined key

def addition(numberOne, numberTwo):
    return numberOne + numberTwo

result = addition(1, 1)
print(result)

#A method is what you actually call with the dot operator, for example
#What method is anything you're calling on an object itself right and a function
#is something that's gonna take an object and apply an operation to it 
name = "pablo"

print(name.upper())