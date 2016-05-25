# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ContainerManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ContainerManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def isModalViewsIsExists(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isModalViewsIsExists')

    def canCancelPreviousLoading(self, containerType):
        """
        :param containerType:
        :return Boolean:
        """
        self._printOverrideError('canCancelPreviousLoading')

    def as_getViewS(self, name):
        """
        :param name:
        :return Boolean:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getView(name)

    def as_showS(self, name, x, y):
        """
        :param name:
        :param x:
        :param y:
        :return Boolean:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_show(name, x, y)

    def as_hideS(self, name):
        """
        :param name:
        :return Boolean:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hide(name)

    def as_registerContainerS(self, type, name):
        """
        :param type:
        :param name:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_registerContainer(type, name)

    def as_unregisterContainerS(self, type):
        """
        :param type:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_unregisterContainer(type)

    def as_closePopUpsS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_closePopUps()

    def as_isOnTopS(self, cType, vName):
        """
        :param cType:
        :param vName:
        :return Boolean:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_isOnTop(cType, vName)

    def as_bringToFrontS(self, cType, vName):
        """
        :param cType:
        :param vName:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_bringToFront(cType, vName)

    def as_showContainersS(self, viewTypes):
        """
        :param viewTypes:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showContainers(viewTypes)

    def as_hideContainersS(self, viewTypes):
        """
        :param viewTypes:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideContainers(viewTypes)

    def as_isContainerShownS(self, viewType):
        """
        :param viewType:
        :return Boolean:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_isContainerShown(viewType)