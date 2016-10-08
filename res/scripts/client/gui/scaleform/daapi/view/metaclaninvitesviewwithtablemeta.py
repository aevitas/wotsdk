# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanInvitesViewWithTableMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanInvitesViewWithTableMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def showMore(self):
        self._printOverrideError('showMore')

    def refreshTable(self):
        self._printOverrideError('refreshTable')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_getTableDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getTableDP()

    def as_updateDefaultSortFieldS(self, defaultSortField, defaultSortDirection):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDefaultSortField(defaultSortField, defaultSortDirection)

    def as_showDummyS(self, data):
        """
        :param data: Represented by DummyVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showDummy(data)

    def as_hideDummyS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideDummy()

    def as_updateButtonRefreshStateS(self, enabled, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_updateButtonRefreshState(enabled, tooltip)