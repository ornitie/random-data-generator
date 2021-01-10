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

    def generate_sorted_random_numbers(
        self, amount: int, lower_range: int, upper_range: int
    ):
        if amount > (upper_range - lower_range):
            raise ValueError(
                f"Amount {amount} cannot be bigger than the range of numbers"
            )

        floor = lower_range
        sorted_nums = []
        for i in range(amount, 0, -1):
            floor = self.generate_random_number(floor + 1, upper_range - i)
            sorted_nums.append(floor)

        return sorted_nums
