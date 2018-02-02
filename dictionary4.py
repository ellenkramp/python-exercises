histogram = {
    
}

user_input = raw_input("Please enter a word: ")

for letter in user_input:
  if letter in histogram:
    histogram[letter] = histogram[letter] +1
  else:
    histogram[letter] = 1      

print histogram