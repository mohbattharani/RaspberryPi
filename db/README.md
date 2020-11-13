## setup
To setup mongodb on PI-3, I followed [rpi3-mongodb3](https://github.com/andresvidal/rpi3-mongodb3). 
#### pull MongoDB 
``` $ docker pull mohbattharani/mongodb-pi3 ```
#### run container with authorization enabled. 
Using authorized db even on local system is good practice for building real system in future. 
``` 
$ docker run -d --name mongodb --restart unless-stopped -v ~/data/db:/data/db -v ~/data/configdb:/data/configdb \ 
-p 27017:27017 -p 28017:28017 mohbattharani/mongodb-pi3 mongod --auth 
``` 
Now, create users from container terminal as follows. Here, user `pi` has admin right, can create or delete database. *sensors* is name of database.
          
```
$ docker exec -it mongodb mongo admin
$ db.createUser({ user: "pi", pwd: "pi1234", roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] })
$ db.createUser({ user: "pi", pwd: "pi1234", roles: [{ role: "dbOwner", db: "sensors" }] })

```

From terminal login db as: ```$ db.auth("pi", "pi1234")```
On successful long, it will return `1`

After you have added users, make sure you restart container to ensure the policies are applied.
```
$ docker kill --signal=SIGINT rpi3-mongodb3
$ docker start rpi3-mongodb3
```
## MonogDB Simple example 
Python script *pymongo* can be used to dump the data into MongoDB. A sample script is given in `mongo.py` file. 
For reference see [meduim](https://medium.com/swlh/how-to-run-mongodb-on-local-network-using-a-raspberry-pi-and-docker-4e5c4379cea2)

## Log system information
To illustrate a much better example, `system_info_mongodb.py` can be used to log the system information. The example was created to log *CPU*, *RAM* and *Disk* status of Raspberry Pi 3. The same script can be used log information of any system.
