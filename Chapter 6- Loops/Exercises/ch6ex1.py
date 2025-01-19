##New Project
prompt = "\nwhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when finished:"

while True:
    topping = input (prompt)
    if topping != 'quit':
        print ("I will add " + topping  + " to your pizza")
    else :
        break