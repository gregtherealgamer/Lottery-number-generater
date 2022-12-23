import random

# Set the number of lottery numbers to generate
num_lottery_numbers = 6

# Set the range of numbers to choose from (in this case, 1 to 49)
lottery_range = range(1, 50)

# Generate the lottery numbers
lottery_numbers = random.sample(lottery_range, num_lottery_numbers)

# Print the lottery numbers
print(lottery_numbers)
