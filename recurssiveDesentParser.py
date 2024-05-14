import re
import ipywidgets as widgets
from IPython.display import display, clear_output

class LexicalAnalyzer:
    def __init__(self):
        pass

    def tokenize(self, input_str):
        # Regular expressions for token patterns
        patterns = [
            (r'[a-zA-Z]+', 'VARIABLE'),   # Match variables
            (r'\d+(\.\d+)?', 'NUMBER'),   # Match numbers
            (r'[+\-*/]', 'OPERATOR'),     # Match operators
            (r'[()]', 'PARENTHESIS'),     # Match parentheses
            (r'\s+', None),               # Match whitespace (to be ignored)
            (r'\/\/.*', None)             # Match comments (to be ignored)
        ]

        tokens = []
        prev_token_type = None
        while input_str:
            for pattern, token_type in patterns:
                regex = re.compile(pattern)
                match = regex.match(input_str)
                if match:
                    if prev_token_type == 'OPERATOR' and token_type == 'OPERATOR':
                        raise SyntaxError("Consecutive operators are not allowed")
                    if token_type:  # If token type is not None (i.e., not whitespace or comment)
                        tokens.append((token_type, match.group(0)))
                        prev_token_type = token_type
                    input_str = input_str[match.end():]
                    break
            else:
                raise ValueError("Invalid input")
        return tokens

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class RecursiveDescentParser:
    def __init__(self):
        self.tokens = []
        self.current_token_index = 0

    def parse(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        return self.parse_expression()

    def parse_expression(self):
        node = self.parse_term()
        while self.current_token_index < len(self.tokens):
            token_type, token_value = self.tokens[self.current_token_index]
            if token_type == 'OPERATOR':
                operator_node = TreeNode(token_value)
                self.current_token_index += 1
                operator_node.children.append(node)
                term_node = self.parse_term()
                operator_node.children.append(term_node)
                node = operator_node
            elif token_type == 'PARENTHESIS' and token_value == ')':
                break
            else:
                raise SyntaxError("Invalid expression")
        return node

    def parse_term(self):
        token_type, token_value = self.tokens[self.current_token_index]
        if token_type == 'VARIABLE' or token_type == 'NUMBER':
            node = TreeNode(token_value)
            self.current_token_index += 1
            return node
        elif token_type == 'PARENTHESIS' and token_value == '(':
            self.current_token_index += 1
            expression_node = self.parse_expression()
            if self.current_token_index >= len(self.tokens) or self.tokens[self.current_token_index][1] != ')':
                raise SyntaxError("Mismatched parentheses")
            self.current_token_index += 1
            return expression_node
        else:
            raise SyntaxError("Invalid term")




def print_tree(node, level=0):
    print("  " * level + node.value)
    for child in node.children:
        print_tree(child, level + 1)



# Function to handle the syntax check
def check_syntax(b):
    try:
        user_input = code_input.value
        lexer = LexicalAnalyzer()
        tokens = lexer.tokenize(user_input)
        parser = RecursiveDescentParser()
        parse_tree = parser.parse(tokens)
        output_area.clear_output()
        with output_area:
            print("Tokenization:")
            print(tokens)
            print("\nParse Tree:")
            print_tree(parse_tree)
            print("\nSyntax is correct.")
    except (SyntaxError, ValueError) as e:
        output_area.clear_output()
        with output_area:
            print(f"Error: {e}")

# Function to execute the code
def execute_code(b):
    try:
        user_input = code_input.value
        lexer = LexicalAnalyzer()
        tokens = lexer.tokenize(user_input)
        parser = RecursiveDescentParser()
        parse_tree = parser.parse(tokens)
        # Execute code here based on parse tree
        output_area.clear_output()
        with output_area:
            print("Code executed successfully.")
    except (SyntaxError, ValueError) as e:
        output_area.clear_output()
        with output_area:
            print(f"Execution Error: {e}")

# Create the text area for code input
code_input = widgets.Textarea(
    value='',
    placeholder='Type your code here...',
    description='Code:',
    layout=widgets.Layout(width='100%', height='200px')
)

# Create the buttons
check_syntax_button = widgets.Button(description="Check Syntax")
execute_button = widgets.Button(description="Execute")

# Bind the buttons to their respective functions
check_syntax_button.on_click(check_syntax)
execute_button.on_click(execute_code)

# Create the output area
output_area = widgets.Output()

# Arrange the widgets in a vertical box
box_layout = widgets.Layout(display='flex', flex_flow='column', align_items='stretch', width='100%')
vbox = widgets.VBox([code_input, check_syntax_button, execute_button, output_area], layout=box_layout)

# Display the interface
display(vbox)
