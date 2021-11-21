#pgbackup pastgres://bob@example.com:5432/db_one --driver s3 backups

import pytest
from pgbackup import cli

url = "postgres://bob@example.com:5432/db_one --driver s3 backups"

@pytest.fixture 
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """
    without a specified driver the parser will exit

    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_unknown_driver(parser):
    """
    the parser will exit if it the driver name is unknown

    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', 'destination'])

def test_parser_with_known_driver(parser):
    """
    the parser will not exit if it the driver name is known

    """
    for driver in ['local','s3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])


def test_parser_with_driver(parser):
    """
    the parser will exit if it receives a driver without a destination

    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])


def test_parser_with_driver_and_destination(parser):
    """
    the parser will not exit if it receives a driver and a destination

    """
    args = parser.parse_args([url, '--driver', 'local', '/home/path'])

    assert args.url == url
    assert args.driver == 'local'
    assert args.destination == '/home/path'
