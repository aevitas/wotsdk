# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SkillDropMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SkillDropMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def calcDropSkillsParams(self, tmanCompDescr, xpReuseFraction):
        """
        :param tmanCompDescr:
        :param xpReuseFraction:
        :return Array:
        """
        self._printOverrideError('calcDropSkillsParams')

    def dropSkills(self, dropSkillCostIdx):
        """
        :param dropSkillCostIdx:
        :return :
        """
        self._printOverrideError('dropSkills')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setGoldS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setGold(value)

    def as_setCreditsS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCredits(value)