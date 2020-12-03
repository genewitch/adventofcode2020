with open('input3.txt') as f:
    textlist = list(f)
    #print ( len(textlist))
    height = len(textlist)

    
def calculot(slopeRight, slopeDown, input):
    rowlength = len(input[0]) - 1
    trees = 0
    clear = 0
    cursor = 0
    vertical = 0

    while True:
        vertical = vertical + slopeDown
        if vertical >= height:
            break
        cursor = cursor + slopeRight
        #print(cursor,end='')
        if cursor >= rowlength:
            cursor = 0 + (cursor % rowlength)
            #print (" <-old : new-> ",cursor)
        #print(trees)    

        row = list(textlist[vertical])
        row.pop
        if row[cursor] == ".":
            clear = clear + 1
            #print ("O",end='')
        else:
            #print (row[cursor])
            assert row[cursor] == "#"
            trees = trees + 1
            #print ("X",end='')
    print("slope right, slope down, trees, clear: ", slopeRight, slopeDown, trees, clear)
    return trees

one = calculot(1,1,textlist)
two = calculot(3,1,textlist)
thr = calculot(5,1,textlist)
fou = calculot(7,1,textlist)
fiv = calculot(1,2,textlist)

print("product of all: ", str(one*two*thr*fou*fiv))

    