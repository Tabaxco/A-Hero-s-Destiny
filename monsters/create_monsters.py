import random

def create_monster(floor, difficulty: str= "easy"):
    attributes = []
    
    for attribute in range(6):
        if difficulty == 'easy':
            attributes.append(random.randint(1, 12) + (floor + 2))
        elif difficulty == 'medium':
            attributes.append(random.randint(10, 14) + (floor + 2))
        elif difficulty == 'boss':
            attributes.append(random.randint(12, 18) + (floor + 2))
    print(attributes)