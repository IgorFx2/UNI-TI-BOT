import discord
import asyncio
import info
import youtube_dl

#variaveis

players = {}
COR = 0xFFFFFF
COR1 = 0xFF0000
client = discord.Client()
token = info.token
prefix = info.prefix

#Verificação de funcionamento

@client.event
async  def on_ready():
	print(" Hello World Curse clear")
	print("---------------")
	print(" BOT ONLINE - UniTI ")
	print("---------------")
	print(client.user.name)
	print(client.user.id)
	print('-------UNI-----')

#inicio do código

@client.event
async def on_message(message):
 
	#comando de enter/entrar.

    if message.content.startswith(';entrar'):
        try:
           mscenter = discord.Embed(
               title="\n",
               color=COR1,
               description="Entrei no canal"
           )
           channel = message.author.voice.voice_channel
           await client.join_voice_channel(channel)
           voice_client = client.voice_client_in(message.server)
           await client.send_message(message.channel, embed=mscenter)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "O bot ja esta em um canal de voz")
        except Exception as error:
            await client.send_message(message.channel, "Deu o Erro: ```{error}```".format(error=error))

    #comando de sair/exit.

    if message.content.startswith(';sair'):
        try:
            mscleave = discord.Embed(
                title="\n",
                color=COR,
                description="Sai do canal e parei a musica!"
            )
            voice_client = client.voice_client_in(message.server)
            await client.send_message(message.channel, embed=mscleave)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "O bot não esta em nenhum canal de voz.")
        except Exception as GB:
            await client.send_message(message.channel, "Deu o Erro: ```{haus}```".format(haus=GB))

    #comando de play/tocar.

    if message.content.startswith(';play'):
        try:
            yt_url = message.content[6:]
            if client.is_voice_connected(message.server):
                try:
                    voice = client.voice_client_in(message.server)
                    players[message.server.id].stop()
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb = discord.Embed(
                        title="Música para tocar:",
                        color=COR1
                    )
                    mscemb.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb.add_field(name="Enviado em:", value="`{}`".format(player.uploaded_date))
                    mscemb.add_field(name="Enviado por:", value="`{}`".format(player.uploadeder))
                    mscemb.add_field(name="Duraçao:", value="`{}`".format(player.uploadeder))
                    await client.send_message(message.channel, embed=mscemb)
                except Exception as e:
                    await client.send_message(message.server, "Error: [{error}]".format(error=e))
            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb2 = discord.Embed(
                        title="Música para tocar:",
                        color=COR
                    )
                    mscemb2.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb2.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb2.add_field(name="Enviado em:", value="`{}`".format(player.upload_date))
                    mscemb2.add_field(name="Enviado por:", value="`{}`".format(player.uploader))
                    mscemb2.add_field(name="Duraçao:", value="`{}`".format(player.duration))
                    await client.send_message(message.channel, embed=mscemb2)
                except Exception as error:
                    await client.send_message(message.channel, "Error: [{error}]".format(error=error))
        except Exception as e:
            await client.send_message(message.channel, "Error: [{error}]".format(error=e))


    #comando de pause

    if message.content.startswith(';pause'):
        try:
            mscpause = discord.Embed(
                title="\n",
                color=COR1,
                description="Musica pausada com sucesso!"
            )
            await client.send_message(message.channel, embed=mscpause)
            players[message.server.id].pause()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))
    
    #comando de pause

    if message.content.startswith(';resume'):
        try:
            mscresume = discord.Embed(
                title="\n",
                color=COR,
                description="Musica despausada com sucesso!"
            )
            await client.send_message(message.channel, embed=mscresume)
            players[message.server.id].resume()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))
    #comando de ajuda
    if message.content.startswith(';help'):
    	mschelp = discord.Embed(
    		title="\n",
    		color=COR1,
    		description= ";help = Listar para ver os comandos.\n\n"
    					 ";entrar = O BOT entra no canal de autor do mensagem. \n\n"
    					 ";sair = O BOT saiu do canal. \n\n"
    					 ";play <nome da música/link da música> = O BOT entra no canal e toca a música desejava, ou a adiciona na playlist. \n\n"
    					 ";pause = Pausa a música que o BOT estiver tocando. \n\n"
    					 ";resume = Despausa a música pausada pelo BOT. \n\n"
    		)
    	await client.send_message(message.channel, embed=mschelp)


client.run(token)

