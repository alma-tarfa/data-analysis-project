"""
Task 1
Write variables for the following statement.
1.A patient is called Angela Smith, she is 25 years old and is a new patient.
2.Your favourite colour is Green, you are a girl and you live in Ireland.
"""
name = "Angela Smith"
age = 25

#print("My name is {name}. I am {age} years old. I am a new patient".format(age=age, name=name))

colour = "green"
gender = "girl"
country = "Ireland"

#print("Hi my favorite color is {c}. I am a {g} and I live in {cry}".format(c=colour, g=gender, cry= country))
"""
Task 2
Request for the name of a user, their favourite colour and their age, then print out what the user typed in.
Example “My name is Sarah, my favourite colour is red and I am 15 years old”
"""
print("\nEnter your name: ")
name_input = input()

print("\nWhat is your favorite colour? :")
colour_input = input()

print("\nHow old are you? : ")
age_input = input()

print("My name is {name}, my favourite colour is {colour} and I am {age} years old".format(name=name_input ,colour=colour_input, age=age_input))