http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#pre-installation-actions
```
sudo apt update
sudo apt upgrade
sudo apt install -y python-dev python-pip python-nose gcc g++ git gfortran vim
sudo apt install -y libopenblas-dev liblapack-dev libatlas-base-dev
sudo apt-get install -y build-essential git libblas-dev libopencv-dev

git clone --recursive https://github.com/dmlc/mxnet

wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.5-18_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1404_7.5-18_amd64.deb
sudo apt-get update
sudo apt-get install cuda

sudo apt-get purge nvidia*
sudo add-apt-repository ppa:graphics-drivers
sudo apt-get update

uname -a
sudo apt-get install nvidia-375
lsmod | grep nvidia
# If there is no output, then your installation has probably failed. It is also possible that the driver is not available in your system's driver database. You can run the following command to check if your system is running on the open source driver nouveau. If the output is negative for nouveau, then all is well with your installation.
lsmod | grep nouveau 

sudo apt-get install nvidia-cuda-toolkit
sudo nvidia-smi

# Install Theano
sudo apt-get install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git
sudo pip install Theano

# Install Nvidia drivers, CUDA and CUDA toolkit, following some instructions from http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
wget http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb # Got the link at https://developer.nvidia.com/cuda-downloads
sudo dpkg -i cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb
sudo apt-get update
sudo apt-get install cuda

export PATH=/usr/local/cuda-5.5/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-5.5/lib64:$LD_LIBRARY_PATH

lspci | grep -i nvidia
uname -m && cat /etc/*release
gcc --version
uname -r
sudo apt-get install linux-headers-$(uname -r)


```
