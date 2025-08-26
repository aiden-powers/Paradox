import os

parent_dir_file = os.path.dirname(os.path.abspath(__file__))
print(f"Parent directory of current file: {parent_dir_file}")

missing_assets = 0

if os.path.isdir(parent_dir_file):
    entries = os.listdir(parent_dir_file)
    for entry in entries:
        full_path = os.path.join(parent_dir_file, entry)
        ignore_validate = ['characters.json', 'properties.json', 'readme.md', 'validate.py']
        if entry not in ignore_validate:
            validate_card = os.path.join(full_path, "Card.png")
            if not os.path.isfile(validate_card):
                print(f"Missing Card.png at: {entry}")
                missing_assets += 1
            validate_icon = os.path.join(full_path, "icon.png")
            if not os.path.isfile(validate_icon):
                print(f"Missing icon.png at: {entry}")
                missing_assets += 1
            validate_render = os.path.join(full_path, "render.png")
            if not os.path.isfile(validate_render):
                print(f"Missing render.png at: {entry}")
                missing_assets += 1
            validate_type = os.path.join(full_path, "type.png")
            if not os.path.isfile(validate_type):
                print(f"Missing type.png at: {entry}")
                missing_assets += 1

if missing_assets > 0:
    print(f"Found {missing_assets} missing assets")