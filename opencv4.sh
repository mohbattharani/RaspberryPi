
# Update the swap memory size
# sudo nano /etc/dphys-swapfile
# CONF_SWAPSIZE=2048
#sudo /etc/init.d/dphys-swapfile stop
#sudo /etc/init.d/dphys-swapfile start
# chmod +x opencv4.sh

cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.1.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.1.zip
unzip opencv.zip
unzip opencv_contrib.zip
mv opencv-4.1.1 opencv
mv opencv_contrib-4.1.1 opencv_contrib


cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D CMAKE_SHARED_LINKER_FLAGS=-latomic \
    -D BUILD_EXAMPLES=OFF ..

make -j4

sudo make install
sudo ldconfig

cd /usr/local/lib/python3.7/site-packages/cv2/python-3.7
sudo mv cv2.cpython-37m-arm-linux-gnueabihf.so cv2.so
cd ~/.virtualenvs/cv/lib/python3.7/site-packages/
ln -s /usr/local/lib/python3.7/site-packages/cv2/python-3.7/cv2.so cv2.so

pip install opencv-contrib-python

