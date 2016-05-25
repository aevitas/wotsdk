# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/LoaderManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class LoaderManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def viewLoaded(self, name, view):
        """
        :param name:
        :param view:
        :return :
        """
        self._printOverrideError('viewLoaded')

    def viewLoadError(self, alias, name, text):
        """
        :param alias:
        :param name:
        :param text:
        :return :
        """
        self._printOverrideError('viewLoadError')

    def viewInitializationError(self, config, alias, name):
        """
        :param config:
        :param alias:
        :param name:
        :return :
        """
        self._printOverrideError('viewInitializationError')

    def as_loadViewS(self, config, alias, name, viewTutorialId):
        """
        :param config:
        :param alias:
        :param name:
        :param viewTutorialId:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_loadView(config, alias, name, viewTutorialId)