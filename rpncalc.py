#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RPN calculator
Python 3
"""

import operator

operators = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}

while True:
    try:
        stack = []
        for token in (input('> ').split()):
            if token in operators:
                y, x = stack.pop(), stack.pop()
                z = operators[token](x, y)
            else:
                z = float(token)
            stack.append(z)
        assert len(stack) <= 1
        if len(stack) == 1:
            print(stack.pop())
    except (EOFError, InterruptedError):
        print("Goodbye")
        break
