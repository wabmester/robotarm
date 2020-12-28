from Servo import *
servo=Servo()

# Main program logic follows:
if __name__ == '__main__':

    import sys
    if len(sys.argv)<3:
        print ("testservo pin angle")
        exit() 
    servo.setServoAngle((int) (sys.argv[1]), (int) (sys.argv[2]))
