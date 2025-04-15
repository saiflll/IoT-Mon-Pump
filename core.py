import urequests
import time
from machine import Pin, ADC

water_level = ADC(Pin(32))     
moisture = ADC(Pin(33))       
ph_sensor = ADC(Pin(34))       
temp_sensor = ADC(Pin(35))     
ammonia = ADC(Pin(36))         
relay = Pin(25, Pin.OUT)      
alarm = Pin(26, Pin.OUT)       

server_url = "http://192.168.4.1:5000/update"  

def read_sensor(adc):
    return adc.read() / 4095 * 100  

while True:
    wl = read_sensor(water_level)
    moist = read_sensor(moisture)
    ph = read_sensor(ph_sensor)
    temp = read_sensor(temp_sensor)
    nh3 = read_sensor(ammonia)

    # alarm & refil
    if wl < 25:
        alarm.on()
        relay.on()
    else:
        alarm.off()
        relay.off()

    # Kirim erver 
    try:
        data = {
            "water_level": wl,
            "moisture": moist,
            "ph": ph,
            "temperature": temp,
            "ammonia": nh3
        }
        res = urequests.post(server_url, json=data)
        res.close()
    except Exception as e:
        print("Gagal kirim:", e)

    time.sleep(5)