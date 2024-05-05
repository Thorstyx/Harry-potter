import network   #import des fonction lier au wifi
import urequests #import des fonction lier au requetes http
import utime #import des fonction lier au temps
import ujson #import des fonction lier aà la convertion en Json
import random
from machine import Pin, Timer, PWM

pwm_red = PWM(Pin(17,mode=Pin.OUT))
pwm_green = PWM(Pin(18,mode=Pin.OUT))
pwm_blue = PWM(Pin(19,mode=Pin.OUT))

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'iPhone de Cheikh'
password = 'Cheikh75'
wlan.connect(ssid) # connecte la raspi au réseau
urls = ["https://api-pokemon-fr.vercel.app/api/v1/pokemon/1", "https://api-pokemon-fr.vercel.app/api/v1/pokemon/4","https://api-pokemon-fr.vercel.app/api/v1/pokemon/7"]

while not wlan.isconnected():
    print("pas connecté au wifi")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        request = urequests.get(urls[random.randint(0,2)]) # lance une requete sur l'url
        
        
        resultat = request.json()
        
        
        print(resultat["types"][0]["name"])# traite sa reponse en Json
        
        type = resultat["types"][0]["name"]
        
        if type == "Plante":
            pwm_green.duty_u16(13000)
            pwm_red.duty_u16(0)
            pwm_blue.duty_u16(0)
        
        if type == "Feu":
            pwm_red.duty_u16(13000)
            pwm_green.duty_u16(0)
            pwm_blue.duty_u16(0)
        
        if type == "Eau":
            pwm_red.duty_u16(0)
            pwm_green.duty_u16(0)
            pwm_blue.duty_u16(13000)
        
        request.close() # ferme la demande
        utime.sleep(0.5)  
    except Exception as e:
        print(e)
        