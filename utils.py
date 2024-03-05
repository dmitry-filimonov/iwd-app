import random

def load_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return [line.strip() for line in content.split('---') if line.strip()]

def get_random_item(items, shown_items):
    available_items = [item for item in items if item not in shown_items]
    if not available_items:
        shown_items.clear()
        return None
    chosen_item = random.choice(available_items)
    shown_items.append(chosen_item)
    return chosen_item