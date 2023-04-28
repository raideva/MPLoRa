import serial
ser = serial.Serial('/dev/cu.usbserial-1420', 9600)
p = open("dataset.csv", "a")
var = 1
l = 2
p.write("\n")
while 1:
    a = ser.readline()
    a = a.decode()
    v = [a.split()]
    try:
        x = v[0][3]
        y = v[0][-1]
        x = x[:-1:]
        print(x, y)
        p.write(str(x) + " " + str(y) + " " + str(var) + " f" + str(l) +  "\n")
    except:
        print("l")
