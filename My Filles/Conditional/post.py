post = "Harry is a good boy"
post = post.lower()
req = input("Enter a word you want to search: ")
req = req.lower()
if req in post:
    print(F"{req} is in post")
else:
    print(F"{req} is not in post")