dic={}
p="系統功能 -> 1.新贈 2.修改 3.刪除 4.查詢 5.產品列表 其他.離開 :"
dic={}
while (True):
    inp = int(input(p))
    if inp == 1:
        a = input("編號")
        if not a in dic.keys():
            b = input("品名")
            c = input("單價")
            dic[a] = b, c
    elif inp == 2:
        a = input("編號")
        if not a in dic.keys():
            print("沒有這項商品")
        else:
            b = input("品名")
            c = input("單價")
            dic[a] = b, c
    elif inp == 3:
        a = input("編號")
        if not a in dic.keys():
            print("沒有這項商品")
        else:
            del dic[a]
    elif inp == 4:
        a = input("編號")
        if not a in dic.keys():
            print("沒有這項商品")
        else:
            print("品名："+dic[a][0]+" 單價"+str(dic[a][1]))
    elif inp == 5:
        print("編號\t品名\t單價")
        for i in dic.keys():
            print(i+"\t"+dic[i][0]+"\t"+dic[i][1])
    else:
        print("離開系統")
        break