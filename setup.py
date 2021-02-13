import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pg-extras",
    version="0.1.4",
    author="Pawel Urbanek",
    author_email="contact@pawelurbanek.com",
    description="Python PostgreSQL database performance insights. Locks, index usage, buffer cache hit ratios, vacuum stats and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pawurb/python-pg-extras",
    packages=['pg_extras'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database"
    ],
    python_requires='>=3.6',
    install_requires=[
      "SQLAlchemy>=1.3",
      "setuptools",
      "tabulate",
      "psycopg2"
    ]
)
