import sys
from typing import List

import boto3
import botocore.exceptions


def describe_all_buckets_encryption() -> None:

    s3_client = boto3.client("s3")

    response = s3_client.list_buckets()

    bucket_names = [b["Name"] for b in response["Buckets"]]

    print("|Bucket|SSEAlgorithm|KMSMasterKeyID|")
    for name in bucket_names:
        try:
            encryption = s3_client.get_bucket_encryption(Bucket=name)
            default_sse = encryption["ServerSideEncryptionConfiguration"]["Rules"][0]["ApplyServerSideEncryptionByDefault"]

        except botocore.exceptions.ClientError:
            default_sse = None

        if default_sse:
            print(f"|{name:50s}|{default_sse['SSEAlgorithm']}|{default_sse.get('KMSMasterKeyID', None)}|")
        else:
            print(f"|{name}|None|None|")


def main(args: List[str] = sys.argv[1:]) -> None:
    describe_all_buckets_encryption()

if __name__ == "__main__":
    main()
