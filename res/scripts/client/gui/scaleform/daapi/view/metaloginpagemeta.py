# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LoginPageMeta.py
from gui.Scaleform.framework.entities.View import View

class LoginPageMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def onLogin(self, user, password, host, isSocial):
        """
        :param user:
        :param password:
        :param host:
        :param isSocial:
        :return :
        """
        self._printOverrideError('onLogin')

    def onRegister(self, host):
        """
        :param host:
        :return :
        """
        self._printOverrideError('onRegister')

    def onRecovery(self):
        """
        :return :
        """
        self._printOverrideError('onRecovery')

    def onTextLinkClick(self, linkId):
        """
        :param linkId:
        :return :
        """
        self._printOverrideError('onTextLinkClick')

    def onLoginBySocial(self, socialId, host):
        """
        :param socialId:
        :param host:
        :return :
        """
        self._printOverrideError('onLoginBySocial')

    def onSetRememberPassword(self, remember):
        """
        :param remember:
        :return :
        """
        self._printOverrideError('onSetRememberPassword')

    def onExitFromAutoLogin(self):
        """
        :return :
        """
        self._printOverrideError('onExitFromAutoLogin')

    def doUpdate(self):
        """
        :return :
        """
        self._printOverrideError('doUpdate')

    def isToken(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isToken')

    def resetToken(self):
        """
        :return :
        """
        self._printOverrideError('resetToken')

    def onEscape(self):
        """
        :return :
        """
        self._printOverrideError('onEscape')

    def isCSISUpdateOnRequest(self):
        """
        :return Boolean:
        """
        self._printOverrideError('isCSISUpdateOnRequest')

    def isPwdInvalid(self, password):
        """
        :param password:
        :return Boolean:
        """
        self._printOverrideError('isPwdInvalid')

    def isLoginInvalid(self, login):
        """
        :param login:
        :return Boolean:
        """
        self._printOverrideError('isLoginInvalid')

    def showLegal(self):
        """
        :return :
        """
        self._printOverrideError('showLegal')

    def startListenCsisUpdate(self, startListenCsis):
        """
        :param startListenCsis:
        :return :
        """
        self._printOverrideError('startListenCsisUpdate')

    def saveLastSelectedServer(self, server):
        """
        :param server:
        :return :
        """
        self._printOverrideError('saveLastSelectedServer')

    def changeAccount(self):
        """
        :return :
        """
        self._printOverrideError('changeAccount')

    def switchBgMode(self):
        """
        :return :
        """
        self._printOverrideError('switchBgMode')

    def setMute(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('setMute')

    def onVideoLoaded(self):
        """
        :return :
        """
        self._printOverrideError('onVideoLoaded')

    def musicFadeOut(self):
        """
        :return :
        """
        self._printOverrideError('musicFadeOut')

    def as_setDefaultValuesS(self, loginName, pwd, rememberPwd, rememberPwdVisible, isIgrCredentialsReset, showRecoveryLink):
        """
        :param loginName:
        :param pwd:
        :param rememberPwd:
        :param rememberPwdVisible:
        :param isIgrCredentialsReset:
        :param showRecoveryLink:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultValues(loginName, pwd, rememberPwd, rememberPwdVisible, isIgrCredentialsReset, showRecoveryLink)

    def as_setErrorMessageS(self, msg, errorCode):
        """
        :param msg:
        :param errorCode:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setErrorMessage(msg, errorCode)

    def as_setVersionS(self, version):
        """
        :param version:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVersion(version)

    def as_setCopyrightS(self, copyrightVal, legalInfo):
        """
        :param copyrightVal:
        :param legalInfo:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCopyright(copyrightVal, legalInfo)

    def as_showWallpaperS(self, isShow, path, showSwitcher, isMuted):
        """
        :param isShow:
        :param path:
        :param showSwitcher:
        :param isMuted:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showWallpaper(isShow, path, showSwitcher, isMuted)

    def as_showLoginVideoS(self, path, isMuted):
        """
        :param path:
        :param isMuted:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showLoginVideo(path, isMuted)

    def as_setCapsLockStateS(self, isActive):
        """
        :param isActive:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCapsLockState(isActive)

    def as_setKeyboardLangS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setKeyboardLang(value)

    def as_doAutoLoginS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_doAutoLogin()

    def as_enableS(self, enabled):
        """
        :param enabled:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_enable(enabled)

    def as_switchToAutoAndSubmitS(self, key):
        """
        :param key:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_switchToAutoAndSubmit(key)

    def as_showSimpleFormS(self, isShow, socialList):
        """
        :param isShow:
        :param socialList:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showSimpleForm(isShow, socialList)

    def as_showSocialFormS(self, haveToken, userName, icoPath, socialId):
        """
        :param haveToken:
        :param userName:
        :param icoPath:
        :param socialId:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showSocialForm(haveToken, userName, icoPath, socialId)

    def as_resetPasswordS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_resetPassword()

    def as_getServersDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getServersDP()

    def as_setSelectedServerIndexS(self, serverIndex):
        """
        :param serverIndex:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedServerIndex(serverIndex)