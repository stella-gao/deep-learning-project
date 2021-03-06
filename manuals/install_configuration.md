http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#pre-installation-actions

http://www.pyimagesearch.com/2016/07/18/installing-keras-for-deep-learning/

http://www.pyimagesearch.com/2016/07/04/how-to-install-cuda-toolkit-and-cudnn-for-deep-learning/

https://www.tensorflow.org/versions/r0.10/get_started/os_setup

https://developer.nvidia.com/cuda-downloads

https://developer.nvidia.com/rdp/cudnn-download

http://www.nvidia.com/object/gpu-accelerated-applications-tensorflow-installation.html

http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#abstract

```
# pre install
sudo apt update
sudo apt upgrade
sudo apt install -y python-dev python-pip python-nose gcc g++ git gfortran vim
sudo apt install -y libopenblas-dev liblapack-dev libatlas-base-dev
sudo apt-get install -y build-essential git libblas-dev libopencv-dev


# install cuda from https://developer.nvidia.com/cuda-downloads
wget https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda-repo-ubuntu1404-8-0-local-ga2_8.0.61-1_amd64-deb
sudo dpkg -i cuda-repo-ubuntu1404-8-0-local-ga2_8.0.61-1_amd64.deb
sudo apt-get update
sudo apt-get install cuda


# Install NVIDIA drivers from NVIDIA
# Download and install latest drivers
wget http://us.download.nvidia.com/XFree86/Linux-x86_64/375.20/NVIDIA-Linux-x86_64-375.20.run
chmod +x NVIDIA-Linux-x86_64-375.20.run
sudo ./NVIDIA-Linux-x86_64-375.20.run

# Install NVIDIA drivers from Ubuntu
sudo apt install ubuntu-drivers-common
# list the devices
ubuntu-drivers devices
# or install automatically
sudo ubuntu-drivers autoinstall
# or
sudo apt-get purge nvidia*
sudo add-apt-repository ppa:graphics-drivers
sudo apt-get update
sudo apt-get install nvidia-375


uname -a
lsmod | grep nvidia
# If there is no output, then your installation has probably failed. It is also possible that the driver is not available in your system's driver database. You can run the following command to check if your system is running on the open source driver nouveau. If the output is negative for nouveau, then all is well with your installation.
lsmod | grep nouveau 


# Install Theano
sudo apt-get install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git
sudo pip install Theano
sudo pip install numpy scipy
sudo pip install scikit-learn
sudo pip install pillow
python -c "import keras; print keras.__version__"


sudo apt-get install libhdf5-dev
pip install h5py




# Install common tools from the scipy stack
sudo apt-get install -y libfreetype6-dev libpng12-dev
pip install -U matplotlib ipython[all] pandas scikit-image

# Install Nvidia drivers, CUDA and CUDA toolkit, following some instructions from http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
# wget http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb # Got the link at https://developer.nvidia.com/cuda-downloads
# sudo dpkg -i cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb
sudo apt-get update
sudo apt-get install cuda
cat /usr/local/cuda/version.txt

lspci | grep -i nvidia
uname -m && cat /etc/*release
gcc --version
uname -r
sudo apt-get install linux-headers-$(uname -r)

# Ubuntu/Linux 64-bit
sudo apt-get install python-pip python-dev

# Ubuntu/Linux 64-bit, GPU enabled, Python 2.7
# Requires CUDA toolkit 7.5 and CuDNN v5. For other versions, see "Install from sources" below.
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl

sudo pip install --upgrade $TF_BINARY_URL


vi ~/.keras/keras.json
'''
{
    "image_dim_ordering": "tf", 
    "epsilon": 1e-07, 
    "floatx": "float32", 
    "backend": "tensorflow"
}
{
    "image_dim_ordering": "th",
    "epsilon": 1e-07,
    "floatx": "float32",
    "backend": "theano"
}
'''
python -c "from keras import backend; print backend._BACKEND"
＃specify the backend to use by Keras on the command line by specifying the KERAS_BACKEND environment variable, as follows:
KERAS_BACKEND=theano python -c "from keras import backend; print(backend._BACKEND)"

# update python from 2.7.6 to 2.7.12
sudo add-apt-repository ppa:fkrull/deadsnakes-python2.7
sudo apt-get update
sudo apt-get install python2.7
python --version


wget https://web.njit.edu/~xg54/cudnn-8.0-linux-x64-v6.0.tgz
cd ~
tar -zxf cudnn-8.0-linux-x64-v6.0.tgz
cd cuda
sudo cp lib64/* /usr/local/cuda/lib64/
sudo cp include/* /usr/local/cuda/include/



```

