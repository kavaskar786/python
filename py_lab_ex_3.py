dict1={
    "name":"kavaskar",
    "domain_name":"library management",
    "r_no":"2347230" 
}
inp=input()
spl_wrd=inp.split("_")
key=list(dict1.keys())
tem=0
for i in spl_wrd:
   if i=='':
      continue
   else:
      dict1[key[tem]]=i
      tem=tem+1

print(dict1)
