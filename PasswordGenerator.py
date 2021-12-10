import string, random


def generatePassword(totalLength):
    global password, special_chars
    
    password = []

    special_chars = "@#$%&_?"
    uppercaseAmount = random.randrange(2, 6)
    randomNumAmount = random.randrange(4, 7)
    lowercaseAmount = totalLength - (uppercaseAmount + randomNumAmount + 3)

    password += (random.choices(string.ascii_uppercase, k = uppercaseAmount)) # Add the uppercase characters
    password += (random.choices(string.digits, k = randomNumAmount)) # Add the numbers
    password += (random.choices(string.ascii_lowercase, k = lowercaseAmount)) # Add the lowercase characters
    password += (random.choices(special_chars, k = 3)) # Add the special characters
    random.shuffle(password)
    firstThree()

def firstThree():
    for character in password[:3]:
        if character.isnumeric():
            generatePassword(24)
    else:
        specialChars()

def specialChars():
    if password[0] in special_chars and password[-1] in special_chars:
        generatePassword(24)
    else:
        print(*password, sep = "")

generatePassword(24)