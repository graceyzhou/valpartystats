import valorant
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = valorant.LocalClient(reigon='na')

session = client.get_session()
presences = client.get_presences()

running=True

def formatter(presences):
	player_list = []
	for player in presences['participants']:
		player_info = player['game_name'] + '#' + player['game_tag']
		player_list.append(player_info)

	print(player_list)

while running:
	chat = client.get_pregame_chat_info()
	if len(chat['conversations']) == 0:
		print("Not in Pregame Lobby")
		time.sleep(5)
	else:
		#edge case: someone whispers to me. that means i got a lot of friends. go you!
		participants = client.fetch_participants(chat['conversations'][0]['cid'])
		running=False
		formatter(participants)

#edge case: will stop running after one game




