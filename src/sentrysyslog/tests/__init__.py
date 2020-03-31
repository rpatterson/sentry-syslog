"""
Tests for sending syslog messages to Sentry as events.
"""

import pathlib

from sentry_sdk import hub

with open(pathlib.Path(__file__).parent / "info.syslog.log") as info_opened:
    SYSLOG_INFO_LINES = info_opened.read()
with open(pathlib.Path(__file__).parent / "alert.syslog.log") as alert_opened:
    SYSLOG_ALERT_LINES = alert_opened.read()
with open(pathlib.Path(__file__).parent / "invalid.syslog.log") as invalid_opened:
    SYSLOG_INVALID_LINES = invalid_opened.read()

DSN_VALUE = "https://<key>@sentry.io/1"


def cleanupBreadcrumbs():
    """
    Clear any collected breadcrumbs between tests.
    """
    for client, scope in hub.Hub.current._stack:
        scope.clear_breadcrumbs()
