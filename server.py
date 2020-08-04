from aiohttp import web
import aiohttp_jinja2
import jinja2
from aiohttp.web import middleware
from endpoints.endpoint import app_routes
from os import environ

routes = web.RouteTableDef()


@middleware
async def middleware(request, handler):
    try:
        resp = await handler(request)
        print(resp.headers)
        return resp
    except web.HTTPException as e:
        if e.status == 404:
            return aiohttp_jinja2.render_template('404.html', request, context=None)
        if e.status == 500:
            return aiohttp_jinja2.render_template('500.html', request, context=None)

app = web.Application(middlewares=[middleware])


@routes.get('/')
async def index(request):
    return aiohttp_jinja2.render_template('index.html', request, context=None)


@routes.get('/docs')
async def docs(request):
    return aiohttp_jinja2.render_template('docs.html', request, context=None)

if __name__ == '__main__':
    app.add_routes(routes)
    app.add_routes(app_routes)
    app.router.add_static('/assets/',
                          path='./views/assets',
                          name='assets')
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./views'))
    port = int(environ.get('PORT', 8080))
    web.run_app(app, port=port)
