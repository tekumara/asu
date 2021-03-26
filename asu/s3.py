from typing import List, Optional

import boto3
import botocore.exceptions


def describe_all_buckets_encryption() -> List[List[Optional[str]]]:

    s3_client = boto3.client("s3")

    response = s3_client.list_buckets()

    bucket_names: List[str] = [b["Name"] for b in response["Buckets"]]

    result: List[List[Optional[str]]] = [["Bucket", "SSEAlgorithm", "KMSMasterKeyID"]]

    for name in bucket_names:
        try:
            encryption = s3_client.get_bucket_encryption(Bucket=name)
            default_sse = encryption["ServerSideEncryptionConfiguration"]["Rules"][0]["ApplyServerSideEncryptionByDefault"]

        except botocore.exceptions.ClientError:
            default_sse = None

        if default_sse:
            result.append([name, default_sse['SSEAlgorithm'], default_sse.get('KMSMasterKeyID', None)])
        else:
            result.append([name, None, None])

    return result
