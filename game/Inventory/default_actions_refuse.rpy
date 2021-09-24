label cant_use(name, item_inventory, item_inventory_data, object_data):
    # name - character_name
    $ print name
    # item_inventory[item_name, amount]
    $ item_description = item_inventory_data["description"]
    mt "[item_description!t] and It? I can't use that!"
    return
