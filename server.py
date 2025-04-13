from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='.', **kwargs)
    
    def guess_type(self, path):
        # Override MIME type guessing for common image types
        ext = os.path.splitext(path)[1]
        if ext.lower() in ('.jpg', '.jpeg'):
            return 'image/jpeg'
        elif ext.lower() == '.png':
            return 'image/png'
        return super().guess_type(path)

with HTTPServer(('localhost', PORT), Handler) as httpd:
    print(f'Serving on http://localhost:{PORT}')
    httpd.serve_forever()
