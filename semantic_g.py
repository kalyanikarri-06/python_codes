# Semantic network
network = {
    "Dog": {"is_a": ["Mammal"], "has": ["Fur"], "can": ["Bark"]},
    "Cat": {"is_a": ["Mammal"], "has": ["Fur"], "can": ["Meow"]},
    "Bird": {"is_a": ["Bird"], "has": ["Wings"], "can": ["Fly"]},
}

# Query functions
def get_relations(node): return network.get(node, {})
def can_do(animal, action): return action in network.get(animal, {}).get("can", [])

# Examples
print(get_relations("Dog"))
print(can_do("Cat", "Fly"))