import wordList

allowed_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def checker(black, yellow, green):
    if not black and not yellow and green == ".....":
        return wordList.wordList
    if not set(black).issubset(allowed_char):
        return "Black tiles contain invalid character" # Black tiles contain invalid character
    if not set(yellow).issubset(allowed_char):
        return "Yellow tiles contain invalid character" # Yellow tiles contain invalid character
    for i in green:
        if i != '.' and i not in allowed_char:
            return "Green tiles contain invalid character" # Yellow tiles contain invalid character
    if len(green) != 5:
        return "Greentiles length is different from 5" # Greentiles length is different from 5
    if '.' not in green:
        return "Greentiles do not contain dot ('.'), perhaps you already solved the word??"
        # Greentiles do not contain dot ('.'), perhaps you already solved the word??
    return None

def solver(black, yellow, green):
    # Shrink 1
    validList = []
    for i in wordList.wordList:
        for j in black:
            if j in i: 
                break
            if j is black[-1]:
                validList.append(i) if i not in validList else None
    
    print("First shrink", validList)

    
    for i in green:
        if i != '.':
            yellow.append(i) if i not in yellow else None

    # Shrink 2
    validList_s2 = []
    for i in validList:
        for j in yellow:
            if j not in i:
                break
            if j is yellow[-1]:
                validList_s2.append(i) if i not in validList_s2 else None

    print("Second shrink", validList_s2)

    # Shrink 3
    if green == ".....":
        print("Results: ", validList_s2)
        return 

    validList_s3 = []
    for i in validList_s2:
        for j in range(5):
            if green[j] == '.':
                continue
            else:
                if i[j] != green[j]:
                    break # Stop evaluate that word in the shrank word list
                continue
        if j == 4:
            validList_s3.append(i)

    print("Results: ", validList_s3)
            
# Driver code
if __name__ == '__main__':
    black = list(set(input("Black tiles: ").lower()))

    yellow = list(set(input("Yellow tiles: ").lower()))

    green = input("Green tiles, input example is : A..VE --> AboVE: \n").lower()

    solver(black, yellow, green) if not checker(black, yellow, green) else print(checker(black, yellow, green))