import re
a = "long 123 zi 456 789"
pattern = re.compile(r'(\w*?)\s(\d*)\s(\w*?)\s(\d*?)\s(\d*?)',re.S)
pat = re.search(pattern,a)
print a.count("zi")
