list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
countPlayers = len(list_players)
teamOne = list_players[0: int(countPlayers/2)]
teamTwo = list_players[int(countPlayers/2): countPlayers]

print(teamOne)
print(teamTwo)
