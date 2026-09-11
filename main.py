import random

names = [
    "Courier", "Lone Wanderer", "Sole Survivor", "Vulpes", "Morrowind", "Dovahkiin",
    "Nerevar", "Tiber", "Ulfric", "Ayla", "Breno", "Cael", "Dália", "Eron", "Fiona",
    "Gael", "Helena", "Ícaro", "Júlia", "Kael", "Lívia", "Milo", "Nádia", "Orion",
    "Pietro", "Quíron", "Ravi", "Sofia", "Téo", "Ulisses", "Valentina", "Willa",
    "Yara", "Zara", "José", "Maria", "Pedro",
]

classes = [
    "Vault Dweller", "Ranger (NCR)", "Paladino (Brotherhood)", "Ghoul Scavenger", "Caçador de Dragões",
    "Dovahkiin", "Alquimista", "Arqueiro", "Bardo", "Clérigo", "Druida", "Feiticeiro",
    "Guerreiro", "Ladino", "Mago", "Monge", "Paladino", "Ranger",
    "Cavaleiro", "Necromante", "Berserker",
]

races = [
    "Humano", "Anão", "Elfo", "Meio-elfo", "Orc", "Troll", "Goblin",
    "Halfling", "Draconato", "Tiefling", "Fada", "Gnomo", "Vampiro",
    "Sereiano", "Gigante", "Centauro",
    "Ghoul", "Super Mutante", "Khajiit", "Argoniano", "Dunmer (Dark Elf)",
    "Altmer (High Elf)", "Nórdico", "Dragonborn (Dovahkiin)",
]

attributes = [
    "Força",
    "Percepção",
    "Resistência",
    "Carisma",
    "Inteligência",
    "Agilidade",
    "Sorte",
]

def generate_character():
    character_attributes = {}

    for attr in attributes:
        value = random.randint(1, 20)
        character_attributes[attr] = value

    character = {
        "nome": random.choice(names),
        "classe": random.choice(classes),
        "raça": random.choice(races),
        "atributos": character_attributes,
    }

    return character

def max_attribute(character):
    major_value = 1
    major_attr = ""

    for attr, value in character["atributos"].items():
        if value > major_value:
            major_value = value
            major_attr = attr

    return major_attr, major_value

def main():
    character = generate_character()

    print("=" * 38)
    print("       GERADOR DE PERSONAGENS")
    print("=" * 38)
    print("Seu novo personagem está pronto!\n")

    print(f"Nome: {character['nome']}")
    print(f"Classe: {character['classe']}")
    print(f"Raça: {character['raça']}")

    formatted_attributes = []

    for attr, value in character["atributos"].items():
        text = f"{attr}: {value}"
        formatted_attributes.append(text)

    result = "\n".join(formatted_attributes)

    print(f"\nAtributos:")
    print(result)

    major_attr, major_value = max_attribute(character)

    print(f"O maior atributo é {major_attr} com {major_value} pontos!")

    print("\nBoa aventura!")

if __name__ == "__main__":
    main()
