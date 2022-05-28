import sys 

def main(argv):
    f = open(argv, 'r')
    lines = f.readlines() 
    first = lines[0].strip()
    second = lines[1].strip() 
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip('\n').split(' ')
       
    scoring = {}
    for i in range(3, len(lines)):
        col = lines[i]
        for j in range(1, len(col)):
            scoring[col[0] + lines[2][j]] = int(col[j])
    
    
    dictionary_help = [first, second, scoring]

    #Outputs score of finalized optimal string using given scoring matrix
    def score_helper(dictionary, a, b):
        joint = []
        for i in range(len(a)):
            joint.append(a[i] + b[i])
        res = 0
        for i in joint:
            for j in dictionary.keys():
                if i == j:
                    res += dictionary[i]
        return res


    def matrix(dictionary): 
        table = []
        str1 = dictionary[0]
        str2 = dictionary[1]
        score = dictionary[2]
        table = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
        
        for i in range(1, len(str2) + 1):
            for j in range(1, len(str1) + 1):

                #levenshtein edit distance just with max instead of min 
                table[i][j] = max(table[i][j-1] + score[str1[j-1] + "-"], 
                                  table[i-1][j] + score["-" + str2[i-1]], 
                                  table[i - 1][j - 1] + score[str1[j - 1] + str2[i - 1]])

        #Traverse latter table to find optimal strings from bottom right up left 
        fin1 = ""
        fin2 = ""
        n = len(str1)
        m = len(str2)
    
        while n or m: 

            #diagonal check with current 
            if table[m][n]  == table[m-1][n-1] + score[str1[n-1] + str2[m - 1]]: 
                fin1 += str1[n-1]
                fin2 += str2[m-1]
                n -= 1 
                m -= 1

            #vertical up check with current
            elif table[m][n]  == table[m][n-1] + score[str1[n-1] + "-"]:
                fin1 += str1[n - 1] 
                fin2 += "-"
                n -= 1

            #left check with current
            else:
                fin1 += "-"
                fin2 += str2[m - 1] 
                m -= 1


        out1 = fin1[::-1]
        out2 = fin2[::-1]
        score_fin = score_helper(score, out1, out2)
        print(table)
        print("x: " + " ".join(out1) + "\n" + "y: " + " ".join(out2) + "\n" + "Score: " + str(score_fin))
    
    return matrix(dictionary_help)

if __name__ == "__main__":
    main(sys.argv[1]) 



