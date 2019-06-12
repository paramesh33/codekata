def camel(str):
  return ' '.join([t.title() for t in str.split()])
s=input()
print(camel(s))
