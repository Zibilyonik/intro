# first part of the project
print("Hello! My name is PotatoHelper3000")
print("I was created in 2023")
# second part of the project
print('Please, remind me your name.')
user_input = input()
print('What a great name you have, ' + user_input + "!")
# third part of the project
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(age) + "; that's a good time to start programming!")
# fourth part of the project
print('Now I will prove to you that I can count to any number you want.')
number = int(input())
count = 0
while count <= number:
    print(str(count) + " !")
    count += 1
print('Completed, have a nice day!')
