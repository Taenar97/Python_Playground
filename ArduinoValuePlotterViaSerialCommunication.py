import serial
import time
ser = serial.Serial('COM6', 9600)
print("[timestamp temperature humidity]")
while True:
    data1 = int(ser.readline().decode())
    data2 = int(ser.readline().decode())
    current_time = time.strftime("%H:%M:%S")
    print(current_time + " " + str(data1) + " " + str(data2))
    ser.reset_input_buffer()    
    f = open("data/" + str(time.strftime("%d.%m.%Y")) + ".txt", "a")
    f.write(current_time + " " + str(data1) + " " + str(data2) +  "\n")
    f.close()
