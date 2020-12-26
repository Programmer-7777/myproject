import eng_to_ipa as ipa




def read_file_get_ipa(file, write_file):
    f = open(file, "r")
    ff = open(write_file, "w")
    string = f.read()
    list = string.splitlines()
    for word in list:
        transc = ipa.convert(word)
        ff.write(word + "\n" + "[" + transc + "]" + "\n\n")
    f.close()
    ff.close()

read_file_get_ipa('textare.txt', "test.txt")       

        
        
