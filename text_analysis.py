import operator
f = open("test.txt", "r")
#ff = open("episode2words.txt", "x")
#ffff = open("episode2words.txt", "w")
fff = open("sql.txt", "w")
string = f.read()
#string = string.upper()
print(type(string))
list1 = string.splitlines()
list2 = []
dic = {}
newdic = {}
for text in list1:
    list3 = text.split(" ")
    list2.extend(list3)

fff.write("Words:" + str(len(list2)) + "\n")
k = 0
while k<len(list2):
    z = 1
    i = k+1
    while i<len(list2):
        if list2[k] == list2[i]:
           del list2[i]
           z += 1
        else:
            i = i+1
    #fff.write(list2[k] + "     " + str(z) + "\n")
    #print(list2[k], end = '  ')
    #print(z)
    dic[list2[k]] = z
    k = k + 1
    #print("\n")
#print(list2[0])
#{k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
#dict(sorted(dic.items(), key=lambda item: item[1]))
fff.write("Dics:" + str(len(list2)) + "\n")
newdic = dict( sorted(dic.items(), key=operator.itemgetter(1),reverse=True))
for key, value in newdic.items():
    fff.write(key + "     " + str(value) + "\n")
    #ffff.write(key + "\n")
    
print(newdic)
f.close()
fff.close()
#ffff.close()
            
    
    
    
