```
ssh ****@login.xsede.org
password:[password]
gsissh xstream
cd $WORK
ls
mkdir Deeplearning
```

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

ml foss/2015.05
ml HDF5/1.8.15-patch1
ml scipy/0.16.1-Python-2.7.9
ml Theano/0.8.2-Python-2.7.9-noMPI
```

```
ls -alh /home/xsede/users/xs-nksg
vi .theanorc
squeue -u xs-nksg

```

* pwd
* wget http://deepsea.princeton.edu/media/code/deepsea_train_bundle.v0.9.tar.gz
* tar -xvzf deepsea_train_bundle.v0.9.tar.gz
* module load torch/20160414-cbb5161 HDF5/1.8.15-patch1 MATIO/1.5.8
* th
* du -sh *mat


remove the whole folder
```
rm -rf TORCS/
```

check the remaining spaces of GPU
```
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$ nvidia-smi
```

Install packages
```
pip2.7 install --upgrade --user numpy
```

submit jobs
```
#!/bin/bash
#SBATCH --job-name=[this job file name]
#SBATCH --output=./output/[output file name.txt]
#SBATCH --workdir=/cstor/xsede/users/[current dir]
#SBATCH --time=2-00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=16000
#SBATCH --gres gpu:1

ml foss/2015.05
ml HDF5/1.8.15-patch1
ml scipy/0.16.1-Python-2.7.9
ml Theano/0.8.2-Python-2.7.9-noMPI
python [program].py [parameters]


sbatch PLEK_job.txt
squeue | grep nksg
scancel [jobid]
```

How to append contents of multiple files into one file: You need the cat (short for concatenate) command, with shell redirection (>) into your output file

```
cat 1.txt 2.txt 3.txt > 0.txt
```
