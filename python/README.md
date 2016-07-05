Python Questioner
=================

How to import:
from questioner import *

Functions:
    askYN(question)
        asks a yes/no question
        ex: askYN("Do you like pi?")

    askChoices(question, choices)
        asks question with choices
        can answer as the number or match the string of the choice
        ex: askChoices("What is your favorite color?", ["red", "green", "blue"])

    askChoices(question, choices, default)
        asks question with choices
        can answer as the number or match the string of the choice
        by answering with nothing, default value is used
        ex: askChoices("What is your favorite color?", ["red", "green", "blue"], "2")

    askString(question)
        asks question and returns a string of the answer
        ex: askString("What is your favorite color?")

    askInt(question)
        asks question and scrubs for int as answer
        ex: askInt("Pick a number between 1 and 10:")

    askFloat(question)
        asks question and scrubs for float as answer
        ex: askFloat("Pick a number:")
