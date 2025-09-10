import pytest
from src.shipping import calc_total


@pytest.mark.parametrize(
        "sous_total, express, fragile, total_attendu",
        [
            (40, False, False, 45),
            (40, True, False, 55),
            (40, False, True, 47),
            (40, True, True, 57),
            (50, False, False, 50),
            (50, True, False, 60),
            (50, False, True, 52),
            (50, True, True, 62)
        ]
)
def test_calc_total(sous_total, express, fragile, total_attendu):
    total = calc_total(float(sous_total), express, fragile)
    assert int(total) == total_attendu