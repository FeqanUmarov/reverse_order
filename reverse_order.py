info = input("Her hansi bir ifade daxil edin:")

info_list = list(info)


info_list_len=-(len(info_list))

sentence=[]

m=-1

for s in info_list:
    if m>=info_list_len:
        sentence.insert(m,s)
        m+=-1
for s in sentence:
    print(s,end="")
