# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileTechniqueMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileTechniqueMeta(ProfileSection):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ProfileSection
    null
    """

    def as_responseVehicleDossierS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_responseVehicleDossier(data)