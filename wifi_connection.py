from pystubit_iot import *
from pystubit.board import *
from util import *
import network
import time

#Wi-Fi configuration & connection
def wifiConnection(ssid, pwd, s_time):
    wifi_config(ssid, pwd)
    sta_if = network.WLAN(network.STA_IF)

    res=wifi_connect(trytime = 3)
    if not res:
        display.scroll('Err')
        print("Error")
        exit()
    else:
        print("Network connected.")
        print(sta_if.ifconfig())
        connected_time = float(time.time())
        print(float(connected_time - s_time))



