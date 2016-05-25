# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StaticFormationLadderViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StaticFormationLadderViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def showFormationProfile(self, fromationId):
        """
        :param fromationId:
        :return :
        """
        self._printOverrideError('showFormationProfile')

    def updateClubIcons(self, ids):
        """
        :param ids:
        :return :
        """
        self._printOverrideError('updateClubIcons')

    def as_updateHeaderDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateHeaderData(data)

    def as_updateLadderDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateLadderData(data)

    def as_setLadderStateS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setLadderState(data)

    def as_onUpdateClubIconsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onUpdateClubIcons(data)

    def as_onUpdateClubIconS(self, clubId, iconPath):
        """
        :param clubId:
        :param iconPath:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onUpdateClubIcon(clubId, iconPath)