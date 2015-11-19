"""
Controller class for running commands (list, get, create, update)
on facility records.
"""

# from mytardisclient.logs import logger
from mytardisclient.models.facility import Facility
from mytardisclient.models.instrument import Instrument
from mytardisclient.views import render


class FacilityController(object):
    """
    Controller class for running commands (list, get, put, patch)
    on facility records.
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
            return self.list(args.limit, render_format)
        if command == "get":
            return self.get(args.facility_id, render_format)

    def list(self, limit, render_format):
        """
        Display list of facility records.
        """
        facilities = Facility.list(self.config, limit=limit)
        print render(facilities, render_format)

    def get(self, facility_id, render_format):
        """
        Display facility record.
        """
        facility = Facility.get(self.config, facility_id)
        print render(facility, render_format)
        if render_format == 'table':
            instruments = Instrument.list(self.config, facility_id)
            print render(instruments, render_format)
