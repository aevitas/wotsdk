# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsPersonalWelcomeViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsPersonalWelcomeViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def success(self):
        self._printOverrideError('success')

    def as_setDataS(self, data):
        """
        :param data: Represented by QuestsPersonalWelcomeViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_showMiniClientInfoS(self, description, hyperlink):
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)