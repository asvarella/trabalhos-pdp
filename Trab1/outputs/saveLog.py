def generateInputPath(e,t):
    return 'entrada' + e + '/teste'+ t + '.out'

def generateOutputPath(e,t):
    return 'entrada' + e + '/teste' + t + '.txt'

def main():
    e = input('entrada: ')
    t = input('teste: ')
    outPath = generateOutputPath(e,t)
    inPath = generateInputPath(e,t)
    outFile = open(outPath, 'a')
    sum = 0.0

    for i in range(5):
        inFile = open(inPath, 'r')
        outFile.write('Run #'+ str(i+1) + ':\n')
        lines = inFile.readlines()
        outFile.write("Ans: " + lines[0] + "Time: " + lines[1] + ' seconds\n\n')
        sum += float(lines[1])      
        inFile.close()
        print("Run #" + str(i+1) + " completed.")
        if(i != 4):
            input("Continue? [Y] ")

    average = sum/5    
    outFile.write('Average time: ' + str(average) + ' seconds')
    outFile.close()
    
    
   


if __name__ == "__main__":
    main()
