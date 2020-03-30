"""
Tests for sending syslog messages to Sentry as events.
"""

import pathlib

from sentry_sdk import hub

with open(pathlib.Path(__file__).parent / "info.syslog.log") as info_opened:
    SYSLOG_INFO_LINE = info_opened.read()
with open(pathlib.Path(__file__).parent / "alert.syslog.log") as alert_opened:
    SYSLOG_ALERT_LINE = alert_opened.read()

DSN_VALUE = "https://<key>@sentry.io/1"


def cleanupBreadcrumbs():
    """
    Clear any collected breadcrumbs between tests.
    """
    for client, scope in hub.Hub.current._stack:
        scope.clear_breadcrumbs()
