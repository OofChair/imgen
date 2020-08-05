from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from aiohttp import web
from utils.textutils import render_text_with_emoji, wrap, auto_text_size
from utils.skew import skew
from endpoints.tools import getavatar, getarg

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
