import pymongo
import time, datetime
import os, psutil
import cfg
# pip3 install Adafruit_DHT
import Adafruit_DHT

'''
In a database, document is created for each node where data from various interfaced sensors,
and system information are dumped.
In this tutorial, only system information is dumped. 

'''

client = pymongo.MongoClient ('mongodb://%s:%s/'%(cfg.mongo_server_cfg.get('host'),cfg.mongo_server_cfg.get('port')),
                              username=cfg.mongo_server_cfg.get('usr'),
                              password = cfg.mongo_server_cfg.get('pwd')
                              )


class MongoDB ():
    def __init__ (self):
        self.db = client[cfg.db.get('name')][cfg.node.get('name')]
    
    def insert (self, sensor, data):
        self.db[sensor].insert_one (data)
        

class Sensors ():
    def __init__ (self):
        self.data = None
        
    def __next__ (self):
        self.update()
        return (self.data)
    
    def update (self):
        # update the sensor values in data
        # do something
        # self.data = updated values
        pass
        
        
class pi_core (Sensors):
    def __init__ (self):
        super().__init__()
    
    def read_core_temp(self):
        temp = os.popen ('vcgencmd measure_temp').readline()
        return float(temp.split('=')[-1].split("'")[0])
    def to_mb(self, kbs):
        return round (kbs/1024.0/1024.0, 2)
    def to_gb(self, kbs):
        return round (kbs/1024.0/1024.0/1024.0, 2)
    
    def cpu_usage(self):
        return round (psutil.cpu_percent(), 2)
    def memory_usage(self):
        memory = psutil.virtual_memory()
        total = self.to_mb(memory.total)
        free = self.to_mb(memory.available)
        return total - free 
    def memory_free(self):
        memory = psutil.virtual_memory()
        free = self.to_mb(memory.available)
        return free 
    
    def disk_usage (self):
        disk = psutil.disk_usage('/')
        total = self.to_mb(disk.total)
        free = self.to_mb (disk.free)
        return round (total - free, 1)
    
    def disk_free (self):
        disk = psutil.disk_usage('/')
        free = self.to_mb (disk.free)
        return free
    
    def update (self):
        temp = os.popen ('vcgencmd measure_temp').readline()
                
        self.data = {
            'name': 'cvlab-pi3',
            'cpu': {'usage': self.cpu_usage(),
                    'Temperature': self.read_core_temp(),
                    'unit': 'Centigrade'
                    },
            'memory':{'usage': self.memory_usage(),
                      'free': self.memory_free(),
                      'unit': 'MB'
                      },
            'disk':{'usage': self.disk_usage(),
                      'free': self.disk_free(),
                      'unit': 'MB'
                      },
            
            'time': datetime.datetime.now()
            }
        
class DHT22 (Sensors):
    def __init__(self, gpio_pin = 4):
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = gpio_pin
        super().__init__()
    
    def update (self):
        h, t = Adafruit_DHT.read_retry (self.DHT_SENSOR, self.DHT_PIN)
        self.data = {
            'name': 'DHT22',
            'Temperature': round (t, 3),
            'Humadity' : round (h, 3)
            }
        

dht22_gpio = 4

db = MongoDB()
dht22 = DHT22(dht22_gpio)
pi_ = pi_core ()

update_freq = 30 #seconds

while (True):
    data = pi_.__next__()
    db.insert('pi3', data)
    print (data)
    data = dht22.__next__()
    db.insert ('sensors', data)
    print (data)
    time.sleep(update_freq)
    break
