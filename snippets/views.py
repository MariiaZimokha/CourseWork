from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import length
# from rest_framework import generics
# from rest_framework import mixins

'''
    something else
'''
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet , Serial, Season, Episode, User, Subscription
from snippets.serializers import SnippetSerializer, SeasonSerializer, UserSerializer , SerialSerializer, SerialDetailSerializer,SubscriptionSerializer
from snippets.serializers import SeasonSerializer2
from urllib.request import Request, urlopen
from django.db import connection
from rest_framework import serializers
import requests
import json
import urllib.request

from push_notifications.models import APNSDevice, GCMDevice

headers = {
           'Accept': 'application/json'
           }
    
'''
return query like dictionary
'''
def sqltodict(query):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(query)
    fieldnames = [name[0] for name in cursor.description]
    result = []
    for row in cursor.fetchall():
        rowset = []
        for field in zip(fieldnames, row):
            rowset.append(field)
        result.append(dict(rowset))
    return result


def test(request):
    return render(request, 'test.html', {})

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")



def Cron (request):
    urlOnAir='http://api.themoviedb.org/3/tv/on_the_air?api_key=472ba12809425252de1bb7945f0b82f1'
    json1 = requests.get(urlOnAir).json()
    results =  json1.get('results')
    i = 0
    
    query = """SELECT SerialId FROM snippets_serial; """
    cursor = connection.cursor()
    cursor.execute(query)
    SerialsSite = cursor.fetchall()

    SerialIdSite =[]
#     clear list
    del SerialIdSite[:]

    for index in range(len(SerialsSite)):
        SerialIdSite.append(SerialsSite[index][0])

    
    
    if type(results) == list:
        Listlength = len(results)
        
        while(i < Listlength):
            serial = results[i]            
            id = serial.get('id') 
                       
            for index in range(len(SerialIdSite)):
                if SerialIdSite[index] == int(id):
                    
#                    Take id of serial from table
                    cursor = connection.cursor()
                    cursor.execute("""SELECT id FROM snippets_serial where SerialId = '%d' """ % (int(id)))
                    Serials = cursor.fetchall()
                    SerialId=Serials[0][0]
                                  
#                         get registrations id for subscribe users
                    cursor.execute("""select RegistrationId from snippets_user join snippets_subscription
on snippets_user.id = snippets_subscription.UserId_id 
where snippets_subscription.SerialId_id =  '%d' """ % (SerialId))
                                                    
            i += 1
    
    
    request = Request('http://api.themoviedb.org/3/tv/on_the_air?api_key=472ba12809425252de1bb7945f0b82f1&page=3')
    response_body = urlopen(request).read()
    return HttpResponse(response_body)



# fill table Serial
def call(request):

#    serial on air
    urlq = 'http://api.themoviedb.org/3/tv/on_the_air?api_key=472ba12809425252de1bb7945f0b82f1&page=2'
    Testjson1 = requests.get(urlq).json()

    r = Testjson1.get('results')
    total = Testjson1.get('total_pages')

#     r =  json1.get('results')
    counter = 1
    if type(r) == list:
        Listlength = len(r)
        while(counter < Listlength):
            serial = r[counter]
            counter = counter + 1
            nameSerial = serial.get('name')
            img = serial.get('poster_path')
            if img is None:
                img = ""
            serialId = serial.get('id')

            temp = ''

            cursor = connection.cursor()
            cursor.execute("""insert into snippets_serial( Name, Image_url, SerialId,LongDescription, ShortDesctiption) values (?,?,?,?,?)""",(nameSerial, img, serialId, temp, temp))


    request = Request('http://api.themoviedb.org/3/tv/on_the_air?api_key=472ba12809425252de1bb7945f0b82f1&page=3')
    response_body = urlopen(request).read()
    return HttpResponse(response_body)

