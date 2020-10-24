from number_generator import NumberGenerator

print("What kind of data do you need?")  # Only number by now
data_type = input()

if data_type == "number":
    number_generator = NumberGenerator()
    print("What kind of numbered data do you need?")
    number_type = input()

    if number_type == "sorted":
        try:
            print("Give me the amount")
            amount = int(input())

            print("Give me the lower_bound")
            lower_bound = int(input())

            print("Give me the upper_bound")
            upper_bound = int(input())

            print(
                number_generator.generate_sorted_random_numbers(
                    amount, lower_bound, upper_bound
                )
            )
        except Exception as e:
            print(f"Could not handle your input with error: {e}")
