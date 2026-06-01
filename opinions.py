import json

reactions = {
    -2: "Yuck, {a_thing}!",
    -1: "Ew, {a_thing}.",
    0: "Oh, {a_thing}.",
    1: "Oh, {a_thing}!",
    2: "Yum, {a_thing}!",
    3: "Yum, {a_thing}!!",
    4: "Yum, {a_thing}!!! :3"
}

try:
    with open('opinions.json') as f:
        opinions = json.load(f)
except FileNotFoundError:
    opinions = dict()

def get_opinion(label: str) -> int:
    try:
        return opinions[label]
    except KeyError:
        print("Could not find opinion for `{}`".format(label))
        return 0