def fill_episodes(request):
    '''
    list serial ID from site
    '''
    query = """SELECT id FROM snippets_serial; """
    cursor = connection.cursor()
    cursor.execute(query)
    Serials = cursor.fetchall()

    ListOfSerialId =[]
#     clear list
    del ListOfSerialId[:]

    for index in range(len(Serials)):
        ListOfSerialId.append(Serials[index][0])



    query = """SELECT SerialId FROM snippets_serial; """
    cursor = connection.cursor()
    cursor.execute(query)
    SerialsSite = cursor.fetchall()

    SerialIdSite =[]
#     clear list
    del SerialIdSite[:]

    for index in range(len(SerialsSite)):
        SerialIdSite.append(SerialsSite[index][0])
    '''
    insert
    '''
    count_episodes = 0

    for index in range(len(ListOfSerialId)):
        cursor = connection.cursor()
        cursor.execute("""SELECT NumberOfSeason FROM snippets_season where serial_id  = '%d' """ % (ListOfSerialId[index]))
        NumberOfSeason = cursor.fetchall()
        getNumber = NumberOfSeason[0]

        urlq = 'http://api.themoviedb.org/3/tv/'+ str(SerialIdSite[index]) +'/season/' + str(getNumber[0]) +'?api_key=472ba12809425252de1bb7945f0b82f1'


        json1 = requests.get(urlq).json()
        episodes = json1.get('episodes')

        count_episodes =  len(episodes)

        cursor.execute("""SELECT id FROM snippets_season where serial_id  = '%d' """ % (ListOfSerialId[index]))
        id = cursor.fetchall()
        getid = id[0]

        k =0
        while(k < count_episodes):
            tmp = episodes[k]
            name = tmp.get('name')
            episode_number = tmp.get('episode_number')
            air_date = tmp.get('air_date')
            idEpisode = tmp.get('id')

            cursor.execute("""insert into snippets_episode (Name, Number, DayRealease, season_id, EpisodeId) values(?,?,?,?,?)""",(name, episode_number, air_date, getid[0], idEpisode) )


#             cursor.execute("""insert into snippets_snippet (created, title, code, linenos, language, style) values(?,?,?,?,?,?)""",("2014-09-22", "ffff","dddd", 0 ,"s" ,"s") )
            k = k + 1

        del episodes[:]



    request = Request('http://api.themoviedb.org/3/tv/'+ str(ListOfSerialId[15]) +'/season/' + str(1) +'?api_key=472ba12809425252de1bb7945f0b82f1')
    response_body = urlopen(request).read()
    return HttpResponse(response_body)

# fill two tabels

def fill(request):
    query = """SELECT SerialId FROM snippets_serial; """
    cursor = connection.cursor()
    cursor.execute(query)
    Serials = cursor.fetchall()

    ListOfSerialId =[]
#     clear list
    del ListOfSerialId[:]

    for index in range(len(Serials)):
        ListOfSerialId.append(Serials[index][0])


    for index in range(len(ListOfSerialId)):
        urlq = 'http://api.themoviedb.org/3/tv/'+ str(ListOfSerialId[index]) +'?api_key=472ba12809425252de1bb7945f0b82f1'
#         urlq = 'http://api.themoviedb.org/3/tv/1418?api_key=472ba12809425252de1bb7945f0b82f1'
        Testjson1 = requests.get(urlq).json()

        '''
        fill season table
        '''
        number_of_seasons = Testjson1.get('number_of_seasons')
#         j = 0
#         while(j < seasons):
#         cursor = connection.cursor()
        cursor.execute("""SELECT id FROM snippets_serial where SerialId = %d """% (ListOfSerialId[index]))
        tmp = cursor.fetchall()
        t = tmp[0]
        y = int(t[0])

        seasons = Testjson1.get('seasons')
        count_seasons = len(seasons)
        seasonId = seasons[count_seasons-1].get('id')

        cursor.execute("""INSERT INTO snippets_season(NumberOfSeason, serial_id, SeasonId) values(?,?,?) """, (number_of_seasons, y, seasonId ))

        '''
        fill overview
        '''
