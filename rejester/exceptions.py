'''Exceptions raised in various places in rejester.

.. This software is released under an MIT/X11 open source license.
   Copyright 2012-2014 Diffeo, Inc.
'''

class RejesterException(Exception):
    'base exception for rejester package'
    pass

class EnvironmentError(RejesterException):
    '''indicates that the registry lost a lock or experienced a similar
failure that probably indicates a network or remote server failure'''
    pass

class LockError(RejesterException):
    'attempt to get a lock exceeded acquire time (atime)'
    pass

class NoSuchWorkSpecError(RejesterException):
    """A `TaskMaster` function was called with a nonexistent work spec"""
    def __init__(self, work_spec_name, *args, **kwargs):
        super(NoSuchWorkSpecError, self).__init__(*args, **kwargs)
        #: Name of the nonexistent work spec
        self.work_spec_name = work_spec_name
    pass

class NoSuchWorkUnitError(RejesterException):
    '''Valid work spec but invalid work unit.

    This occurs when a :class:`rejester.TaskMaster` function that
    manipulates existing work units is called with a valid work spec name
    but an invalid work unit name.

    '''
    def __init__(self, work_unit_name, *args, **kwargs):
        super(NoSuchWorkUnitError, self).__init__(*args, **kwargs)
        #: Name of the nonexistent work unit
        self.work_unit_name = work_unit_name
    pass

class ProgrammerError(RejesterException):
    pass

class PriorityRangeEmpty(RejesterException):
    '''
    given the priority_min/max, no item is available to be returned
    '''
    pass

class LostLease(RejesterException):
    '''worker waited too long between calls to update and another worker
got the WorkItem'''
    pass

class ItemInUseError(RejesterException):
    '''tried to add an item to a queue that was already in use'''
    pass
