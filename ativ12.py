t1 = 0
t2 = 1

print("10 primeiros termos da sequencia de fibonacci:")
print(t1)
print(t2)

for i in  range(8):
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    