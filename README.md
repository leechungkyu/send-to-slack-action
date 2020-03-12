# Send-To-Slack Github Actions  
> When a push occurs in the master branch, a slack alarm is generated.

## Parameters
Make sure that these parameters are required as [Github Secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets)
| Parameter | Type | Description |
|-----------|------|-------------|
| `SLACK_URL` | `string` | [Incoming Webhooks for Slack](https://api.slack.com/messaging/webhooks) |

## Usage

```yaml
name: When a push occurs in the master branch, a slack alarm is generated.
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - name: notify
        id: notify
        
        uses: leechungkyu/send-to-slack-action@master
        with:
          slack_url: ${{ secrets.SLACK_URL }}
      
      - name : Run
        run: |
          echo 'Run!'
```

## License

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
