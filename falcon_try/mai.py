import falcon
from wsgiref.simple_server import make_server


class Resource():
    def on_get(self, req, resp):
        qs = req.params

        resp.body = '{"message":"test"}'
        resp.body = str(qs)
        resp.status = falcon.HTTP_200


api = falcon.API()
r = Resource()
api.add_route('/',r)

ser = make_server('', 8080, api)
ser.serve_forever()
