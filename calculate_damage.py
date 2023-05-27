import jogador
import inimigo
def calculate_damage(attacker, target):
    if(isinstance(attacker, jogador.Jogador)):
        damage = attacker.show_atack_player - target.show_defense_enemy
        if damage <= 0:
            target.modify_hp(0)
        else:
            target.modify_hp(damage)

    elif(isinstance(attacker, inimigo.Inimigo)):
        damage = attacker.show_atack_enemy - target.show_defense_player
        if damage <= 0:
            target.modify_hp(0)
        else:
            target.modify_hp(damage)

    


