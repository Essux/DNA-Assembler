from random import randint

numberOfSecuences = 30000
minimumLength = 300
maximumLength = 3000

for filename in ["AB042837.txt", "AY325307.txt"]:
    thefile = open(filename,'r')
    text = thefile.read()
    thefile.close()
    adn = text.split("ORIGIN")[1]
    lines = adn.split('\n')[:-2]
    lines = map(lambda x: x.strip().split(" ")[1:], lines[1:])    
    newadn = ""
    for line in lines:
        for segment in line:
            newadn += segment
    newFilename = filename.replace(".txt", "")+"ADN.txt"
    
    thefile = open(newFilename,'w')
    thefile.write(newadn)
    thefile.close()

    newFilename = filename.replace(".txt", "")+"ADN-segments.txt"
    thefile = open(newFilename, 'w')

    thefile.write(str(len(newadn))+"\n\n")
    
    # Print the beginning
    length = randint(minimumLength, maximumLength)
    substring = newadn[:length+1]
    thefile.write(substring+"\n\n")

    # Print the end
    length = randint(minimumLength, maximumLength)
    begin = len(newadn) - length
    substring = newadn[begin:]
    thefile.write(substring+"\n\n")

    for x in range(1,numberOfSecuences):
        length = randint(minimumLength,maximumLength)
        begin = randint(0, len(newadn)-length-1)
        end = begin + length
        substring = newadn[begin:end+1]
        thefile.write(substring+"\n\n")

    thefile.close()


