from io import BytesIO

from flask import send_file
from PIL import Image

from utils import http
from utils.endpoint import Endpoint


class Slap(Endpoint):
    def generate(self, avatars, text, usernames):
        base = Image.open('assets/batslap/batman.jpg').resize((1000, 500))
        avatar = Image.open(http.get_image(avatars[0])).resize((220, 220))
        avatar2 = Image.open(http.get_image(avatars[1])).resize((200, 200))
        base.paste(avatar, (580, 260), avatar)
        base.paste(avatar2, (350, 70), avatar2)

        b = BytesIO()
        base.save(b, format='png')
        b.seek(0)
        return send_file(b, mimetype='image/png')


def setup():
    return Slap()