import configparser

from caller.config.parser import parse_literal, parse_string, parse_list, parse_benchmarks, parse_bool


class ConfigMicro(object):
    def __init__(self):
        """
            Sets the default values for the micro benchmarks
        """
        # run
        self.values = 5
        self.processes = 20
        self.bm_cooldown = 10
        self.speed = [100]
        self.clear_db = True

        # app
        self.url = "127.0.0.1"
        self.port = "5000"
        self.protocol = "http"
        self.webserver = "gunicorn"
        self.output = "file"

        # fmd
        self.levels = [-1, 0, 1, 2, 3]
        self.db_url = 'sqlite:///micro_fmd.db'

        # benchmarks
        self.benchmarks = [('pidigits', 'Compute digits of pi.')]

    def init_from(self, file=None):
        config_parser = configparser.RawConfigParser()
        config_parser.read(file)

        # parse run
        self.values = parse_literal(config_parser, 'run', 'values', self.values)
        self.processes = parse_literal(config_parser, 'run', 'processes', self.processes)
        self.bm_cooldown = parse_literal(config_parser, 'run', 'bm_cooldown', self.bm_cooldown)
        self.speed = parse_list(config_parser, 'run', 'speed', self.speed)
        self.clear_db = parse_bool(config_parser, 'run', 'clear_db', self.clear_db)

        # parse app
        self.url = parse_string(config_parser, 'app', 'url', self.url)
        self.port = parse_string(config_parser, 'app', 'port', self.port)
        self.protocol = parse_string(config_parser, 'app', 'protocol', self.protocol)
        self.webserver = parse_string(config_parser, 'app', 'webserver', self.webserver)
        self.output = parse_string(config_parser, 'app', 'output', self.output)

        # parse fmd
        self.levels = parse_list(config_parser, 'fmd', 'levels', self.levels)
        self.db_url = parse_string(config_parser, 'fmd', 'db_url', self.db_url)

        # parse benchmarks
        self.benchmarks = parse_benchmarks(config_parser, 'benchmarks', self.benchmarks)


class ConfigMacro(object):
    def __init__(self):
        """
            Sets the default values for the macro benchmark
        """
        # run
        self.values = 5
        self.processes = 5
        self.bm_cooldown = 10
        self.users = [1, 2, 5, 10]

        # app
        self.app_db = 'sqlite:///macro.db'
        self.url = "127.0.0.1"
        self.port = "5000"
        self.protocol = "http"
        self.webserver = "gunicorn"

        # fmd
        self.levels = [-1, 0, 1, 2, 3]
        self.fmd_db = 'sqlite:///macro_fmd.db'

    def init_from(self, file=None):
        config_parser = configparser.RawConfigParser()
        config_parser.read(file)

        # parse run
        self.values = parse_literal(config_parser, 'run', 'values', self.values)
        self.processes = parse_literal(config_parser, 'run', 'processes', self.processes)
        self.bm_cooldown = parse_literal(config_parser, 'run', 'bm_cooldown', self.bm_cooldown)
        self.users = parse_list(config_parser, 'run', 'users', self.users)

        # parse app
        self.app_db = parse_string(config_parser, 'app', 'app_db', self.app_db)
        self.url = parse_string(config_parser, 'app', 'url', self.url)
        self.port = parse_string(config_parser, 'app', 'port', self.port)
        self.protocol = parse_string(config_parser, 'app', 'protocol', self.protocol)
        self.webserver = parse_string(config_parser, 'app', 'webserver', self.webserver)

        # parse fmd
        self.levels = parse_list(config_parser, 'fmd', 'levels', self.levels)
        self.fmd_db = parse_string(config_parser, 'fmd', 'fmd_db', self.fmd_db)
