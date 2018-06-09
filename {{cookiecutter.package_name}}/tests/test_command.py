"""Tests related to the cli entrypont."""

from click.testing import CliRunner
from {{ cookiecutter.package_name }}.command import {{ cookiecutter.cli_sub_command }}


def test_cli_output():
    """It returns the CLI description."""
    runner = CliRunner()
    result = runner.invoke({{ cookiecutter.cli_sub_command }})
    assert 'Subcommand to attach to {{ cookiecutter.cli_entry_point }}.'