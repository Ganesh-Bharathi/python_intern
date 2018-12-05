def minion_game(string):
    v=0
    c=0
    # your code goes here
    vowel = ['A','E','I','O','U']
    string=string.upper()
    ip = list(string)
    leng=len(ip)
    for i in range(leng):
        if (ip[i] in vowel):
            v+=len(ip[i:leng])
        else:
            c+=len(ip[i:leng])
            
    if(v>c):
        print("Kevin "+str(v))
    else:
        print("Stuart "+str(c))