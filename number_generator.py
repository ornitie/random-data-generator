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

    def generate_n_unique_numbers(
        self, amount: int, lower_range: int, upper_range: int
    ):
        visited = {}
        counter = 0

        while counter < amount:
            num = self.generate_random_number(lower_range, upper_range)
            if visited.get(num) != None:
                continue
            visited[num] = 1
            counter += 1

        return sorted(visited.keys())

    def generate_sorted_random_numbers(
        self, amount: int, lower_range: int, upper_range: int, unique: bool = True
    ):
        if amount > (upper_range - lower_range):
            raise ValueError(
                f"Amount {amount} cannot be bigger than the range of numbers"
            )

        return (
            sorted(self.generate_n_unique_numbers(amount, lower_range, upper_range))
            if unique
            else sorted(self.generate_n_between_range(amount, lower_range, upper_range))
        )