#         overview = Testjson1.get('overview')
#         cursor = connection.cursor()
#         cursor.execute("""UPDATE snippets_serial SET LongDescription = ? WHERE SerialId = ? """,(overview, ListOfSerialId[index]))

        i = index

    request = Request('http://api.themoviedb.org/3/tv/'+ str(ListOfSerialId[i]) +'?api_key=472ba12809425252de1bb7945f0b82f1')
    response_body = urlopen(request).read()
    return HttpResponse(response_body)


# test for push notifications 

def my_scheduled_job(request):
    urlOnAir='http://api.themoviedb.org/3/tv/on_the_air?api_key=472ba12809425252de1bb7945f0b82f1'
    json1 = requests.get(urlOnAir).json()
    total_pages = json1.get('total_pages')
    i = 0
    page = 0
    
    while(page < total_pages):
        urlOnAir='http://api.themoviedb.org/3/tv/airing_today?api_key=472ba12809425252de1bb7945f0b82f1&page='+str(page)
        json1 = requests.get(urlOnAir).json()
        results =  json1.get('results')    
        
        page +=1
        
        if type(results) == list:
            Listlength = len(results)
                  
            while(i < Listlength):
                serial = results[i]            
                id = serial.get('id')
                                            
    #             if Serial.objects.filter(SerialId=id):
                serials = Serial.objects.filter(SerialId=id)
                if serials :
                    serials = Serial.objects.get(SerialId=id)
                    '''
                    insert new records
                    '''
                    urlq = 'http://api.themoviedb.org/3/tv/'+ str(id) +'?api_key=472ba12809425252de1bb7945f0b82f1'
                    seasonId=0
                    Testjson1 = requests.get(urlq).json()
                    number_of_seasons = Testjson1.get('number_of_seasons')
                    season= Season.objects.filter(NumberOfSeason=number_of_seasons)
                    

                    if  season is  None:
                        seasons = Testjson1.get('seasons')
                        count_seasons = len(seasons)
                        seasonId = seasons[count_seasons-1].get('id')
                        cursor = connection.cursor()
                        cursor.execute("""insert into snippets_season(NumberOfSeason, serial_id, SeasonId) values(?,?,?) """, (number_of_seasons, id, seasonId ))
                    
                    
                    season= Season.objects.filter(NumberOfSeason=number_of_seasons)[0]
                    lastSeason = season.id
                    
                    episodes1 = Episode.objects.filter(season_id=lastSeason)
                    countEpisodes = len(episodes1)                 
                                   
                    urlq = 'http://api.themoviedb.org/3/tv/'+ str(id) +'/season/' + str(number_of_seasons) +'?api_key=472ba12809425252de1bb7945f0b82f1'
                                                            
                    json1 = requests.get(urlq).json()
                                  
                    episodes = json1.get("episodes")
#                     return HttpResponse( episodes)
                                         
