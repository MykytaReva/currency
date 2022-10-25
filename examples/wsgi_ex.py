def hello():
    return "hello"

def world():
    return "world"

urls = {
    "/world/": world,
    "/hello/": hello
}



def app(environ, start_response):
    data = b"hello,World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
