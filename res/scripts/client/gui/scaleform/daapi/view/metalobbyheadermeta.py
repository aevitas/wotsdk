# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyHeaderMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class LobbyHeaderMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def menuItemClick(self, alias):
        self._printOverrideError('menuItemClick')

    def showLobbyMenu(self):
        self._printOverrideError('showLobbyMenu')

    def showExchangeWindow(self):
        self._printOverrideError('showExchangeWindow')

    def showExchangeXPWindow(self):
        self._printOverrideError('showExchangeXPWindow')

    def showPremiumDialog(self):
        self._printOverrideError('showPremiumDialog')

    def onPremShopClick(self):
        self._printOverrideError('onPremShopClick')

    def onPayment(self):
        self._printOverrideError('onPayment')

    def showSquad(self):
        self._printOverrideError('showSquad')

    def fightClick(self, mapID, actionName):
        self._printOverrideError('fightClick')

    def as_setScreenS(self, alias):
        if self._isDAAPIInited():
            return self.flashObject.as_setScreen(alias)

    def as_creditsResponseS(self, credits, btnDoText, tooltip, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_creditsResponse(credits, btnDoText, tooltip, tooltipType)

    def as_goldResponseS(self, gold, btnDoText, tooltip, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_goldResponse(gold, btnDoText, tooltip, tooltipType)

    def as_doDisableNavigationS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_doDisableNavigation()

    def as_doDisableHeaderButtonS(self, btnId, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_doDisableHeaderButton(btnId, isEnabled)

    def as_setGoldFishEnabledS(self, isEnabled, playAnimation, tooltip, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setGoldFishEnabled(isEnabled, playAnimation, tooltip, tooltipType)

    def as_updateSquadS(self, isInSquad, tooltip, tooltipType, isEvent, icon):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSquad(isInSquad, tooltip, tooltipType, isEvent, icon)

    def as_nameResponseS(self, data):
        """
        :param data: Represented by AccountDataVo (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_nameResponse(data)

    def as_setClanEmblemS(self, tID):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(tID)

    def as_setPremiumParamsS(self, btnLabel, doLabel, isHasAction, tooltip, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setPremiumParams(btnLabel, doLabel, isHasAction, tooltip, tooltipType)

    def as_setPremShopDataS(self, iconSrc, premShopText, tooltip, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setPremShopData(iconSrc, premShopText, tooltip, tooltipType)

    def as_updateBattleTypeS(self, battleTypeName, battleTypeIcon, isEnabled, tooltip, tooltipType, battleTypeID):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBattleType(battleTypeName, battleTypeIcon, isEnabled, tooltip, tooltipType, battleTypeID)

    def as_setServerS(self, name, tooltip, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setServer(name, tooltip, tooltipType)

    def as_updatePingStatusS(self, pingStatus, isColorBlind):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePingStatus(pingStatus, isColorBlind)

    def as_setWalletStatusS(self, walletStatus):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)

    def as_setFreeXPS(self, freeXP, btnDoText, isHasAction, tooltip, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setFreeXP(freeXP, btnDoText, isHasAction, tooltip, tooltipType)

    def as_disableFightButtonS(self, isDisabled):
        if self._isDAAPIInited():
            return self.flashObject.as_disableFightButton(isDisabled)

    def as_setFightButtonS(self, label):
        if self._isDAAPIInited():
            return self.flashObject.as_setFightButton(label)

    def as_setCoolDownForReadyS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownForReady(value)

    def as_showBubbleTooltipS(self, message, duration):
        if self._isDAAPIInited():
            return self.flashObject.as_showBubbleTooltip(message, duration)

    def as_setFightBtnTooltipS(self, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setFightBtnTooltip(tooltip)

    def as_updateOnlineCounterS(self, clusterStats, regionStats, tooltip, isAvailable):
        if self._isDAAPIInited():
            return self.flashObject.as_updateOnlineCounter(clusterStats, regionStats, tooltip, isAvailable)

    def as_initOnlineCounterS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_initOnlineCounter(visible)

    def as_setHangarMenuDataS(self, data):
        """
        :param data: Represented by HangarMenuVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHangarMenuData(data)

    def as_setButtonCounterS(self, btnAlias, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonCounter(btnAlias, value)

    def as_removeButtonCounterS(self, btnAlias):
        if self._isDAAPIInited():
            return self.flashObject.as_removeButtonCounter(btnAlias)