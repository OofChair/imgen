from aiohttp import ClientSession
from io import BytesIO
from PIL import Image
from aiohttp import web
from random import randint


async def getarg(request):
    res = [[], [], []]
    arg = [
        request.headers.get("avatars"),
        request.headers.get("usernames"),
        request.headers.get("text"),
        request.query.get("avatars"),
        request.query.get("usernames"),
        request.query.get("text"),
    ]
    if all(a is None for a in arg):
        raise web.HTTPInternalServerError()
    for i, j in enumerate(arg):
        if j:
            t = j.split(",")
            res[i % 3] = t
    return [None if i == [] else i for i in res]


async def get(session: object, url: object) -> object:
    async with session.get(url) as response:
        return await response.read()


async def getavatar(array: list) -> list:
    result = []
    for url in array:
        async with ClientSession() as session:
            url = await get(session, url)
        file = BytesIO(url)
        img = Image.open(file)
        result.append(img)
    return \
        result


def modify_all_pixels(im, noise_gen):
    width, height = im.size
    pxls = im.load()
    for x in range(width):
        for y in range(height):
            pxls[x, y] = noise_gen(x, y, *pxls[x, y])


def add_noise(image, strength=100):
    def pixel_noise(x, y, r, g, b):
        noise = int(randint(0, strength) - strength / 2)
        return max(0, min(r + noise, 255)), max(0, min(g + noise, 255)), max(0, min(b + noise, 255))
    modify_all_pixels(image, pixel_noise)
    return image