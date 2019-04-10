from machine import Timer

tim = Timer(1)

import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('wisonlau', 'wisonlau')
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())

def func(t):
    import timetask
    timetask.timegy30.run()

# 五分钟
tim.init(period=300000, mode=Timer.PERIODIC, callback=func)
