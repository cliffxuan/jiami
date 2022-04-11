import click
from cli.encryption import password_decrypt, password_encrypt


@click.group()
def cli():
    pass


@cli.command()
@click.option("--text", "-t", prompt="Type in your text", help="The text to encrypt")
@click.option(
    "--password", "-p", prompt=True, hide_input=True, confirmation_prompt=True
)
def encrypt(text, password):
    cypher = password_encrypt(text.encode("utf-8"), password)
    click.secho(cypher, fg="green")


@cli.command()
@click.option(
    "--cypher", "-c", prompt="Type in your encrypted text", help="The encrypted text"
)
@click.option(
    "--password", "-p", prompt=True, hide_input=True, confirmation_prompt=True
)
def decrypt(cypher, password):
    cypher = password_decrypt(cypher.encode("utf-8"), password)
    click.secho(cypher, fg="green")
