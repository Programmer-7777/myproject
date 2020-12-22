def sortword(word):
    if word.find('a') != -1:
        if word.index('a')>0 and word.index('a')<len(word)-1:
            return 1
        else:
            return 0
    else:
        return 0

def my_func(list):
    list1 = []
    for word in list:
        if word[4] == 'a':
            list1.append(word)
    return list1
list = ['kdwja', 'bhbhabhjdcb', 'asdneecj']
print(my_func(list))
            
    
                
            
            