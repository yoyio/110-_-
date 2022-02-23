import  random
dic={"青眼白龍":20,"紅髮女妖":11,"白骷髏王":9,"碧眼狐妖":12}
k=100
s=0
while(k>0):
    a=int(input("功能選項:1.抽卡 2.用了幾張卡 3.離開 :"))
    if a== 1:
        r = random.choice(list(dic.keys()))
        s += 1
        k -= dic[r]
        print(" 使用 " + r + " ，扣 " + str(dic[r]) + "點, 魔王剩 " + str(k) + " 點")
    elif a== 2:
        print(" 使用"+str(s)+"張卡")
    elif a==3:
       break
    else:
        print("請重新輸入")
print("byebye")