```
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 14.04.5 LTS
Release:        14.04
Codename:       trusty
$ ls -l /usr/local/cuda/lib64/libcud*
-rw-r--r-- 1 root root   556000  1月 27 07:48 /usr/local/cuda/lib64/libcudadevrt.a
lrwxrwxrwx 1 root root       16  1月 27 07:51 /usr/local/cuda/lib64/libcudart.so -> libcudart.so.8.0
lrwxrwxrwx 1 root root       19  1月 27 07:51 /usr/local/cuda/lib64/libcudart.so.8.0 -> libcudart.so.8.0.61
-rw-r--r-- 1 root root   415432  1月 27 07:48 /usr/local/cuda/lib64/libcudart.so.8.0.61
-rw-r--r-- 1 root root   775162  1月 27 07:48 /usr/local/cuda/lib64/libcudart_static.a
-rwxr-xr-x 1 root root 98851840  5月  9 05:08 /usr/local/cuda/lib64/libcudnn.so
-rwxr-xr-x 1 root root 98851840  5月  9 05:08 /usr/local/cuda/lib64/libcudnn.so.6
-rwxr-xr-x 1 root root 98851840  5月  9 05:08 /usr/local/cuda/lib64/libcudnn.so.6.0.21
$ git rev-parse HEAD
70de76e696c21da617fd2e6435cf7fedab220db8
$ bazel version
Build label: 0.4.5
Build target: bazel-out/local-fastbuild/bin/src/main/java/com/google/devtools/build/lib/bazel/BazelServer_deploy.jar
Build time: Thu Mar 16 12:19:38 2017 (1489666778)
Build timestamp: 1489666778
Build timestamp as int: 1489666778
```

```
$ sudo apt-get install software-properties-common swig 
$ sudo add-apt-repository ppa:webupd8team/java 
$ sudo apt-get update 
$ sudo apt-get install oracle-java8-installer 
$ echo "deb http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list 
$ curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | sudo apt-key add - 
$ sudo apt-get update 
$ sudo apt-get install bazel 

$ git clone https://github.com/tensorflow/tensorflow
$ cd tensorflow 
$ git reset --hard 

$ ./configure
Please specify the location of python. [Default is /usr/bin/python]: 
Found possible Python library paths:
  /usr/local/lib/python2.7/dist-packages
  /usr/lib/python2.7/dist-packages
Please input the desired Python library path to use.  Default is [/usr/local/lib/python2.7/dist-packages]

Using python library path: /usr/local/lib/python2.7/dist-packages
Do you wish to build TensorFlow with MKL support? [y/N] 
No MKL support will be enabled for TensorFlow
Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -march=native]: 
Do you wish to use jemalloc as the malloc implementation? [Y/n] 
jemalloc enabled
Do you wish to build TensorFlow with Google Cloud Platform support? [y/N] 
No Google Cloud Platform support will be enabled for TensorFlow
Do you wish to build TensorFlow with Hadoop File System support? [y/N] 
No Hadoop File System support will be enabled for TensorFlow
Do you wish to build TensorFlow with the XLA just-in-time compiler (experimental)? [y/N] 
No XLA support will be enabled for TensorFlow
Do you wish to build TensorFlow with VERBS support? [y/N] 
No VERBS support will be enabled for TensorFlow
Do you wish to build TensorFlow with OpenCL support? [y/N] 
No OpenCL support will be enabled for TensorFlow
Do you wish to build TensorFlow with CUDA support? [y/N] y
CUDA support will be enabled for TensorFlow
Do you want to use clang as CUDA compiler? [y/N] y
Clang will be used as CUDA compiler
Please specify which clang should be used as device and host compiler. [Default is /usr/bin/clang]: 
Please specify the CUDA SDK version you want to use, e.g. 7.0. [Leave empty to use system default]: 
Please specify the location where CUDA  toolkit is installed. Refer to README.md for more details. [Default is /usr/local/cuda]: 
Please specify the cuDNN version you want to use. [Leave empty to use system default]: 
Please specify the location where cuDNN  library is installed. Refer to README.md for more details. [Default is /usr/local/cuda]: 
Please specify a list of comma-separated Cuda compute capabilities you want to build with.
You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.
Please note that each additional compute capability significantly increases your build time and binary size.
[Default is: "3.5,5.2"]: 5.2,6.1                     
INFO: Starting clean (this may take a while). Consider using --async if the clean takes more than several minutes.
Configuration finished

$ wget https://ci.tensorflow.org/view/Nightly/job/nightly-matrix-linux-gpu/TF_BUILD_IS_OPT=OPT,TF_BUILD_IS_PIP=PIP,TF_BUILD_PYTHON_VERSION=PYTHON2,label=gpu-linux/lastSuccessfulBuild/artifact/pip_test/whl/tensorflow_gpu-1.1.0-cp27-none-linux_x86_64.whl
$ sudo pip install --upgrade tensorflow_gpu-1.1.0-cp27-none-linux_x86_64.whl
```

