s=input("enter string : ")
c=0
for i in range(0,len(s)):
    if s[i] == "a"or s[i]=="e"or s[i]=="i"or s[i]=="o"or s[i]=="u"or s[i]=="A"or s[i]=="E"or s[i]=="I"or s[i]=="U"or s[i]=="O":
        c+=1
        print(s[i],end=" ")
print("\n",c)
