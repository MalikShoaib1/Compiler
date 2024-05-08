import re

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

# Example usage:
user_input = input("Enter an arithmetic expression: ")

# Tokenization
lexer = LexicalAnalyzer()
tokens = lexer.tokenize(user_input)
print("Tokenization:")
print(tokens)

# Lexical Analysis
print("\nLexical Analysis:")
for token in tokens:
    print(token)

# Parsing using Recursive Descent and constructing parse tree
print("\nParse Tree (Recursive Descent Parsing):")
parser_recursive = RecursiveDescentParser()
parse_tree_recursive = parser_recursive.parse(tokens)
print_tree(parse_tree_recursive)
