from django.shortcuts import render

from django.db import models
from rest_framework.views import APIView
import requests
from rest_framework.response import Response

fotos={}
fotos['Jon Snow'] = "https://media.vogue.es/photos/62ac53d4a656dae6cbba3b2c/master/pass/JonSnow.jpeg"
fotos['Sansa Stark'] = 'https://static.posters.cz/image/1300/art-photo/juego-de-tronos-sansa-stark-i112374.jpg'
fotos['Eddard \"Ned\" Stark'] = 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/juego-de-tronos-sean-bean-habla-sobre-el-legado-de-ned-stark-1552810613.jpg'
fotos['Catelyn Stark'] = 'https://cronicaglobal.elespanol.com/uploads/s1/31/90/90/7/senora-de-aguasdulces.png'
fotos['Jaime Lannister'] = 'https://media.revistagq.com/photos/5cde6e0ecb3e97b1f35fa2b4/4:3/w_1800,h_1350,c_limit/juego%20de%20tronos%20jaime%20lannister%20vivo.jpeg'
fotos['Tyrion Lannister'] = 'https://i.ytimg.com/vi/ih0eEkxiLww/maxresdefault.jpg'
fotos['Cersei Lannister'] = 'https://media.vogue.mx/photos/5ca61d4d41573abbc3c67f2d/2:3/w_2560%2Cc_limit/cersei-lannister.jpg'
fotos['Joffrey Baratheon']='https://img.asmedia.epimg.net/resizer/h8CwRBz_GB93wb2vIZdu6WbF1Vo=/1952x1098/cloudfront-eu-central-1.images.arcpublishing.com/diarioas/PG57H5FPKNPEBO467ETUYDLBCE.jpg'
fotos['Aerys II Targaryen'] = 'https://img.buzzfeed.com/buzzfeed-static/static/2017-08/8/2/asset/buzzfeed-prod-fastlane-03/sub-buzz-7286-1502174447-1.png?output-quality=auto&output-format=auto&downsize=640:*'
fotos['Aemon Targaryen']='https://lossietereinos.com/wp-content/uploads/2012/05/aemon-targaryen-1024.jpg'
fotos['Daenerys Targaryen']='https://imagenes.20minutos.es/files/image_990_v3/uploads/imagenes/2021/01/28/emilia-clarke-en-juego-de-tronos.jpeg'
fotos['Tywin Lannister'] = 'https://forbes.es/wp-content/uploads/2017/05/2015417115724_1.jpg'
fotos['Ramsay Bolton'] = 'https://i.ytimg.com/vi/zBuPXFH_2oM/maxresdefault.jpg'
fotos['Arya Stark']='https://static.posters.cz/image/1300/art-photo/game-of-thrones-arya-stark-i135445.jpg'
fotos['Robert Baratheon']='https://i0.wp.com/imgs.hipertextual.com/wp-content/uploads/2021/01/robert-baratheon.jpg?fit=2500%2C1735&quality=50&strip=all&ssl=1'
fotos['Theon Greyjoy']='https://images.hola.com/imagenes/actualidad/2015061179228/lily-allen-hermano-juego-tronos/0-324-383/lily-allen-alfie2-z.jpg?tx=w_360'
fotos['Samwell Tarly']='https://areajugones.sport.es/wp-content/uploads/2019/05/samtarlygot.jpg'
fotos['Lord Varys']='https://imagenes.elpais.com/resizer/z5CEL--AS_1cx3qjxwFhojwA9eE=/1960x1470/arc-anglerfish-eu-central-1-prod-prisa.s3.amazonaws.com/public/UGTXECQTUYHIS2WH2DHEBODQDU.jpg'
fotos['Bran Stark']='https://imagenes.heraldo.es/files/og_thumbnail/uploads/imagenes/2015/07/23/_branhorizontal_deb6780e.jpg'
fotos['Brienne of Tharth']='https://i.pinimg.com/originals/d0/1e/90/d01e90cd69c0b60a7f023c68ba1db451.jpg'
fotos['Petyr Baelish'] = 'https://static.onecms.io/wp-content/uploads/sites/6/2017/06/littlefinger-2000.jpg'
fotos['Tormund'] = 'https://as01.epimg.net/epik/imagenes/2020/11/18/portada/1605692473_697151_1605692530_noticia_normal_recorte1.jpg'
fotos['Melisandre']='https://gcdn.lanetaneta.com/wp-content/uploads/2019/05/8-profec%C3%ADas-de-Melisandre-que-se-han-hecho-realidad-y.jpg'
fotos['Olenna Tyrell']='https://media.glamour.es/photos/616f7920303e546fa790049a/master/w_1600%2Cc_limit/689923.jpg'
fotos['Mance Rayder'] = 'https://i.ytimg.com/vi/nR7K-wk7I9g/mqdefault.jpg'
fotos['Ygritte']='https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/hc_1440x810/public/media/image/2014/07/363676-top-chicas-juego-tronos-ygritte.jpg?itok=KKu2LxCl'





#print(fotos)

# Create your models here.
class api(APIView):
    def get(self, request):
        url= "https://api.gameofthronesquotes.xyz/v1/characters"
        r=requests.get(url)
        data = r.json()
     
        lista =[]
       
        for i in range(len(data)):
            lista.append({'id':i+1})
            lista[i]['name']=data[i]['name']
            
            if data[i]['house']:
                lista[i]['casa']=data[i]['house']['name']
            
            
            lista[i]['frases']=data[i]['quotes']
            lista[i]['fotos']=fotos[lista[i]['name']]
            
        return Response(lista)
