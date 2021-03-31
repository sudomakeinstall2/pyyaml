import sys
import os
#sys.path.append(os.getcwd() + '/..')
import yaml
from yaml import Loader
from yaml.reader import ReaderError
from yaml.scanner import ScannerError
from yaml.parser import ParserError
from yaml.constructor import ConstructorError
from yaml.composer import ComposerError
from pythonfuzz.main import PythonFuzz



@PythonFuzz
def fuzz(buf):
    try:
        str = buf.decode('utf-8')
        data = yaml.load(str, Loader=Loader)
    except (UnicodeError, ReaderError, ScannerError, ParserError, ConstructorError, ComposerError):
        pass


if __name__ == '__main__':
    fuzz()
