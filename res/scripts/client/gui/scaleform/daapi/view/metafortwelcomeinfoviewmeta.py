# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortWelcomeInfoViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortWelcomeInfoViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onCreateBtnClick(self):
        """
        :return :
        """
        self._printOverrideError('onCreateBtnClick')

    def onNavigate(self, code):
        """
        :param code:
        :return :
        """
        self._printOverrideError('onNavigate')

    def openClanResearch(self):
        """
        :return :
        """
        self._printOverrideError('openClanResearch')

    def as_setWarningTextS(self, text, disabledBtnTooltip):
        """
        :param text:
        :param disabledBtnTooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWarningText(text, disabledBtnTooltip)

    def as_setCommonDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCommonData(data)

    def as_setRequirementTextS(self, text):
        """
        :param text:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRequirementText(text)

    def as_showMiniClientInfoS(self, description, hyperlink):
        """
        :param description:
        :param hyperlink:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)