# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortWelcomeInfoViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortWelcomeInfoViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onCreateBtnClick(self):
        self._printOverrideError('onCreateBtnClick')

    def onNavigate(self, code):
        self._printOverrideError('onNavigate')

    def openClanResearch(self):
        self._printOverrideError('openClanResearch')

    def as_setWarningTextS(self, text, disabledBtnTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setWarningText(text, disabledBtnTooltip)

    def as_setCommonDataS(self, data):
        """
        :param data: Represented by FortWelcomeViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCommonData(data)

    def as_setRequirementTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setRequirementText(text)

    def as_showMiniClientInfoS(self, description, hyperlink):
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)