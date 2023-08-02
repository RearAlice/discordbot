import discord
from discord.ext import commands

# botのトークン
TOKEN = 'MTA3MDk1NDU3Mzk3MzQ0MjYyMA.GMwnlU.caatXPsmqLBLp3dTvom3hJRP9icrN5gL1PzjCg'

# CSVファイル名
CSV_FILENAME = 'names.csv'

intents = discord.Intents.default()  # すべてのデフォルトのIntentsを有効化
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='vrc_link')
async def vrc_link(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send("名前を入力してください。")
    
    try:
        name_msg = await bot.wait_for('message', check=check, timeout=60)  # 60秒以内に名前を入力
        name = name_msg.content
        
        # メッセージにチェックマークのリアクションを追加
        await name_msg.add_reaction('✅')
        
        # CSVファイルに名前を追加
        with open(CSV_FILENAME, 'a') as f:
            f.write(f'{name}\n')
        
        await ctx.send(f'{name} をCSVファイルに記録しました。')

    except asyncio.TimeoutError:
        await ctx.send("タイムアウトしました。もう一度試してください。")

bot.run(TOKEN)
