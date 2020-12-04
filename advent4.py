with open('input4.txt') as f:
    textlist = list(f)
    possibleFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    lineNumber = 0 
    part1Valid = 0
    invalid = 0
    part2Valid = 0

for line in textlist:
    lineNumber = lineNumber + 1
    docFields = [x for x in possibleFields if x in line]
    #print (docFields, len(docFields))
    if (len(docFields) == 7 and possibleFields[7] not in docFields) or len(docFields) == 8:
        part1Valid = part1Valid + 1
        checksum = 0
        flag = False
        #print (line)
        
        for field in line.split(" "):
            #print(field)
            field,value = field.split(":")
            if chr(10) in str(value):
                #print("stripping backslash n")
                value = value[:-1]
            #print(field,value)
            checksum += (field == possibleFields[0] and int(value) >= 1920 and int(value) <= 2002) 
            checksum += (field == possibleFields[1] and int(value) >= 2010 and int(value) <= 2020) 
            checksum += (field == possibleFields[2] and int(value) >= 2020 and int(value) <= 2030) 
            if field == possibleFields[3]:
                #print(field,value)
                if "cm" == str(value[-2:]):
                    checksum += (int(value[:-2]) >= 150 and int(value[:-2]) <= 193) 
                    #print (value.split("c")[0], (int(value.split("c")[0]) >= 150 and int(value.split("c")[0]) <= 193) )
                elif "in" == str(value[-2:]):
                    checksum += (int(value[:-2]) >= 59 and int(value[:-2]) <= 76)
                    #print(value.split("i")[0], (int(value.split("i")[0]) >= 59 and int(value.split("i")[0]) <= 76) )
                else:
                    print('',end='')
            
            if field == possibleFields[4]: # hcl
                #print(field, value)
                if value[0] == "#":                    
                    #if len(value) == 7 or (len(value) == 8 and value[-1:] == chr(10)):
                    if len(value) == 7:
                        numChk = 0
                        alphChk = 0
                        for x in range(1, 7):
                            if value[x].isnumeric():
                                numChk = numChk + 1
                            elif ord(value[x]) in range(97, 103):
                                alphChk = alphChk + 1
                        if alphChk + numChk == 6:
                            checksum = checksum + 1
                        #checksum += (alphChk == 6 or numChk == 6)
                        #print("numChk/alphChk/value",numChk,alphChk,value)
                    else:
                        #print(value)
                        print('',end='')

            checksum += (field == possibleFields[5] and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
            
            checksum +=  (field == possibleFields[6] and value.isnumeric() and len(value) == 9)
            
            if field == possibleFields[6] and not len(value.zfill(9)) == len(value):
                flag = True
            #if field == possibleFields[6] and len(value.zfill(9)) == 9 and len(value) <= 10:
            #    #print (value)
            #    chk6 = 0
            #    for x in range(9):
            #        chk6 += value.zfill(9)[x].isnumeric()                  
                    
            #    checksum += (chk6 == 9)

            #part2Valid += (checksum == 7)
            #print ( (checksum == 7))
        part2Valid += (checksum == 7)
        if flag and checksum == 6:
            print(line)
        #if (checksum == 7):
        #    print ("valid:", line)
        #print(part2Valid,checksum)
        #print("-----------")
        
    else:
        #print("#*#*#* INVALID PASSPORT DETECTED: ", lineNumber,)
        invalid = invalid + 1
print("part1Valid/Invalid/Total/CHKSUM: ", part1Valid, invalid, lineNumber, [part1Valid+invalid == lineNumber])
print("part2Valid: ",part2Valid)
