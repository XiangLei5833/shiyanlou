def get_number():
    number = float(input("Enter a float number: "))
    return number

try:
    raise ValueError("A value error happened.")
except ValueError:
    print("ValueError in our code")
