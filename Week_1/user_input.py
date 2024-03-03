
def user_info():
    name = input("What is your name? ")
    age = input("What is your age? ")
    location = input("What is your location? ")

    return f"Hello {name}, you are {age} years old and live in {location}."

if __name__ == "__main__":
    print(user_info())