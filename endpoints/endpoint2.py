from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageEnhance
from io import BytesIO
from os import listdir
from aiohttp import web
from utils.textutils import render_text_with_emoji, wrap
from endpoints.tools import getavatar, getarg, add_noise
from random import randint
from math import ceil

app_routes2 = web.RouteTableDef()


@app_routes2.get('/cry')
async def cry(request):
    base = Image.open('assets/cry/cry.bmp')
    font = ImageFont.truetype('assets/fonts/tahoma.ttf', size=20)
    canv = ImageDraw.Draw(base)
    text = request.headers.get('text')
    text = wrap(font, text, 180)
    render_text_with_emoji(base, canv, (382, 80), text, font=font, fill='Black')

    b = BytesIO()
    base.save(b, format='jpeg')
    b.seek(0)
    with open('temp.jpeg', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.jpeg')


@app_routes2.get('/dab')
async def dab(request):
    base = Image.open('assets/dab/dab.bmp').convert('RGBA')
    args = await getarg(request)
    avatar = await getavatar(array=args[0])
    avatar = avatar[0].resize((500, 500)).convert('RGBA')
    final_image = Image.new('RGBA', base.size)

    final_image.paste(avatar, (300, 0), avatar)
    final_image.paste(base, (0, 0), base)

    b = BytesIO()
    final_image.save(b, format='png')
    b.seek(0)
    with open('temp.png', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.png')


@app_routes2.get('/dank')
async def dank(request):
    args = await getarg(request)
    avatar = await getavatar(array=args[0])
    avatar = avatar[0].resize((320, 320)).convert('RGBA')

    horn = Image.open('assets/dank/horn.bmp') \
        .convert('RGBA') \
        .resize((100, 100)) \
        .rotate(315, resample=Image.BICUBIC)
    horn2 = ImageOps.mirror(horn.copy().resize((130, 130)).rotate(350, resample=Image.BICUBIC))
    hit = Image.open('assets/dank/hit.bmp').convert('RGBA').resize((40, 40))
    gun = Image.open('assets/dank/gun.bmp').convert('RGBA').resize((250, 205))
    faze = Image.open('assets/dank/faze.bmp').convert('RGBA').resize((60, 40))

    blank = Image.new('RGBA', (256, 256), color=(254, 0, 0))
    blank.paste(avatar, (-20, -20), avatar)
    frames = []

    for i in range(8):
        base = blank.copy()
        if i == 0:
            base.paste(horn, (175, 0), horn)
            base.paste(horn2, (-60, 0), horn2)
            base.paste(hit, (90, 65), hit)
            base.paste(gun, (120, 130), gun)
            base.paste(faze, (5, 212), faze)
        else:
            base.paste(horn, (165 + randint(-8, 8), randint(0, 12)), horn)
            base.paste(horn2, (-50 + randint(-6, 6), randint(-2, 10)), horn2)
            base.paste(hit, (110 + randint(-30, 30), 55 + randint(-30, 30)), hit)
            base.paste(gun, (120, 130), gun)
            base.paste(faze, (12 + randint(-6, 6), 210 + randint(-2, 10)), faze)

        frames.append(base)

    b = BytesIO()
    frames[0].save(b, save_all=True, append_images=frames[1:], format='gif', loop=0, duration=20,
                   optimize=True)
    b.seek(0)
    with open('temp.gif', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.gif')


@app_routes2.get('/deepfry')
async def deepfry(request):
    args = await getarg(request)
    avatar = await getavatar(array=args[0])
    avatar = avatar[0].resize((400, 400)).convert('RGBA')

    joy, hand, hundred, fire = [
        Image.open(f'assets/deepfry/{asset}.bmp')
            .resize((100, 100))
            .rotate(randint(-30, 30))
            .convert('RGBA')
        for asset in ['joy', 'ok-hand', '100', 'fire']
    ]

    avatar.paste(joy, (randint(20, 75), randint(20, 45)), joy)
    avatar.paste(hand, (randint(20, 75), randint(150, 300)), hand)
    avatar.paste(hundred, (randint(150, 300), randint(20, 45)), hundred)
    avatar.paste(fire, (randint(150, 300), randint(150, 300)), fire)

    noise = avatar.convert('RGB')
    noise = add_noise(noise, 25)
    noise = ImageEnhance.Contrast(noise).enhance(randint(5, 20))
    noise = ImageEnhance.Sharpness(noise).enhance(17.5)
    noise = ImageEnhance.Color(noise).enhance(randint(-15, 15))

    b = BytesIO()
    noise.save(b, format='png')
    b.seek(0)
    with open('temp.png', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.png')


@app_routes2.get('/delete')
async def delete(request):
    base = Image.open('assets/delete/delete.bmp').convert('RGBA')
    args = await getarg(request)
    avatar = await getavatar(array=args[0])
    avatar = avatar[0].resize((195, 195)).convert('RGBA')

    base.paste(avatar, (120, 135), avatar)
    base = base.convert('RGBA')

    b = BytesIO()
    base.save(b, format='png')
    b.seek(0)
    with open('temp.png', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.png')


@app_routes2.get('/disability')
async def disability(request):
    args = await getarg(request)
    avatar = await getavatar(array=args[0])
    avatar = avatar[0].resize((175, 175)).convert('RGBA')
    base = Image.open('assets/disability/disability.bmp').convert('RGBA')

    base.paste(avatar, (450, 325), avatar)
    base = base.convert('RGBA')

    b = BytesIO()
    base.save(b, format='png')
    b.seek(0)
    with open('temp.png', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.png')


@app_routes2.get('/doglemon')
async def doglemon(request):
    base = Image.open('assets/doglemon/doglemon.bmp')
    font = ImageFont.truetype('assets/fonts/medium.woff', size=30)
    canv = ImageDraw.Draw(base)
    text = request.headers.get('text')
    try:
        lemon, dog = text.replace(' ,', ',', 1).split(',', 1)
    except ValueError:
        lemon = 'Text that is not seperated by comma'
        dog = 'Dank Memer'
    lemon = wrap(font, lemon, 450)
    dog = wrap(font, dog, 450)
    render_text_with_emoji(base, canv, (850, 100), lemon[:180], font=font, fill='Black')
    render_text_with_emoji(base, canv, (500, 100), dog[:200], font=font, fill='White')

    base = base.convert('RGB')
    b = BytesIO()
    base.save(b, format='jpeg')
    b.seek(0)
    with open('temp.jpeg', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.jpeg')


@app_routes2.get('/door')
async def door(request):
    args = await getarg(request)
    avatar = await getavatar(array=args[0])
    avatar = avatar[0].resize((479, 479)).convert('RGBA')
    base = Image.open('assets/door/door.bmp').convert('RGBA')
    final_image = Image.new('RGBA', base.size)

    final_image.paste(avatar, (250, 0), avatar)
    final_image.paste(base, (0, 0), base)
    final_image = final_image.convert('RGBA')

    b = BytesIO()
    final_image.save(b, format='png')
    b.seek(0)
    with open('temp.png', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.png')


@app_routes2.get('/egg')
async def egg(request):
    base = Image.open('assets/egg/egg.bmp').resize((350, 350)).convert('RGBA')
    args = await getarg(request)
    avatar = await getavatar(array=args[0])
    avatar = avatar[0].resize((50, 50)).convert('RGBA')

    base.paste(avatar, (143, 188), avatar)
    base = base.convert('RGBA')

    b = BytesIO()
    base.save(b, format='png')
    b.seek(0)
    with open('temp.png', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.png')


@app_routes2.get('/excuseme')
async def excuseme(request):
    base = Image.open('assets/excuseme/excuseme.bmp')

    font = ImageFont.truetype('assets/fonts/sans.ttf', size=40)
    canv = ImageDraw.Draw(base)
    text = request.headers.get('text')
    text = wrap(font, text, 787)
    render_text_with_emoji(base, canv, (20, 15), text, font=font, fill='Black')

    base = base.convert('RGB')

    b = BytesIO()
    base.save(b, format='jpeg')
    b.seek(0)
    with open('temp.jpeg', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.jpeg')


@app_routes2.get('/expanddong')
async def expanddong(request):
    text = request.headers.get('text')
    text = text[:500]
    lines = ceil((len(text) * 128) / 1920) + 1
    base = Image.new('RGBA', (1920, lines * 128), (255, 255, 255, 0))
    line = 0
    pos = 0
    chars = dict()
    for i in listdir('assets/expanddong'):
        if i.endswith('.bmp'):
            chars[i[0]] = Image.open(f'assets/expanddong/{i}')
    for word in text.split(' '):
        if 15 - pos <= len(word):
            pos = 0
            line += 1
        for char in word:
            char = char.lower()
            if chars.get(char):
                base.paste(chars[char], (pos * 128, line * 128))
            pos += 1
        pos += 1
        if pos >= 15:
            pos = 0
            line += 1

    base = base.convert('RGBA')

    b = BytesIO()
    base.save(b, format='png')
    b.seek(0)
    with open('temp.png', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.png')


@app_routes2.get('/expandingwwe')
async def expandingwwe(request):
    base = Image.open('assets/expandingwwe/expandingwwe.jpg')
    font = ImageFont.truetype('assets/fonts/verdana.ttf', size=30)

    text = request.headers.get('text')
    text = text.replace(', ', ',')

    if len(text.split(',')) < 5:
        a, b, c, d, e = 'you need, five items, for this, command, (split by commas)'.split(',')
    else:
        a, b, c, d, e = text.split(',', 4)

    a, b, c, d, e = [wrap(font, i, 225).strip() for i in [a, b, c, d, e]]

    canvas = ImageDraw.Draw(base)
    canvas.text((5, 5), a, font=font, fill='Black')
    canvas.text((5, 205), b, font=font, fill='Black')
    canvas.text((5, 410), c, font=font, fill='Black')
    canvas.text((5, 620), d, font=font, fill='Black')
    canvas.text((5, 825), e, font=font, fill='Black')

    b = BytesIO()
    base.save(b, format='jpeg')
    b.seek(0)
    with open('temp.jpeg', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.jpeg')