def jumble(S):
    S_list = list(S)
    len_S = len(S)
    for i in range(0, len_S):
        first = []
        first.append(S_list[i])
        
        j = i+1
        second = []
        second.append(S_list[j])
        
        i += 2
    
    First_Str = ' '.join(first)
    Second_Str = ' '.join(second)
    
    print(First_Str, Second_Str)
        
        
if __name__ == '__main__':

    n = int(input()) 
    for i in range(n):
        S = str(input())
        jumble(S)
