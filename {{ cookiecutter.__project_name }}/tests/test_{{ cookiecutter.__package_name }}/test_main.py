from {{ cookiecutter.__package_name }}.main import get_hello

def it_prints_hi_to_the_project_author():
    expected = 'Hello, {{ cookiecutter.author_name }}!'
    actual = get_hello('{{ cookiecutter.author_name }}')
    assert actual == expected