list = [[{"shtrix":4601546000013}, {"name": "acer 5"}, {"sold": 0}], [{"shtrix": 4601546000024}, {"name": "acer 6"}, {"sold": 1}], [{"shtrix": 4601550000015}, {"name": "hp"}, {"sold": 1}], [{"shtrix": 4601546000036}, {"name": "acer 7"}, {"sold": 0}], [{"shtrix": 4601530000019}, {"name": "samsung3"}, {"sold": 1}], [{"shtrix": 4601606000018}, {"name": "Asus 4"}, {"sold": 1}]]
list1 = [[1546, "acer"], [1550, "hp"], [1530, "samsung"], [1606, "asus"]]
k = 0
for word in list1:
    for word1 in list:
        x = slice(3,7)
        if str(word1[0]["shtrix"])[x] == str(word[0]):
            k +=1
    print(word[1], end = " ")
    print("kompyuterlar soni: ", end = " ")
    print(k)
    k = 0
            
        
        

    
   
    