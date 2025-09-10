from behave import given, when, then
from src.shipping import calc_total

# before_all
# before_feature
# before_step
def before_scenario(context, scenario):
    context.sous_total = 0.0
    context.express = False
    context.fragile = False
    context.total = None

def _to_bool(text: str) -> bool:
    return text.strip().lower() in ("true", "vrai", "oui", "yes", "1")

@given("un sous_total de {sous_total:d}")
def step_sous_total(context, sous_total):
    context.sous_total = float(sous_total)

@given("l'option express est \"{flag}\"")
def step_express(context, flag):
    context.express = _to_bool(flag)

@given("l'option fragile est \"{flag}\"")
def step_fragile(context, flag):
    context.express = _to_bool(flag)

@when("Je calcule le total")
def step_calc_total(context):
    context.total = calc_total(context.sous_total, context.express, context.fragile)

@then("Le total doit être {total_attendu:d}")
def step_total_attendu(context, total_attendu):
    assert int(context.total) == total_attendu, f"Total attendu {total_attendu}, obtenu {context.total}"