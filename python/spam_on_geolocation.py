from telethon.sync import TelegramClient
from telethon import functions, types

api_id = 25953954 # api_id и api_hash передаю в открытый доступ!
api_hash = 'f0d777b955c2acd946d3075d7bffc690' #Используйте api_id и api_hash честно,и не нарушайте законы!

print("GRAB - Started")

message = "test";

def file_put_contents(file, data, append=0):
    if append==0:
        stat = "w"
    else:
        stat = "a"
    my_file = open(file, stat, encoding='utf-8')
    my_file.write(data)
    my_file.close()
    


with TelegramClient('geo', api_id, api_hash) as client:
    result = client(functions.contacts.GetLocatedRequest(
        geo_point=types.InputGeoPoint(
            lat=1.0,    # <
            long=1.0    # <
        ),
        self_expires=42
    ))

    l = len(result.users)
    for i in range(l):
        print(result.users[i],i)
        client.send_message(result.users[i], message)
