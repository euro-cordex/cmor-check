import click

from .cmor_check import check_file


@click.command()
@click.option("--cv", help="path to CV table")
@click.argument("filename")
def check(filename, cv):
    check_file(filename, cv)
