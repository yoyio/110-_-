dic ={"monday":"星期一","tuesday":"星期二",
      "wednesday":"星期三","thursday":"星期四",
      "friday":"星期五","saturday":"星期六","sunday":"星期天"}
a= input()

if not a in dic.keys():
    print("不存在")
else:
    print(dic[a])

