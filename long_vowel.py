vowels = "a, e, i, o, u"

input = raw_input("Type a word. ")
length = len(input)
new_word = ""

for i in range(0,(length)):
    if i < (length - 1):
        if input[i] == input[i+1]:
          new_word = new_word + (input[i]*4)
        else:
          new_word = new_word + input[i]
    elif i == (length - 1):
          new_word = new_word + input[i]
print new_word
