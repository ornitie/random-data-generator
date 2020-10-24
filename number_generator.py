import random


class NumberGenerator:
    def generate_random_number(self, lower_range: int, upper_range: int):
        try:
            random_number = random.randint(lower_range, upper_range)

            return random_number
        except ValueError:
            print(f"Values {lower_range} and {upper_range} are invalid")

    def generate_n_between_range(self, amount: int, lower_range: int, upper_range: int):
        return [
            self.generate_random_number(lower_range, upper_range) for _ in range(amount)
        ]
