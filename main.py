import interactions
import random

bot = interactions.Client(token="MTEyNTk2NTE2MTI1ODMwMzY1OQ.GhPZUR.kXRXPPoz72K95EK51Ut6GKKwbPFzczQSSIkI4o")
guild = 820008929517109269


burasiminecraftsozler = ["Bu akşam bir sesler var kapımın önünde Bu akşam bir hırıltı var kapımın önündeKaderde var savaşmak Asla kaçmam ben savaştan", "Benim adımı herkes duysun Bu savaşın galibi Doktor Burak Zombi çok yaratık bol elmas kılıcım var Fark etmez bana yaratık hepinizi yenerim", "Zombi çok yaratık bol elmas kılıcım var Fark etmez bana yaratık hepinizi yenerim Burası Minecraft hiç bitmez burada savaşmak Bloklar, silahlar Minecraft'ta bitmez savaşmak"]

@bot.command(
    name="tavukdoner",
    description="Tavuk döner indeksi şu an ki fiyatı 50tl",
    scope=guild,
    options = [
        interactions.Option(
            name="fiyat",
            description="Fiyatı yazın",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def tavukdoner(ctx: interactions.CommandContext, fiyat: str):
    idk = int(fiyat)
    solution = idk / 50
    await ctx.send("Döner indexi " + str(solution))

@bot.command(
        name="baskin",
        description="FBI OPEN UP",
        scope=guild
)
async def baskin(ctx: interactions.CommandContext):
    await ctx.send("https://tenor.com/view/f-bi-raid-swat-gif-11500735")

@bot.command(
        name="traktor",
        description="BLYAT",
        scope=guild
)
async def traktor(ctx: interactions.CommandContext):
    await ctx.send("https://www.youtube.com/watch?v=t5uHaXcIFJM")

@bot.command(
        name="elinizevereyim",
        description="Efsane an",
        scope=guild
)
async def elinizevereyim(ctx: interactions.CommandContext):
    await ctx.send("Elimizde yok, elimizde yok, ELİMİZDE YOK E ELİNİZE VEREYİM O ZAMAN O YOK BU YOK NE BOKTAN SİLAH MAĞAZASISIN SEN")

@bot.command(
        name="burasiminecraft",
        description="Burası minecrafttan rastgele bir söz söyler",
        scope=guild
)
async def burasiminecraft(ctx: interactions.CommandContext):
    epic = random.randint(0, 2)
    epic2 = str(burasiminecraftsozler[epic])
    await ctx.send(epic2)

@bot.command(
        name="yazitura",
        description="Yazı tura atar... bu kadar",
        scope=guild
)
async def yazitura(ctx: interactions.CommandContext):
    olasilik = ["Yazı", "Tura"]
    rastgele = random.randint(0,1)
    sonuc = olasilik[rastgele]
    await ctx.send(sonuc)

@bot.command(
        name="psppazar",
        description="PSP PAZAR... PAZAR... PAZAR... PAZAR... PAZAR",
        scope=guild
)
async def psppazar(ctx: interactions.CommandContext):
    await ctx.send("PSP PAZAR... PAZAR... PAZAR... PAZAR... PAZAR")


@bot.event
async def on_message(message):
    channel = message.channel
    chance = 69
    if(chance == 69):
        await channel.send("noluyo sikicceö")

@bot.event
async def on_ready():
    print("Ready")

bot.start()

