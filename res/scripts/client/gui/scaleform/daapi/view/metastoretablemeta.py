# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StoreTableMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StoreTableMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def refreshStoreTableDataProvider(self):
        """
        :return :
        """
        self._printOverrideError('refreshStoreTableDataProvider')

    def as_getTableDataProviderS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getTableDataProvider()

    def as_setTableTypeS(self, type):
        """
        :param type:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTableType(type)

    def as_scrollToFirstS(self, level, disabled, currency):
        """
        :param level:
        :param disabled:
        :param currency:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToFirst(level, disabled, currency)

    def as_setGoldS(self, gold):
        """
        :param gold:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setGold(gold)

    def as_setCreditsS(self, credits):
        """
        :param credits:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCredits(credits)