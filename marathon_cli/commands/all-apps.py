import click

from marathon_cli.output import format_json
from marathon_cli.settings import LOGGER
from marathon_cli.x import get


@click.command()
def cli():
    """Get all containers deployed to a marathon instance.
    """
    LOGGER.debug('Get all containers deployed to a marathon instance.')
    apps = get('apps').json()
    click.echo(format_json({'app-ids': apps, 'count': len(apps)}))


if __name__ == '__main__':
    cli()
