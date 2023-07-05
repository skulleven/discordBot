from interactions import Client, Intents, listen, slash_command, SlashContext, OptionType, slash_option
import random

bot = Client(Intents=Intents.DEFAULT)

guild = 820008929517109269

burasiminecraftsozler = ["Bu akşam bir sesler var kapımın önünde Bu akşam bir hırıltı var kapımın önündeKaderde var savaşmak Asla kaçmam ben savaştan", "Benim adımı herkes duysun Bu savaşın galibi Doktor Burak Zombi çok yaratık bol elmas kılıcım var Fark etmez bana yaratık hepinizi yenerim", "Zombi çok yaratık bol elmas kılıcım var Fark etmez bana yaratık hepinizi yenerim Burası Minecraft hiç bitmez burada savaşmak Bloklar, silahlar Minecraft'ta bitmez savaşmak"]

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
    idk = int(fiyat)
    solution = idk / 50
    await ctx.send("Döner indexi " + str(solution))

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

@listen()
async def on_ready():
    print("Ready")

bot.start("MTEyNTk2NTE2MTI1ODMwMzY1OQ.GhPZUR.kXRXPPoz72K95EK51Ut6GKKwbPFzczQSSIkI4o")

