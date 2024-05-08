**Arithmetic Expression Parser**

This Python project provides functionality to tokenize and parse arithmetic expressions entered by the user. It supports both lexical analysis and parsing using two different algorithms: Recursive Descent and LR(1).

**Features:**

- Tokenization of arithmetic expressions  
- Lexical analysis to identify variables, numbers, operators, and parentheses  
- Parsing of arithmetic expressions using Recursive Descent algorithm  
- Constructing parse tree to represent the structure of the expression  
- Error handling for invalid input and mismatched parentheses  

**How it Works?**

1. **Tokenization:** The input arithmetic expression is tokenized using a Lexical Analyzer. This process identifies variables, numbers, operators, and parentheses in the input string.

2. **Lexical Analysis:** The tokens generated during tokenization are then analyzed to ensure they follow the grammar rules. Consecutive operators are not allowed, and comments and whitespace are ignored.

3. **Parsing:** The parsed tokens are fed into a Parser, which constructs a parse tree using a Recursive Descent algorithm. The parse tree represents the hierarchical structure of the arithmetic expression.

**Usage**

1. **Tokenization:**
    ```python
    lexer = LexicalAnalyzer()
    tokens = lexer.tokenize("3.14 + (4 * 5)")
    print(tokens)
    ```

2. **Lexical Analysis:**
    ```python
    for token in tokens:
        print(token)
    ```

3. **Parsing using Recursive Descent:**
    ```python
    parser = RecursiveDescentParser()
    parse_tree = parser.parse(tokens)
    print_tree(parse_tree)
    ```

**Requirements**

- Python 3.x
- re module (for regular expressions)
