class Jogador:
    def __init__(self, name_player, hp_player, atack_player, defense_player):
        self.__name_player = name_player
        self.__hp_player = hp_player
        self.__atack_player = atack_player
        self.__defense_player = defense_player

    @property
    def show_name_player(self):
        return self.__name_player

    @property
    def show_hp_player(self):
        return self.__hp_player
    
    @show_hp_player.setter
    def __modify_hp_player(self, damage):
        self.__hp_player -= damage

    @property
    def show_atack_player(self):
        return self.__atack_player
    
    @show_atack_player.setter
    def __modify_atack_player(self,value):
        self.__atack_player += value
    
    @property
    def show_defense_player(self):
        return self.__defense_player
    
    @show_defense_player.setter
    def __modify_defense_player(self,value):
        self.__defense_player += value


    def attack_enemy(self, target):
        pass
   

   