import eng_to_ipa as ipa


#f = open("sortword.txt", "r")
#ff = open("sql.txt", "x")
#fff = open("sql.txt", "w")

string = f.read()


lists = string.splitlines()

# print(type(lists))
i = 1
for word in lists:
    trans = ipa.convert(word)
    fff.write("(" + str(i) + ", '" + word + "', '" + trans + "'),\n")
    i = i+1
#fff.write(";")
f.close()
#ff.close()
fff.close()
