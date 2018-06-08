"""Tests related to the cli entrypont."""

from click.testing import CliRunner
from {{ cookiecutter.package_name }}.cli import entrypont


def test_cli_output():
    """It returns the CLI description."""
    runner = CliRunner()
    result = runner.invoke(entrypont)
    assert 'Entrypoint to your CLI.'
