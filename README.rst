================================================
sentry-syslog
================================================
Send Syslog RFC 5424 Messages to Senty as Events
------------------------------------------------

.. image:: https://github.com/rpatterson/sentry-syslog/workflows/Run%20linter,%20tests%20and,%20and%20release/badge.svg

The `sentry-syslog` command-line script sends `RFC 5424 IETF Syslog Protocol`_
message to Sentry as events as follows:

#. Re-configures `Python's logging facility`_ to closer match Syslog
#. Initializes `Sentry's Python logging integration`_
#. Accepts one message per-line
#. Converts each message into a Python `logging` message
#. Logs the Python message to be handled by the `Sentry's Python logging integration`_

This can be used, for example, with `Rsyslog's omprog output module`_ as the `binary` to
selectively forward a system's syslog messages to Sentry as events.  See the `example
omprog configuration`_.


.. _RFC 5424 IETF Syslog Protocol: https://tools.ietf.org/html/rfc5424
.. _Sentry's Python logging integration: https://docs.sentry.io/platforms/python/logging/
.. _Python's logging facility: https://docs.python.org/3/library/logging.html
.. _Rsyslog's omprog output module:
   https://www.rsyslog.com/doc/v8-stable/configuration/modules/omprog.html
.. _example omprog configuration: ./src/sentry_syslog/etc/rsyslog.d/99-sentry.conf
