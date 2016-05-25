# Embedded file name: scripts/common/VersionUpdater.py
import sys
from debug_utils import LOG_DEBUG

class VersionUpdaterBase(object):
    """Base class for different types of version updaters. Suggested descendant implementation:
    
        @singleton
        class SomeVersionUpdater(VersionUpdaterBase):
            def __init__(self):
                super(self.__class__, self).__init__(UPDATE_FUNCTION_TEMPLATE, LATEST_VERSION)
    
            def updateVersion(self, logID, owner, data):
                self._updateToLatestVersion(lambda _, data: data['ver'], logID, owner, data)
    
    Usage:
        SomeVersionUpdater.updateVersion('Some, id:%d' % (owner.id,), owner, owner.data)
    """

    def __init__(self, template, latestVersion, moduleWithUpdaters = None):
        self._startVersion = None
        self._updaters = None
        self._template = template
        self._latestVersion = latestVersion
        self._module = moduleWithUpdaters
        if moduleWithUpdaters is None:
            self._module = sys.modules[self.__module__]
        return

    latestVersion = property(lambda self: self._latestVersion)

    def __buildUpdaters(self):
        """Builds and caches list of updater functions."""
        raise self._updaters is None or AssertionError('Build once is enough')
        self._updaters = []
        for fromVer in xrange(self._latestVersion):
            args = (fromVer,) if self._template.count('%d') == 1 else (fromVer, fromVer + 1)
            funcName = self._template % args
            func = getattr(self._module, funcName, None)
            if func is not None:
                self._updaters.append(func)
                if self._startVersion is None:
                    self._startVersion = fromVer
            else:
                raise self._startVersion is None or AssertionError('Sequence of updaters should be continuous, absentFunc=%s, ' % (funcName,))

        raise self._startVersion is not None or AssertionError
        raise len(self._updaters) == self._latestVersion - self._startVersion or AssertionError
        LOG_DEBUG('__buildUpdaters', self.__class__, self._startVersion, self._latestVersion)
        return

    def __getUpdaters(self, startVersion):
        """Returns list of updaters from startVersion to self._latestVersion."""
        if startVersion == self._latestVersion:
            return []
        else:
            if self._updaters is None:
                self.__buildUpdaters()
            raise startVersion >= self._startVersion or AssertionError('%s >= %s' % (startVersion, self._startVersion))
            raise startVersion <= self._latestVersion or AssertionError('%s <= %s' % (startVersion, self._latestVersion))
            return enumerate(self._updaters[startVersion - self._startVersion:], start=startVersion)

    def _updateToLatestVersion(self, versionOrGetter, logID, *args):
        """Updates data to latest version by applying updaters [currentVersion..latestVersion).
        logID is a data owner identity, f.e. account.logID.
        versionOrGetter is current data version or function to get current data version from args.
        args is an argument list to be passed to every updater function. Also used by versionOrGetter.
        Returns updated args.
        Update algorithm depends on callable(versionOrGetter), True or False:
            for ver, updater: updater(args)
        or
            for ver, updater: ver, args = updater(args)
        """
        isCallable = callable(versionOrGetter)
        currentVersion = versionOrGetter(*args) if isCallable else versionOrGetter
        for fromVer, updater in self.__getUpdaters(currentVersion):
            LOG_DEBUG('_updateToLatestVersion', logID, fromVer)
            result = updater(*args)
            if isCallable:
                resultVer = versionOrGetter(*args)
            else:
                resultVer, args = result[0], result[1:]
            raise resultVer == fromVer + 1 or resultVer == self._latestVersion or AssertionError('resultVer=%s, ver=%s, updater=%s' % (resultVer, fromVer, updater.__name__))
            if resultVer == self._latestVersion:
                break

        return args