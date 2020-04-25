"""
Send syslog messages to Sentry as events, distribution/package metadata.
"""

import setuptools

with open("README.rst", "r") as readme:
    LONG_DESCRIPTION = readme.read()

setuptools.setup(
    name="sentry-syslog",
    author="Ross Patterson",
    author_email="me@rpatterson.net",
    description="Send syslog messages to Sentry as events",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    url="https://github.com/rpatterson/sentry-syslog",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    use_scm_version=dict(
        write_to="src/sentrysyslog/version.py", local_scheme="no-local-version",
    ),
    setup_requires=["setuptools_scm"],
    install_requires=["syslog-rfc5424-parser", "sentry-sdk"],
    extras_require=dict(
        dev=[
            "pytest",
            "pre-commit",
            "coverage",
            "flake8",
            "autoflake",
            "autopep8",
            "flake8-black",
        ]
    ),
    entry_points=dict(console_scripts=["sentry-syslog=sentrysyslog:main"]),
)
