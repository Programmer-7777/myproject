f = open("dic", "r")
string = f.read()
string1 = string.split()
string2 = {}
j = 0
k = 1
m = 1
z = len(string1)
print(z)
while j<z:
    while k<z:
        if string1[j] == string1[k]:
            m = m+1
            del string1[k]
            z = z-1
            k = k
        else:
            k = k+1
    #print(string1[j], end = " ")
    #print(m)
    string2[string1[j]] = m
    m =1
    j = j+1
    k = j+1
print(string2)
print(len(string2))


string3 = sorted(string2.items(), key=lambda x: x[1], reverse=True)
ff = open("style", "w")
for i in string3:
    ff.write(i[0])
    ff.write("\t")
    ff.write(str(i[1]))
    ff.write("\n")
ff.close()




            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            


