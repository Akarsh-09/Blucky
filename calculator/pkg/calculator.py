# calculator/pkg/calculator.py

import math
import re

class Calculator:
    def __init__(self):
        # Binary operators: (precedence, function)
        self.operators = {
            "+": (1, lambda a, b: a + b),
            "-": (1, lambda a, b: a - b),
            "*": (2, lambda a, b: a * b),
            "/": (2, lambda a, b: a / b),
            "^": (3, lambda a, b: a ** b),
        }
        # Unary operators: (precedence, function)
        self.unary_operators = {
            "sin": (4, lambda a: math.sin(math.radians(a))),
            "cos": (4, lambda a: math.cos(math.radians(a))),
            "tan": (4, lambda a: math.tan(math.radians(a))),
            "log": (4, lambda a: math.log10(a)),
            "ln": (4, lambda a: math.log(a)),
            "sqrt": (4, lambda a: math.sqrt(a)),
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        
        # Tokenize expression
        tokens = re.findall(r'\d*\.\d+|\d+|[a-zA-Z]+|[+\-*/^()]', expression)
        
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        for token in tokens:
            if token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    self._apply_operator(operators, values)
                if not operators:
                    raise ValueError("mismatched parentheses")
                operators.pop() # remove '('
            elif token in self.unary_operators:
                # Unary operators are prefix and have high precedence
                operators.append(token)
            elif token in self.operators:
                while (operators and operators[-1] != '(' and 
                       (operators[-1] in self.unary_operators or 
                        (operators[-1] in self.operators and self.operators[operators[-1]][0] >= self.operators[token][0]))):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            if operators[-1] == '(':
                raise ValueError("mismatched parentheses")
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return
            
        operator = operators.pop()
        if operator in self.unary_operators:
            if len(values) < 1:
                raise ValueError(f"not enough operands for unary operator {operator}")
            val = values.pop()
            values.append(self.unary_operators[operator][1](val))
        elif operator in self.operators:
            if len(values) < 2:
                raise ValueError(f"not enough operands for binary operator {operator}")
            b = values.pop()
            a = values.pop()
            values.append(self.operators[operator][1](a, b))
        else:
            raise ValueError(f"unknown operator {operator}")
