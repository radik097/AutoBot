from telethon import TelegramClient, events
import os.path
import pickle
name=input('Nikname telegram: ')
file=os.path.exists(name+'.session')
if file== False:
    api_id=int(input('Write u app_id for https://my.telegram.org: '))
    api_hash=input('Write u app_hash: ')
    save=open(name,'wb')
    user=[]
    user.append(api_id)
    user.append(api_hash)
    pickle.dump(user,save)
    bot=TelegramClient(name, api_id , api_hash)
elif file == True:
    with open(name, 'rb') as save:
        user=pickle.load(save)
        api_hash=user[1]
        api_id=user[0]
        bot=TelegramClient(name, api_id , api_hash)
bot.start()
@bot.on(events.NewMessage())
async def getMessage(event):
    if event.message.nikname != 'c4eburak228':
        print(event.text)
        await event.reply(event.text)
bot.run_until_disconnected()