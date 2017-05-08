http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#pre-installation-actions

http://www.pyimagesearch.com/2016/07/18/installing-keras-for-deep-learning/

https://www.tensorflow.org/versions/r0.10/get_started/os_setup

https://developer.nvidia.com/cuda-downloads

https://developer.nvidia.com/rdp/cudnn-download




http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#abstract

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
sudo pip install numpy scipy
sudo pip install scikit-learn
sudo pip install pillow
sudo pip install h5py
python -c "import keras; print keras.__version__"

# Install Nvidia drivers, CUDA and CUDA toolkit, following some instructions from http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
wget http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb # Got the link at https://developer.nvidia.com/cuda-downloads
sudo dpkg -i cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb
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

# update python from 2.7.6 to 2.7.12
sudo add-apt-repository ppa:fkrull/deadsnakes-python2.7
sudo apt-get update
sudo apt-get install python2.7
python --version

wget http://developer2.download.nvidia.com/compute/machine-learning/cudnn/secure/v6/prod/8.0_20170427/cudnn-8.0-linux-x64-v6.0.tgz?JzRV9lJ6NXf7C3xvAjnDlMuFnqy4aM0N2AyiLa1ENSXPlXFyaQNUlLPjovGNvFakc34E6qd2m-1FkK25ODMGCwSzwD35JovZHyTCiHyGuUw64vpP6j2sg-0GrHCOr2MoFqGiAlecBA6Xo8ulUIRoXE4RGecU785FzIgvj_J23O2EY9yP8IMZ_iQUigiGojWYago-NW59



```
