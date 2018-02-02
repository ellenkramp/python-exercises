w = int(raw_input("Choose a width "))
h = int(raw_input("Choose a height "))
mid_width = int(h - 2)
h_list = range(1,(h+1))
outer = w*"*"
middle = "*" + " "*(w-2) + "*" 
print outer
for i in h_list:
  print middle
print outer
