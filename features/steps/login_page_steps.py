from behave import given, when, then


@given('Open signin page')
def open_signin_page(context):
    context.app.signin_page.open_signin_page()


@when('User log in')
def signin_successfully(context):
    context.app.signin_successfully('nomacas893@fogdiver.com', 'ReelyCool!')
