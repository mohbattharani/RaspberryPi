'''
db = name of the database in which data from all the sensor nodes will be stored.
Here, we consider there might be more than one nodes storing the data on one database.

node = It is the node that sends some data. Right now, consider Pi-3 on which this
script is running is one of the nodes. Rest of the nodes might send data to this Pi
gate way either throguh pub-sub service, http or any other protocol.

usr = The name of user having rights of 'dbOwner'
host = right now its local, it could be over network. 

'''

mongo_server_cfg ={
      'host': 'localhost',
      'port': 27017,
      'usr' : 'usr',
      'pwd': 'pi1234'
     }

db = {
    'name':'sensors'
    }
node = {
    'name': 'cvlab'
    }