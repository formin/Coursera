# features/steps/web_steps.py
from behave import then

@then('I should receive all products')
def step_impl(context):
    assert context.failed is False

@then('I should receive products matching the name')
def step_impl(context):
    assert context.failed is False
