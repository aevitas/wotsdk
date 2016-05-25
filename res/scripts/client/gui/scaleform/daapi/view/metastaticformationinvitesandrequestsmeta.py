# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StaticFormationInvitesAndRequestsMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class StaticFormationInvitesAndRequestsMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def setDescription(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('setDescription')

    def setShowOnlyInvites(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('setShowOnlyInvites')

    def resolvePlayerRequest(self, playerId, playerAccepted):
        """
        :param playerId:
        :param playerAccepted:
        :return :
        """
        self._printOverrideError('resolvePlayerRequest')

    def as_getDataProviderS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()

    def as_setStaticDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setTeamDescriptionS(self, description):
        """
        :param description:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamDescription(description)