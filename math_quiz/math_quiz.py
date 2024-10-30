import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).

    Args:
        min_value (int): The minimum value for the random integer.
        max_value (int): The maximum value for the random integer.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def select_random_operator():
    """
    Randomly select an arithmetic operator from the list of available operators.

    Returns:
        str: A randomly chosen arithmetic operator ('+', '-', '*').
    """
    return random.choice(['+', '-', '*'])

def calculate_expression(number1, number2, operator):
    """
    Calculate the result of a mathematical expression given two numbers and an operator.

    Args:
        number1 (int): The first number.
        number2 (int): The second number.
        operator (str): The arithmetic operator.

    Returns:
        tuple: A tuple containing the expression of the math operation as a string and the calculated result.
    """
    expression = f"{number1} {operator} {number2}"
    
    if operator == '+': ##sums the numbers
        result = number1 + number2 
    elif operator == '-': ## substracts the numbers
        result = number1 - number2  
    elif operator == '*': ##multiplies the numbers
        result = number1 * number2  
    else:
        raise ValueError("Invalid operator")  # Raise error for unexpected operator
    
    return expression, result

def math_quiz():
    """
    Main function to run the Math Quiz Game.

    This function presents a series of math problems to the user,
    collects user input, and evaluates the responses.
    """
    score = 0  # Initialize the user's score
    total_questions = 3  # Total number of questions to ask

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = generate_random_integer(1, 10)  # Generate first random number
        number2 = generate_random_integer(1, 5)  # Generate second random number, fixed max to be an integer
        operator = select_random_operator()  # Select a random operator

        problem, answer = calculate_expression(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = input("Your answer: ")
            user_answer = int(user_answer)  # Convert input to integer
            
            # Check if the user's answer is correct
            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1  # Increment score for a correct answer
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        
        except ValueError:  # Handle the case where input cannot be converted to an integer
            print("Invalid input. Please enter a valid integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
