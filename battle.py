from mage import Mage

def simulate_battle(mage1, mage2):
    distance = 10  # Initial distance
    turn = 1
    while mage1.health > 0 and mage2.health > 0:
        if turn % 2 == 1:
            # Mage1's turn
            if distance > mage1.range:
                distance -= mage1.movement_points
            else:
                mage1.cast_spell(mage2)
        else:
            # Mage2's turn
            if distance > mage2.range:
                distance -= mage2.movement_points
            else:
                mage2.cast_spell(mage1)
        turn += 1

    winner = "Mage1" if mage1.health > 0 else "Mage2"
    return winner, turn