import requests
import os
import base64
import hashlib

current_dir = os.path.dirname(os.path.abspath(__file__))

patron_path = os.path.join(current_dir, "../Patron")
cards_path = os.path.join(current_dir, "../Patron/Cards")

characters = [
    ["Abrams", "https://deadlocked.wiki/images/6/6d/Abrams_card.png"],
    ["Bebop", "https://deadlocked.wiki/images/4/49/Bebop_card.png"],
    ["Dynamo", "https://deadlocked.wiki/images/7/70/Dynamo_card.png"],
    ["Grey Talon", "https://deadlocked.wiki/images/5/5a/Grey_Talon_card.png"],
    ["Haze", "https://deadlocked.wiki/images/1/1b/Haze_card.png"],
    ["Infernus", "https://deadlocked.wiki/images/6/6b/Infernus_card.png"],
    ["Ivy", "https://deadlocked.wiki/images/2/2c/Ivy_card.png"],
    ["Kelvin", "https://deadlocked.wiki/images/7/76/Kelvin_card.png"],
    ["Lash", "https://deadlocked.wiki/images/5/5a/Lash_card.png"],
    ["McGinnis", "https://deadlocked.wiki/images/5/55/McGinnis_card.png"],
    ["Mirage", "https://deadlocked.wiki/images/7/77/Mirage_card.png"],
    ["Mo & Krill", "https://deadlocked.wiki/images/a/a1/Mo_%26_Krill_card.png"],
    ["Paradox", "https://deadlocked.wiki/images/0/08/Paradox_card.png"],
    ["Pocket", "https://deadlocked.wiki/images/0/06/Pocket_card.png"],
    ["Seven", "https://deadlocked.wiki/images/c/cf/Seven_card.png"],
    ["Shiv", "https://deadlocked.wiki/images/b/b8/Shiv_card.png"],
    ["Vindicta", "https://deadlocked.wiki/images/6/69/Vindicta_card.png"],
    ["Viscous", "https://deadlocked.wiki/images/5/53/Viscous_card.png"],
    ["Warden", "https://deadlocked.wiki/images/1/10/Warden_card.png"],
    ["Wraith", "https://deadlocked.wiki/images/8/85/Wraith_card.png"],
    ["Yamato", "https://deadlocked.wiki/images/2/2b/Yamato_card.png"],
    ["Lady Geist", "https://deadlocked.wiki/images/e/e8/Lady_Geist_card.png"],
]

# using 9/27/2024 LIVE GAME CHARACTER list

def hash_string(input_string):
    # Create a new sha256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the bytes of the input string
    sha256_hash.update(input_string.encode('utf-8'))
    # Return the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

def check_card(character_card):
    """

    :param character_card:
    """
    #charactername = hash_string(character_card[0])
    charactername = character_card[0]
    print(charactername)
    name = cards_path + f"/{charactername}.png"
    name = name.replace(" ", "_")
    if not os.path.isfile(name):
        img_data = requests.get(character_card[1]).content
        with open(name, "wb") as f:
            f.write(img_data)

for character in characters:
    check_card(character)
    print(character[0])
