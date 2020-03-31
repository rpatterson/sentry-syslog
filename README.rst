================================================
sentry-syslog
================================================
Send Syslog RFC 5424 Messages to Senty as Events
------------------------------------------------

.. image:: https://github.com/rpatterson/sentry-syslog/workflows/Run%20linter,%20tests%20and,%20and%20release/badge.svg

The `sentry-syslog` command-line script sends `RFC 5424 IETF Syslog Protocol`_
message to Sentry as events as follows:

#. Initializes `Sentry's Python logging integration`_
#. Accepts one message per-line
#. Converts each message into a Python `logging` message
#. Logs the Python message to be handled by the `Sentry's Python logging integration`_


Installation
============

Install using any tool for installing standard Python 3 distributions such as `pip`_::

  $ sudo pip3 install sentry-syslog


Usage
=====

See the command-line help for details on options and arguments::

  $ sentry-syslog --help
  usage: sentry-syslog [-h] [--input-file INPUT_FILE]
                       [--event-level EVENT_LEVEL]
                       sentry_dsn

  Send syslog messages to Sentry as events.

  positional arguments:
    sentry_dsn            The DSN for your sentry DSN or client key.

  optional arguments:
    -h, --help            show this help message and exit
    --input-file INPUT_FILE, -i INPUT_FILE
                          Take the syslog messages from this file, one per-line.
                          (default: stdin)
    --event-level EVENT_LEVEL, -e EVENT_LEVEL
                          Capture log messages of this level and above as Sentry
                          events. All other events are captured as Sentry
                          breadcrumbs. (default: 40)

The script expects all the syslog lines it receives to be already filtered down to those
that should be captured in Sentry.  The level setting only determines which lines are
captured as breadcrumbs or events.

The correct invocation can then be used, for example, with `Rsyslog's omprog output
module`_ as the `binary` to selectively forward a system's syslog messages to Sentry as
events.  See the `example omprog configuration`_ which might be installed as follows
(will require adapting to the system)::

  $ sudo curl https://raw.githubusercontent.com/rpatterson/sentry-syslog/master/src/sentry_syslog/etc/rsyslog.d/99-sentry.conf >/etc/rsyslog.d/99-sentry.conf
  $ sudo editor /etc/rsyslog.d/99-sentry.conf
  $ sudo systemctl restart rsyslog.service


.. _RFC 5424 IETF Syslog Protocol: https://tools.ietf.org/html/rfc5424
.. _Sentry's Python logging integration: https://docs.sentry.io/platforms/python/logging/
.. _Python's logging facility: https://docs.python.org/3/library/logging.html
.. _pip: https://pip.pypa.io/en/stable/installing/
.. _Rsyslog's omprog output module:
   https://www.rsyslog.com/doc/v8-stable/configuration/modules/omprog.html
.. _example omprog configuration: ./src/sentry_syslog/etc/rsyslog.d/99-sentry.conf
