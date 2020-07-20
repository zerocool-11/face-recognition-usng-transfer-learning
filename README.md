# face-recognition-usng-transfer-learning


####  here the transfer learning means we will use a pre trained model weights and train our model using that weights it will use less resources and works effectively   for this you can use any models -
* MobileNet
* ResNet
* VGG16
#### i used VGG16 for this 

![alt text](https://github.com/zerocool-11/face-recognition-usng-transfer-learning/blob/master/vgg.png)

#### first of all i used dataset.py to generate dataset of my face  

![alt text](https://github.com/zerocool-11/face-recognition-usng-transfer-learning/blob/master/train_data.png)

### then after that i used train.ipynb  file in order to train my model 

#### here is my model

![alt text](https://github.com/zerocool-11/face-recognition-usng-transfer-learning/blob/master/model-transfer-learning.png)

#### i got good accuracy after training the model

![alt text](https://github.com/zerocool-11/face-recognition-usng-transfer-learning/blob/master/acc-transer-learning.png)

#### here i runned my whole code on google collab it gives you good gpu and ram with a juoyter notebook so after this just save your model and load it use by using model.predict() function  
##### In my github repo i added both code file you can use it to train according  to you face
