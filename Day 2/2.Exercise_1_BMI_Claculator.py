# Program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

print (type(weight))

weight_as_int = int(weight)
height_as_float = int(height)

# Using the exponent operator **
BMI = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
BMI = weight_as_int / (height_as_float * height_as_float)

print (int(BMI))