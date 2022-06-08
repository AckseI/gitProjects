f = open("baza tel numbers.txt", encoding='utf-8').readlines()
f = [line.split() for line in f]
f.sort()
print("\n".join(repr(e) for e in f))
output = open("output.txt", "w+", encoding='utf-8')
for i in range(len(f)):
    output.write(str(f[i])+ "\n")
output.close()