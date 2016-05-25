# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileSectionMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ProfileSectionMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def setActive(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('setActive')

    def requestData(self, data):
        """
        :param data:
        :return :
        """
        self._printOverrideError('requestData')

    def requestDossier(self, type):
        """
        :param type:
        :return :
        """
        self._printOverrideError('requestDossier')

    def as_updateS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)

    def as_setInitDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_responseDossierS(self, type, data, frameLabel, emptyScreenLabel):
        """
        :param type:
        :param data:
        :param frameLabel:
        :param emptyScreenLabel:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_responseDossier(type, data, frameLabel, emptyScreenLabel)