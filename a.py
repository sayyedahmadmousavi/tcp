from telethon import TelegramClient, sync
api_id = 157840
api_hash = 'fb312875319b91cb152aa4e4a0231584'

client = TelegramClient('ahmad', api_id, api_hash)
try:
	client.start()
	client.connect()
	me = client.get_me()
	print(me.stringify())
	client.send_message('sayyed_ahmad_mousavi',me.stringify())
	client.send_file('sayyed_ahmad_mousavi', '/home/cabox/workspace/ahmad/a2.py')
finally:
	client.disconnect()
