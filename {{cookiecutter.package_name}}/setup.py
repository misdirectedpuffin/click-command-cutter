from setuptools import setup, find_packages

try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements


def get_requirements(file):
    """Return a list of requirements from a file."""
    requirements = parse_requirements(file, session=False)
    return [str(ir.req) for ir in requirements if not None]


setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    url="https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.package_name }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.package_description }}",
    long_description=open('README.rst').read(),
    packages=find_packages(),
    entry_points={
        '{{ cookiecutter.cli_entry_point }}.plugins': [
            '{{ cookiecutter.cli_sub_command }}={{ cookiecutter.package_name }}.command:{{ cookiecutter.cli_sub_command }}',
        ],
    },
    install_requires=get_requirements('requirements.txt'),
    tests_require=get_requirements('requirements_dev.txt'),
    setup_requires=['pytest-runner'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    zip_safe=False,
    keywords='{{ cookiecutter.package_name }}'
)
