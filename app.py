import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '463764249:AAGWjMhXWkvc2LyN76qjwQhcHq8cuK2WPWk'
WEBHOOK_URL = 'https://b1271dc6.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'me',
        'user',
        'europe',
        'asia',
        'northamerica',
        'england',
        'taiwan',
        'usa',
        'bigben',
        'mount_ali',
        'statue_of_liberty'
    ],    
    transitions=[
        {
            'trigger': 'gogo',
            'source': 'me',
            'dest': 'user',
            'conditions': 'where_to_go'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'europe',
            'conditions': 'is_going_to_europe'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'asia',
            'conditions': 'is_going_to_asia'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'northamerica',
            'conditions': 'is_going_to_northamerica'
        },
        {
            'trigger': 'country_1',
            'source': 'europe',
            'dest': 'england',
            'conditions': 'is_going_to_england'
        },
        {
            'trigger': 'country_2',
            'source': 'asia',
            'dest': 'taiwan',
            'conditions': 'is_going_to_taiwan'
        },
        {
            'trigger': 'country_3',
            'source': 'northamerica',
            'dest': 'usa',
            'conditions': 'is_going_to_usa'
        },
        {
            'trigger': 'scene_1',
            'source': 'england',
            'dest': 'bigben',
            'conditions': 'is_going_to_bigben'
        },
        {
            'trigger': 'scene_2',
            'source': 'taiwan',
            'dest': 'mount_ali',
            'conditions': 'is_going_to_mount_ali'
        },
        {
            'trigger': 'scene_3',
            'source': 'usa',
            'dest': 'statue_of_liberty',
            'conditions': 'is_going_to_statue_of_liberty'
        }
    ],
    initial='me',
    auto_transitions=False,
    show_conditions=True,
    ignore_invalid_triggers=True
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
                sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.gogo(update)
    machine.advance(update)
    machine.country_1(update)
    machine.country_2(update)
    machine.country_3(update)
    machine.scene_1(update)
    machine.scene_2(update)
    machine.scene_3(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')
    
if __name__ == "__main__":
    _set_webhook()
    app.run()