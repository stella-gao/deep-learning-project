```sh
git clone https://github.com/jhjin/tensorflow-cpp.git
cd tensorflow-cpp/
ll
mkdir lib
mkdir include
cp /usr/local/cuda-8.0/lib64/libcudnn.so.5 lib/
cp /usr/local/cuda-8.0/include/cudnn.h lib/
mkdir build
cd build
cmake ..
make -j`nproc`
ll
cd ..
ll
ll lib/
ll include/
make clean
make
echo $LD_LIBRARY_PATH
export LB_LIBRARY_PATH=$LD_LIBRARY_PATH:./lib && CUDA_VISIBLE_DEVICES=0
echo $LD_LIBRARY_PATH
./app data/grace_hopper.jpg

```
