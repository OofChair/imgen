from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from aiohttp import web
from utils.textutils import render_text_with_emoji, wrap, auto_text_size
from endpoints.tools import getavatar, get, getarg

app_routes = web.RouteTableDef()


@app_routes.get('/abandon')
async def abandon(request):
    args = await getarg(request)
    text = args[2][0]
    base = Image.open('assets/abandon/abandon.bmp')
    font = ImageFont.truetype('assets/fonts/verdana.ttf', 24)
    canv = ImageDraw.Draw(base)
    render_text_with_emoji(base, canv, (25, 413), wrap(font, text, 320), font, 'black')
    base = base.convert('RGB')
    b = BytesIO()
    base.save(b, format='jpeg')
    b.seek(0)
    with open('temp.jpeg', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.jpeg')


@app_routes.get('/airpods')
async def airpods(request):
    blank = Image.new('RGBA', (400, 128), (255, 255, 255, 0))
    args = await getarg(request)
    avatar = await getavatar(array=args[0])
    avatar = avatar[0]
    left = Image.open('assets/airpods/left.gif')
    right = Image.open('assets/airpods/right.gif')
    out = []
    for i in range(0, left.n_frames):
        left.seek(i)
        right.seek(i)
        f = blank.copy().convert('RGBA')
        l = left.copy().convert('RGBA')
        r = right.copy().convert('RGBA')
        f.paste(l, (0, 0), l)
        f.paste(avatar, (136, 0), avatar)
        f.paste(r, (272, 0), r)
        out.append(f.resize((400, 128), Image.LANCZOS).convert('RGBA'))

    b = BytesIO()
    out[0].save(b, format='gif', save_all=True, append_images=out[1:], loop=0, disposal=2, optimize=True,
                duration=30, transparency=0)
    b.seek(0)
    with open('temp.gif', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.gif')


@app_routes.get('/america')
async def america(request):
    args = await getarg(request)
    av = await getavatar(array=args[0])
    img1 = av[0].convert('RGBA').resize((480, 480))
    img2 = Image.open('assets/america/america.gif')
    img1.putalpha(128)
    out = []
    for i in range(0, img2.n_frames):
        img2.seek(i)
        f = img2.copy().convert('RGBA').resize((480, 480))
        f.paste(img1, (0, 0), img1)
        out.append(f.resize((256, 256)))

    b = BytesIO()
    out[0].save(b, format='gif', save_all=True, append_images=out[1:], loop=0, disposal=2, optimize=True, duration=30)
    b.seek(0)
    with open('temp.gif', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.gif')


@app_routes.get('/aborted')
async def aborted(request):
    base = Image.open('assets/aborted/aborted.bmp')
    args = await getarg(request)
    av = await getavatar(array=args[0])
    img1 = av[0].convert('RGBA').resize((90, 90))
    base.paste(img1, (390, 130), img1)
    base = base.convert('RGB')

    b = BytesIO()
    base.save(b, format='jpeg')
    b.seek(0)
    with open('temp.jpeg', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.jpeg')


@app_routes.get('/affect')
async def affect(request):
    args = await getarg(request)
    av = await getavatar(array=args[0])
    avatar = av[0].resize((200, 157)).convert('RGBA')
    base = Image.open('assets/affect/affect.bmp').convert('RGBA')

    base.paste(avatar, (180, 383, 380, 540), avatar)
    base = base.convert('RGB')

    b = BytesIO()
    base.save(b, format='jpeg')
    b.seek(0)
    with open('temp.jpeg', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.jpeg')


@app_routes.get('/armor')
async def armor(request):
    base = Image.open('assets/armor/armor.bmp').convert('RGBA')
    args = await getarg(request)
    text = args[2][0]
    font = ImageFont.truetype('assets/fonts/sans.ttf')
    font, text = auto_text_size(text, font, 207,
                                font_scalar=0.8)
    canv = ImageDraw.Draw(base)

    render_text_with_emoji(base, canv, (34, 371), text, font=font, fill='Black')
    base = base.convert('RGB')

    b = BytesIO()
    base.save(b, format='jpeg')
    b.seek(0)
    with open('temp.jpeg', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.jpeg')


@app_routes.get('/balloon')
async def balloon(request):
    args = await getarg(request)
    text = args[2]
    base = Image.open('assets/balloon/balloon.bmp').convert('RGBA')
    font = ImageFont.truetype('assets/fonts/sans.ttf')
    canv = ImageDraw.Draw(base)
    print(text)
    if len(text) != 2:
        text = ["Separate the items with a", "comma followed by a space"]

    balloon, label = text

    balloon_text_1_font, balloon_text_1 = auto_text_size(balloon, font, 162)
    balloon_text_2_font, balloon_text_2 = auto_text_size(balloon, font, 170, font_scalar=0.95)
    balloon_text_3_font, balloon_text_3 = auto_text_size(balloon, font, 110, font_scalar=0.8)
    label_font, label_text = auto_text_size(label, font, 125)

    render_text_with_emoji(base, canv, (80, 180), balloon_text_1, font=balloon_text_1_font, fill='Black')
    render_text_with_emoji(base, canv, (50, 530), balloon_text_2, font=balloon_text_2_font, fill='Black')
    render_text_with_emoji(base, canv, (500, 520), balloon_text_3, font=balloon_text_3_font, fill='Black')
    render_text_with_emoji(base, canv, (620, 155), label_text, font=label_font, fill='Black')
    base = base.convert('RGB')

    b = BytesIO()
    base.save(b, format='jpeg')
    b.seek(0)
    with open('temp.jpeg', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.jpeg')


@app_routes.get('/bed')
async def bed(request):
    args = await getarg(request)
    av = await getavatar(array=args[0])
    avatar = av[0].resize((100, 100)).convert('RGBA')
    avatar2 = av[1].resize((100, 100)).convert('RGBA')
    base = Image.open('assets/bed/bed.bmp').convert('RGBA')
    avatar_small = avatar.copy().resize((70, 70))
    base.paste(avatar, (25, 100), avatar)
    base.paste(avatar, (25, 300), avatar)
    base.paste(avatar_small, (53, 450), avatar_small)
    base.paste(avatar2, (53, 575), avatar2)
    base = base.convert('RGBA')

    b = BytesIO()
    base.save(b, format='png')
    b.seek(0)
    with open('temp.png', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.png')


@app_routes.get('/bongocat')
async def bongocat(request):
    args = await getarg(request)
    avatar = await getavatar(array=args[0])
    base = Image.open('assets/bongocat/bongocat.bmp').convert('RGBA')
    avatar = avatar[0].resize((750, 750)).convert('RGBA')

    avatar.paste(base, (0, 0), base)
    avatar = avatar.convert('RGBA')

    b = BytesIO()
    avatar.save(b, format='png')
    b.seek(0)
    with open('temp.png', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.png')

"""
@app_routes.get('/boo')
async def boo(request):
    base = Image.open(self.assets.get('assets/boo/boo.bmp')).convert('RGBA')
    # We need a text layer here for the rotation
    canv = ImageDraw.Draw(base)

    text = text.split(', ')

    if len(text) != 2:
        text = ["Separate the items with a", "comma followed by a space"]

    first, second = text

    first_font, first_text = auto_text_size(first,
                                            self.assets.get_font('assets/fonts/sans.ttf'), 144,
                                            font_scalar=0.7)
    second_font, second_text = auto_text_size(second,
                                              self.assets.get_font('assets/fonts/sans.ttf'),
                                              144,
                                              font_scalar=0.7)

    canv.text((35, 54), first_text, font=first_font, fill='Black')
    canv.text((267, 57), second_text, font=second_font, fill='Black')
    base = base.convert('RGB')

    b = BytesIO()
    base.save(b, format='jpeg')
    b.seek(0)

"""
@app_routes.get('/brain')
async def brain(request):
    base = Image.open('assets/brain/brain.bmp')
    font = ImageFont.truetype('assets/fonts/verdana.ttf', size=30)
    args = await getarg(request)
    text = args[2]
    if len(text) < 4:
        a, b, c, d = 'you need, four items, for this, command (split by commas)'.split(',')
    else:
        a, b, c, d = text[:4]

    a, b, c, d = [wrap(font, i, 225).strip() for i in [a, b, c, d]]

    canvas = ImageDraw.Draw(base)
    canvas.text((15, 40), a, font=font, fill='Black')
    canvas.text((15, 230), b, font=font, fill='Black')
    canvas.text((15, 420), c, font=font, fill='Black')
    canvas.text((15, 610), d, font=font, fill='Black')

    b = BytesIO()
    base.save(b, format='jpeg')
    b.seek(0)
    with open('temp.jpeg', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.jpeg')


@app_routes.get('/brazzers')
async def brazzers(request):
    args = await getarg(request)
    avatar = await getavatar(array=args[0])
    avatar = avatar[0]
    base = Image.open('assets/brazzers/brazzers.bmp')
    aspect = avatar.width / avatar.height

    new_height = int(base.height * aspect)
    new_width = int(base.width * aspect)
    scale = new_width / avatar.width
    size = (int(new_width / scale / 2), int(new_height / scale / 2))

    base = base.resize(size).convert('RGBA')
    avatar.paste(base, (avatar.width - base.width,
                        avatar.height - base.height), base)
    avatar = avatar.convert('RGBA')

    b = BytesIO()
    avatar.save(b, format='png')
    b.seek(0)
    with open('temp.png', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.png')


@app_routes.get('/byemom')
async def byemom(request):
    base = Image.open('assets/byemom/mom.bmp')
    args = await getarg(request)
    print(args)
    avatar = await getavatar(array=args[0])
    avatar = avatar[0].convert('RGBA').resize((70, 70), resample=Image.BICUBIC)
    avatar2 = avatar.copy().resize((125, 125), resample=Image.BICUBIC)
    text_layer = Image.new('RGBA', (350, 25))
    bye_layer = Image.new('RGBA', (180, 51), (255, 255, 255))
    font = ImageFont.truetype('assets/fonts/arial.ttf', size=20)
    bye_font = ImageFont.truetype('assets/fonts/arimobold.ttf', size=14)
    canv = ImageDraw.Draw(text_layer)
    bye = ImageDraw.Draw(bye_layer)
    username = args[1][0] or 'Tommy'
    msg = 'Alright {} im leaving the house to run some errands'.format(username)
    text = args[2][0]
    text = wrap(font, text, 500)
    msg = wrap(font, msg, 200)

    render_text_with_emoji(text_layer, canv, (0, 0), text, font=font, fill='Black')
    render_text_with_emoji(bye_layer, bye, (0, 0), msg, font=bye_font, fill=(42, 40, 165))
    text_layer = text_layer.rotate(24.75, resample=Image.BICUBIC, expand=True)

    base.paste(text_layer, (350, 443), text_layer)
    base.paste(bye_layer, (150, 7))
    base.paste(avatar, (530, 15), avatar)
    base.paste(avatar2, (70, 340), avatar2)
    base = base.convert('RGBA')

    b = BytesIO()
    base.save(b, format='png')
    b.seek(0)
    with open('temp.png', 'wb') as e:
        e.write(b.getvalue())
    return web.FileResponse(path='./temp.png')
