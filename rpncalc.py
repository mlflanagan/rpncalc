#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import operator

operators = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.div}

while True:
    try:
        stack = []
        for token in string.split(raw_input('> ')):
            if token in operators:
                y, x = stack.pop(), stack.pop()
                z = operators[token](x, y)
            else:
                z = float(token)
            stack.append(z)
        assert len(stack) <= 1
        if len(stack) == 1:
            print(stack.pop())
    except EOFError:
        break
    except:
        print('error')
