alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

def atbash(text):
    newString = ""
    for letter in str(text):
        isUpper = False
        if (letter.lower() != letter.upper()):
            if letter == letter.upper():
                isUpper = True
                letter = letter.lower()
            letter = str(alphabet[25 - alphabet.index(letter)])
            if (isUpper):
                letter = letter.upper()
        newString += letter
    return newString

def ceaser(text, shift): # Shifts the letters in a text line to either encode (positive shift) or decode (negative shift) the message
    newString = ""
    for letter in str(text):
        if letter.upper() != letter.lower():
            if letter.islower():
                letter = alphabet[(shift + alphabet.index(letter)) % 26]
            else:
                letter = alphabet[(shift + alphabet.index(letter.lower())) % 26].upper()
        newString += letter
    return newString

def vigenere(text, key, crypt): # crypt: 1 for encode, -1 for decrypt
  keyIndex = 0
  keyLen = len(key)
  newString = ""
  for letter in str(text):
    if letter.upper() != letter.lower():
      if letter.islower():
        letter = alphabet[(alphabet.index(letter) + crypt*alphabet.index(key[keyIndex])) % 26]
      else:
        letter = alphabet[(alphabet.index(letter.lower()) + crypt*alphabet.index(key[keyIndex])) % 26].upper()
      keyIndex = (keyIndex + 1) % keyLen
    newString += letter
  return newString

result = "Jonisafool"
key = "robotics"
for index in range(1):
  result = vigenere(result, key.lower(), 1)
print(result)
            
# text = "moab"
# for index in range(26):
#     print("Ceaser (Shift = " + str(index) + "): " + ceaser(text, -index))
# print("\nAtbash: " + atbash(text) + "\n")
