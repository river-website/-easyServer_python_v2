from reactor.epollReactor import *
from reactor.selectReactor import *
import selectors


def getReactor():
    if hasattr(selectors, 'EPollSelector'):
        return epollReactor()
    elif hasattr(selectors, 'PollSelector'):
        _ServerSelector = selectors.PollSelector
    else:
        return selectReactor()