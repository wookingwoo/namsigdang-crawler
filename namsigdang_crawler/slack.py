import requests

from data.account.slack_key import token, status_channel, debug_channel, send_slack


def slack_msg(msg, channel):
    print(msg)
    if not send_slack:
        return
    requests.post("https://slack.com/api/chat.postMessage",
                  headers={"Authorization": "Bearer " + token},
                  data={"channel": channel, "text": msg})
