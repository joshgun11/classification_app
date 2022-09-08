
import sys
import keras
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re

model_path='models/base_line/base_line.h5'
tokenizer_path='models/base_line/tokenizer.pickle'

model = keras.models.load_model(model_path)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


with open(tokenizer_path, 'rb') as handle:
    tokenizer = pickle.load(handle)



def clean_text(x):
    pattern = r'[^a-zA-z0-9\s]'
    
    text = re.sub(pattern, '', x)
    text = re.sub(r'[^\w\s]', '', text)
    return text

def clean_numbers(x):
    if bool(re.search(r'\d', x)):
        x = re.sub('[0-9]{5,}', '#####', x)
        x = re.sub('[0-9]**{4}**', '####', x)
        x = re.sub('[0-9]**{3}**', '###', x)
        x = re.sub('[0-9]**{2}**', '##', x)
    return x

def predict(text,model,tokenizer):

    
    #text = clean_text(text)
    #text = clean_numbers(text)


    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=50)
    pred = model.predict(padded)
    predicted_class = pred.argmax(axis=-1)
   
    classes  = {'Irrelevant': 0, 'Negative': 1, 'Neutral': 2, 'Positive': 3}
    actual_class = classes[str(predicted_class[0])]
    result = {"text":text,"used model":"Base Line","prediction":actual_class}
    return result


def predict_model(text):
    return predict(text,model,tokenizer)







if __name__== "__main__":
    #Text-to classify should be-in a list.
   text = ["I love you"]
   for i in text:
    predictions = predict_model(i)
    print(predictions)




