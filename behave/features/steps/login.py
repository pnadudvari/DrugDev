from behave import *


@given(u'the user has the correct credentials')
def step_impl(context):
    context.browser.get('http://www.google.com')
    raise NotImplementedError(
        u'STEP: Given the user has the correct credentials')


@when(u'the enter username')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the enter username')


@when(u'the user enters password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user enters password')


@when(u'clicks Login')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clicks Login')


@then(u'the user is presented with a welcome message')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the user is presented with a welcome message')


@given(u'the user has the incorrect credentials')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Given the user has the incorrect credentials')


@then(u'the user is presented with a error message')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the user is presented with a error message')