```
python -c 'import tensorflow as tf; print(tf.__version__)'
```
vi ~/.bashrc
```
# added by Anaconda2 4.0.0 installer
#export PATH="/home/terry/anaconda2/bin:$PATH"
#export CAFFE_ROOT=/home/terry/pkgs/caffe
#export PYTHONPATH=$CAFFE_ROOT/python:$PYTHONPATH
export PATH="/home/terry/pkgs/bedtools2/bin:$PATH"
export PATH="/home/terry/pkgs/samtools-1.3.1:$PATH"
export PATH=/home/terry/pkgs/meme/bin:$PATH
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"
export CUDA_HOME=/usr/local/cuda
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:$CUDA_HOME/lib"
export PATH="$CUDA_HOME/bin:$PATH"
```
source ~/.profile

```
lspci | grep -i nvidia 
uname -m && cat /etc/*release
gcc --version



# Check your boot partition 
df -h
# Get your current kernel 
uname -r
# List installed kernels 
dpkg --list 'linux-image*'
# Remove some of them
sudo apt-get remove  linux-image-4.4.0-21-generic linux-image-4.4.0-45-generic linux-image-4.4.0-47-generic linux-image-4.4.0-51-generic
# You can erase manually the kernels you do not need
rm /boot/vmlinuz-4.4.0-42-generic
# Remove also your NVIDIA drivers
sudo apt-get purge nvidia*
# Remove the packages that you don’t need anymore
sudo apt-get autoremove
# update
sudo apt-get update && sudo apt-get -y upgrade


sudo apt-get install linux-headers-$(uname -r)
```
print the versions of installed libraries
```
import scipy
print('scipy: {}'.format(scipy.__version__))
import numpy
print('numpy: {}'.format(numpy.__version__))
import matplotlib
print('matplolib: {}'.format(matplotlib.__version__))
import pandas
print('pandas: {}'.format(pandas.__version__))
import sklearn
print('sklearn: {}'.format(sklearn.__version__))
```
check the cuda version
```
nvcc --version
# if the version is old, then try to use the commands
export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}$ 
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

### for mac
1. http://www.pyimagesearch.com/2016/11/28/macos-install-opencv-3-and-python-2-7/
2. https://stackoverflow.com/questions/20518632/importerror-numpy-core-multiarray-failed-to-import

### for ubuntu
1. http://pythoncentral.io/how-to-install-virtualenv-python/
