import eng_to_ipa as p
import nltk
f = open("list.txt", "x")
ff = open("list.txt", "w")
list = ["hello", "world", "everyone", "run"]
#print("word "+"PofS "+"[us] "+ "[uk] "+ "Sylcount")
for text in list:
    trans = p.ipa_list(text)
    trans = trans[0]
    if len(trans) == 1:
        us = trans[0]
        uk = trans[0]
    else:
        us = trans[0]
        uk = trans[1]
    Sylcount =  p.syllable_count(text)
    PofS = nltk.word_tokenize(text)
    pofs = nltk.pos_tag(PofS)
    #print(type(text))
    #print(type(us))
    #print(type(uk))
    #print(type(Sylcount))
    print(text + "   " + pofs[0][1] + "   ["  + us + "]   [" + uk + "]   " +  str(Sylcount))
    print("\n")
#print(type(str(Sylcount)))
    
#f.close()
#ff.close()











