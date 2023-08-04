import json
import logging
import mimetypes
import os

import boto3
from botocore.exceptions import ClientError

from storipy.io import read_csv
from storipy.io.prompt import prompt

# "/media/cristian/Ubuntu/dev/stori/txns.csv"


def main():
    # Read inputs from prompt
    name, email, file_name = prompt()

    if name and email:
        file_name = file_name or "txns.csv"
        print(f"Reading CSV file: {file_name}...")

        # Read CSV input file
        rows = read_csv(file_name)
        print(f"Total records: {len(rows)}...")

        body = {
            "user": {"name": name, "email": email},
            "data": rows,
        }
        body = json.dumps(body)

        # Save the CSV as JSON in S3
        if create_file(body, "csv-trnx-card", file_name):
            print(f"Upload successful...")
        else:
            print(f"File upload failed!")


def create_file(body, bucket, file_name):
    """Upload a JSON file to an S3 bucket"""

    object_name = os.path.basename(file_name.replace(".csv", ".json"))
    mime, _ = mimetypes.guess_type(object_name)

    # Initialize boto3 to use the S3 client.
    s3_client = boto3.client("s3")

    print(f"Uploading `{file_name}` to S3...")
    try:
        res = s3_client.put_object(
            Body=body, Bucket=bucket, Key=object_name, ContentType=mime
        )
    except ClientError as e:
        logging.error(e)
        return False

    # Generate the S3 presigned URL
    presigned_url = s3_client.generate_presigned_url(
        ClientMethod="get_object", Params={"Bucket": bucket, "Key": object_name}
    )

    # Print the created S3 presigned URL
    print(f"URL -> {presigned_url}")
    return True


if __name__ == "__main__":
    main()
