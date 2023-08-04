evt = {
    "Records": [
        {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "us-east-1",
            "eventTime": "2023-08-03T15:45:16.651Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {"principalId": "AWS:AIDA3UJ5MYOHPZKQ3YR66"},
            "requestParameters": {"sourceIPAddress": "181.167.199.143"},
            "responseElements": {
                "x-amz-request-id": "8YS976MFA742K314",
                "x-amz-id-2": "GR3Ce4yf6z50t2OIzqp9ihqAKdkgtP2G9IZD8TO9iyDp4fL88hPhQ2IleDmW/ABeUQ/UejAn8PdqB9FdvMSs0cGF5GKJ6Jg7",
            },
            "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "487595db-d088-4e46-8318-2a6ec1d72370",
                "bucket": {
                    "name": "csv-trnx-card",
                    "ownerIdentity": {"principalId": "A2AZ8FS1MQREIN"},
                    "arn": "arn:aws:s3:::csv-trnx-card",
                },
                "object": {
                    "key": "txns.json",
                    "size": 393,
                    "eTag": "86f05c096ebbe00e63dd5f83e5f67089",
                    "sequencer": "0064CBCB8C22D35573",
                },
            },
        }
    ]
}


if __name__ == "__main__":
    import json

    print(json.dumps(evt))