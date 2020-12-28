#coding:utf-8
import Adafruit_PCA9685
import time 
class Servo:
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()   
        self.pwm.set_pwm_freq(50)               # Set the cycle frequency of PWM
    #Convert the input angle to the value of pca9685
    def setServoAngle(self,channel, angle):  
#	0 deg = 5% = 205, 90 deg = 7.5% = 307, 180 deg = 10% = 409
#	51 added to be backwards compatible with old code at 90 deg
        data = (1 + angle/180) * 205
        self.pwm.set_pwm(channel, 0, int(data))
        print(data, data/4096 * 100)
 
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    S=Servo()
    for i in range(16):
        S.setServoAngle(i,90)
        


        
        
        
        
