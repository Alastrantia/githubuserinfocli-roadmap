from event_types import *

event_functions = {
    "CreateEvent": create_event,
    "IssuesEvent": issue_event,
    "IssueCommentEvent": issue_comment_event,
    "PushEvent": push_event,
    "WatchEvent": star_event
}


event_counts = {
    "CreateEvent": {
        "repository": [],
        "count": 0
    },
    "IssuesEvent": {
        "repository": [],
        "count": 0
    },
    "IssueCommentEvent": {
        "repository": [],
        "count": 0
    },
    "PushEvent": {
        "repository": [],
        "count": 0
    },
    "WatchEvent": {
        "repository": [],
        "count": 0
    }
}