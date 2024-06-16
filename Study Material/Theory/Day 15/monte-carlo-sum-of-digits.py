'''
Design a simple game:

Choose a number between 1 and 100.
If the sum of the digits of your chosen number exceeds 12, you win 3 dollars.
If the sum falls below the threshold, you lose 1 dollar.
The game will be repeated 1000 times to simulate a large number of trials.

'''
import random

# Initialize variables
total_winnings = 0
total_losses = 0

# Simulate 1000 trials
for _ in range(1000):
 # Choose a random number between 1 and 100
 chosen_number = random.randint(1, 100)

 # Calculate the sum of digits
 digit_sum = sum(int(digit) for digit in str(chosen_number))

 # Check if win or loss
 if digit_sum > 12:
   total_winnings += 3
 else:
   total_losses += 1

# Calculate net winnings/losses
net_result = total_winnings - total_losses

# Print the results
print(f"Total winnings: ${total_winnings}")
print(f"Total losses: ${total_losses}")
print(f"Net result: ${net_result}")
