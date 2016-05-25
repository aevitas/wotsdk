# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/BaseDAAPIModuleMeta.py
from gui.Scaleform.framework.entities.DAAPIEntity import DAAPIEntity

class BaseDAAPIModuleMeta(DAAPIEntity):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends DAAPIEntity
    null
    """

    def as_populateS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_populate()

    def as_disposeS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()