#!/usr/bin/env python3

from team_info import *
from team_abbreviation import get_abbreviations
import pprint

import click

@click.command()
@click.option(
    '--team',
    type=click.Choice(get_abbreviations(), case_sensitive=False),
    help='input team abbreviation (not case sensitive), ie. SJS for San Jose Sharks'
)
def main(team):
    """
    A simple CLI tool that grabs relevant stats and data from the official NHL's
    REST API
    """
    info = get_team_roster(team)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(info)

if __name__ == '__main__':
    main()