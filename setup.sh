# RUN this sh file to setup OPENCV on it.

#sudo apt-get update
#sudo apt-get upgrade -y
#sudo apt-get install build-essential cmake pkg-config -y
#sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev -y

#sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
#sudo apt-get install libxvidcore-dev libx264-dev

#sudo apt-get install libfontconfig1-dev libcairo2-dev 
#sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev -y
#sudo apt-get install libgtk2.0-dev libgtk-3-dev -y
#sudo apt-get install libatlas-base-dev gfortran -y

#sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103 -y
#sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5 -y

#sudo apt-get install python3-dev -y

wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py -y
sudo python3 get-pip.py -y
sudo rm -rf ~/.cache/pip -y
pip install opencv-contrib-python==4.1.0.25 -y

pip install numpy