#                     return HttpResponse (len(episodes))
                    if episodes is  None:
                        break
                    count_episodes =  len(episodes)                        
                    serialId = serials.id
                    
                    k =0
                    while(k < count_episodes):
                        if k == countEpisodes+1:
                            tmp = episodes[k]
                            name = tmp.get('name')
                            episode_number = tmp.get('episode_number')
                            air_date = tmp.get('air_date')
                            if air_date is None:
                                break
                            idEpisode = tmp.get('id')
                            test = Episode.objects.filter(Name=name)
                            if  test is  None:
                                cursor.execute("""insert into snippets_episode (Name, Number, DayRealease, season_id, EpisodeId) values(?,?,?,?,?)""",(name, episode_number, air_date, serialId.id, idEpisode) )
                            elif test=="":
                                cursor.execute("""update  snippets_episode set Name = ? WHERE EpisodeId = ? """,(name,idEpisode))
                    
                        k = k + 1
     
                    '''
                    cheak if subscribe
                    '''
                    gcm_reg_id = 'b67fb6fe3896d95a183fefff49815964c836bd54bded9cc362e62247aee5f1ab'
                    device_Ios = APNSDevice.objects.get(registration_id=gcm_reg_id)
                    message = "Today released a new series of The big bang theory"
                    device_Ios.send_message(message)

                    subscribe = Subscription.objects.filter(SerialId=serials.id)
                    if subscribe:
                        subscribe = Subscription.objects.get(SerialId=serials.id)
                        
                        name = subscribe.SerialId.Name                
        #                 return HttpResponse(name)

                        
                        gcm_reg_id = subscribe.UserId.RegistrationId
                        
                        device_Ios = APNSDevice.objects.get(registration_id=gcm_reg_id)

                        device = GCMDevice.objects.get(registration_id=gcm_reg_id)
                        message = "Today released a new series of '" + name +"'"
                        device.send_message(message)
                else:
                    urlq = 'http://api.themoviedb.org/3/tv/'+ str(id) +'?api_key=472ba12809425252de1bb7945f0b82f1'
                    Testjson1 = requests.get(urlq).json()
                    overview = Testjson1.get('overview')
                    if overview is None:
                        overview=""
                         
                    name = Testjson1.get('name')
                    if name is None:
                        break
                     
                    poster_path = Testjson1.get('poster_path')
                    if poster_path is None:
                        poster_path=""
                    else:
                        poster_path="http://image.tmdb.org/t/p/w500"+str(poster_path)
    #                 return HttpResponse(poster_path)
     
                    cursor = connection.cursor()
                    cursor.execute("""insert into snippets_serial(SerialId,LongDescription, Name, Image_url,ShortDesctiption)  values(?,?,?,?,?) """,(id, overview, name,poster_path,""))
    #                 return HttpResponse(poster_path)
                    '''
                    fill season table
                    '''
                    number_of_seasons = Testjson1.get('number_of_seasons')
                    cursor.execute("""SELECT id FROM snippets_serial where SerialId = %d """% (id))
                    tmp = cursor.fetchall()
                    t = tmp[0]
                    y = int(t[0])
             
                    seasons = Testjson1.get('seasons')
                    count_seasons = len(seasons)
                    seasonId = seasons[count_seasons-1].get('id')
             
                    cursor.execute("""INSERT INTO snippets_season(NumberOfSeason, serial_id, SeasonId) values(?,?,?) """, (number_of_seasons, y, seasonId ))
                     
                    '''
                    fill episode table
                    '''
                    urlq = 'http://api.themoviedb.org/3/tv/'+ str(id) +'/season/' + str(number_of_seasons) +'?api_key=472ba12809425252de1bb7945f0b82f1'
                    json1 = requests.get(urlq).json()
                    episodes = json1.get('episodes')
             
                    count_episodes =  len(episodes)
                     
                    serialId = Serial.objects.get(SerialId=id)
                     
                    k =0
                    while(k < count_episodes):
                        tmp = episodes[k]
                        name = tmp.get('name')
                        episode_number = tmp.get('episode_number')
                        air_date = tmp.get('air_date')
                        idEpisode = tmp.get('id')
              
                        cursor.execute("""insert into snippets_episode (Name, Number, DayRealease, season_id, EpisodeId) values(?,?,?,?,?)""",(name, episode_number, air_date, serialId.id, idEpisode) )
              
                        k = k + 1
              
                    del episodes[:]
                    
    #                                                           
                i += 1
            
    request = Request('http://api.themoviedb.org/3/tv/1418?api_key=472ba12809425252de1bb7945f0b82f1')
    response_body = urlopen(request).read()
    return HttpResponse(response_body)

