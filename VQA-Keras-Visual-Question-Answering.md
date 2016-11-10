https://github.com/anantzoid/VQA-Keras-Visual-Question-Answering
http://www.visualqa.org/download.html


```linux

[Xin.Lenovo-Xin] ➤ ssh nksg@login.xsede.org
Please login to this system using your XSEDE username and password:
password:

[nksg@ssohub ~]$ gsissh xstream
[xs-nksg@xstream-ln02 ~]$ cd $WORK
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$ ls
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$ ml foss/2015.05
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$ ml HDF5/1.8.15-patch1
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$ ml scipy/0.16.1-Python-2.7.9
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$ ml Theano/0.8.2-Python-2.7.9-noMPI
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$ mkdir VQA-Keras-Visual-Question-Answering
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$ ls
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg]$ cd VQA-Keras-Visual-Question-Answering/

[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ sftp xg54@afs1.njit.edu
xg54@afs1.njit.edu's password:
Connected to afs1.njit.edu
sftp> get model_weights.h5
sftp> exit

[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ wget http://nlp.stanford.edu/data/glove.6B.zip

[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ wget https://filebox.ece.vt.edu/~jiasenlu/codeRelease/vqaRelease/train_only/data_train_val.zip

[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ wget http://visualqa.org/data/mscoco/vqa/Annotations_Val_mscoco.zip

[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ wget https://github.com/anantzoid/VQA-Keras-Visual-Question-Answering/raw/master/train.py

[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ wget https://github.com/anantzoid/VQA-Keras-Visual-Question-Answering/raw/master/models.py

[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ wget https://github.com/anantzoid/VQA-Keras-Visual-Question-Answering/raw/master/constants.py

[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ wget https://github.com/anantzoid/VQA-Keras-Visual-Question-Answering/raw/master/prepare_data.py

[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ unzip Annotations_Val_mscoco.zip
Archive:  Annotations_Val_mscoco.zip
  inflating: mscoco_val2014_annotations.json
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ unzip data_train_val.zip
Archive:  data_train_val.zip
  inflating: data_img.h5
  inflating: data_prepro.h5
  inflating: data_prepro.json
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ unzip glove.6B.zip
Archive:  glove.6B.zip
  inflating: glove.6B.50d.txt
  inflating: glove.6B.100d.txt
  inflating: glove.6B.200d.txt
  inflating: glove.6B.300d.txt
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ mkdir data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ mv mscoco_val2014_annotations.json ./data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ mv data_img.h5 ./data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ mv data_prepro.h5 ./data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ mv data_prepro.json ./data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ mv glove.6B.100d.txt ./data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ mv glove.6B.200d.txt ./data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ mv glove.6B.300d.txt ./data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ mv glove.6B.50d.txt ./data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ mv model_weights.h5 ./data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ mv *.zip ./data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ cd data/
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ mkdir Questions_Train_mscoco
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ mv mscoco_val2014_annotations.json ./Questions_Train_mscoco/
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ cd Questions_Train_mscoco/
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data/Questions_Train_mscoco]$ cp mscoco_val2014_annotations.json 1.json
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data/Questions_Train_mscoco]$ mv 1.json MultipleChoice_mscoco_train2014_questions.json

[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data/Questions_Train_mscoco]$ cd ..
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ mkdir ckpts
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ cd ckpts
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data/ckpts]$ cd ..
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ mv model_weights.h5 ./ckpts/
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ mkdir validation_data
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ mv Questions_Train_mscoco/mscoco_val2014_annotations.json ./validation_data/
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ cd validation_data/
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data/validation_data]$ cd ..
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ cd ckpts/
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data/ckpts]$ ls
model_weights.h5
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data/ckpts]$ cp model_weights.h5 1.h5
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data/ckpts]$ cd ..
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ mv ckpts/1.h5 ./
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ mv 1.h5 model_weights.h5
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ rm *.zip
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ rm -rf Questions_Train_mscoco/
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ wget http://visualqa.org/data/mscoco/vqa/Questions_Train_mscoco.zip

[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ unzip Questions_Train_mscoco.zip
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ rm *.zip
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ mkdir Questions_Train_mscoco
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ mv MultipleChoice_mscoco_train2014_questions.json ./Questions_Train_mscoco/
[xs-nksg@xstream-ln02 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering/data]$ mv OpenEnded_mscoco_train2014_questions.json ./Questions_Train_mscoco/

                                                                                                                                         
```


