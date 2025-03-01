import re

s = "rabcdeefgyYhFjkIoomnpOeorteeeeet"

pattern = r"[aeiouAEIOU]"

result = re.findall(pattern, s)

print("this is result\n", result)
print("e occurrence", result.count('e'))
print("o occurrence", result.count('o'))
