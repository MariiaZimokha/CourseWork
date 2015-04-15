from urllib.request import Request, urlopen
from django.db import connection
from push_notifications.models import APNSDevice, GCMDevice

# def my_scheduled_job():
#     urlOnAir='http://api.themoviedb.org/3/tv/on_the_air?api_key=472ba12809425252de1bb7945f0b82f1'
#     json1 = requests.get(urlOnAir).json()
#     results =  json1.get('results')
    
def my_scheduled_job (request):
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
                    
                    gcm_reg_id='1235d5d5d4djdgjydjufv545654ee'

                    device = GCMDevice.objects.get(registration_id=gcm_reg_id)
                    device.send_message("You've got mail")
                                                    
            i += 1
            
            
            
            
    