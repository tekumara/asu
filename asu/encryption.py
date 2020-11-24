from typing import Any, Dict, List, Optional

import boto3
import botocore.exceptions
import sys


def describe_all_buckets_encryption() -> None:

    s3_client = boto3.client("s3")

    response = s3_client.list_buckets()

    bucket_names = [b["Name"] for b in response["Buckets"]]

    for name in bucket_names:
        try:
            encryption = s3_client.get_bucket_encryption(Bucket=name)
            default_sse = encryption["ServerSideEncryptionConfiguration"]["Rules"][0]["ApplyServerSideEncryptionByDefault"]

        except botocore.exceptions.ClientError as error:
            default_sse = None

        print(f"{name}\t{default_sse['SSEAlgorithm'] if default_sse else 'None'}\t{default_sse['KMSMasterKeyID'] if default_sse and default_sse.get('KMSMasterKeyID', None) else 'None'}")


def main(args: List[str] = sys.argv[1:]) -> None:
    describe_all_buckets_encryption()

if __name__ == "__main__":
    main()
