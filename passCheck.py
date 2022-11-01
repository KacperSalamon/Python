import string

password = "python"

#password = input("Enter your password") -- in that case we can add our password, but in cmd not in VSC :)

upperCase = any([1 if c in string.ascii_uppercase else 0 for c in password])
lowerCase = any([1 if c in string.ascii_lowercase else 0 for c in password])
specialCharacters = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

allCharacters = [upperCase, lowerCase, specialCharacters, digits]

lengthPass = len(password)

score = 0

with open("manypass.txt", "r") as f:
    common = f.read().splitlines()

if password in common:
    print("Your password can be weak... :(")
    exit()

if lengthPass > 10 :
    score += 1
if lengthPass > 15:
    score += 1
if lengthPass > 20:
    score += 1

print(f"Password length is {str(lengthPass)}, so it add {str(score)}")

if sum(allCharacters) > 1:
    score += 1
if sum(allCharacters) > 2:
    score += 1

print(f"Password has {str(sum(allCharacters))} various char types, so it add {str(sum(allCharacters) - 1)} point's ")

if score < 3 :
    print(f"Your password is too weak. Please try again. Your score = {str(score)}")
elif score == 3:
    print(f"Your password is fine. Your score = {str(score)}")
elif score > 3 and score < 5 :
    print(f"Your password is pretty goood. Your score = {str(score)}")
elif score > 5:
    print(f"Your password is strong. Your score = {str(score)}")
    

