import smbus
import mysql.connector as mariadb
import time
import paho.mqtt.client as mqtt
#import
mariadb_connection = mariadb.connect(user='root', password='sgs', database='sgs')
cursor = mariadb_connection.cursor()
#maridb initialisieren
client = mqtt.Client()
client.connect("test.mosquitto.org", port=1883)
#MQTT
i2cbus=smbus.SMBus(1) # Bus 1
tc74Adress=0x4d # Adresse
# cmd-Word des TC74
i2cbus.write_byte_data(tc74Adress, 0x00, 0x00)
while True:
        #SQL
        actualtemp=i2cbus.read_byte(tc74Adress)
        cursor.execute("INSERT INTO temp (temp) VALUES ({})".format(actualtemp))
        mariadb_connection.commit()
        #MQTT
        client.publish("/sgs/temp/jz", actualtemp)
        #Console
        print(actualtemp)
        time.sleep(10)
