from aiohttp import web
import aiohttp_jinja2
import jinja2
from endpoints.endpoint import app_routes
from os import environ

routes = web.RouteTableDef()
app = web.Application()


@routes.get('/')
async def index(request):
    return aiohttp_jinja2.render_template('index.html', request, context=None)

if __name__ == '__main__':
    app.add_routes(routes)
    app.add_routes(app_routes)
    app.router.add_static('/assets/',
                          path='./views/assets',
                          name='assets')
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./views'))
    port = int(environ.get('PORT', 8080))
    web.run_app(app, port=port)
