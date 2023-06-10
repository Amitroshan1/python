import re


st='this is 5my name.'
math=re.findall(r'\bis',st)
print(len(math),math)