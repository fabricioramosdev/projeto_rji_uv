#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name


import serial,time
from datetime import datetime


if __name__ == '__main__':
    
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
        time.sleep(0.5) 
        if arduino.isOpen():
            try:
                while True:            
                    while arduino.inWaiting() == 0: pass
                    if  arduino.inWaiting() > 0: 
                        answer=arduino.readline()                       
                        print("{}\t{}".format(datetime.now(), answer))
                        with open("/home/pi/projeto_uv/uv_log.csv","a+") as file:
                            file.write("{};{}\n".format(datetime.now(), answer))                        
                        arduino.flushInput() #remove data after reading
                    time.sleep(10)
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")


    
