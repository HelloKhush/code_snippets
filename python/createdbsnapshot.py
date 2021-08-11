import argparse

import boto3

rds = boto3.client("rds")

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--snapshot-id", 
        help='The DB snapshot identifier (the new snapshot name)',
        required=True)
    parser.add_argument("--db-instance-id", 
        help='The DB instance identifier.',
        required=True)
    parser.add_argument("--destination-account-id", 
        help="The account ID to share this snapshot with")

    args = parser.parse_args()
    return args

def main():
    """
    Helper script used to create rds snapshot
    """
    args = parse_args()
    snapshot_id = args.snapshot_id
    db_instance_id = args.db_instance_id
    dest_account_id = args.destination_account_id

    resp = rds.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_id,
        DBInstanceIdentifier=db_instance_id,
    )

    waiter = rds.get_waiter('db_snapshot_completed')
    waiter.config.max_attempts = 120
    waiter.config.delay = 60
    print("Waiting for snapshot creation")
    waiter.wait(DBSnapshotIdentifier=snapshot_id)
    print("Snapshot created")

    # Modifies the snapshot so that it's available to the destination account 
    # ID.
    if dest_account_id:
        rds.modify_db_snapshot_attribute(
            DBSnapshotIdentifier=snapshot_id,
            AttributeName="restore",
            ValuesToAdd=[dest_account_id],
        )

if __name__ == "__main__":
    main()
