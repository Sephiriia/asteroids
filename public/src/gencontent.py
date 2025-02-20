import os
from markdown_blocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")


# Add this to your existing gencontent.py
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)
    
    for entry in entries:
        current_path = os.path.join(dir_path_content, entry)
        
        if os.path.isfile(current_path):
            if current_path.endswith('.md'):
                relative_path = os.path.relpath(current_path, dir_path_content)
                html_path = os.path.splitext(relative_path)[0] + '.html'
                output_path = os.path.join(dest_dir_path, html_path)
                
                # Make sure output directory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # Generate the page
                generate_page(current_path, template_path, output_path)
        else:
            # It's a directory - recursively process it
            new_content_path = current_path
            new_dest_path = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(new_content_path, template_path, new_dest_path)