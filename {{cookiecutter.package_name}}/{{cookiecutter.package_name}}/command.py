"""Subcommands to attach to CLI in setup.py"""
import click

@click.group()
@click.pass_context
def {{ cookiecutter.cli_sub_command }}(ctx):
    """Subcommand to attach to {{ cookiecutter.cli_entry_point }}."""


@{{ cookiecutter.cli_sub_command }}.command('configure')
@click.pass_context
def configure(ctx):
    """The configure subcommand."""


{{ cookiecutter.cli_sub_command }}.add_command(configure)