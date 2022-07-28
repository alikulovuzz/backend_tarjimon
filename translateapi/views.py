from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from translateapi.models import Translate
from .serializer import TranslateSerializer

# Create your views here.
import numpy as np

import tensorflow as tf

import tensorflow_text as tf_text

text1 = tf.constant([' '])
reloaded1 = tf.saved_model.load('./translator_Uzb_Rus_5')
reloaded2 = tf.saved_model.load('./translator_Rus_UZ_15')
reloaded3 = tf.saved_model.load('./translator_Uzb_Eng_5')
reloaded4 = tf.saved_model.load('./translator_Eng_uzb_5')
reloaded5 = tf.saved_model.load('./translator_Rus_eng_15')
reloaded6 = tf.saved_model.load('./translator_Eng_rus_15')


class TranslateApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'text': request.GET['text'],
            'from_lang': request.GET['from_lang'],
            'to_lang': request.GET['to_lang'],
        }

        serializer = TranslateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        result = translate(serializer.data)
        return Response({'result': result}, status=status.HTTP_201_CREATED)


class IzoxTemplate(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'izox': request.GET['izox'],
            'text': request.GET['text'],
            'from_lang': request.GET['from_lang'],
            'to_lang': request.GET['to_lang'],
        }

        serializer = TranslateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
 
        result = izox_saxla(serializer.data)
        return Response({'result': result}, status=status.HTTP_201_CREATED)

def izox_saxla(data):
    global fortune
    from_lang = data['from_lang']
    to_lang = data['to_lang']
    text = data['text']
    izox = data['izox']
    fortune = Translate(izox=izox,to_lang=to_lang,from_lang=from_lang,text=text)
    fortune.save()  





def translate(data):
    from_lang = data['from_lang']
    to_lang = data['to_lang']
    text = data['text']
    b = ""
    res = text.split(".")
    for a in res:
        if res[-1] != a:
            a = a + "."
        k = a.split("?")
        for l in k:
            if k[-1] != l:
                l = l + "?"
            o = l.split("!")
            for w in o:
                if o[-1] != w:
                    w = w + "!"
                if len(w)!= 0:
                    text1 = w
                    w=w.split(' ')
                    print(len(w))
                    if from_lang == '1' and to_lang == '2':
                        result = reloaded1(text1)
                    if from_lang == '2' and to_lang == '1':
                        result = reloaded2(text1)
                    if from_lang == '1' and to_lang == '3':
                        result = reloaded3(text1)
                    if from_lang == '3' and to_lang == '1':
                        result = reloaded4(text1)
                    if from_lang == '2' and to_lang == '3':
                        result = reloaded5(text1)
                    if from_lang == '3' and to_lang == '2':
                        result = reloaded6(text1)

                    text1 = result.numpy().decode()
                    b = b + text1

    return b

