f = open("nbrs.txt", "w")
for i in range(1, 10):
    f.write("0000000" + str(i) + '\n')	
for i in range(11, 100):
    f.write("000000" + str(i) + '\n')
for i in range(111, 1000):
    f.write("00000" + str(i) + '\n')
for i in range(1111, 10000):
    f.write("0000" + str(i) + '\n')	
for i in range(11111, 100000):
    f.write("000" + str(i) + '\n')
for i in range(111111, 1000000):
    f.write("000" + str(i) + '\n')
for i in range(1111111, 10000000):
    f.write("00" + str(i) + '\n')
for i in range(11111111, 100000000):
    f.write("0" + str(i) + '\n')	
for i in range(1, 100000000):
    f.write(i + '\n')
f.close()