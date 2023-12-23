#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""monitor module for kumaone"""

# Import builtin python libraries
from pathlib import Path
from typing import Optional

# Import external python libraries
from rich.console import Console
from typing_extensions import Annotated
import typer

# Import custom (local) python packages
from .config import check_config
from .connection import connect_login, disconnect
from .monitors import list_monitors
from src.kumaone.core.utils import log_manager

# Source code meta data
__author__ = "Dalwar Hossain"
__email__ = "dalwar23@pm.me"

# Create typer app and turn off debug mode by default
app = typer.Typer()
state = {"log_level": "NOTSET"}
console = Console()


@app.command(name="add", help="Add one or more monitor(s).")
def monitor_add(
    monitor_data: Annotated[Optional[Path], typer.Option(..., "--file", "-f", help="Monitor data file path.")],
    config_file: Annotated[
        Optional[Path], typer.Option(..., "--config", "-c", help="Uptime kuma configuration file path.")
    ] = Path.home().joinpath(".config/kumaone/kuma.yaml"),
    log_level: Annotated[str, typer.Option(help="Set log level.")] = "NOTSET",
):
    """
    Adds uptime kuma monitor(s)

    :return: None
    """

    if log_level != "NOTSET":
        state["log_level"] = log_level
        logger = log_manager(log_level=log_level)
    else:
        logger = None
    pass


@app.command(name="list", help="List all monitor groups and processes.")
def monitor_list(
    config_file: Annotated[
        Optional[Path], typer.Option(..., "--config", "-c", help="Uptime kuma configuration file path.")
    ] = Path.home().joinpath(".config/kumaone/kuma.yaml"),
    log_level: Annotated[str, typer.Option(help="Set log level.")] = "NOTSET",
):
    """
    Lists all monitor groups and processes

    :return: None
    """

    if log_level != "NOTSET":
        state["log_level"] = log_level
        logger = log_manager(log_level=log_level)
    else:
        logger = None

    config_data = check_config(config_path=config_file, logger=logger)
    connect_login(config_data=config_data)
    list_monitors()
    disconnect()


@app.callback()
def monitor_mission_control(log_level: Annotated[str, typer.Option(help="Set log level.")] = "NOTSET"):
    """
    Mission control for kumaone monitor, an uptime kuma helper python package.
    """

    if log_level:
        state["log_level"] = log_level


if __name__ == "__main__":
    app()