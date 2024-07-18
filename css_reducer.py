import re

def process_css(file_path):
    with open(file_path, 'r') as file:
        css_content = file.read()

    comments = re.findall(r'/\*.*?\*/', css_content, flags=re.DOTALL)
    css_content_no_comments = re.sub(r'/\*.*?\*/', '/*COMMENT_PLACEHOLDER*/', css_content, flags=re.DOTALL)

    rules = re.findall(r'([^{]+){([^}]+)}', css_content_no_comments)

    processed_rules = []
    for selector, properties in rules:
        selector = selector.strip()
        properties_list = [prop.strip() for prop in properties.split(';') if prop.strip()]
        properties = '; '.join(properties_list) + ';'
        processed_rule = f"{selector} {{{properties}}}"
        processed_rules.append(processed_rule)
    
    processed_css = '\n'.join(processed_rules)

    for comment in comments:
        processed_css = processed_css.replace('/*COMMENT_PLACEHOLDER*/', f'\n\n{comment}\n\n', 1)
    
    processed_css = re.sub(r'\n{3,}', '\n\n', processed_css)

    return processed_css

def save_processed_css(processed_css, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(processed_css)

if __name__ == "__main__":
    # Modify the paths to the input and output files
    input_file_path = '../../../../Desktop/example.css'
    output_file_path = '../../../../Desktop/example_compiled.css'
    
    processed_css = process_css(input_file_path)
    save_processed_css(processed_css, output_file_path)

    print(f"Archivo procesado guardado en {output_file_path}")


    