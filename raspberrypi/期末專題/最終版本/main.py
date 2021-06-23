import sys
import time
import smbus2
import RPi.GPIO as GPIO
import webcam as takepicture


GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 

GPIO.setup(13, GPIO.OUT)#設定綠燈
GPIO.setup(15, GPIO.OUT)#設定藍燈
GPIO.setup(16, GPIO.OUT)#設定紅燈
GPIO.setup(11, GPIO.IN)#觸摸版
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)#設定紅外線

#--------設定燈號初始狀態
GPIO.output(13,0)
GPIO.output(15,1)
#--------設定lcd螢幕及狀態
sys.modules['smbus'] = smbus2

from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', address=0x27, port=1, backlight_enabled=True)#設定lcd顯示螢幕
#--------偵測到有人通過紅外線,紅燈閃爍    
def action(channel):
    print ("Motion detected")

    for i in range(10):
        GPIO.output(16, 1)
        time.sleep(0.2)
        GPIO.output(16, 0)
        time.sleep(0.2)
#閃完紅燈後開啟攝像頭，如果可以為登陸成員則螢幕顯示
    if takepicture.main() == True :
        print("Welecome Home")    
#偵測到有人觸摸後執行
try:
    print('loading')
    lcd.clear()
    while True:
        if GPIO.input(11):
            GPIO.output(13,1)
            GPIO.output(15,0)
#在LCD螢幕顯示,並觸發紅外線感測器執行
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Please standing ")
            lcd.cursor_pos = (1, 0)
            lcd.write_string("   on LINE  ")
            GPIO.add_event_detect(12, GPIO.RISING, callback=action, bouncetime=200)
        time.sleep(1)
        

except KeyboardInterrupt:
    print('close')
finally:
    lcd.clear()