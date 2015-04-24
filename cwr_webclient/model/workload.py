# -*- encoding: utf-8 -*-

from enum import Enum

"""
Offers services for CWR files.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class WorkloadStatus(Enum):
    waiting = 1
    processing = 2
    done = 3


class WorkloadInfo(object):
    def __init__(self, file, status):
        self._file = file
        self._status = status

    @property
    def file(self):
        return self._file

    @property
    def status(self):
        return self._status
