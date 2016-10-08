# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/SearchContactViewMeta.py
from messenger.gui.Scaleform.view.lobby.BaseContactView import BaseContactView

class SearchContactViewMeta(BaseContactView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseContactView
    """

    def search(self, data):
        self._printOverrideError('search')

    def as_getSearchDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()

    def as_setSearchResultTextS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchResultText(message)

    def as_setSearchDisabledS(self, coolDown):
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchDisabled(coolDown)