## RaspberryPi
This is a step-wise to setup Raspberry Pi for deep learning applications.
* Python 3.7, Tesnorflow 1.8
#### Install [raspbian OS](https://www.raspberrypi.org/downloads/raspbian/)
#### Setup Python on Pi
Download this directory and run [step.sh](https://github.com/mohbattharani/RaspberryPi/blob/master/setup.sh) file on terminal.
```
$ git clone https://github.com/mohbattharani/RaspberryPi.git
$ cd RaspberryPi
$ chmod +x setup.sh
$ sudo ./setup.sh 
```
#### Install OpenCV 4

Update the swap memory size in `dphys-swapfile` file 
```
sudo nano /etc/dphys-swapfile
CONF_SWAPSIZE=2048
```
and restart the service.
```
$ sudo /etc/init.d/dphys-swapfile stop
$ sudo /etc/init.d/dphys-swapfile start
```
Run [opencv4.sh](https://github.com/mohbattharani/RaspberryPi/blob/master/opencv4.sh) file in the terminal as 
```
$ chmod +x opencv4.sh
$ sudo ./opencv4.sh 
```
#### Install Tensorflow
Run [tf4.sh](https://github.com/mohbattharani/RaspberryPi/blob/master/tf4.sh) file in the terminal as 
```
$ chmod +x tf4.sh
$ sudo ./tf4.sh 
```
