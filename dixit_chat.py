infile = open("C:/Users/arund\Downloads/Software/Data Visualization/dixit_chat.txt", "r",encoding="utf8")
outfile = open("C:/Users/arund\Downloads/Software/Data Visualization/dixit_chat_out.txt", "w",encoding="utf8")
lines = infile.readlines()[1:]
for line in lines:
    pos = line.find("]")
    len = line.__len__()
    line1 = line[pos:len]
    poscol = line1.find(":")
    #print(poscol)
    if poscol == -1:
        pass
    else:
        outfile.write(line1[1:poscol] )
        outfile.write(",1\n")
infile.close()
outfile.close()