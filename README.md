# botsnack

Image classifier for a Telegram group chat.
A [separate repository](https://github.com/fluv/telegram-trading/) handles the Telegram stuff.

This repo contains a HTTP API that the bot can talk to.
It forwards on what people say when they invoke `/botsnack`, and we send what the bot should say in response.

## Configuration

Environment variables:
* `CLASSIFIER_MODEL`

Optional `options.json` configuration file.
Format `{"tench": 0, ...}` with an integer opinion rating from -2 (hate) to 0 (neutral) to 4 (adore).
