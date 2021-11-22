from argparse import Action, ArgumentParser
from botocore.client import ClientError
import boto3

known_drivers = ['local', 's3']
class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unkown driver. Available drivers are 'local' & 's3'")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('url', help="URL of the PostgreSQL database to backup")
    parser.add_argument('--driver', help="how & where to store the backup",
            nargs=2,
            action=DriverAction,
            required=True)
    return parser

def create_bucket(bucketn):
    s3 = boto3.resource('s3')
    try:
        s3.meta.client.head_bucket(Bucket=bucketn)
    except ClientError:
        bucket = s3.create_bucket(Bucket=bucketn)

def main():
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        create_bucket(args.destination)
        storage.s3(client, dump.stdout, args.destination, 'example.sql')
    else:
        outfile = open(args.destination, 'wb')
        storage.local(dump.stdout, outfile)

