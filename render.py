from jinja2 import Environment, FileSystemLoader
import os
import json

def render(template_name, folder='templates', **kwargs):
    # Set up environment
    env = Environment(loader=FileSystemLoader(folder))
    # Load template
    template = env.get_template(template_name)
    # Render template with data
    return template.render(**kwargs)

def save(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def main():
    # Get template
    template = 'user-data.jinja'
    # Get context from environment
    context = json.loads(os.environ['JINJA_CONFIG'])
    # Render template with context
    content = render(template, env=os.environ, **context)
    save('user-data', content)

if __name__ == '__main__':
    if os.environ["JINJA_CONFIG"] == "":
        os.environ["JINJA_CONFIG"] = """{
            "username": "ubuntu",
            "hostname": "ubuntu-server",
            "hashed_password": "$6$exDY1mhS4KUYCE/2$zmn9ToZwTKLhCw.b4/b.ZRTIZM30JZ4QrOQ2aOXJ8yk96xpcCof0kxKwuX1kqLG/ygbJ1f8wxED22bTL4F46P0"
        }
        """
    main()