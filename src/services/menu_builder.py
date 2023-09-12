from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from src.models.dish import Dish

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        dishes = []

        for dish in self.menu_data.dishes:
            if (
                restriction is None
                or restriction not in dish.get_restrictions()
            ):
                if self._are_ingredients_available(dish):
                    menu_item = {
                        "dish_name": dish.name,
                        "ingredients": list(dish.get_ingredients()),
                        "price": dish.price,
                        "restrictions": list(dish.get_restrictions())
                    }
                    dishes.append(menu_item)

        return dishes

    def _are_ingredients_available(self, dish: Dish) -> bool:
        for ingredient in dish.get_ingredients():
            if self.inventory.inventory.get(ingredient, 0) <= 0:
                return False
        return True