def send(request):    
    body = {
        "registration_ids" : ["APA91bHhV6LWXHf2e0LjdZyKLCmmpmR-ohZk9sspQJCzX-Ir-DAWTfm4mwh2tZYKlrb1munRGhIiFvdmIC_P172kdZdyNO5Jo2I7GfIR-ThKrlRXp62eeGw4QvA78Xypd04LGKeZRByHtlSoqjNxVwt_Nwt8SW97wQ"],
        "data" : {
                  "message":"you have got new notification"
                  }
            }  

    myurl = "https://android.googleapis.com/gcm/send"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization','key=AIzaSyBqq3B-GwEp8BMFi1qxL9rWO67UiFOwd0M')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
#     print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes) 
    
    return HttpResponse("Hello, world. You're at the poll index.")

    

class SerialList(APIView):
    """
    List all serials, or create a new serial.
    """
#     List
    def get(self, request, format=None):
        snippets = Serial.objects.all()
        serializer = SerialSerializer(snippets, many=True)
        return Response(serializer.data)



class SerialDetail(APIView):
    """
    Retrieve, update or delete a serial instance.
    """

    def get(self, request, pk, registrationId, format=None):
        serial = get_object_or_404(Serial, pk=pk)
        serializer = SerialDetailSerializer(serial,
                                            context={'registration_id': registrationId, 'serial_id':pk})
        return Response(serializer.data)


class UserAPI(APIView):
    def post(self, request, format=None):
        comeJSON = request.data
        action = comeJSON.get("action")
        if action == "register":
            device_type = comeJSON.get('device_type')
            registration_id = comeJSON.get('registration_id')

            cursor = connection.cursor()
            cursor.execute("""insert into snippets_user (Device_type, RegistrationId ) values (?,?)""",(device_type, registration_id))
            if device_type == "Android":
                cursor.execute("""insert into push_notifications_gcmdevice (active, registration_id)  values (?,?)""",('true', registration_id))
            elif device_type == "IOS":
                cursor.execute("""insert into push_notifications_apnsdevice ( active, registration_id)  values (?,?)""",( 'true',registration_id))
            return Response( status=status.HTTP_201_CREATED)
        elif action == 'update':
            registration_id = comeJSON.get("registration_id")
            subscriptions = comeJSON.get('subscribtions')
            count_subscriptions = len(subscriptions)            
            k = 0
            while(k < count_subscriptions):
                
                subscribe = subscriptions[k].get('subscribe')
                serial_id = subscriptions[k].get('serial_id')
                
                cursor = connection.cursor()
#                     cursor.execute("""SELECT id FROM snippets_user where RegistrationId = ? """, (registration_id,))
                cursor.execute("""SELECT id FROM snippets_user where RegistrationId = '%s' """ % (registration_id))
                tmp = cursor.fetchall()

                if len(tmp) == 0:
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    t = tmp[0]
                    id_user = int(t[0])

                    if subscribe :
                        #return HttpResponse ("""insert into snippets_subscription (SerialId_id, UserId_id) values(?,?)""", (serial_id, id_user ))
                        cursor.execute("""INSERT INTO snippets_subscription (SerialId_id, UserId_id) values(?,?) """, (serial_id, id_user ))
                    elif subscribe == False:# unsubscribe
#                          cursor.execute("""DELETE FROM snippets_subscription WHERE UserId_id = ? """, (id_user,))
                        cursor.execute("""DELETE FROM snippets_subscription WHERE UserId_id = ? and SerialId_id = ?""", (id_user, serial_id ))
                k += 1
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class SubscribeList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request,registrationId, format=None):
        serial = Serial.objects.filter()[0]
        serializer = SerialDetailSerializer(serial,
                                            context={'registration_id': registrationId, 'serial_id':serial.id})
        #temp = serializer.data.filter(is_subscribed = true)

        temp2 = {k: v for k, v in serializer.data.items() if (k == "is_subscribed" and v) }
        return Response(temp2)
 
class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
   
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Serial.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
#         SerialSerializer(s).data
        serializer = SerialSerializer(snippet)
        return Response(serializer.data)

# update
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





