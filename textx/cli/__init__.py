import click
import pkg_resources


@click.group()
@click.option('--debug', default=False, is_flag=True,
              help="Debug/trace output.")
@click.pass_context
def textx(ctx, debug):
    ctx.obj = {'debug': debug}


def register_textx_subcommands():
    """
    Find and use all textx sub-commands registered through the extension point.

    Entry point used for commands registration is `textx_commands`.
    In this entry point you should register a callable that accepts the top
    level click `textx` command and register additional commands(s) on it.
    """
    global textx
    for subcommand in pkg_resources.iter_entry_points(group='textx_commands'):
        subcommand.load()(textx)


# Register sub-commands specified through extension points.
register_textx_subcommands()
