dic= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}

def translate(a):
    for i in a:
        print(dic[i],end=' ')
a=[]
a=(input().split())
translate(a)