"""
Send syslog messages to Sentry as events.
"""

import sys
import logging
import argparse

# Manage version through the VCS CI/CD process
try:
    from . import version
except ImportError:  # pragma: no cover
    version = None
if version is not None:  # pragma: no cover
    __version__ = version.version


def logging_level_type(level_name):
    """
    Lookup the logging level corresponding to the named level.
    """
    try:
        level = getattr(logging, level_name)
    except Exception as exc:
        raise argparse.ArgumentTypeError(
            "Could not look up logging level from name:\n{}".format(exc.args[0])
        )
    if not isinstance(level, int):
        raise argparse.ArgumentTypeError(
            "Level name {!r} doesn't correspond to a logging level, got {!r}".format(
                level_name, level
            )
        )

    looked_up_level_name = logging.getLevelName(level)
    if looked_up_level_name != level_name:
        raise argparse.ArgumentTypeError(
            (
                "Looked up logging level {!r} "
                "doesn't match the given level name {!r}"
            ).format(level, level_name)
        )

    return level


# Define command line options and arguments
parser = argparse.ArgumentParser(description=__doc__.strip())
parser.add_argument(
    "--input-file",
    "-i",
    type=argparse.FileType("r"),
    default=sys.stdin,
    help="Take the syslog messages from this file, one per-line. (default: stdin)",
)
parser.add_argument(
    "--event-level",
    "-e",
    type=logging_level_type,
    default=logging.ERROR,
    help=(
        "Capture log messages of this level and above as Sentry events.  "
        "All other events are captured as Sentry breadcrumbs. "
        "(default: %(default)s)"
    ),
)


def run(
    input_file=parser.get_default("input_file"),
    event_level=parser.get_default("event_level"),
):
    pass


run.__doc__ = __doc__


def main(args=None):
    args = parser.parse_args(args=args)
    with args.input_file:
        return run(**vars(args))


main.__doc__ = __doc__


if __name__ == "__main__":  # pragma: no cover
    main()
