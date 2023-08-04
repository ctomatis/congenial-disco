import os

from mailjet_rest import Client


def send(to, name, body):
    mj = Client(auth=(os.environ["MJ_KEY"], os.environ["MJ_SECRET"]), version="v3.1")

    payload = {
        "Messages": [
            {
                "From": {"Email": "cgtomatis@gmail.com", "Name": "Cristian Tomatis"},
                "To": [{"Email": to, "Name": name}],
                "Subject": "Your account recap!",
                "HTMLPart": body,
            }
        ]
    }
    res = mj.send.create(data=payload)
    return res.json()
