#!/usr/bin/env python

# region Imports
from enum import Enum
from util.generator import Generator
import argparse
import logging
import os
import json
# endregion

# region Variables
__args = None
# endregion


# region Helper Functions
def _get_template():
    logging.debug('BigG :: _get_template')


def _get_project():
    logging.debug('BigG :: _get_project')


def _read_project():
    logging.debug('BigG :: _read_project')


def _build_project():
    logging.debug('BigG :: _build_project')
# endregion


# region main()
def main(args=None):
    global _args
    _args = args
    #print(_args) # TODO : DELTEME

    # configure the logger
    logging.basicConfig(filename=_args.log_file,
                        level=_args.log_level.value)
    logging.debug('BigG :: Start')
    logging.debug('BigG :: PWD : ' +
        os.getcwd())
    logging.debug('BigG :: SCRIPT_LOCATION : ' +
        os.path.dirname(os.path.abspath(__file__)))
    generator = Generator(project_file=_args.big_g_project_file)
    generator.generate()
    logging.debug('BigG :: End')
# endregion


# region Classes
class LogLevel(Enum):
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET
# endregion

if __name__ == "__main__":
    description = u'''
    This is an attempt to build a code generator using Python's MAKO framework.
The hope is to end up with a platform agnostic code generator to preform basic CRUD operations over varying REST
APIs.
    '''

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--big_g_project_file',
                        help='This is used to tell BigG to generate a given project.' +
                        '  See help docs on BIG_G_PROJECT_FILES for more information')

    parser.add_argument('--log_file',
                        default='./logs/BigG.log',
                        help='Name of the log file you would like BigG to redirect output to.' +
                        '  By default BigB will output to "BigG.Log" in its current directories log folder.')

    parser.add_argument('--log_level',
                        default=LogLevel.ERROR.name,
                        choices=[LogLevel.ERROR.name,
                                 LogLevel.WARNING.name,
                                 LogLevel.CRITICAL.name,
                                 LogLevel.INFO.name,
                                 LogLevel.DEBUG.name,
                                 LogLevel.NOTSET.name],
                        help='The level of logging that BigG will produce while it runs.' +
                        '  By default BigB will only log at level ERROR.')

    parser.add_argument('--replace',
                        type=bool,
                        default=True,
                        help='Force BigG to only overwrite existing files that do not match.' +
                        '  By default, this is set to "True".')

    parser.add_argument('--force',
                        type=bool,
                        default=False,
                        help='Force BigG to overwrite existing files even if they completely match')

    args = parser.parse_args()
    args.log_level = LogLevel[args.log_level]

    main(args=args)

# EOF
