a="2014-10-23"
import re
s=re.sub("(\d{4})-(\d{2})-(\d{2})","\\3-\\2-\\1",a)
print(s)
