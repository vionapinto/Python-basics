
#TASK_1

print(int(234))
print(float(43.12))
print(3+2j)
print(str('Hello'))
print(bool('string'))



#TASK2

print(int (123), type(123), sep=' is type of ')
print(float (43.23), type(43.23), sep=' is type of ')
print(complex (4-1j), type(4-1j), sep=' is type of ')
print(str('How are you?'), type('How are you?'), sep= ' is type of ')
print(bool('True'), type(bool('true')), sep=' is type of ')



#TASK3

print(isinstance('city', str))
print(isinstance('city', int))
print(isinstance(3.14, float))
print(isinstance(True, bool))
print(isinstance(4, complex))


#TASK4

print('Is 123 an instance of int?:' , isinstance(123,int))
print('Is 43.23 an instance of bool?:', isinstance(43.23,bool))
print('Is (4-1j) an instance of complex?:', isinstance(4-1j,complex))
print('Is True an instance of bool?:', isinstance(True,bool))
print("Is 'How are you?' an instance of float?:", isinstance('How are you?',float))


#TASK5

# This is my first comment
# Block comments are indented to the same level as that code
print("Hello")
print("Line with inline code!")  # remember about spacing

print(type(123.45)) # getting type of number 

""" You can use triple-quoted strings. When they're not a docstring the first thing in a class/function/module), they are ignored. Read aforementioned answer from Stack Overflow!"""