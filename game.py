import time

class Hero:
    def __init__(self, health):
        self.health = health

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health <= 0

class Monster:
    def __init__(self, name, health, attack_interval, attack_damage):
        self.name = name
        self.health = health
        self.attack_interval = attack_interval
        self.attack_damage = attack_damage
        self.last_attack_time = time.monotonic()

    def hit(self, damage):
        self.health -= damage
        print(f"Hero hits {self.name}. {self.name} health is {self.health}")

    #def can_attack(self):
    #    return time.monotonic() - self.last_attack_time >= self.attack_interval
    def can_attack(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_attack_time
        return elapsed_time >= self.attack_interval


    def attack(self, hero):
        self.last_attack_time = time.monotonic()
        hero.hit(self.attack_damage)
        print(f"{self.name} hits hero. Hero health is {hero.health}")

    def is_dead(self):
        return self.health <= 0

hero = Hero(40)
orc = Monster("orc", 7, 1.5, 1)
dragon = Monster("dragon", 20, 2, 3)

print("Game start!\n")

while True:
    time.sleep(0.1)

    if orc.is_dead():
        print("Orc is dead!")
    elif orc.can_attack():
        orc.attack(hero)

    if dragon.is_dead():
        print("Dragon is dead!")
    elif dragon.can_attack():
        dragon.attack(hero)

    if orc.is_dead() and dragon.is_dead():
        print("You win!")
        break

    player_input = input("Type 'attack orc' or 'attack dragon': ")
    if player_input == "attack orc":
        orc.hit(2)
    elif player_input == "attack dragon":
        dragon.hit(2)
    else:
        print("Invalid input. Try again.")

    if hero.is_dead():
        print("You lose!")
        break

    print(f"Hero health: {hero.health}")
    print(f"Orc health: {orc.health}")
    print(f"Dragon health: {dragon.health}\n")
