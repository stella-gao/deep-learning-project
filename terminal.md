* ssh nksg@login.xsede.org


Please login to this system using your XSEDE username and password:


* password:[password]
* gsissh xstream


[xs-nksg@xstream-ln02 ~]$


* cd $WORK


[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$


* ls
* mkdir DeepSEA


```
sftp xg54@afs1.njit.edu

sftp> put C:\\Users\\Xin\\Desktop\\submit.sh
Uploading C:\Users\Xin\Desktop\submit.sh to /afs/cad.njit.edu/u/x/g/xg54/submit.sh
C:\Users\Xin\Desktop\submit.sh 

sftp> get submit.sh ./DanQ
Fetching /afs/cad.njit.edu/u/x/g/xg54/submit.sh to ./DanQ/submit.sh
/afs/cad.njit.edu/u/x/g/xg54/submit.sh                                                                        100%  241     0.2KB/s   00:00
sftp> exit

```

```
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$ cd DanQ
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/DanQ]$ ls
DanQ_seya  DanQ_seya.tar.gz  submit.sh
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/DanQ]$ less submit.sh
#!/bin/bash
#
#SBATCH --job-name=danq_nn
#SBATCH --output=res.txt
#SBATCH --workdir=/cstor/xsede/users/xs-nksg/DanQ
#SBATCH --time=2-00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=65536
#SBATCH --gres gpu:1
ml foss/2015.05
ml HDF5/1.8.15-patch1
ml scipy/0.16.1-Python-2.7.9
ml Theano/0.8.2-Python-2.7.9-noMPI

The following have been reloaded with a version change:
  1) cuDNN/4.0 => cuDNN/5.0-CUDA-7.5.18
  
```
```
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/DanQ]$ ls -alh /home/xsede/users/xs-nksg
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/DanQ]$ vi .theanorc
:quit[ENTER]
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/DanQ]$ squeue -u xs-nksg

```

* pwd
* cd DeepSEA
* wget http://deepsea.princeton.edu/media/code/deepsea_train_bundle.v0.9.tar.gz
* tar -xvzf deepsea_train_bundle.v0.9.tar.gz
* cd deepsea_train/
* module load torch/20160414-cbb5161 HDF5/1.8.15-patch1 MATIO/1.5.8
* less run.sh
* sh run.sh
* th
* du -sh *mat


remove the whole folder
* rm -rf TORCS/


check the remaining spaces of GPU
```
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$ nvidia-smi
```

Install packages
```
pip2.7 install --upgrade --user numpy
```


