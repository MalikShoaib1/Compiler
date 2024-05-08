import re
 
class ArithmeticParser:
    def __init__(self):
        self.tokens = []
 
    def tokenize_input(self, input_str):
        # Regular expressions to match numbers, operators, and parentheses
        number_pattern = r'\d+(\.\d+)?'
        operator_pattern = r'[+\-*/]'
        parenthesis_pattern = r'[()]'
 
        # Compile regular expressions
        number_regex = re.compile(number_pattern)
        operator_regex = re.compile(operator_pattern)
        parenthesis_regex = re.compile(parenthesis_pattern)
 
        # Tokenize input string
        while input_str:
            # Skip whitespace
            if input_str[0].isspace():
                input_str = input_str[1:]
                continue
            # Match numbers
            if number_match := number_regex.match(input_str):
                self.tokens.append(('NUMBER', float(number_match.group(0))))
                input_str = input_str[number_match.end():]
                continue
            # Match operators
            if operator_match := operator_regex.match(input_str):
                self.tokens.append(('OPERATOR', operator_match.group(0)))
                input_str = input_str[1:]
                continue
            # Match parentheses
            if parenthesis_match := parenthesis_regex.match(input_str):
                self.tokens.append(('PARENTHESIS', parenthesis_match.group(0)))
                input_str = input_str[1:]
                continue
            # If none of the patterns matched, raise an error
            raise ValueError("Invalid input")
 
    def accept_input(self):
        while True:
            try:
                user_input = input("Enter an arithmetic expression: ")
                self.tokenize_input(user_input)
                break
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid arithmetic expression.")
 
        print("Input tokens:", self.tokens)
 
# Create an instance of the ArithmeticParser class
parser = ArithmeticParser()
 
# Accept input from the user and tokenize it
parser.accept_input(
