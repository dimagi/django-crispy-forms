#!/usr/bin/env python

import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
parent = os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))))

sys.path.insert(0, parent)

from django.test.simple import DjangoTestSuiteRunner
from django.conf import settings

settings.CRISPY_TEMPLATE_PACK = 'bootstrap3_transitional'


def runtests():
    return DjangoTestSuiteRunner(failfast=False).run_tests([
        'bootstrap3_crispy.TestBasicFunctionalityTags',
        'bootstrap3_crispy.TestFormHelper',
        'bootstrap3_crispy.TestBootstrapFormHelper',
        'bootstrap3_crispy.TestFormLayout',
        'bootstrap3_crispy.TestBootstrapFormLayout',
        'bootstrap3_crispy.TestBootstrap3FormLayout',
        'bootstrap3_crispy.TestLayoutObjects',
        'bootstrap3_crispy.TestBootstrapLayoutObjects',
        'bootstrap3_crispy.TestDynamicLayouts'
    ], verbosity=1, interactive=True)


if __name__ == '__main__':
    if runtests():
        sys.exit(1)
