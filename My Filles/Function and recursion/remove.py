def remove_split(strr,word):
    req = strr.replace(word," ")
    req = req.strip()
    return req

strr = "ram is a good boy"
print(strr)
a = remove_split(strr,"ram")
print(a)
