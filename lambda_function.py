import json
import os

import boto3

from storipy import evt
from storipy.models import Account
from storipy.render import render_body
from storipy.sender import send


__DIR__ = os.path.dirname(os.path.abspath(__file__))


def lambda_handler(event, context):
    data = get_object(event)

    account = Account()
    account.insert(data["data"])

    body = account.recap(**data["user"])
    print(body)

    tmpl = os.path.join(__DIR__, "templates", "email.html")
    html = render_body(tmpl, **body)

    res = send(data["user"]["email"], data["user"]["name"], html)
    print(res)
    return res


def get_object(event):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    s3 = boto3.resource("s3")
    obj = s3.Object(bucket, key)
    content = obj.get()["Body"].read().decode("utf-8")

    data = json.loads(content)

    return data


if __name__ == "__main__":
    lambda_handler(evt, None)
