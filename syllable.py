import http.client
f = open("wordtest.txt", "r")
ff = open("test.txt", "w")
string = f.read()
newlist = string.splitlines()

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "dfe3a8c794mshc8c15473180b4aep1f0d61jsneb98c00a9caf",
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }
list = []
i = 0
//str="""for word in newlist:
  //  conn.request("GET", "/words/" + word + "/syllables", headers=headers)
  //  res = conn.getresponse()
  //  data = res.read()
  //  wlist = data.decode("utf-8")
  //  begin = find_nth(wlist, '[', 1)
  //  end =  find_nth(wlist, ']', 1)
  //  end = end+1
  //  wlist = wlist[begin:end]
  //  if len(wlist)!=0:
  //      for sylb in wlist:
  //          list.append(sylb)
    //print(i)
   // i = i+1"""
k = 0
for word in newlist:
    conn.request("GET", "/words/" + word + "/syllables", headers=headers)
    res = conn.getresponse()
    data = res.read()
    wlist = data.decode("utf-8")
    begin = find_nth(wlist, '[', 1)
    end =  find_nth(wlist, ']', 1)
    end = end+1
    wlist = wlist[begin:end]

    qbegin = find_nth(wlist, '"', 1)
    count = 0
  
    for i in wlist: 
        if i == '"': 
            count = count + 1

##if len(wlist)!=0:
  #  for sylb in wlist:
    sylb = 1  #     list.append(sylb)
    while sylb<=count:
        qbegin = find_nth(wlist, '"', sylb) + 1
        sylb = sylb + 1
        qend = find_nth(wlist, '"', sylb)
        sylb = sylb +1
        list.append(wlist[qbegin:qend])
        ff.write(wlist[qbegin:qend] + "\n")
    print(k)
    k = k+1
        

    
    
    
    
print(list)
f.close()
ff.close()
