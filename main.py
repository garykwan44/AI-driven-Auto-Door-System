from pystubit_iot import *
from pystubit.board import *
from pyatcrobo2 import *
from util import *
import _thread
import network
import time
import random
import math
import button
import wifi_connection as wifi_connection
import ufirebase as firebase


s_time = float(time.time())
setMotor(0,Servomotor('P16'))
setCalibAngle([2, 0, 0, 0])
calibDC = [88, 91]

def doorOpens():
    setAngle('P13', 0)
    setImage([
    (1,0,0x001f00),
    (2,0,0x001f00),
    (3,0,0x001f00),
    (0,1,0x001f00),
    (4,1,0x001f00),
    (0,2,0x001f00),
    (4,2,0x001f00),
    (0,3,0x001f00),
    (4,3,0x001f00),
    (1,4,0x001f00),
    (2,4,0x001f00),
    (3,4,0x001f00)])

def doorCloses():
    setAngle('P13', 180)
    setImage([
    (0,0,0x1f0000),
    (4,0,0x1f0000),
    (1,1,0x1f0000),
    (3,1,0x1f0000),
    (2,2,0x1f0000),
    (1,3,0x1f0000),
    (3,3,0x1f0000),
    (0,4,0x1f0000),
    (4,4,0x1f0000)])


#Wi-Fi configuration & connection
#wifi_connection.wifiConnection("WINSTARS", "28092299", s_time)
#wifi_connection.wifiConnection("KWAN", "27023816", s_time)
#wifi_connection.wifiConnection("Gary", "okt32s4A4", s_time)
wifi_connection.wifiConnection("Karen", "91492071", s_time)

#Firebase settings
URL = 'aiautodoor-390ed'

firebase.put(URL+'/state', 'close') #default settings

while True:
    state = firebase.get(URL+'/state')

    if state == 'close':
        doorCloses()

    elif state == 'open':
        doorOpens()
