"""Exercise 50. Simple project with lpthw.web."""
import web

urls = (
    '/', 'Index',
    '/foo', 'Foo'
)
app = web.application(urls, globals())
render = web.template.render('templates/')


class Index:
    def GET(self):
        greeting = "Hello World!"
        return render.index(greeting=greeting)


class Foo:
    def GET(self):
        message = "foo2"
        return render.foo(message)


if __name__ == "__main__":
    app.run()
