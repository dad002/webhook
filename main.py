import requests
import json

yourKey = '193119f42d583601d5095b462bde9300'
yourToken = '051f6534202857a75e06a3c58358840f62a4e54fe268648aad672465cb2cb4c6'

boards_list = []
lists_list = []
cards_list = []

def auth():
	url = f'https://trello.com/1/authorize?expiration=1day&name=MyPersonalToken&scope=read&response_type=token&key={yourKey}'

def get_boards():
	url = f'https://api.trello.com/1/members/me/boards?key={yourKey}&token={yourToken}'

	response = requests.request(
		"GET",
		url
	)

	return json.loads(response.text)


def get_lists(boards_list):
	res = []
	for board in boards_list:
		board_id = board['id']
		url = f'https://api.trello.com/1/boards/{board_id}/lists?fields=all&id={board_id}&key={yourKey}&token={yourToken}'

		response = requests.request(
			"GET",
			url
		)
		res.extend(json.loads(response.text))
	return res


def get_card(lists_list):
	res = []
	for list_ in lists_list:
		lid = list_['id']
		url = f'https://api.trello.com/1/lists/{lid}/cards?key={yourKey}&token={yourToken}'

		response = requests.get(url)
		res.extend(json.loads(response.text))
	
	return res


lists_list = get_lists(get_boards())

cards = get_card(lists_list)
for card in cards:
	print(json.dumps(card, sort_keys=True, indent=4, separators=(",", ": "), ensure_ascii=False))