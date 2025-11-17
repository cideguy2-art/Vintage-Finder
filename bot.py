import discord
from discord.ext import commands
from vinted_api import VintedAPI

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())
api = VintedAPI()

@bot.event
async def on_ready():
    print(f"Bot eingeloggt als {bot.user}")

@bot.command(name="vinted")
async def vinted_search(ctx, *, query: str):
    """Suche Vintage-Artikel auf Vinted"""
    try:
        await ctx.send(f"🔍 Suche nach **{query}**...")

        items = api.search(query=query, per_page=5, order="price_asc")

        if not items:
            return await ctx.send("❌ Keine Artikel gefunden.")

        for item in items:
            embed = discord.Embed(
                title=item["title"],
                url=item["url"],
                description=f"💶 Preis: **{item['price']} {item['currency']}**",
                color=0x7E57C2
            )
            embed.set_thumbnail(url=item["photo"])
            embed.add_field(name="Zustand", value=item["status"], inline=True)
            embed.add_field(name="Ort", value=item["city"], inline=True)

            await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"⚠️ Fehler: {e}")

bot.run(MTQzNzA1MjM1NzAxMDY1NzM5Mg.G4jXVH.xLGCO2_rbw8YvJynrPbeB2ZlRMx8hcZ_nHgrrk)
