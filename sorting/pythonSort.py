import time

start_time = time.time()

f = open("gitProjects/sorting/test.txt", "r").readlines()
f = [line.rstrip() for line in f]
f1 = [int(item) for item in f]
f1.sort()
output = open("gitProjects/sorting/output.txt", "w+")
for i in range(len(f1)):
    output.write(str(f1[i])+ "\n")
output.close()

time_execution =  time.time() - start_time

print("Время выполнения: ", time_execution)