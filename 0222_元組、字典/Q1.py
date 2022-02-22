ts = (89, 87, 36, 55, 64)
tn = ("AAA", "BBB", "CCC", "DDD", "EEE")

for i in range(5):
    print(tn[i] + "\t" + str(ts[i]))

print("==================")

print("最高分" + ":" + str(max(ts)))
print("最低分" + ":" + str(min(ts)))
s = 0
for j in range(5):
    s += int(ts[j])
print("平均" + ":" + str(s / 5))