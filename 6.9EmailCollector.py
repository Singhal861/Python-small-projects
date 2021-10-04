import re
my_str = '''Get million free email addresses all over the world visit and download at
http://freeemailaddressesdirectory.OurToolbar.com/ it is true and guerantee
bball1puc2@aol.com
lemuus@aol.com
dcve1@aol.com
goal1986@aol.com
bozo23456@aol.com
hbdidier@aol.com
lle013@aol.com
rtlpropgrp@aol.com
fwlker4478@aol.com
sgaerner@aol.com
rn4ever5b@aol.com
beckyb510@aol.com
goal1996@aol.com
cafebreve@aol.com
onbelay99@aol.com
fjdrake@aol.com
violeta79@aol.com
lumnum@aol.com
ghoug78930@aol.com


rn4fires@aol.com
lemux1@aol.com
markmax@aol.com
tb4ever31@aol.com
hbdiesel@aol.com
tb4fish@aol.com
bball1st@aol.com
Get million free email addresses all over the world visit and download at
http://freeemailaddressesdirectory.OurToolbar.com/ it is true and guerantee
'''

# h1 = re.compile(r'[\w]+@[\w.]+')
# h = re.finditer(r'[\w]+@[\w.]+' ,my_str)
h = re.findall(r"[\w]+@[\w.]+", my_str)
for count, text in enumerate(h):
    count += 1
    print(f"E-mail{count} = {text}")