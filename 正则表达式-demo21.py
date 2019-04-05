import re
content='Hello 123 4567 World_This is a Regex Demo'
print(len(content))

# res = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
# res=re .match('^Hello\s(\d+)\s(\d+)\s\w{10}',content)

# res=re .match('^Hello.*Demo$',content)
res = re .match('^He.*?(\d+).*Demo$',content)

print(res)
print(res.group())      #输出匹配到的信息
print(res.group(1))

print(res.span())       #输出匹配的范围