class Flames:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        self.relationships = {
            "F": "Friendship",
            "L": "Love",
            "A": "Affection",
            "M": "Marriage",
            "E": "Enemy",
            "S": "Sibling"
        }

    def get_flames_count(self):
        # Normalize names: lowercase and remove spaces
        name1 = self.name1.lower().replace(" ", "")
        name2 = self.name2.lower().replace(" ", "")

        # Remove common characters
        for char in name1[:]:
            if char in name2:
                name1 = name1.replace(char, "", 1)
                name2 = name2.replace(char, "", 1)

        # Store remaining characters for breakdown
        self.name1_remaining = name1
        self.name2_remaining = name2

        # Calculate the total count of remaining characters
        return len(name1) + len(name2)

    def get_flames_result(self, total_count):
        # Handle the case where total_count is 0
        if total_count == 0:
            return "Not compatible! Single forever </3"

        flames = list("FLAMES")
        index = 0

        # Circularly count and eliminate letters
        while len(flames) > 1:
            index = (index + total_count - 1) % len(flames)
            flames.pop(index)

        # Return the result based on the final letter
        return self.relationships[flames[0]]

    def calculate_and_print(self):
        # Get the flames count
        flames_count = self.get_flames_count()

        # Get the result of FLAMES
        result = self.get_flames_result(flames_count)

        # Prepare detailed breakdown
        name1_length = len(self.name1_remaining)
        name2_length = len(self.name2_remaining)

        # Print the result
        print("---------------------------------")
        print(f"Your name                    : {self.name1}\n"
              f"Partner name                 : {self.name2}\n"
              f"Your name remaining          : {self.name1_remaining}\n"
              f"Crush name remaining         : {self.name2_remaining}\n"
              f"Count remaining [your name]  : {name1_length}\n"
              f"Count remaining [crush]      : {name2_length}\n"
              f"Sum                          : {flames_count}\n"
              f"Relationship                 : {result}")
        print("---------------------------------")

while True:
    user_name = input("\nYour name: ")
    crush_name = input("Crush name: ")

    flames = Flames(user_name, crush_name)
    flames.calculate_and_print()

    try_again = int(input("Do you want to try again? Press 1 for Yes. "))

    if not try_again == 1:
        break