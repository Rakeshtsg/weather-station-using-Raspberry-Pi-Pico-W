import network
import socket
from time import sleep
from machine import Pin, I2C
import gc
gc.collect()
from bmp085 import BMP180

ssid = 'Your network name' #Your network name
password = 'Your WiFi password' #Your WiFi password

led_onboard = Pin("LED", Pin.OUT)
i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 1000000)

#Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.isconnected() == False:
    led_onboard.value(1)
    print('Connecting...')
    sleep(1)
ip = wlan.ifconfig()[0]
print('Connection successful')
print(f'Connected on {ip}')
led_onboard.value(0)

def web_page():
    #Sensor Configuration
    bmp = BMP180(i2c)
    bmp.oversample = 2
    bmp.sealevel = 101325
    temp = bmp.temperature
    press = bmp.pressure
    altitude = bmp.altitude
    temp_f= (temp * (9/5) + 32)
    pressure = "{:.2f}".format(press)
    alti = "{:.2f}".format(altitude)

#HTML CODE  
    html = """<html>
    <head>
  <title>V V Elctronics pvt.ltd Raspberry Pico W Web Server</title>
  <meta http-equiv="refresh" content="10">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <link rel="icon" href="data:,">
  <style>
    html {font-family: Arial; display: inline-block; text-align: center;}
    p {  font-size: 1.2rem;}
    body {  margin: 0;}
    .topnav { overflow: hidden; background-color: #8f8e54; color: white; font-size: 1.7rem; }
    .content { padding: 20px; }
    .card { background-color: white; box-shadow: 2px 2px 12px 1px rgba(140,140,140,.5); }
    .cards { max-width: 700px; margin: 0 auto; display: grid; grid-gap: 2rem; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
    .reading { font-size: 2.8rem; }
    .card.temperature { color: #544bd6; }
    .card.humidity { color: #17bebb; }
    .card.pressure { color: #d9415f; }
  </style>
</head>
<body>
  <div class="topnav">
    <h2><u> V ELECTRONICS PVT LTD Raspberry Pico weather station</u></h2>
  </div>
  <div class="content">
    <div class="cards">
      <div class="card temperature">
        <h4><i class="fas fa-thermometer-half"></i>Temp. Celsius</h4><p><span class="reading">""" + str(temp) + """ &#8451; </p>
      </div>
      <div class="card temperature">
        <h4><i class="fas fa-thermometer-half"></i> Temp. Fahrenheit</h4><p><span class="reading">""" + str(temp_f) + """ &#8457; </p>
      </div>
      <div class="card pressure">
        <h4><i class="fas fa-angle-double-down"></i> PRESSURE</h4><p><span class="reading">""" + str(press) + """ Pa</p>
      </div>
      <div class="card humidity">
        <h4><i class="fas fa-mountain"></i> ALTITUDE</h4><p><span class="reading">""" + str(alti) + """ Meter</p>
      </div>
    </div>
  </div>
</body>

</html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  try:
    if gc.mem_free() < 102000:
      gc.collect()
    conn, addr = s.accept()
    conn.settimeout(3.0)
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    conn.settimeout(None)
    request = str(request)
    print('Content = %s' % request)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  except OSError as e:
    conn.close()
    print('Connection closed')