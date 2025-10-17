import requests
import config
import sys

base_events = []
event_functions = config.event_functions
event_counts = config.event_counts

def fetch_user_info(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}/events")
        if response.status_code == 404:
            print("User not found!")
            sys.exit(1)
    except Exception as e:
        print("Could not connect to the API, perhaps you have no internet connection?")
        sys.exit(1)

    for event in response.json():
        structure = {
            "type": event["type"],
            "repository": event["repo"]["name"],
            "payload": event["payload"]
        }
        base_events.append(structure)

    for i in base_events:
        event_counts[i["type"]].update({ "repository": event_counts[i["type"]]["repository"] + [i["repository"]], "count": (event_counts[i["type"]]["count"] + 1)})
        # event counts is crazy at this point
    
    print(create_output())

def create_output():
    console_output = "Output:\n"
    for thing in event_counts:
        if event_counts[thing]["count"] == 0:
            continue
        console_output += f"- {event_functions[thing](event_counts[thing]["repository"], event_counts[thing]["count"])}\n"
    return console_output
