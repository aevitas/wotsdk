# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TechTreeMeta.py
from gui.Scaleform.daapi.view.lobby.techtree.ResearchView import ResearchView

class TechTreeMeta(ResearchView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ResearchView
    null
    """

    def requestNationTreeData(self):
        """
        :return :
        """
        self._printOverrideError('requestNationTreeData')

    def getNationTreeData(self, nationName):
        """
        :param nationName:
        :return Object:
        """
        self._printOverrideError('getNationTreeData')

    def goToNextVehicle(self, vehCD):
        """
        :param vehCD:
        :return :
        """
        self._printOverrideError('goToNextVehicle')

    def onCloseTechTree(self):
        """
        :return :
        """
        self._printOverrideError('onCloseTechTree')

    def as_setAvailableNationsS(self, nations):
        """
        :param nations:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAvailableNations(nations)

    def as_setSelectedNationS(self, nationName):
        """
        :param nationName:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedNation(nationName)

    def as_refreshNationTreeDataS(self, nationName):
        """
        :param nationName:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_refreshNationTreeData(nationName)

    def as_setUnlockPropsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setUnlockProps(data)

    def as_showMiniClientInfoS(self, description, hyperlink):
        """
        :param description:
        :param hyperlink:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)