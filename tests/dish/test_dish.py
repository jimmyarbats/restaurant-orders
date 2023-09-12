from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    first_dish = Dish("Lasanha", 20.00)
    sec_dish = Dish("Lasanha", 20.00)
    first_ingredient = Ingredient("queijo mussarela")
    sec_ingredient = Ingredient("presunto")

    assert first_dish == sec_dish
    assert first_dish.price == 20.00
    assert first_dish.name == 'Lasanha'

    with pytest.raises(
        TypeError
    ):
        Dish("Lasanha", "20.00")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Lasanha", -20.00)
    assert first_dish.__hash__() == hash("Dish('Lasanha', R$20.00)")
    first_dish.add_ingredient_dependency(first_ingredient, 1)
    first_dish.add_ingredient_dependency(sec_ingredient, 1)
    assert first_dish.recipe == {first_ingredient: 1, sec_ingredient: 1}
    assert first_dish.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }

    assert first_dish.get_ingredients() == {first_ingredient, sec_ingredient}
