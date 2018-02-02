height = int(raw_input("What height should the triangle be? "))
width = (height*2)-1

for i in range(1, width, 2):
    stars = i*"*"
    space = ((width - i)/2)*" "
    print space + stars
    
