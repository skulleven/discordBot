from interactions import Client, Intents, listen, slash_command, SlashContext, OptionType, slash_option, Embed, events
from interactions.api.events import MessageCreate, MemberAdd
import random
import os
from dotenv import load_dotenv

bot = Client(Intents=Intents.DEFAULT)

burasiminecraftsozler = ["Bu akşam bir sesler var kapımın önünde Bu akşam bir hırıltı var kapımın önündeKaderde var savaşmak Asla kaçmam ben savaştan", "Benim adımı herkes duysun Bu savaşın galibi Doktor Burak Zombi çok yaratık bol elmas kılıcım var Fark etmez bana yaratık hepinizi yenerim", "Zombi çok yaratık bol elmas kılıcım var Fark etmez bana yaratık hepinizi yenerim Burası Minecraft hiç bitmez burada savaşmak Bloklar, silahlar Minecraft'ta bitmez savaşmak"]

guckartlari_array = ["help", "reverse", "napim", "eee", "şeyimiye", "gavat", "delirme", "adnanoktar", "ilberortaylı", "ösym", "laf", "???", "komik", "as", "amk", "örümcek", "kokarca", "köpek kartal", "kahkaha", "ss", "boş", "çomar", "bizene", "ğ"]

load_dotenv()

@slash_command(
    name="tavukdoner",
    description="Tavuk döner indeksi şu an ki fiyatı 50tl",
)
@slash_option(
    name="fiyat",
    description="Fiyatı yazın",
    opt_type=OptionType.STRING,
    required=True,
)
async def tavukdoner_function(ctx: SlashContext, fiyat: str):
    try:
        idk = float(fiyat)
        solution = idk / 50
        await ctx.send("Döner indexi " + str(solution))
    except ValueError:
        await ctx.send("Lütfen sayı giriniz")
        
@slash_command(
        name="baskin",
        description="FBI OPEN UP",
)
async def baskin(ctx: SlashContext):
    await ctx.send("https://tenor.com/view/f-bi-raid-swat-gif-11500735")

@slash_command(
        name="traktor",
        description="BLYAT",
)
async def traktor(ctx: SlashContext):
    await ctx.send("https://www.youtube.com/watch?v=t5uHaXcIFJM")

@slash_command(
        name="elinizevereyim",
        description="Efsane an",
)
async def elinizevereyim(ctx: SlashContext):
    await ctx.send("Elimizde yok, elimizde yok, ELİMİZDE YOK E ELİNİZE VEREYİM O ZAMAN O YOK BU YOK NE BOKTAN SİLAH MAĞAZASISIN SEN")

@slash_command(
        name="burasiminecraft",
        description="Burası minecrafttan rastgele bir söz söyler",
)
async def burasiminecraft(ctx: SlashContext):
    epic = random.randint(0, 2)
    epic2 = str(burasiminecraftsozler[epic])
    await ctx.send(epic2)

@slash_command(
        name="yazitura",
        description="Yazı tura atar... bu kadar",
)
async def yazitura(ctx: SlashContext):
    olasilik = ["Yazı", "Tura"]
    rastgele = random.randint(0,1)
    sonuc = olasilik[rastgele]
    await ctx.send(sonuc)

@slash_command(
        name="psppazar",
        description="PSP PAZAR... PAZAR... PAZAR... PAZAR... PAZAR",
)
async def psppazar(ctx: SlashContext):
    await ctx.send("PSP PAZAR... PAZAR... PAZAR... PAZAR... PAZAR")

@slash_command(
        name="guckartlari",
        description="Karşındakine kiminle konuştuğunu göster",
)
@slash_option(
    name="kart",
    description="Kullanabileceğin kartları görmek için help yaz.",
    opt_type=OptionType.STRING,
    required=True,
)
async def guckartlari(ctx: SlashContext, kart: str):
    found = False
    for anan in guckartlari_array:
        if(kart == anan):
            found = True
            if(kart == "help"):
                epic = Embed(
                    title="Güç Kartları",
                    description="reverse, napim, eee, şeyimiye, gavat, delirme, adnanoktar, ilberortaylı, ösym, laf, ???, komik, as, amk, örümcek, kokarca, köpek kartal, kahkaha, ss, boş, çomar, bizene, ğ",
                )
                await ctx.send(embed=epic)
            if(kart == "reverse"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155358511431780/EXnuJGzU8AAGGQY.jpg")
            if(kart == "napim"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155491411361812/ErMrKtIXAAAOrLf.jpg")
            if(kart == "eee"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155491172941884/l6qvqordtq861.jpg")
            if(kart == "şeyimiye"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155490861645894/xion9n7bcah61.jpg")
            if(kart == "gavat"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155490585215026/bw2e0pvq0ve51.jpg")
            if(kart == "delirme"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155490350071849/2932947_ofa6e.jpg")
            if(kart == "adnanoktar"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155490144682034/rd3DNq.jpg")
            if(kart == "ilberortaylı"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155489926316062/rd3Qqj.jpg")
            if(kart == "ösym"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155416811208814/BxFa0AvCUAIyOAc.jpg")
            if(kart == "laf"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155416610013274/66fbd9e6e3b43839a6be7ce1ef0cd1a8.jpg")
            if(kart == "???"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155416430575646/132533ee46ffef0663d51baf3c6ece48.jpg")
            if(kart == "komik"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155416228724816/3351997_o67b5.jpg")
            if(kart == "as"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155416086380584/agxazbKL_700w_0.jpg")
            if(kart == "amk"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155415901044776/2777633_o43e1.jpg")
            if(kart == "örümcek"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155415272292352/f108a2e207e4d7b639a793938058afb1.jpg")
            if(kart == "kokarca"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155415083941918/3fcec5c39b2c218742994778c5f11899.jpg")
            if(kart == "köpek kartal"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155359425921044/d7cbc49a4ec8ed9d5756c83092903a29.jpg")
            if(kart == "kahkaha"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155359224070204/3217846_od7f2.jpg")
            if(kart == "ss"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155359093522482/25c9ce01ed633d5e8fa4553d4d9c0838.jpg")
            if(kart == "boş"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155358913560576/fe1a5fa24574dd73edee06ab8740f550.jpg")
            if(kart == "çomar"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155358343790622/IMG_20210306_145313_988.jpg")
            if(kart == "bizene"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155358070374410/FB_IMG_1618260014690.jpg")
            if(kart == "ğ"):
                await ctx.send("https://cdn.discordapp.com/attachments/766672422979502083/834155357486972958/IMG_20210420_120455_128.jpg")
    if(found == False):
        await ctx.send("Kart bulunamadı")

@listen()
async def on_ready():
    print("Ready")

@listen()
async def on_message_create(event: MessageCreate):
    if(event.message.author != bot):
        chance = random.randint(0, 100)
        if(chance == 69):
            await event.message.channel.send("noluyo sikicceö")

bot.start(os.getenv("TOKEN"))

