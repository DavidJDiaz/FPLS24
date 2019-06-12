###################################
# Author: David Diaz              #
# Date:   4/18/2019               #
#                                 #
# Sudoku Pair Latin Squares       #
# (3,b) for b = 1 mod 3           #
# overwrites to and reads from    #
# file: 'SPLS24.txt'              #
###################################


def main():
    n = 0
    name = 'SPLS24.txt'
    empty = 99
    
    while n%9 is not 6:
        n = int(input("Enter size of FPLS: "))
    
    M = [[empty for col in range(n)] for row in range(n)]
    for i in range(n):
        M[i][int(n/3)] = i
        M[-1-i][-1-int(n/3)] = i
        M[int(n/3)][i] = i
        M[-1-int(n/3)][-1-i] = i

    M1 = [[0,1,2],[3,4,5],[6,7,8]]
    M2 = [[15,16,17],[18,19,20],[21,22,23]]
    B = [0,4,6]

    for i in range(len(M1)):
        for j in range(len(M1[i])):
            for k in range(len(B)):
                for m in range(len(B)):
                    M[3*B[k]+i][3*B[m]+j] = M1[(1-m+i)%3][(1-k+j)%3]
                    M[-3*B[k]-i-1][3*B[m]+j] = M2[(1-m+i)%3][(1-k+j)%3]
                    M[-3*B[k]-i-1][-3*B[m]-j-1] = M1[(1-m+i)%3][(1-k+j)%3]
                    M[3*B[k]+i][-3*B[m]-j-1] = M2[(1-m+i)%3][(1-k+j)%3]

    printFile(M, name)

    M = permute(M)

    printFile(M, name)

    M = replace(M)

    printFile(M, name)

    return

def permute(M, empty=99):
    M2 = [[empty for col in range(len(M))] for row in range(len(M))]

    for col in range(len(M)):
        for row in range(len(M)):
            if col//3 % 3 == 2 or col%3 == 1 or row//3 % 3 == 2:
                M2[row][col] = M[row][col]
            else:
                M2[row][col] = M[row - row%3 + (row-(col-1)%3)%3][col]
    
    return M2

def replace(M):
    for block in [0,1,6,7]:
        target = M[8][3*block:3*block+3] + M[15][3*block:3*block+3]
        for col in range(3):
            for row in range(6):
                if M[9 + row][3*block + col] in target:
                    M[9 + row][3*block + col] = 99
                if M[3*block + col][9+row] in target:
                    M[3*block + col][9+row] = 99
    return M

def writeFile(M, name, empty = 99):
    with open(name,'w',encoding = 'utf-8') as f:
        for row in M:
            for item in row:
                if item is empty:
                    f.write('{:^4}'.format(""));
                else:
                    f.write('{:^4}'.format(item));
            f.write("\n")
        f.write("==================\n")
        f.close()
    return

def readFile(name):
    with open(name,'r',encoding = 'utf-8') as f:
        print(f.read())
    f.close()
    return

def printFile(M, name):
    writeFile(M, name)
    readFile(name)
    return

def disp(M, empty=99): #NOT IN USE
    for row in M:
        for item in row:
            if item is empty:
                print('{:^4}'.format(""), end = "")
            else:
                print('{:^4}'.format(item), end = "")
        print("")
    print("===============================")
    return



#def dup(M):
#    dupflag = False

#    for i in range(len(M)):
#        for j in range(len(M)):
#            while not dupflag:
                
            
        
            

   


if __name__ == "__main__":
    main()
