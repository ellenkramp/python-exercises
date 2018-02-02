str = raw_input("Input a string." ).upper()
leet_letters = {
    "A":"4",
    "E": "3",
    "G": "6",
    "I": "1",
    "O": "0",
    "S": "5",
    "T": "7"
}
for char in leet_letters:
     str = str.replace(char, leet_letters[char])
print str

#def multipleReplace(text, wordDict):
 #   for key in wordDict:
  #      text = text.replace(key, wordDict[key])
   # return text
      
