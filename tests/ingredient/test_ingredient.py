from src.models.ingredient import Ingredient, Restriction
# noqa: F401, E261, E501


# Req 1
def test_ingredient():
    first_ing = Ingredient("bacon")
    second_ing = Ingredient("frango")
    third_ing = Ingredient("bacon")
    assert first_ing.name == "bacon"
    assert first_ing.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    assert first_ing.__eq__(second_ing) is False
    assert first_ing.__eq__(third_ing) is True
    assert repr(first_ing) == "Ingredient('bacon')"
    assert hash(first_ing) == hash(third_ing)
    assert hash(first_ing) != hash(second_ing)
