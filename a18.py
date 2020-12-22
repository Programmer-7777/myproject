f = open("words.txt", "r")
string = f.read()
string1 = string.splitlines()
#fff = open("a.18", "x")
fff = open("a.18", "w")
#functions

# del number /-------------------------
def del_number(list):
    del_num_words = []
    for word in list:
        if word.isalpha():
            del_num_words.append(word)
    return del_num_words
# del number -------------------------/

# del all upper
def del_upper_case(list):
    del_upper_case_words = []
    k = 0
    for word in list:
        for w in word:
            if w.upper() == w:
               k = k+1
        if (k == 1 and word[0].lower() != word[0]) or k == 0:
            del_upper_case_words.append(word)
        k = 0
    return del_upper_case_words
#------------------------------------------------------------
#compare first and second letters
def compare(list):
    coverlist = []
    for word in list:
        if len(word) != 1:
            if word[0] != word[1] and ((ord(word[0]) - ord(word[1]) != 32) and (ord(word[1]) - ord(word[0]) != 32)):
                coverlist.append(word)
    return coverlist
#---------------------------------------------------------------------------------------------
#sorted list
def sortword(list):
    coverlist1 = []
    for word in list:
        if word.find('a') != -1:
            if word.index('a')>0 and word.index('a')<len(word)-1:
                coverlist1.append(word)
    return coverlist1
#---------------------------------------------------------------------------------------------
#get list element with one  specific letter
def with_one_a_letter(list):
    coverlist = []
    for word in list:
        if (word.count('a') == 1 and word.count('A') == 0) or (word.count('a') == 0 and word.count('A') == 1):
            coverlist.append(word)
    return coverlist
#---------------------------------------------------------------------------------------------
#get list element without one  specific letter
def without_one_specific_letter(list, x):
    coverlist = []
    for word in list:
        if word.count(x) == 0:
            coverlist.append(word)
    return coverlist
#---------------------------------------------------------------------------------------------
#write to file
def write_to_file(list):
    for word in list:
        fff.write(word)
        fff.write("\n")
#get_letter/------------------------------
def get_letter(list, x, i):
    coverlist = []
    for word in list:
        if word[i] == x:
            coverlist.append(word)
    return coverlist
#get_letter------------------------------/
def sortlength(list):
    coverlist = []
    for word in list:
        if len(word)>=3:
            coverlist.append(word)
    return coverlist
#get_letter_without/----------------
def get_letter_without(list, x, i):
    coverlist = []
    for word in list:
        if word[i] != x:
            coverlist.append(word)
    return coverlist
#get_letter_without---------------/
def comp_exp(list):
    coverlist = []
    for word in list:
        if word.find("af") > 0 or word.find("Af") > 0:
            coverlist.append(word)
    return coverlist

def sort_len(list):
    dic = {}
    coverlist = []
    for word in list:
        x = len(word)
        dic[word] = x
    sort_orders = sorted(dic.items(), key=lambda x: x[1])
    for i in sort_orders:
        coverlist.append(i[0])
    return coverlist
            
       
list = []
list = del_number(string1)
list = del_upper_case(list)
list = sortlength(list)
list = compare(list)
list = comp_exp(list)
list = sort_len(list)
write_to_file(list)
fff.close()





