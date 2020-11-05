If the you install headless "raspbian OS" then there are multiple way to connect it with the network. 

###### Method -1: Connect LCD and login through terminal. In the terminal window you have following options:
* 1. Use the command to add the network: `sudo ifconfig eth0 192.168.72.6 netmask 255.255.255.0` Without network mask it should work. 




References: 
* [1] https://vitux.com/ubuntu-network-configuration/
