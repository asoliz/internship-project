from behave import given, when, then


@when("Click on off plan in left side menu")
def click_offplan_link(context):
    context.app.main_page.click_offplan_link()


@when("Filter by sales status of Out of Stocks")
def filter_by_outofstock(context):
    context.app.main_page.filter_by_outofstocks()


@then("Verify each product contains the out of stock tag")
def verify_correct_tag(context):
    context.app.main_page.verify_correct_tag('Out of Stock')
