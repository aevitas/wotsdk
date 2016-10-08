# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ContactNoteManageViewMeta.py
from messenger.gui.Scaleform.meta.BaseManageContactViewMeta import BaseManageContactViewMeta

class ContactNoteManageViewMeta(BaseManageContactViewMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseManageContactViewMeta
    """

    def sendData(self, data):
        self._printOverrideError('sendData')

    def as_setUserPropsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setUserProps(value)