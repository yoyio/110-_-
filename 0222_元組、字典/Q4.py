dic={"aaa":180,"Jim":170,"Kate":160,"ddd":150}
dic["zoe"]=165
del dic["Jim"]
dic["Kate"] = 164
for i,j in dic.items():
    print(i + " is " + str(j) + " cm")