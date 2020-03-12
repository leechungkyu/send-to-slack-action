import json
import requests
import os

def main():
    slack_url = os.environ["INPUT_SLACK_URL"]
    slack_payload = {"text": " Push has occurred in master branch"}
    res = requests.post(url=slack_url, data=json.dumps(slack_payload))
    print(res)

if __name__ == "__main__":
    main()