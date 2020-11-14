import sys

assert ('linux' in sys.platform), "This code runs on Linux only."

#_________________________________________________________ v.1

import sys

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
except:
    print('Linux function was not executed')

#_________________________________________________________ v.2

import sys

# def linux_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     print('Doing something.')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('The linux_interaction() function was not executed')

#_________________________________________________________ v.3

import sys

# def linux_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     print('Doing something.')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')

#_________________________________________________________ v.4

import sys

# def linux_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     print('Doing something.')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
