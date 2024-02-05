# Read the input.txt file
def read_input(filename):
    with open(filename, 'r') as file:
        # Initialize the total score variable
        total_score = 0
        # Iterate over each line in the file
        for line in file:
            # Split the line into opponent choice and desired outcome
            opponent_choice, desired_outcome = line.strip().split()
            # Calculate the score for the current round
            score = calculate_score(opponent_choice, desired_outcome)
            # Accumulate the score to the total score
            total_score += score
        # Return the calculated total score
        return total_score

# Solution function to calculate the score for a round
def calculate_score(opponent_choice, desired_outcome):
    # Define the score for each choice
    choices = {'A': 1, 'B': 2, 'C': 3}

    # Decide what to play based on the desired outcome
    if desired_outcome == 'X':  # You need to lose
        if opponent_choice == 'A':
            your_choice = 'C'  # Play Scissors
        elif opponent_choice == 'B':
            your_choice = 'A'  # Play Rock
        else:
            your_choice = 'B'  # Play Paper
    elif desired_outcome == 'Y':  # You need to draw
        your_choice = opponent_choice  # Choose the same as the opponent to draw
    else:  # You need to win
        if opponent_choice == 'A':
            your_choice = 'B'  # Play Paper
        elif opponent_choice == 'B':
            your_choice = 'C'  # Play Scissors
        else:
            your_choice = 'A'  # Play Rock

    # Calculate the score for the round
    score = choices[your_choice]

    # Add the outcome to the score
    if desired_outcome == 'X':
        score += 0
    elif desired_outcome == 'Y':
        score += 3
    else:
        score += 6

    # Return the calculated score for the round
    return score

# Other parts of code here to run your functions and printing of the input.
# Specify the input file path
input_file_path = r"C:\Users\DELL\Downloads\input_4_cap1.txt"
# Call the read_input function to get the total score
total_score = read_input(input_file_path)
# Print the total score
print(f'The total score is: {total_score}')
