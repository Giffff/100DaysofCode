print("------------Pattern 8---------")
txt = ""
i = 0
for i in range(5):
    for j in range(5-i):
        txt = txt+" "
    for k in range(5):
        txt = txt+"*"
    print(txt)
    j = 0
    k = 0
    txt = ""
