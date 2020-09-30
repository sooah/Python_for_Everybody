import json
import urllib.request, urllib.parse, urllib.error

url = input("Enter URL: ")
print("Retrieving ", url)

uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)
total = 0
print("Retrieved: ",len(data),"characters")
print("Count: ", len(info["comments"]))

for i in range(0, len(info["comments"])):
    total += int(info["comments"][i]["count"])
print("Sum", total)