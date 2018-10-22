from items import *

room_reception = {
    "name": "The Reception",

    "description":
    """You have just entered the Reception. The interior is very modern, with sleek furnishings and glass walls. 
    To your North, you can see the cafeteria. 
    To your west, you can see the cinema. 
    To your east, you can see the shopping centre. In front of you, sits a short, moustached receptionist, reading a newspaper.
    """,

    "exits": {"east": "The Shopping Centre", "west": "The Cinema", "north": "The Cafeteria"},

    "items": [item_keycard]
}

room_lab = {
    "name": "The Lab",

    "description":
    """You enter the lab. It isn't too crowded. A few people are around, working and seeing that stresses you 
    out becuase you feel that you should be working too. You look around, not knowing who you're looking for.""",

    "exits":  {"west": "The Library", "east": "The Cafeteria", "south": "The Cinema"},

    "items": [item_github, item_thebae]
}

room_library = {
    "name": "The Library",

    "description":
    """You are standing in the library, Everyone is working or reading quietly.
    As everyone is focusing on their own work, nobody notice that there is a notepad on the floor.
    The exit is to the east""",

    "exits": {"east": "The Lab"},

    "items": [item_notes, item_voucher, item_profoak]
}

room_cinema = {
    "name": "The Cinema",

    "description":
    """You wander around the city aimlessly and you find a cinema that you've never noticed before.
    It is oddly empty and you are perplexed as you've been in this area many times in the past and have never noticed it.
    The only movie you find playing is David Fincher's The Social Network.""",

    "exits": {"east": "The Reception", "north": "The Lab"},

    "items": [item_zucc]
}

room_cafeteria = {
    "name": "The Cafeteria",

    "description":
    """You walk in the cafeteria and immediately notice the lingering waft of coffee in the air. 
    You look at the black board by the cashier and notice that they're serving hotdogs and tiramisu. """,

    "exits": {"west": "The Lab", "north": "Home", "east": "The Closet", "south": "The Reception"},

    "items": [item_food, item_water, item_bluebear]
}

room_shoppingcentre = {
    "name": "The Shopping Centre",

    "description":
    """INSERT DESCRIPTION""",

    "exits": {"west": "The Reception", "north": "The Closet"},

    "items": [item_laptop, item_hideokojima]
}

room_home = {
    "name": "Home",

    "description":
    """INSERT DESCRIPTION""",

    "exits": {"east": "The Closet", "south": "The Cafeteria"},

    "items": [item_phone]
}

room_bar = {
    "name": "The Closet",

    "description":
    """You walk into The Closet to the sounds of loud music and people shouting. 
    There is a constant flashing of disco lights and on the board you see that all drinks are £1.13""",

    "exits": {"west": "The Cafeteria", "north": "Home", "south": "The Shopping Centre"},

    "items": [item_NICoffee, item_turing]
}

room_petshop = {
    "name": "The Petshop",

    "description":
    """INSERT DESCRIPTION""",

    "exits": {"INSERT EXITS"},

    "items": [item_food, item_water, item_bluebear, item_pythonguy]
}

room_cofffeeshop = {
    "name": "The Coffee Shop",

    "description":
    """You walk into the coffee shop and the strong aroma of coffee beans lingers around the room. 
    You can hear the constant grinding of beans and in the corner of your eye you notice a man with a grey beard wearing glasses.
    """,

    "exits": {"east": "The Shopping Centre", "west": "The Cinema", "north": "The Cafeteria"},

    "items": [item_keycard]
}



rooms = {
    "The Reception": room_reception,
    "The Lab": room_lab,
    "The Library": room_library,
    "The Cinema": room_cinema,
    "The Cafeteria": room_cafeteria,

    "The Shopping Centre": room_shoppingcentre,
    "The Closet": room_bar,
    "Home": room_home,
    "The Petshop": room_petshop,

}