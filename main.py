import argparse

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import (
    TemplateNotFound,
    TemplateError,
    TemplateRuntimeError,
    TemplateSyntaxError
)

parser = argparse.ArgumentParser(description='Dockerfile & compose.yaml generator')

parser.add_argument('--python-version', '-v', default='3.10', help='Python Version')
parser.add_argument('--platform', '-p', default='linux/arm64/v8', choices=['linux/amd64', 'linux/arm64/v8'], help='OS platform')

args = parser.parse_args()


def main():
    template_meta = {
        'Dockerfile': {
            'python_version': args.python_version
        },
        'compose.yaml': {
            'python_version': args.python_version,
            'platform':  args.platform
        }
    }

    for k, v in template_meta.items():
        file_content = load_template(
            template=k,
            data=v
        )

        if not file_content:
            print(f'Could not generate file from template: {k}')

        with open(k, 'w') as f:
            f.writelines(file_content)


def load_template(template: str, data: dict[str, str]) -> str:
    '''Function to load jinja2 template file

    Args:
        template (str): template name
        data (dict): variables to populate template

    Returns:
        str: file content
    '''

    try:
        env = Environment(loader=FileSystemLoader('templates/'))
        t = env.get_template(template)
        content = t.render(data=data)
    except (
        TemplateNotFound,
        TemplateError,
        TemplateRuntimeError,
        TemplateSyntaxError,
        Exception
    ) as e:
        print(e)
    else:
        return content


if __name__ == '__main__':
    main()
