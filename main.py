import enum
from tracemalloc import start


alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

# --- Atbash Cipher ---

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


# --- Caeser Cipher ---

def caeser(text, shift): # Shifts the letters in a text line to either encode (positive shift) or decode (negative shift) the message
    newString = ""
    for letter in str(text):
        if letter.upper() != letter.lower():
            if letter.islower():
                letter = alphabet[(shift + alphabet.index(letter)) % 26]
            else:
                letter = alphabet[(shift + alphabet.index(letter.lower())) % 26].upper()
        newString += letter
    return newString


# --- Vigenere Cipher ---

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

# --- Playfair Cipher ---

def generateKey(key):
  grid = [[0 for i in range(5)] for j in range(5)]
  if key != "":
    key = ''.join([j for i, j in enumerate(key) if j not in key[:i]]).replace('j', 'i').lower()
    for letter in alphabet:
      if letter not in key and letter != 'j': key += letter
  else: key = ''.join(alphabet.remove('j')) # Make the grid
  index = -1
  for col in range(5):
    for row in range(5):
      index = index + 1
      grid[col][row] = key[index]
  return grid

def search(key, a, b, pos):
  for col in range(5):
    for row in range(5):
      if key[col][row] == a:
        pos[0] = col
        pos[1] = row
      elif key[col][row] == b:
        pos[2] = col
        pos[3] = row


def playfair(text, key, crypt): # 1 for encrypt, -1 for decipher
  text = ''.join([i for i in text if i.isalpha()]).lower().replace("j", "i")
  if crypt == 1:
    ind = len(text)
    for index in range(len(text)-1, 0, -1):
      if text[index] == text[index-1]:
        text = text[:index] + "x" + text[index:]
        ind = ind + 1
  if len(text) % 2 != 0: return "Number of letters in text must be even (Add filler letters such as \"z\" or \"x\")"
  newString = ""
  pos = [0 for i in range(4)]
  key = generateKey(key)
  for ind in range(1, len(text), 2):
    a = text[ind-1] 
    b = text[ind]
    search(key, a, b, pos)
    if pos[0] == pos[2]:
      a = key[pos[0]][(pos[1]+crypt) % 5]
      b = key[pos[2]][(pos[3]+crypt) % 5]
    elif pos[1] == pos[3]:
      a = key[(pos[0]+crypt) % 5][pos[1]]
      b = key[(pos[2]+crypt) % 5][pos[3]]
    else:
      a = key[pos[0]][pos[3]]
      b = key[pos[2]][pos[1]]
    newString += a + "" + b
  return (f"\nOriginal Text: {text}\nCiphered Code: {newString.upper()}\n")
    
print(playfair("crashthemarketonfriday", "capitalism", 1))
