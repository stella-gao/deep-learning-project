##Building Protobuf

###Below versions of Protobuf are available in respective distributions at the time of creation of these build instructions:

```
Ubuntu 16.04 has 2.6.1
Ubuntu 16.10 has 3.0.0
The instructions provided below specify the steps to build Google Protobuf v3.3.0 on IBM z Systems for


Ubuntu (16.04, 16.10)
General notes:

When following the steps below please use a standard permission user unless otherwise specified.
A directory /<source_root>/ will be referred to in these instructions, this is a temporary writeable directory anywhere you'd like to place it
Step 1: Building Protobuf 3.3.0

1.1) Install the build time dependencies

Ubuntu (16.04, 16.10)
sudo apt-get install tar wget autoconf libtool automake g++ make git bzip2 curl unzip zlib1g-dev
You may already have these packages installed - just install any missing.


1.2) Clone the protobuf repository and checkout the correct version

cd /<source_root>/
git clone https://github.com/google/protobuf.git
cd protobuf
git checkout v3.3.0

1.3) Generate and then run the configuration

./autogen.sh
./configure

1.4) Build and test

make
make check
Note: There are 7 tests/suites. All 7 should pass

1.5) Install Protobuf and verify the installation

sudo make install
export LD_LIBRARY_PATH=/usr/local/lib
protoc --version
sudo ldconfig

Note: Protobuf should report version libproto 3.3.0

References:

https://developers.google.com/protocol-buffers/
https://github.com/google/protobuf/
```
