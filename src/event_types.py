def create_event(repository, amount):
    message = f"Created {amount} new repository(s): {repository}"
    return message

def star_event(repository, amount):
    message = f"Starred {amount} new repository(s): {repository}"
    return message

def issue_event(repository, amount):
    message = f"Made {amount} issue-related-action(s) in {repository}"
    return message

def push_event(repository, amount):
    message = f"Pushed {amount} commits to {repository}"
    return message

def issue_comment_event(repository, amount):
    message = f"Did {amount} something(s) with a comment in {repository}"
    return message