# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortSettingsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortSettingsWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def activateDefencePeriod(self):
        self._printOverrideError('activateDefencePeriod')

    def disableDefencePeriod(self):
        self._printOverrideError('disableDefencePeriod')

    def cancelDisableDefencePeriod(self):
        self._printOverrideError('cancelDisableDefencePeriod')

    def as_setFortClanInfoS(self, data):
        """
        :param data: Represented by FortSettingsClanInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFortClanInfo(data)

    def as_setMainStatusS(self, title, msg, toolTip):
        if self._isDAAPIInited():
            return self.flashObject.as_setMainStatus(title, msg, toolTip)

    def as_setViewS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setView(value)

    def as_setDataForActivatedS(self, data):
        """
        :param data: Represented by FortSettingsActivatedViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDataForActivated(data)

    def as_setCanDisableDefencePeriodS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCanDisableDefencePeriod(value)

    def as_setDataForNotActivatedS(self, data):
        """
        :param data: Represented by FortSettingsNotActivatedViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDataForNotActivated(data)