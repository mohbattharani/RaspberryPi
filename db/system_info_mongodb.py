import pymongo
import time, datetime
import os, psutil
import cfg

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
        return round (kbs/1024.0/1024.0, 1)
    def to_gb(self, kbs):
        return round (kbs/1024.0/1024.0/1024.0, 1)
    
    def cpu_usage(self):
        return round (psutil.cpu_percent(), 1)
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
        total = self.to_gb(disk.total)
        free = self.to_gb (disk.free)
        return round (total - free, 1)
    
    def disk_free (self):
        disk = psutil.disk_usage('/')
        free = self.to_gb (disk.free)
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
                      'unit': 'GB'
                      },
            
            'time': datetime.datetime.now()
            }
        

db = MongoDB()
pi_ = pi_core ()

update_freq = 30 #seconds

while (True):
    data = pi_.__next__()
    db.insert('pi3', data)
    print (data)
    time.sleep(update_freq)
    break
