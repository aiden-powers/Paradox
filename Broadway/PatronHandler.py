import requests
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

patron_path = os.path.join(current_dir, "../Patron")
cards_path = os.path.join(current_dir, "../Patron/Cards")

characters = [
    ["Abrams", "https://deadlocked.wiki/images/6/6d/Abrams_card.png"],
    ["Bebop", "https://deadlocked.wiki/images/4/49/Bebop_card.png"],
    ["Dynamo", "https://deadlocked.wiki/images/7/70/Dynamo_card.png"],
    ["Grey_Talon", "https://deadlocked.wiki/images/5/5a/Grey_Talon_card.png"],
]

def check_card(character_card):
    """

    :param character_card:
    """
    name = cards_path + f"/{character_card[0]}.png"
    if not os.path.isfile(name):
        img_data = requests.get(character_card[1]).content
        with open(name, "wb") as f:
            f.write(img_data)

for character in characters:
    check_card(character)
    print(character[0])
