import discord
import random

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # botun mesaj içeriğine erişimini aktif hale getiriyoruz.

bot = commands.Bot(command_prefix='$', intents=intents)
#Bu özellik, botun kendisine gönderilen komutları tanıması için bir ön ek tanımlar.
#  $ işareti komut ön eki olarak belirlenmiştir. Yani bot sadece $ ile başlayan komutlara yanıt verir.

@bot.event # bot belirli bir olay gerçekleştiğinde tetiklensin.
async def on_ready(): # bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{bot.user} olarak giriş yaptık')

ev_esyalari_yok_olma_sureleri = [
    ("İşte Bir Bilgi! Plastik şişe", "450 yıl"),
    ("İşte Bir Bilgi! Cam şişe", "1 milyon yıl veya daha fazla"),
    ("İşte Bir Bilgi! Alüminyum kutu", "80-200 yıl"),
    ("İşte Bir Bilgi! Kağıt", "2-5 ay"),
    ("İşte Bir Bilgi! Ahşap mobilya", "15 yıl"),
    ("İşte Bir Bilgi! Pamuklu kumaş", "1-5 ay"),
    ("İşte Bir Bilgi! Plastik poşet", "10-1000 yıl"),
    ("İşte Bir Bilgi! Lastik (örneğin, ayakkabı tabanı)", "50-80 yıl"),
    ("İşte Bir Bilgi! Metal mutfak eşyaları", "500 yıl"),
    ("İşte Bir Bilgi! Gıda atıkları (örneğin, meyve kabukları)", "2-4 hafta"),
]


@bot.command() # botun bir komutu tanıması için bu dekoratörü kullanırız.
async def hello(ctx): # hello adında bir komut tanımladık. ctx(context), komutun çağrıldığı yer hakkındaki bilgileri içerir.
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
#Bu komutun çalışması için, kullanıcı sohbette $hello yazmalıdır. 


@bot.command()
async def atiksureleri(ctx):
    await ctx.send(random.choice(ev_esyalari_yok_olma_sureleri))

@bot.command()
async def video(ctx):
    await ctx.send("https://youtu.be/7n2o-C_-x4o")    

@bot.command()
async def oneri(ctx):
    await ctx.send("plastik poşetler yerine bez poşet kullanabilirsin👍")    

bot.run("token")
