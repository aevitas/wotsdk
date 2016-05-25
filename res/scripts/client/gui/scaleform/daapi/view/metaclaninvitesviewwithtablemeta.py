# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanInvitesViewWithTableMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanInvitesViewWithTableMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def showMore(self):
        """
        :return :
        """
        self._printOverrideError('showMore')

    def refreshTable(self):
        """
        :return :
        """
        self._printOverrideError('refreshTable')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_getTableDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getTableDP()

    def as_updateDefaultSortFieldS(self, defaultSortField, defaultSortDirection):
        """
        :param defaultSortField:
        :param defaultSortDirection:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateDefaultSortField(defaultSortField, defaultSortDirection)

    def as_showDummyS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showDummy(data)

    def as_hideDummyS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideDummy()

    def as_updateButtonRefreshStateS(self, enabled, tooltip):
        """
        :param enabled:
        :param tooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateButtonRefreshState(enabled, tooltip)