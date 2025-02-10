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