"""
Tests for sending syslog messages to Sentry as events.
"""

from sentry_sdk import hub


SYSLOG_INFO_LINE = (
    "<78>1 2016-01-15T00:04:01+00:00 host1 CROND 10391 - "
    '[meta sequenceId="29"] some_message\n'
)
SYSLOG_ALERT_LINE = "<409>1 2016-01-15T00:00:00Z host2 prg - - - message\n"

DSN_VALUE = "https://<key>@sentry.io/1"


def cleanupBreadcrumbs():
    """
    Clear any collected breadcrumbs between tests.
    """
    for client, scope in hub.Hub.current._stack:
        scope.clear_breadcrumbs()
