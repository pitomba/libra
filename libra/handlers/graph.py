from tornado.web import RequestHandler


class GraphHandler(RequestHandler):

    def get(self, **kwargs):
        self.render("graph.html")
