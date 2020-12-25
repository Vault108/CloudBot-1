import requests
from requests import HTTPError

from cloudbot import hook


def get_data(url, reply, bot, params=None):
    try:
        r = requests.get(url, headers={'User-Agent': bot.user_agent}, params=params)
        r.raise_for_status()
    except HTTPError:
        reply("an error has occurred.")
        raise

    return r


@hook.command(autohelp=False)
def insult(reply, bot):
    """- insults someone"""
    r = get_data('https://evilinsult.com/generate_insult.php?lang=en&type=json', reply, bot, params={'max_length': 100})
    json = r.json()
    response = json['insult']
    return response


