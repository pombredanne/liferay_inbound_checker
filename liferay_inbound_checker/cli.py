# SPDX-FileCopyrightText: © 2020 Liferay, Inc. <https://liferay.com>
#
# SPDX-License-Identifier: LGPL-2.1-or-later

"""Console script for liferay_inbound_checker."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for liferay_inbound_checker."""
    click.echo("Replace this message by putting your code into "
               "liferay_inbound_checker.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
