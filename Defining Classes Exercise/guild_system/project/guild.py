
class Guild:
    def __init__(self, name: str):
        self.name = name
        self.player_list = []

    def assign_player(self, player):
        if player.guid == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != 'Unaffiliated' and player.guild != self.name:
            return f"Player {player.name} is in another guild."
        else:
            self.player_list.append(player.name)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in [p.name for p in self.player_list]:
            return f"Player {player_name} is not in the guild."
        self.player_list.remove(player_name)
        return f"Player {player_name} has been removed from the guild."


    def guild_info(self):
        data = f'Guild: {self.name}'
        for p in self.player_list:
            data += p.player_info()
        return data








