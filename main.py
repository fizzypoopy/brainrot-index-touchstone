#The Roblox game 'My Fishing Brainrot' consists of various purchaseable brainrots with varying profits 
#User can choose to input a new brainrot entry to be sorted by rank against other brainrots or by name
#User can also choose to view already inputted entries by rank or by name

import ast

#Main function, the point of entry
def promptUser():
    
    #Initiates a false input, until a valid input is received from the user
    validInput = False
    #Loops while there isn't a valid input
    while validInput == False:
        userInput = input("If you would like to"
            + "\n1. View current brainrot by rank. Enter: 'view_by_rank'"
            + "\n2. View current brainrot by name. Enter: 'view_by_name'"
            + "\n3. Add a new brainrot. Enter: 'add_brainrot'"
            + "\nYour Input: ")
        
        #Checks for these specific user inputs to be valid
        if userInput == 'view_by_rank':
            rankView()
            validInput = True
        elif userInput == 'view_by_name':
            nameView()
            validInput = True
        elif userInput == 'add_brainrot':
            updateBrainrotDict()
            validInput = True
        
        #Checks if input is valid to display the user's choice or else display that the user has to try again
        if validInput == True:
            print('Processed Input: ' + userInput)
        else:
            print('Invalid input. Try again.\n')

#Checks if string inputted is valid
def checkStr(prompt):
    #Keep looping the prompt until a valid input can be returned, or else let the user know that their input is invalid
    while True:
        try:
            #Removes any empty spaces before or after input and capitalizes input
            user_input = input(prompt).strip().capitalize()
            #Checks if input is valid, or else let the user know that their input is invalid
            if user_input:
                return user_input
            else:
                print('Invalid input. Cannot be empty. Try again.\n')
        except:
            print('Invalid input. Try again.\n')

#Checks if number inputted is valid
def checkInt(prompt):
    #Keep looping the prompt until a valid input can be returned or else let the user know that their input is invalid
    while True: 
        try: 
            #Ensures that input is an integer
            user_input = int(input(prompt))
            #Checks if input is an invalid zero, or else return their valid input
            if user_input == 0:
                print('Invalid input. Cannot be zero. Try again.\n')
            else:
                return user_input
        except ValueError:
            print('Invalid input. Only numbers accepted (no letters or decimals). Try again.\n')


brainrotDict = {}
#Runs the add_brainrot option and displays user input
def updateBrainrotDict():
    #Prompt user to enter information for their brainrot entry
    updateName = checkStr("Enter brainrot name: ")
    updateCategory = checkStr("Enter brainrot category: ")
    updateType = checkStr("Enter brainrot type(s): ")
    
    updateCost = checkInt("Enter brainrot cost: ")
    updateProfit = checkInt("Enter brainrot profit: ")
    updateProfitSecs = checkInt("Enter profit speed in seconds: ")
    
    #Calculations for each of the numbers inputted from the prompts
    calcProfitPerSec = updateProfit/updateProfitSecs
    calcRepayCostEstimate = updateCost/(updateProfit/updateProfitSecs)
    calcHr24Profit = (calcProfitPerSec * 86000) - updateCost
    
    #Updates the brainrotDict dictionary
    brainrotDict.update({'entry' : 
        {
        'name' : updateName,
        'category' : updateCategory,
        'type' : updateType,
        'cost' : updateCost,
        'profit' : updateProfit,
        'profitSecs' : updateProfitSecs,
        'profitPerSec' : calcProfitPerSec,
        'repayCostEstimate' : calcRepayCostEstimate,
        'hr24Profit' : calcHr24Profit,
        }
    })
    
    #Open file to append the newly entered brainrot information
    fout = open('updatedRank.txt', 'a')
    for values in brainrotDict.values():
        fout.write(str(values) + '\n')
    fout.close()
    
    #Open file to read and pull out saved brainrot entries
    #Initializes a dictionary for lines from text file
    data_r = {}
    #Opens file, loops through each line to store it's information in the initialized dictionary
    fin = open('updatedRank.txt', 'r')
    for values in fin:
        data_r[len(data_r) + 1] = ast.literal_eval(values)
    fin.close()
    
    print('User Input: ' + str(brainrotDict))

    #Sorts brainrot entries by rank, based on their profit after 24 hours (considering cost debt)
    rankedBrainrots = dict(sorted(data_r.items(), key=lambda item: item[1]['hr24Profit'], reverse=True))
    #Open file to write newly sorted information into the ranking file, overwriting old information
    fout = open('updatedRank.txt', 'w')
    for values in rankedBrainrots.values():
        fout.write(str(values) + '\n')
    fout.close()

    #Sorts brainrot entries by name, type, and category in alphabetical order
    nameSorted = dict(sorted(rankedBrainrots.items(), key=lambda item: (item[1]['name'], item[1]['category'], item[1]['type'])))
    #Open file to write newly sorted information into the naming file, overwriting old information
    fout = open('updatedName.txt', 'w')
    for values in nameSorted.values():
        fout.write(str(values) + '\n')
    fout.close()


#Runs the view_by_rank option, displays the brainrot entries ranked by their profit after 24 hours (considered cost debt)
def rankView():
    print('Displaying Rank View')

    #Initializes a dictionary for lines from text file
    data_r = {}
    #Opens file, loops through each line to store it's information in the initialized dictionary
    fin = open('updatedRank.txt', 'r')
    for values in fin:
        data_r[len(data_r) + 1] = ast.literal_eval(values)
    fin.close()

    #Loops through the dictionary to display each entry line-by-line
    for key, value in data_r.items():
        print(f"{key}: {value}")


#Runs the view_by_name option, displays the brainrot entries sorted by name, type, and category in alphabetical order
def nameView():
    print('Displaying Name View')
    
    #Initializes a dictionary for lines from text file
    data_r = {}
    #Opens file, loops through each line to store it's information in the initialized dictionary
    fin = open('updatedName.txt', 'r')
    for values in fin:
        data_r[len(data_r) + 1] = ast.literal_eval(values)
    fin.close()

    #Loops through the dictionary to display each entry line-by-line
    for key, value in data_r.items():
        print(f"{key}: {value}")


promptUser()
