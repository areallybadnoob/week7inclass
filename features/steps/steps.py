from calculator import add, subtract, multiply, divide, cosine, sine, tangent
from behave import given, when, then

@given("the calculator is open")
def step_given_calculator_open(context):
    context.result = None
    context.error = None

@when("I add {a:d} and {b:d}")
def step_when_add(context, a, b):
    context.result = add(a, b)

@then("the result should be {expected_result:d}")
def step_then_result(context, expected_result):
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"

@when("I subtract {b:d} from {a:d}")
def step_when_subtract(context, a, b):
    context.result = subtract(a, b)

@when("I multiply {a:d} and {b:d}")
def step_when_multiply(context, a, b):
    context.result = multiply(a, b)

@when("I divide {a:d} by {b:d}")
def step_when_divide(context, a, b):
    try:
        context.result = divide(a, b)
    except ValueError as e:
        context.error = str(e)

@then('I should see an error message "{expected_error}"')
def step_then_error_message(context, expected_error):
    assert context.error == expected_error, f"Expected error message '{expected_error}', but got '{context.error}'"

@when("I calculate the cosine of {x:d}")
def step_when_cosine(context, x):
    context.result = cosine(x)

@when("I calculate the sine of {x:d}")
def step_when_sine(context, x):
    context.result = sine(x)

@when("I calculate the tangent of {x:d}")
def step_when_tangent(context, x):
    try:
        context.result = tangent(x)
    except ValueError as e:
        context.error = str(e)

@when("I calculate the tangent of 90 degrees (π/2 radians)")
def step_when_tangent_90(context):
    try:
        context.result = tangent(90)
    except ValueError as e:
        context.error = str(e)