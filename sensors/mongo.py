import pymongo

client = pymongo.MongoClient ('mongodb://localhost:27017/',
                              username='usr', password ='pi1234',
                              authSource = 'sensors')
print (client)

sensorsdb = client ['sensors']
#collection = sensorsdb['cvlab']
print (sensorsdb)
#print (collection)

reading = {'Temperature': 37, 'Humadity': 25}
sensorsdb.cvlab.pi.insert_one (reading)

x = sensorsdb.cvlab.find_one ()
print (x)


#db.createUser ({user:'usr', pwd:'pi1234', roles:[{role:'dbOwner', db:'sensors'}]})

#db.createUser ({user:'admin', pwd:'pi1234', roles:[{role:'userAdminAnyDatabase', db:'admin'}]})