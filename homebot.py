"""
Main client file. This creates the slack connection
and parses for the trigger word then hands off
to the command parser to see what should be done.
"""
from slackclient import SlackClient
from command_parser import parse_command
from config import read_value
import time

def check_sessions():
    required_sessions = ''
    for session in ['Nest', 'Hue']:
        if read_value(session) == "True":
            required_sessions.append(session)
    return required_sessions


def create_sessions(required_sessions):




def create_slack_connection(token: str):
    sc = SlackClient(token)
    return sc


def listener(sc, trigger):
    sc.rtm_connect()
    while True:
        try:
            for slack_message in sc.rtm_read():
                message = slack_message.get('text')
                user = slack_message.get('user')
                room = slack_message.get('channel')
                if message and message.lower().startswith(trigger):
                    command = message.split(" ")[1:]
                    parse_command(command, sc)
            #
            time.sleep(.25)
        except:
            # horrible broad exception, but there's so many reasons
            # that you might not be able to read, it'd be messy to
            # catch them all explicitly. We don't care why it failed
            # only that we can reconnect.
            sc.rtm_connect()
