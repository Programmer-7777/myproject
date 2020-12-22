import http.client
from PIL import Image
import requests
from io import BytesIO

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

conn = http.client.HTTPSConnection("contextualwebsearch-websearch-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "dfe3a8c794mshc8c15473180b4aep1f0d61jsneb98c00a9caf",
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }

conn.request("GET", "/api/Search/ImageSearchAPI?q=" + "mobile_phone" + "&pageNumber=1&pageSize=1&autoCorrect=true", headers=headers)

res = conn.getresponse()
data = res.read()
string = data.decode("utf-8")
begin = find_nth(string, '"', 11)+1
end = find_nth(string, '"', 12)

url = string[begin:end]
response = requests.get(url)
img = Image.open(BytesIO(response.content))

img.show()