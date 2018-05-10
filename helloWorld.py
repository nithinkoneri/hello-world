# This program says hello and asks for name.

print('Hello World!')
print('Whats your name?')

myName = input()
print('It is good to meet you '+myName+'.' )
print('Length of your name is : '+ str((len(myName))))
# print(len(myName))

print('Whats your age?')
myAge = input()
# print(myAge)

print('You will be ' + str(int(myAge) + 1) + ' in a year.')
