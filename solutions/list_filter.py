import re

name = ['ferdinand','jamie',1,'andela','???','saint','plane','trees','serve','toy' ]
#using python regular expression
val = filter(lambda x:re.search(r'\b[a-z]{3,8}\b',str(x)) is not None,name)
print val