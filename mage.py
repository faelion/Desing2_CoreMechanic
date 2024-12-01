import math

class Mage:
    def __init__(self, control, focus, stream, physical_condition):
        self.control = control
        self.focus = focus
        self.stream = stream
        self.physical_condition = physical_condition

        # Calculated attributes
        self.health = 50 + physical_condition  # Linear scaling
        self.damage = 5 + focus  # Linear scaling
        self.range = 1 + int(math.log1p(control))  # Logarithmic scaling
        self.area = 1 + int(math.log1p(stream))  # Logarithmic scaling
        self.action_points = 1 + int(math.log1p(stream))  # Logarithmic scaling
        self.movement_points = 1 + int(math.log1p(physical_condition))  # Logarithmic scaling

    def take_damage(self, dmg):
        self.health -= dmg

    def cast_spell(self, target):
        spells_cast = 0
        while self.action_points > 0 and target.health > 0:
            target.take_damage(self.damage)
            self.action_points -= 1
            spells_cast += 1
        self.action_points = 1 + int(math.log1p(self.stream))  # Reset action points
        return spells_cast
