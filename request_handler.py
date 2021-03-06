from entries.request import create_entry
from http.server import BaseHTTPRequestHandler, HTTPServer
from entries import get_single_entry, get_all_entries, delete_entry, search_entries, create_entry, update_entry
import json
from tags import get_tags
from moods import get_moods


class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1] #resource = entries

        if "?" in resource:
            param = resource.split("?")[1]  # param
            resource = resource.split("?")[0] # resource = search
            pair = param.split("=")  
            key = pair[0] 
            value = pair[1] 

            return ( resource, key, value )
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass 
            except ValueError:
                pass  
            return (resource, id)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()
    
    def do_GET(self):
        self._set_headers(200)
        response = {}
        parsed = self.parse_url(self.path)
        if len(parsed) == 2:
            ( resource, id ) = parsed
            if resource == "entries":
                if id is not None:
                    response = f"{get_single_entry(id)}"
                else:
                    response = f"{get_all_entries()}"

            if resource == "tags":
                response = f"{get_tags()}"
            if resource == "moods":
                response = f"{get_moods()}"
        elif len(parsed) == 3:
            ( resource, key, value ) = parsed
            if key == "search" and resource == "entries":
                response = f"{search_entries(value)}"

        self.wfile.write(response.encode())

    def do_DELETE(self):
        """ handles our DELETE method
        """
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)
        if resource == "entries":
            delete_entry(id)
        self.wfile.write("".encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, _) = self.parse_url(self.path)

        new_entry = None

        if resource == "entries":
            new_entry = create_entry(post_body)
            self.wfile.write(f"{new_entry}".encode())

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        success = False

        if resource == "entries":
            success = update_entry(id, post_body)
        
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()