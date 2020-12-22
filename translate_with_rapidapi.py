import http.client

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


conn = http.client.HTTPSConnection("google-translate1.p.rapidapi.com")

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': "dfe3a8c794mshc8c15473180b4aep1f0d61jsneb98c00a9caf",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }
payload = "q=" + "pneumonoultramicroscopicsilicovolcanoconiosis" + "&source=en&target=uz"
conn.request("POST", "/language/translate/v2", payload, headers)

res = conn.getresponse()
data = res.read()
word = data.decode("utf-8")

begin = find_nth(word, '"', 7)
end =  find_nth(word, '"', 8)
end = end+1

word = word[begin:end]
print(word)