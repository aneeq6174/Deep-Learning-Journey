# This will work fine
age = 25
name = "Aneeq"
print(f"{name} is {age} years old")

# But what about this?
age = "twenty-five"  # Oops! Changed to string
result = age + 10    # What happens here?
print(result)