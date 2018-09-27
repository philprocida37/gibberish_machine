#########################################################
#                    By Phil Procida                    #
#########################################################
import random, enchant

wordSuggest = enchant.Dict("en_US")

consList = ['q','w','r','t','y',
            'p','s','d','f','g',
            'h','j','k','l','z',
            'x','c','v','b','n',
            'm']
vowelList = ['a','e','i','o','u']

originalString = list(input("Enter some text: "))

def randomChars(uInput):
    stepThru = 0
    while stepThru < len(uInput):
        for x in range(len(uInput)):
            if uInput[x] == ' ':
                stepThru += 1
            elif uInput[x] in vowelList:
                randomAssignChar = random.choice(consList)
                uInput[x] = randomAssignChar
                stepThru += 1
            elif uInput[x] in consList:
                randomAssignChar = random.choice(vowelList)
                uInput[x] = randomAssignChar
                stepThru += 1
            else:
                stepThru += 1
    removeExtra = 0
    while removeExtra < len(uInput):
        newString = ''
        for x in range(len(uInput)):
            newString = newString + uInput[x]
            removeExtra += 1
    return newString

randomCharString = randomChars(originalString)

def breakString(uInput):
    randomCharString = uInput.split()
    stepThru = 0
    newWordList = ''
    while stepThru < len(randomCharString):
        for x in range(len(randomCharString)):
            newWord = wordSuggest.suggest(randomCharString[x])
            if stepThru == 0:
                newWordList = newWord[0]
                stepThru+= 1
            else:
                newWordList = newWordList + ' ' + newWord[0]
                stepThru += 1
    return newWordList

try:
    finalString = breakString(randomCharString)
    print("Randomly rolled string(s): " + str(randomCharString))
    print("New output(s): " + str(finalString))
except IndexError:
    print("PyEnchant could not find words similar to all of the rolled strings. Please try again.")
