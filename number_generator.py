import random


class NumberGenerator:
    def generate_random_number(self, lower_range: int, upper_range: int):
        try:
            random_number = random.randint(lower_range, upper_range)

            return random_number
        except ValueError:
            print(f"Values {lower_range} and {upper_range} are invalid")
