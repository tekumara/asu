from typing import Generator, List, Optional, Sequence

import boto3
import botocore.exceptions


def describe_all_buckets_encryption() -> Generator[Sequence[Optional[str]], None, None]:

    s3_client = boto3.client("s3")

    response = s3_client.list_buckets()

    bucket_names: List[str] = [b["Name"] for b in response["Buckets"]]

    yield ["Bucket", "SSEAlgorithm", "KMSMasterKeyID"]

    for name in bucket_names:
        try:
            encryption = s3_client.get_bucket_encryption(Bucket=name)
            default_sse = encryption["ServerSideEncryptionConfiguration"]["Rules"][0]["ApplyServerSideEncryptionByDefault"]

        except botocore.exceptions.ClientError:
            default_sse = None

        if default_sse:
            yield [name, default_sse['SSEAlgorithm'], default_sse.get('KMSMasterKeyID', None)]
        else:
            yield [name, None, None]
