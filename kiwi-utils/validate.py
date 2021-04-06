def validate(dataType, questionField="", inputField="", wrongType=""):

    while True:
        
        if questionField != "":
            print(questionField)
        
        userInput = input(inputField)

        if dataType == "str":
            return userInput
        elif dataType == "int":
            try:
                userInput = int(userInput)
                return userInput
            except:
                pass
        elif dataType == "float":
            try:
                userInput = float(userInput)
                return userInput
            except:
                pass
        elif dataType == "bool":
            if userInput == "True":
                return True
            elif userInput == "False":
                return False
        else:
            raise Exception("Error: Enter a valid dataType")
        
        if wrongType != "":
            print(wrongType)