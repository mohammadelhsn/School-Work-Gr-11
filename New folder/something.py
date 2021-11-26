import re 

# mo = "mo "
# a = re.sub(r'\s+', '', mo)
# print(a)
# if (a == "mo"): print("worked")
# else: print("not worked")

mo = "mo s"
b = (r'\s+', '', mo)
print(str(b))
a = mo.replace(r'\s+', '')

print(a)
if (a == "mo"): print("worked")
else: print("not worked")