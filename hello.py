from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

ops = { 'add': lambda a,b: a + b,
        'sub': lambda a,b: a - b,
        'mul': lambda a,b: a * b,
        'div': lambda a,b: a / b }

def simple_math(request):
    op = request.matchdict['op']
    op_fun = ops[op]

    a = int(request.matchdict['a'])
    b = int(request.matchdict['b'])

    result = op_fun(a, b)

    return Response(str(result))

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')

    config.add_route('simple_math', '/math/{a}/{op}/{b}')
    config.add_view(simple_math, route_name='simple_math')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
