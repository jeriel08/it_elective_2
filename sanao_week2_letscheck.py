# Week 2 Let's Check

# Problem 1
user_input = input("Enter a phrase or write a sentence: ")

print(f"Reversed: {user_input[::-1]}")

# Problem 2
input_to_list = list(user_input)
print(f"Output in list: {input_to_list}")

# Problem 3
reversed_string = ' '.join(user_input.split()[::-1])  # Split the string into words, reverse, and join them back
print("Output:", reversed_string)
