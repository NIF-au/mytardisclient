"""
Controller class for running commands (list, get, create, update)
on instrument records.
"""

# from mytardisclient.logs import logger
from mytardisclient.models.instrument import Instrument
from mytardisclient.views import render


class InstrumentController(object):
    """
    Controller class for running commands (list, get, put, patch)
    on instrument records.
    """
    def __init__(self, config):
        self.config = config

    def run_command(self, args):
        """
        Generic run command method.
        """
        command = args.command
        if hasattr(args, 'json') and args.json:
            render_format = 'json'
        else:
            render_format = 'table'
        if command == "list":
            return self.list(args.facility, args.limit, render_format)
        elif command == "get":
            return self.get(args.instrument_id, render_format)
        elif command == "create":
            return self.create(args.facility_id, args.name, render_format)

    def list(self, facility_id, limit, render_format):
        """
        Display list of instrument records.
        """
        instruments = Instrument.list(self.config, facility_id=facility_id,
                                      limit=limit)
        print render(instruments, render_format)

    def get(self, instrument_id, render_format):
        """
        Display instrument record.
        """
        instrument = Instrument.get(self.config, instrument_id)
        print render(instrument, render_format)

    def create(self, facility_id, name, render_format):
        """
        Create instrument record.
        """
        instrument = Instrument.create(self.config, facility_id, name)
        print render(instrument, render_format)
        print "Instrument created successfully."