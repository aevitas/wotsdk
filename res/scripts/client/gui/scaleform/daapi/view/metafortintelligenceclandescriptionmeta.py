# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortIntelligenceClanDescriptionMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortIntelligenceClanDescriptionMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onOpenCalendar(self):
        """
        :return :
        """
        self._printOverrideError('onOpenCalendar')

    def onOpenClanList(self):
        """
        :return :
        """
        self._printOverrideError('onOpenClanList')

    def onOpenClanStatistics(self):
        """
        :return :
        """
        self._printOverrideError('onOpenClanStatistics')

    def onOpenClanCard(self):
        """
        :return :
        """
        self._printOverrideError('onOpenClanCard')

    def onAddRemoveFavorite(self, isAdd):
        """
        :param isAdd:
        :return :
        """
        self._printOverrideError('onAddRemoveFavorite')

    def onAttackDirection(self, uid):
        """
        :param uid:
        :return :
        """
        self._printOverrideError('onAttackDirection')

    def onHoverDirection(self):
        """
        :return :
        """
        self._printOverrideError('onHoverDirection')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_updateBookMarkS(self, isAdd):
        """
        :param isAdd:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateBookMark(isAdd)