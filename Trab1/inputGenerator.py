import random

#creates .in file to use for problem.cpp and solution.cpp inputs.
#user informs desired 'n' and 'k' values.

def generateRandomInput(n):
    array = ''
    for i in range(n):
        array += str(random.randint(1,99))
        array += ' '
    return array

def main():
    f = open("newInput.in", "w")
    n = input("n = ")
    k = input("k = ")
    f.write(n + '\n')
    f.write(k + '\n')
    f.write(generateRandomInput(int(n)))
    f.close()

if __name__ == '__main__':
    main()
