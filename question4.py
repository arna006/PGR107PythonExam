alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","æ","ø","å",)
match = []
unique = []
unused = []

def comparison(stringOne, stringTwo):
    for char1 in stringOne:
        for char2 in stringTwo: 
            if char1 == char2:
                if char1 not in match:
                    match.append(char1)
                    break
                else:
                    break
    return match
        
                
def uniqueCharacters(stringOne, stringTwo):
    for char in stringOne:
        if char not in match and char not in unique:
            unique.append(char)
    for char in stringTwo:
        if char not in match and char not in unique:
            unique.append(char)
    return unique
    

def unusedCharacters(stringOne,stringTwo):
    for char in alphabet:
        if char not in stringOne and char not in stringTwo:
            unused.append(char)
    return unused

stringOne = input("Enter a word ")
stringTwo = input("Enter a second word ")


comparison(stringOne,stringTwo)
uniqueCharacters(stringOne, stringTwo)
unusedCharacters(stringOne,stringTwo)

print(f"lets compare your strings \nfirst word {stringOne}\nSecond word {stringTwo}\n same letters: {', '.join(match)}\nUnique letters: {', '.join(unique)}\nUnused characters: {', '.join(unused)}")
