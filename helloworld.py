name = input("What is your name?: ")
age = input("How old are you?: ")
country = input("What country do you live in?: ")

data_string = name + " is " + str(age) + " years old. They live in " + country + "."

with open("users.txt","w+") as file:
  file.write(data_string)
