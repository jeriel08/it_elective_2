# Week 2 Let's Check

# Problem 1
user_input1 = input("Enter a phrase or write a sentence: ")

print(f"Reversed: {user_input1[::-1]}")

# Problem 2
user_input2 = input("\nEnter a phrase or write a sentence: ")
input_to_list = list(user_input2)
print(f"Output in list: {input_to_list}")

# Problem 3
user_input3 = input("\nEnter a phrase or write a sentence: ")
reversed_string = ' '.join(user_input3.split()[::-1])  # Split the string into words, reverse, and join them back
print("Output:", reversed_string)
