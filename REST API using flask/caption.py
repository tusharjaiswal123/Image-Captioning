#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import *
from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.models import Model, load_model
from keras.preprocessing import image
import pickle


# In[3]:


model = load_model("model_weights/model_70.h5")


# In[4]:


model_temp = ResNet50(weights="imagenet",input_shape=(224,224,3))


# In[5]:


model_resnet = Model(model_temp.input,model_temp.layers[-2].output)


# In[6]:


def preprocess_img(img):
    img = image.load_img(img,target_size=(224,224))
    img = image.img_to_array(img)
    img = np.expand_dims(img,axis=0) # reshape to (1,224,224,3)
    # Noramalisation
    img = preprocess_input(img)
    return img


# In[7]:


def encode_img(img):
    img = preprocess_img(img)
    feature_vector = model_resnet.predict(img)
    feature_vector = feature_vector.reshape((1,-1))
    return feature_vector


# In[10]:


with open('word_to_idx.pkl',"rb") as f:
    word_to_idx = pickle.load(f)
    
with open('idx_to_word.pkl',"rb") as f:
    idx_to_word = pickle.load(f)


# In[11]:


def predict_caption(photo):
    
    max_len = 33
    in_text = "startseq"
    for i in range(max_len):
        sequence = [word_to_idx[w] for w in in_text.split() if w in word_to_idx]
        sequence = pad_sequences([sequence],maxlen=max_len,padding='post')
        
        ypred = model.predict([photo,sequence])
        ypred = ypred.argmax() # word with max prob always
        word = idx_to_word[ypred]
        in_text += ' ' + word
        
        if word == 'endseq':
            break
    
    final_caption = in_text.split()[1:-1]
    final_caption = ' '.join(final_caption)
    
    return final_caption


# In[15]:

def caption_this_image(image):
	enc = encode_img(image)
	caption = predict_caption(enc)
	
	return caption




