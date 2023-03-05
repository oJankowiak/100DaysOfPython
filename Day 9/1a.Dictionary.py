programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retreiving items from dictionary.
# print(programming_dictionary["Bug"])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
print (programming_dictionary["Loop"])

# Create an empty dictionary
# empty_dictionar = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionaty
# for key in programming_dictionary:
#     print(key)
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])