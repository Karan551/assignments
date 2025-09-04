import re

# -------------- .(period meta character)
text = "geeks.forgeeks"
match_1 = re.search(r'.', text)
# print(match_1)

match_2 = re.search(r'\.', text)
# print(match_2)

# -------------- [] (square brackets)
string = "Hello bAd cat World HolA chai"
pattern = "[a-c]"  # similar that ==> [abc]
#  And [0,3] is similar that ==> [0123]
result = re.findall(r'[a-c]', string, flags=re.IGNORECASE)
print(result)
print("a occurrence", result.count("a"))
print("b occurrence", result.count("b"))
print("c occurrence", result.count("c"))
print("A occurrence", result.count("A"))
