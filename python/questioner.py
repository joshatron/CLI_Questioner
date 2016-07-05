def askYN(question):
    while(True):
        yn = input(question + " ").lower()
        if(yn == "y" or yn == "ye" or yn == "yes" or yn == "yeah"):
            return True
        elif(yn == "n" or yn == "no" or yn == "nope"):
            return False
        else:
            print("Please answer yes or no.")

def askChoices(question, choices, default=""):
    print(question)
    for i in range(1, len(choices) + 1):
        print(str(i) + ": " + choices[i-1])
    while(True):
        if(default == ""):
            answer = input("choice: ")
        else:
            answer = input("choice [" + default + "]: ")
            if(answer == ""):
                answer = default
        try:
            final = int(answer)
            if(final > 0 and final < len(choices) + 1):
                return final - 1
            print("Please enter valid choice.")
        except ValueError:
            for k in range(len(choices)):
                if(answer.lower() == choices[k].lower()):
                    return k
            print("Please enter valid choice.")

def askString(question):
    return input(question + " ")

def askInt(question):
    while(True):
        answer = input(question + " ")
        try:
            return int(answer)
        except ValueError:
            print("Please answer as an integer.")

def askFloat(question):
    while(True):
        answer = input(question + " ")
        try:
            return float(answer)
        except ValueError:
            print("Please answer as a number.")
