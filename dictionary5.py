sentence_input = raw_input("Type a sentence. ")
word_count = {

}
sentence_arr = sentence_input.split(" ")

for word in sentence_arr:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
         word_count[word] = 1
print word_count
