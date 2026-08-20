import json
import urllib.request
import urllib.error

BOARD = "https://aidc.nadir.sh/"

TEAM = "3"
BY = "FayAlaamri"
MODEL = "HuggingFaceTB/SmolLM2-135M-Instruct"
IMAGE = "ghcr.io/fayalaamri/aidc-team-server-group3:latest"

import json
import urllib.request
import urllib.error

BOARD = "https://aidc.nadir.sh/"

TEAM = "3"
BY = "FayAlaamri"
MODEL = "HuggingFaceTB/SmolLM2-135M-Instruct"
IMAGE = "ghcr.io/fayalaamri/aidc-team-server-group3:latest"


def request(url, body=None):
    data = json.dumps(body).encode() if body else None

    headers = {
        "User-Agent": "aidc-student/1.0"
    }

    if body:
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(
        url,
        data=data,
        headers=headers
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read())

    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())

status, result = request("http://localhost:8000/generate")

print("my server said", status)
print(json.dumps(result, indent=2))

if status != 200:
    raise SystemExit("/generate failed")

status, reply = request(
    BOARD,
    {
        "team": TEAM,
        "by": BY,
        "model": MODEL,
        "image": IMAGE,
        "tokens_per_sec": result["tokens_per_sec"],
        "sample": result["sample"]
    }
)
print("the board said", status)
print(json.dumps(reply, indent=2))
def request(url, body=None):
    data = json.dumps(body).encode() if body else None

    headers = {
        "User-Agent": "aidc-student/1.0"
    }

    if body:
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(
        url,
        data=data,
        headers=headers
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw_data = r.read()
            try:
                return r.status, json.loads(raw_data)
            except json.decoder.JSONDecodeError:
                return r.status, {"error": "Server returned non-JSON", "raw_response": raw_data.decode(errors="ignore")}

    except urllib.error.HTTPError as e:
        raw_data = e.read()
        try:
            return e.code, json.loads(raw_data)
        except json.decoder.JSONDecodeError:
            return e.code, {"error": "Server returned non-JSON", "raw_response": raw_data.decode(errors="ignore")}


status, result = request("http://localhost:8000/generate")

print("my server said", status)
print(json.dumps(result, indent=2))

if status != 200:
    raise SystemExit("/generate failed")

status, reply = request(
    BOARD,
    {
        "team": TEAM,
        "by": BY,
        "model": MODEL,
        "image": IMAGE,
        "tokens_per_sec": result["tokens_per_sec"],
        "sample": result["sample"]
    }
)
print("the board said", status)
print(json.dumps(reply, indent=2))
