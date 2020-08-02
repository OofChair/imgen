from aiohttp import ClientSession
from io import BytesIO
from PIL import Image


async def getarg(request):
    arg = [request.headers.get('avatars'), request.headers.get('usernames'), request.headers.get('text')]
    return [i.split(',') if i else i for i in arg]


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
    return result
