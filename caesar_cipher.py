# nopqrstuvwxyzabcdefghijklm
dict = {
    "a" : "n",
    "b" : "o",
    "c" : "p",
    "d" : "q",
    "e" : "r",
    "f" : "s",
    "g" : "t",
    "h" : "u",
    "i" : "v",
    "j" : "w",
    "k" : "x",
    "l" : "y",
    "m" : "z",
    "n" : "a",
    "o" : "b",
    "p" : "c",
    "q" : "d",
    "r" : "e",
    "s" : "f",
    "t" : "g",
    "u" : "h",
    "v" : "i",
    "w" : "j",
    "x" : "k",
    "y" : "l",
    "z" : "m"
}
str = (raw_input("Please type a string. ")).lower()
newstr = ""
for char in str:
    if char.isalpha():
        newstr = newstr + dict[char]
    else:
        newstr = newstr + char
print newstr