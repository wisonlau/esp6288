#!/usr/bin/env python3

class timegy30():
    def run():
        import machine
        #
        import bme280
        # I2C(scl=Pin(5), sda=Pin(4))
        i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
        bme = bme280.BME280(i2c=i2c)
        temp = bme.values[0][:-1]
        press = bme.values[1][:-3]
        hum = bme.values[2][:-1]
        #
        import max44009
        lum = max44009.MAX44009()
        lum = lum.luminosity()
        url = "http://www.wisonlau.com/weather.php?home_lumination=%s&home_humidity=%s&home_temperature=%s&home_airpressure=%s" % \
              (lum, hum, temp, press)
        #
        print(url)
        print(lum, hum, temp, press) # 光照强度:lum lux,当前湿度:hum ％RH,当前温度:temp ℃,当前气压:press hpa
        try:
            import urequests as requests
        except ImportError:
            import requests

        r = requests.get(url)
        print(r.text)