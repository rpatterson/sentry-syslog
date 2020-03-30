"""
sentry-syslog tests for integrating with Python's logging facility.
"""

import io
import logging
import unittest

import sentrysyslog
from .. import tests


class SentrySyslogLoggingTests(unittest.TestCase):
    """
    sentry-syslog tests for integrating with Python's logging facility.
    """

    def test_logging_run(self):
        """
        The run loop logs each syslog line as a Python logging record.
        """
        stdin_file = io.StringIO()
        stdin_file.write(tests.SYSLOG_INFO_LINE)
        stdin_file.seek(0)

        with self.assertLogs("cron.CROND", level=logging.INFO) as logged:
            self.addCleanup(tests.cleanupBreadcrumbs)
            sentrysyslog.run(stdin_file)

        self.assertEqual(len(logged.records), 1, "Wrong number of logging records")
        self.assertEqual(
            logged.records[0].msg,
            "some_message",
            "Wrong syslog line log record message",
        )
        self.assertIn(
            "hostname",
            logged.records[0].args,
            "Logging record arguments missing syslog field",
        )
