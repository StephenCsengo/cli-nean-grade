from models import User, Coffee, Rating, session


def add_coffee(self):
    new_coffee = {
        "roaster": input("Enter the roaster: "),
        "name": input("Enter the coffee's name: "),
        "roast_level": input("Enter the roast level: "),
    }

    Coffee.add_new_coffee(
        roaster=new_coffee["roaster"],
        name=new_coffee["name"],
        roast_level=new_coffee["roast_level"],
    )