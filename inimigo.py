class Inimigo:
     def __init__(self, name_enemy, hp_enemy, atack_enemy, defense_enemy):
        self.__name_enemy = name_enemy
        self.__hp_enemy = hp_enemy
        self.__atack_enemy = atack_enemy
        self.__defense_enemy = defense_enemy

     @property
     def show_name_enemy(self):
        return self.__name_enemy

     @property
     def show_hp_enemy(self):
        return self.__hp_enemy
    
     @show_hp_enemy.setter
     def __modify_hp_enemy(self, damage):
        self.__hp_enemy -= damage

     @property
     def show_atack_enemy(self):
        return self.__atack_enemy
    
     @property
     def show_defense_enemy(self):
        return self.__defense_enemy
    
    

    
   

    