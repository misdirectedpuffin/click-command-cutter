"""Console script for {{cookiecutter.package_name}}."""
import sys
import click


from pkg_resources import iter_entry_points

from click_plugins import with_plugins


@with_plugins(iter_entry_points('{{ cookiecutter.package_name }}.plugins'))
@click.group()
def entrypoint():
    """Entrypoint to your CLI."""


if __name__ == "__main__":
    sys.exit(entrypoint())  # pragma: no cover