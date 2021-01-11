#get_reg_text(text, pos_begin, pos_end)
def get_reg_text(**dic):
    new_word_list = []
    p_list = []
    for word in dic:
        p_list.append(dic[word])
    first_list = ["words_list", "text"]
    second_list = ["words_list", "text", "pos_begin"]
    third_list = ["words_list", "text", "pos_begin", "pos_end"]

    if all(x in p_list for x in first_list):
        for word in words_list:
           if word.find(text) != -1:
               new_word_list.append(word)
    elif all(x in p_list for x in second_list):
        for word in words_list:
            if word.find(text) != -1 and word.index(text) == 0:
                new_word_list.append(word)
    elif all(x in p_list for x in third_list):
        for word in words_list:
            if word.find(text) != -1 and word.index(text) == -1:
                new_word_list.append(word)
    retur new_word_list
w_list = []
regex_word_list = get_reg_text(**dic)     
        
  