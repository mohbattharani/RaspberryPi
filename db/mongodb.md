## setup
To setup mongodb on PI-3, I followed [rpi3-mongodb3](https://github.com/andresvidal/rpi3-mongodb3). 
#### pull MongoDB 
``` docker push mohbattharani/mongodb-pi3 ```
#### run container with authorization enabled. 
Using authorized db even on local system is good practice for building real system in future. 
``` 
docker run -d --name mongodb --restart unless-stopped -v ~/data/db:/data/db -v ~/data/configdb:/data/configdb \ 
-p 27017:27017 -p 28017:28017 mohbattharani/mongodb-pi3 mongod --auth 
``` 
Now, create users from container terminal as follows. Here, user 'pi' has admin right, can create or delete database.
          
```docker exec -it mongodb mongo admin ```
```db.createUser({ user: "pi", pwd: "pi1234", roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] })```

From terminal login db as: ```db.auth("pi", "pi1234")```
