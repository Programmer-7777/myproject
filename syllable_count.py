import eng_to_ipa as p
f = open("words.txt", "r")
string = f.read()
list = string.splitlines()
newlist = []
for word in list:
    Sylcount =  p.syllable_count(word)
    newlist.append(Sylcount)
print(newlist)
    