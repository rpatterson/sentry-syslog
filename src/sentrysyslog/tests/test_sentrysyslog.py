"""
sentry-syslog unit and integration tests.
"""

import contextlib
import logging
import io
import tempfile
import unittest

import sentrysyslog


class SentrySyslogTests(unittest.TestCase):
    """
    sentry-syslog unit and integration tests.
    """

    def getCliErrorMessages(self, args):
        """
        Run the CLI script and return any error messages.
        """
        stderr_file = io.StringIO()
        with self.assertRaises(SystemExit):
            with contextlib.redirect_stderr(stderr_file):
                sentrysyslog.main(args=args)
        return stderr_file.getvalue()

    def test_cli_help(self):
        """
        The command line script is self-docummenting.
        """
        stdout_file = io.StringIO()
        with self.assertRaises(SystemExit):
            with contextlib.redirect_stdout(stdout_file):
                sentrysyslog.main(args=["--help"])
        stdout = stdout_file.getvalue()
        self.assertIn(
            sentrysyslog.__doc__.strip(),
            stdout,
            "The console script name missing from --help output",
        )

    def test_cli_options(self):
        """
        The command line script accepts options controlling behavior.
        """
        with tempfile.NamedTemporaryFile() as input_file:
            result = sentrysyslog.main(
                args=["--input-file", input_file.name, "--event-level", "CRITICAL"]
            )
        self.assertIsNone(
            result, "Wrong console script options return value",
        )

    def test_cli_option_errors(self):
        """
        The command line script displays useful messages for invalid option values.
        """
        stderr = self.getCliErrorMessages(args=["--input-file=__non_existent_file__"])
        self.assertIn(
            "No such file or directory: '__non_existent_file__'",
            stderr,
            "Wrong invalid --input-file option message",
        )

        stderr = self.getCliErrorMessages(args=["--event-level=getLogger"])
        self.assertIn(
            "doesn't correspond to a logging level",
            stderr,
            "Wrong invalid --event-level option message",
        )

        stderr = self.getCliErrorMessages(
            args=["--event-level=__non_existent_logging_module_attribute__"]
        )
        self.assertIn(
            "Could not look up logging level",
            stderr,
            "Wrong invalid --event-level option message",
        )

        logging.__non_level_int_attribute__ = 999
        try:
            stderr = self.getCliErrorMessages(
                args=["--event-level=__non_level_int_attribute__"]
            )
        finally:
            del logging.__non_level_int_attribute__
        self.assertIn(
            "doesn't match the given level name",
            stderr,
            "Wrong non-level integer attribute --event-level option message",
        )
