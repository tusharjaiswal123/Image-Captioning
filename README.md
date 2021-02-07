# Image-Captioning
Image Captioning is the process of generating textual description of an image. In this project i have generated Captions for Images using ML, Computer Vision and Deep learning algorithms



### About the Dataset
Can download the dataset from here- https://www.kaggle.com/shadabhussain/flickr8k?select=Flickr_Data
1. Flikr8k_Dataset (Contains Images)
2. Flikr8k_text (Contains Text)
Dataset contains 8000 images, of which 6000 are used for training purpose and remaining for validattion and testing.
Each image has almost 5 captions in Flickr8k.txt. This means in total there are 8000*5=40000 captions in the text file Flikr8k_token.txt



### Steps taken in the project
1.Data collection<br>
2.Understanding the data<br>
3.Data Cleaning<br>
4.Loading the training set<br>
5.Data Preprocessing — Images<br>
6.Data Preprocessing — Captions<br>
7.Data Preparation using Generator Function<br>
8.Word Embeddings<br>
9.Model Architecture<br>
10.Inference<br>


### Model Architecture

![alt text](https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/encoder-decoder.png)



## Explaining Encoder and Decoder
  ## Encoder: 
  ![alt text](https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/encoder.png)
  For Encoder we use ResNet-50. ResNet-50 is a convolutional neural network that is trained on more than a million images from the ImageNet database. The network is 50 layers deep and can classify images into 1000 object categories, such as keyboard, mouse, pencil, and many animals. As a result, the network has learned rich feature representations for a wide range of images. The network has an image input size of 224-by-224.   

## Decode:
![alt text](https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/decoder.png)
For Decoder we use LSTM. Long Short-Term Memory (LSTM) networks are a modified version of recurrent neural networks, which makes it easier to remember past data in memory. The vanishing gradient problem of RNN is resolved here. LSTM is well-suited to classify, process and predict time series given time lags of unknown duration. It trains the model by using back-propagation


## Results
Following are a few results obtained after training the model for 70 epochs.

Image | Caption 
--- | --- 
<img src="https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/2461616306_3ee7ac1b4b.jpg" width="400"> | **Generated Caption:** boy in blue swim trunks jumps into pool.
<img src="https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/3384314832_dffc944152.jpg" width="400"> | **Generated Caption:** small dog jumps over an obstacle.
<img src="https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/3071676551_a65741e372.jpg" width="400"> | **Generated Caption:** surfer is falling off wave.
<img src="https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/491405109_798222cfd0.jpg" width="400"> | **Generated Caption:** little girl in pink dress is laying on her head.
<img src="https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/3108197858_441ff38565.jpg" width="400"> | **Generated Caption:** group of children are posing for picture.
<img src="https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/2301525531_edde12d673.jpg" width="400"> | **Generated Caption:** black dog running through snow.
<img src="https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/0495-0707-0215-4554.jpg" width="400"> | **Generated Caption:** man on motorcycle riding on road.
<img src="https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/738020db6a97154799_0x0.jpg" width="400"> | **Generated Caption:** the basketball player in the orange uniform is trying to make shot.
<img src="https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/_441157258.jpg" width="400"> | **Generated Caption:** child in red coat is skiing down snowy hill.
<img src="https://github.com/tusharjaiswal123/Image-Captioning/blob/main/image/e2c5c0f9fca16d68007.jpg" width="400"> | **Generated Caption:** soccer player in red uniform about to hit ball.
