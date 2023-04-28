import serial

ser = serial.Serial('/dev/cu.usbserial-1420', 9600)
p = open("data/dataset_sf_19.csv", "a")
p.write("index,rssi,snr,sf")
p.write("\n")
while 1:
    a = ser.readline()
    try:
        a = a.decode()
        v = [a.split()]
        print(v[0])
        v = v[0]
        if len(v) == 4:
            p.write(str(v[3]) + "," + str(v[1]) + "," + str(v[2]) + ",")
        elif len(v) == 3:
            p.write(str(v[-1]) + "\n")
    except:
        print("e")
