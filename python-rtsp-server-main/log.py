import time
from concurrent.futures import ThreadPoolExecutor
from subprocess import Popen
from _config import Config


class Log:
    @staticmethod
    def print(info):
        if Config.debug:
            if not info.endswith('\n'):
                info += '\n'
            print(info)

    @staticmethod
    def write(info, host=None):
        print(f'*** {info} ***\n\n')
        if host == '127.0.0.1':
            return

        # We haven't strict necessary to use system command here, but it's the easiest way
        info = info.replace('"', '\\"')
        text = f'{time.strftime("%Y-%m-%d %H:%M:%S")} {info}'
        cmd = f'echo "{text}" >> {Config.log_file}'

        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(Popen, cmd, shell=True)
