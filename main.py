import time

from text_to_speech import robotik_speak
import speech_to_text
import text_to_speech
from fuzzywuzzy import fuzz
from config import *
from execute_cmd import execute_cmd
from PIL import Image
import psutil

TURN_ON_TEXT = f'Hello master. {ROBOTIK_NAME} just woke up from sleep, how can I help you?'


def respond(voice: str):
    includes = [x in voice for x in ROBOTIK_ALIAS]
    if any(includes):
        # Robotik is being addressed
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in ROBOTIK_CMD_LIST.keys():
            execute_cmd('something else')
        else:
            execute_cmd(cmd['cmd'])
    else:
        cmd = recognize_cmd(filter_cmd(voice))
        if cmd['percent'] > 80:
            if cmd['cmd'] not in ROBOTIK_CMD_LIST.keys():
                execute_cmd('something else')
            else:
                execute_cmd(cmd['cmd'])
        elif cmd['percent'] > 60:
            execute_cmd('something else')


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in ROBOTIK_ALIAS:
        cmd = cmd.replace(x, "")

    for x in ROBOTIK_STOP_WORDS:
        cmd = cmd.replace(x, "")

    return cmd.strip()


def recognize_cmd(cmd: str):
    ans = {'cmd': '', 'percent': 0}
    for command, keywords in ROBOTIK_CMD_LIST.items():

        for x in keywords:
            perc = fuzz.ratio(cmd, x)
            if perc > ans['percent']:
                ans['cmd'] = command
                ans['percent'] = perc

    return ans


if __name__ == "__main__":

    speech_to_text.listen(respond)