Open Next Time

```terminal
[Xin.Lenovo-Xin] ➤ ssh nksg@login.xsede.org
Please login to this system using your XSEDE username and password:
password:
[nksg@ssohub ~]$ gsissh xstream
[xs-nksg@xstream-ln01 ~]$ cd $WORK
[xs-nksg@xstream-ln01 /cstor/xsede/users/xs-nksg]$ ls
VQA-Keras-Visual-Question-Answering  
[xs-nksg@xstream-ln01 /cstor/xsede/users/xs-nksg]$ cd VQA-Keras-Visual-Question-Answering/
[xs-nksg@xstream-ln01 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ python
Python 2.7.9 (default, Apr 11 2016, 16:35:11)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import keras
Using Theano backend.
ERROR (theano.sandbox.cuda): ERROR: Not using GPU. Initialisation of device 2 failed:
Bad device number 2. Only 1 devices available.
Using gpu device 0: Tesla K80 (CNMeM is enabled with initial size: 10.0% of memory, cuDNN 5005)
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
[xs-nksg@xstream-ln01 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$ python train.py
Using Theano backend.
ERROR (theano.sandbox.cuda): ERROR: Not using GPU. Initialisation of device 2 failed:
Bad device number 2. Only 1 devices available.
Using gpu device 0: Tesla K80 (CNMeM is enabled with initial size: 10.0% of memory, cuDNN 5005)
Reading Data...
Creating Model...
Embedding Data...
Creating image model...
Creating text model...
Merging final model...
Loading Weights...
Epoch 1/10
215359/215359 [==============================] - 205s - loss: 1.4070 - acc: 0.6563   Epoch 00000: saving model to data/ckpts/model_weights.h5
Epoch 2/10
215359/215359 [==============================] - 205s - loss: 1.4307 - acc: 0.6566   Epoch 00001: saving model to data/ckpts/model_weights.h5
Epoch 3/10
215359/215359 [==============================] - 206s - loss: 1.4304 - acc: 0.6593   Epoch 00002: saving model to data/ckpts/model_weights.h5
Epoch 4/10
215359/215359 [==============================] - 205s - loss: 1.4269 - acc: 0.6630   Epoch 00003: saving model to data/ckpts/model_weights.h5
Epoch 5/10
215359/215359 [==============================] - 205s - loss: 1.4179 - acc: 0.6674   Epoch 00004: saving model to data/ckpts/model_weights.h5
Epoch 6/10
215359/215359 [==============================] - 205s - loss: 1.4097 - acc: 0.6705   Epoch 00005: saving model to data/ckpts/model_weights.h5
Epoch 7/10
215359/215359 [==============================] - 205s - loss: 1.3982 - acc: 0.6745   Epoch 00006: saving model to data/ckpts/model_weights.h5
Epoch 8/10
215359/215359 [==============================] - 206s - loss: 1.3871 - acc: 0.6781   Epoch 00007: saving model to data/ckpts/model_weights.h5
Epoch 9/10
215359/215359 [==============================] - 205s - loss: 1.3797 - acc: 0.6805   Epoch 00008: saving model to data/ckpts/model_weights.h5
Epoch 10/10
215359/215359 [==============================] - 205s - loss: 1.3689 - acc: 0.6845   Epoch 00009: saving model to data/ckpts/model_weights.h5
[xs-nksg@xstream-ln01 /cstor/xsede/users/xs-nksg/VQA-Keras-Visual-Question-Answering]$


```
