import math

class Mage:
    def __init__(self, name, control, focus, stream, physical_condition):
        self.name = name
        self.control = control  # Afecta el rango
        self.focus = focus  # Aumenta el daño
        self.stream = stream  # Aumenta área y puntos de acción
        self.physical_condition = physical_condition  # Aumenta vida y movimiento
        
        # Atributos calculados
        self.health = 50 + self.log_scale(physical_condition)
        self.damage = 5 + self.linear_scale(focus)
        self.range = 1 + self.log_scale(control)
        self.area = 1 + self.log_scale(stream)
        self.action_points = 1 + self.linear_scale(stream)
        self.movement_points = 1 + self.log_scale(physical_condition)
        
    def log_scale(self, stat):
        return int(math.log1p(stat))
    
    def linear_scale(self, stat):
        return stat
    
    def take_damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} ha sido derrotado.")
    
    def cast_spell(self, target, distance):
        if distance <= self.range:
            print(f"{self.name} lanza un hechizo a {target.name} causando {self.damage} de daño.")
            target.take_damage(self.damage)
        else:
            print(f"{self.name} intenta lanzar un hechizo, pero está fuera de rango.")
    
    def move_closer(self, distance):
        movement = min(self.movement_points, distance)
        print(f"{self.name} se mueve {movement} unidades más cerca del oponente.")
        return distance - movement

# Inicialización de los magos
mage1 = Mage("Pyro", control=1, focus=4, stream=1, physical_condition=4)  # Daño y vida/movimiento
mage2 = Mage("Inferno", control=4, focus=1, stream=4, physical_condition=1)  # Rango y puntos de acción

# Simulación del combate
def battle_with_distance(mage1, mage2, initial_distance):
    distance = initial_distance
    turn = 1
    while mage1.health > 0 and mage2.health > 0:
        print(f"\nTurno {turn}")
        if turn % 2 == 1:
            # Turno de Mage1
            if distance > mage1.range:
                distance = mage1.move_closer(distance)
            mage1.cast_spell(mage2, distance)
        else:
            # Turno de Mage2
            if distance > mage2.range:
                distance = mage2.move_closer(distance)
            mage2.cast_spell(mage1, distance)
        
        print(f"Estado actual: {mage1.name}: {mage1.health} HP, {mage2.name}: {mage2.health} HP, Distancia: {distance}")
        turn += 1
    
    winner = mage1.name if mage1.health > 0 else mage2.name
    print(f"\n¡El ganador es {winner}!")

# Ejecutar el combate
battle_with_distance(mage1, mage2, initial_distance=10)
