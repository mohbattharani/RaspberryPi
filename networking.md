If the you install headless "raspbian OS" then there are multiple way to connect it with the network. 

* Add empty ssh file in the root of memory card to enable ssh. The "ssh" file should be empty and with no extension.

###### Method 1:
Connect LCD and login through terminal. In the terminal window you have following options:
* Use the command to add the network: `sudo ifconfig eth0 192.168.72.6 netmask 255.255.255.0` Without network mask it should work. 


###### Method 2:


References: 
* [1] https://vitux.com/ubuntu-network-configuration/
