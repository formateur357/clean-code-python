def calc_total(sous_total: float, express: bool, fragile: bool) -> float :
    port = 0.0 if sous_total >= 50 else 5.0

    if express:
        port += 10.0

    if fragile:
        port += 2.0

    return sous_total + port