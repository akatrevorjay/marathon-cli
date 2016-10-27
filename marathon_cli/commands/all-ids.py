import click
import jmespath

from marathon_cli.output import format_json
from marathon_cli.settings import LOGGER
from marathon_cli.x import get


@click.command()
def cli():
    """Get the ids of all containers deployed to a marathon instance.
    """
    LOGGER.debug('Get the ids of all containers deployed to a marathon instance.')
    apps = get('apps').json()
    apps = jmespath.search('apps[*].id', apps)
    click.echo(format_json({'app-ids': apps, 'count': len(apps)}))


if __name__ == '__main__':
    cli()
