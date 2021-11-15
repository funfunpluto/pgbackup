pgbackup
========


CLI for backup remote PostgreSQL database either locally or to S3


Preparing the Development
-------------------------

1. Ensure ``pig`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:example/pgbackup``
3. ``cd`` into the repository
4. Fetch development dependencies ``make instal``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in a full database URL, the storage driver, and the destination

S3 Example w/ bucket name:


::

        $ pgbackup pastgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

::

        $ pgbackup pastgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql



Running Tests
-------------

Run test locally using ``make`` if virtualenv is active

::
        $ make

if virtualenv isn't active then use:

::
        $ pipenv run make


