# DHTRpi
## DHT11 Sensor Using Raspberry Pi

### Connection
  ```
  Rpi  -- DHT11
  
  Vcc   -- Vcc
  GND   -- Gnd
  Gpio5 -- Signal
```


To Run Some basic commands are:

1--
```
sudo apt-get update
```
2--
```
sudo apt-get upgrade
```
3--
```
sudo apt-get install python3 python3-dev python3-pip
```
4--
```
sudo pip install flask
```
5--
```
sudo apt-get install git
```
6--
```
sudo pip3 install Adafruit_DHT
```
--
```
git clone https://github.com/Tony-Vaniya/DHTRpi.git
```
8--
```
cd DHTRpi
```
9--
```
sudo python3 app.py
```

# Start On Boot ##Follow The Command In cmd

sudo nano /etc/profile

## In Last Add Line

```
sudo python3 /home/pi/FlaskPi/main.py
```
