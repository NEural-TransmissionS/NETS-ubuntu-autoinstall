from jinja2 import Environment, FileSystemLoader
import json
import os


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
    # Get context from config.json
    if os.path.exists('config.json'):
        with open('config.json') as f:
            context = json.loads(f.read())
    else:
        context = {
            "username": "ubuntu",
            "hashed_password": "$6$exDY1mhS4KUYCE/2$zmn9ToZwTKLhCw.b4/b.ZRTIZM30JZ4QrOQ2aOXJ8yk96xpcCof0kxKwuX1kqLG/ygbJ1f8wxED22bTL4F46P0",
            "hostname": "ubuntu-server",
        }
    # Render template with context
    content = render(template, **context)
    save('user-data', content)


if __name__ == '__main__':
    main()