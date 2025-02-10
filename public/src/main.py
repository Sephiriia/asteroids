import os
import shutil
import http.server

from copystatic import copy_files_recursive
from gencontent import generate_page
from gencontent import generate_pages_recursive  # Add this import

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)      

    print("Generating pages...")
    # Replace the single generate_page with generate_pages_recursive
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

    # Add this to serve the files
    print("Starting server...")
    os.chdir(dir_path_public)
    http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8888)


main()