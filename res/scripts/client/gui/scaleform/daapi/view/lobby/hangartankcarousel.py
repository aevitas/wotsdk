# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/TankCarousel.py
from operator import attrgetter
import BigWorld
import constants
from account_helpers.AccountSettings import AccountSettings, STORE_TAB
from CurrentVehicle import g_currentVehicle
from debug_utils import LOG_DEBUG
from gui import GUI_NATIONS
from gui import SystemMessages
from gui.Scaleform import getVehicleTypeAssetPath, getNationsFilterAssetPath, getButtonsAssetPath
from gui.Scaleform.daapi.view.meta.TankCarouselMeta import TankCarouselMeta
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.locale.FALLOUT import FALLOUT
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.game_control import g_instance as g_gameCtrl, getFalloutCtrl
from gui.shared.formatters.ranges import toRomanRangeString
from gui.shared.formatters.text_styles import alert, standard, main, middleTitle, highTitle, statInfo, critical
from gui.shared.formatters.time_formatters import RentLeftFormatter
from gui.shared.tooltips import ACTION_TOOLTIPS_STATE, ACTION_TOOLTIPS_TYPE
from gui.shared.utils.functions import makeTooltip
from gui.prb_control.prb_helpers import GlobalListener
from gui.shared.utils.requesters import REQ_CRITERIA
from gui.shared import events, EVENT_BUS_SCOPE, g_itemsCache
from gui.shared.formatters import icons
from gui.shared.formatters import text_styles
from gui.shared.gui_items import CLAN_LOCK
from gui.shared.gui_items.Vehicle import Vehicle, VEHICLE_TYPES_ORDER
from gui.shared.gui_items.processors.vehicle import VehicleSlotBuyer
from gui.shared.utils import decorators
from gui.Scaleform.daapi.view.lobby.hangar.tank_carousel_filter import IGR_FILTER_ID, createCarouselFilter
from helpers import i18n, int2roman
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER, Vehicle
from gui.shared.formatters import icons
from gui.Scaleform import getVehicleTypeAssetPath
from gui.Scaleform.daapi.view.meta.TankCarouselMeta import TankCarouselMeta
_UPDATE_LOCKS_PERIOD = 60

class TankCarousel(TankCarouselMeta, GlobalListener):

    def __init__(self):
        super(TankCarousel, self).__init__()
        self._filter = None
        self.__updateVehiclesTimerId = None
        self.__falloutCtrl = None
        self.__multiselectionMode = False
        self.__isAttentionCounter = True
        self.__totalVehicleCount = 0
        self.__currentVehicleCount = 0
        return

    def resetFilters(self):
        self._filter.reset()
        self.as_setCarouselFilterS(self._filter.getFilters(('bonus', 'favorite', 'gameMode')))
        self.showVehicles()

    def setVehiclesFilter(self, bonus, favorite, gameMode):
        self._filter.update({'bonus': bonus,
         'favorite': favorite,
         'gameMode': gameMode})
        self.blinkCounter()
        self.showVehicles()

    @property
    def filter(self):
        return self._filter

    @property
    def totalVehiclesCount(self):
        return self.__totalVehicleCount

    @property
    def currentVehiclesCount(self):
        return self.__currentVehicleCount

    @property
    def hasRentedVehicles(self):
        rentedVehicles = g_itemsCache.items.getVehicles(self._filter.getDefaultCriteria() | REQ_CRITERIA.VEHICLE.RENT)
        return len(rentedVehicles) > 0

    def blinkCounter(self):
        self.as_blinkCounterS()

    def _populate(self):
        super(TankCarousel, self)._populate()
        if self.__updateVehiclesTimerId is not None:
            BigWorld.cancelCallback(self.__updateVehiclesTimerId)
            self.__updateVehiclesTimerId = None
        g_gameCtrl.rentals.onRentChangeNotify += self._updateRent
        g_gameCtrl.igr.onIgrTypeChanged += self._updateIgrType
        self.app.loaderManager.onViewLoaded += self.__onViewLoaded
        self.__falloutCtrl = getFalloutCtrl()
        self.__falloutCtrl.onVehiclesChanged += self._updateFalloutVehicles
        self.__falloutCtrl.onSettingsChanged += self._updateFalloutSettings
        self.__multiselectionMode = self.__falloutCtrl.isSelected()
        self._initializeFilters()
        self._setupFilters(self.__multiselectionMode)
        self.__updateMultiselectionData()
        return

    def _dispose(self):
        if self.__updateVehiclesTimerId is not None:
            BigWorld.cancelCallback(self.__updateVehiclesTimerId)
            self.__updateVehiclesTimerId = None
        g_gameCtrl.rentals.onRentChangeNotify -= self._updateRent
        g_gameCtrl.igr.onIgrTypeChanged -= self._updateIgrType
        self.app.loaderManager.onViewLoaded -= self.__onViewLoaded
        self.__falloutCtrl.onVehiclesChanged -= self._updateFalloutVehicles
        self.__falloutCtrl.onSettingsChanged -= self._updateFalloutSettings
        self.__falloutCtrl = None
        self._filter = None
        super(TankCarousel, self)._dispose()
        return

    def _initializeFilters(self):
        xpRate = 'x%d' % g_itemsCache.items.shop.dailyXPFactor
        falloutBattleType = i18n.makeString('#menu:headerButtons/battle/menu/fallout/{0}'.format(getFalloutCtrl().getBattleType()))
        self.as_initCarouselFilterS({'counterCloseTooltip': makeTooltip(TOOLTIPS.TANKSFILTER_COUNTER_CLOSE_HEADER, TOOLTIPS.TANKSFILTER_COUNTER_CLOSE_BODY),
         'paramsFilter': {'icon': getButtonsAssetPath('params'),
                          'tooltip': makeTooltip('#tank_carousel_filter:filter/paramsFilter/header', '#tank_carousel_filter:filter/paramsFilter/body')},
         'favoriteFilter': {'icon': getButtonsAssetPath('favorite'),
                            'tooltip': makeTooltip('#tank_carousel_filter:filter/favoriteFilter/header', '#tank_carousel_filter:filter/favoriteFilter/body')},
         'gameModeFilter': {'icon': getButtonsAssetPath('game_mode'),
                            'tooltip': makeTooltip('#tank_carousel_filter:filter/gameModeFilter/header', i18n.makeString('#tank_carousel_filter:filter/gameModeFilter/body', type=falloutBattleType))},
         'bonusFilter': {'icon': getButtonsAssetPath('bonus_%s' % xpRate),
                         'tooltip': makeTooltip('#tank_carousel_filter:filter/bonusFilter/header', i18n.makeString('#tank_carousel_filter:filter/bonusFilter/body', bonus=xpRate))}})

    def _setupFilters(self, isMultiselectionMode):
        self._filter = createCarouselFilter(isMultiselectionMode)
        self.as_setCarouselFilterS(self._filter.getFilters(('bonus', 'favorite', 'gameMode')))

    def vehicleChange(self, vehInvID):
        g_currentVehicle.selectVehicle(int(vehInvID))

    @decorators.process('buySlot')
    def buySlot(self):
        result = yield VehicleSlotBuyer().request()
        if len(result.userMsg):
            SystemMessages.g_instance.pushI18nMessage(result.userMsg, type=result.sysMsgType)

    def buyTankClick(self):
        AccountSettings.setFilter(STORE_TAB, 0)
        shopFilter = list(AccountSettings.getFilter('shop_current'))
        shopFilter[1] = 'vehicle'
        AccountSettings.setFilter('shop_current', tuple(shopFilter))
        self.fireEvent(events.LoadViewEvent(VIEW_ALIAS.LOBBY_STORE), EVENT_BUS_SCOPE.LOBBY)

    def _updateRent(self, vehicles):
        self.updateVehicles(vehicles)

    def _updateIgrType(self, *args):
        filterCriteria = REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.IS_PREMIUM_IGR
        self.updateVehicles(filterCriteria=filterCriteria)

    def _updateFallout(self):
        filterCriteria = REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.FALLOUT.SELECTED
        self.updateVehicles(filterCriteria=filterCriteria, updateFallout=False)
        self.__updateMultiselectionData()

    def _updateFalloutSettings(self, *args):
        self.__multiselectionMode = self.__falloutCtrl.isSelected()
        self._initializeFilters()
        self._setupFilters(self.__multiselectionMode)
        self.updateVehicles()
        self.__updateMultiselectionData()

    def _updateFalloutVehicles(self, *args):
        filterCriteria = REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.FALLOUT.AVAILABLE
        self.updateVehicles(filterCriteria=filterCriteria, updateFallout=False)
        self.__updateMultiselectionData()

    def showVehicles(self):
        totalVehicles = g_itemsCache.items.getVehicles(self._filter.getDefaultCriteria())
        filteredVehicles = g_itemsCache.items.getVehicles(self._filter.getCriteria())

        def sorting(v1, v2):
            if v1.isFavorite and not v2.isFavorite:
                return -1
            if not v1.isFavorite and v2.isFavorite:
                return 1
            return cmp(v1, v2)

        vehsCDs = map(attrgetter('intCD'), sorted(filteredVehicles.values(), sorting))
        LOG_DEBUG('Showing carousel vehicles:', vehsCDs)
        self.as_showVehiclesS(vehsCDs)
        self.__totalVehicleCount = len(totalVehicles)
        self.__currentVehicleCount = len(filteredVehicles)
        if not self._filter.isDefault():
            if self.__currentVehicleCount == 0:
                currentCountStyle = text_styles.error
            else:
                currentCountStyle = text_styles.stats
            self.as_showCounterS('{0} / {1}'.format(currentCountStyle(self.__currentVehicleCount), text_styles.main(self.__totalVehicleCount)), self.__currentVehicleCount == 0)
        else:
            self.as_hideCounterS()

    def updateVehicles(self, vehicles = None, filterCriteria = None, updateFallout = True):
        isSet = vehicles is None and filterCriteria is None
        filterCriteria = filterCriteria or REQ_CRITERIA.INVENTORY
        if vehicles is not None:
            filterCriteria |= REQ_CRITERIA.IN_CD_LIST(vehicles)
        items = g_itemsCache.items
        filteredVehs = items.getVehicles(filterCriteria)
        if vehicles is None:
            vehicles = filteredVehs.keys()
        hasEmptySlots = self.__multiselectionMode and len(self.__falloutCtrl.getEmptySlots()) > 0
        hasRequiredVehicles = self.__falloutCtrl.getConfig().hasRequiredVehicles()
        vehsData = {}
        multiselectionsData = {}
        for intCD in vehicles:
            vehicle = filteredVehs.get(intCD)
            vehData = None
            if vehicle is not None:
                vState, vStateLvl = vehicle.getState()
                isNotSuitableVeh = not self.__falloutCtrl.isSuitableVeh(vehicle)
                if isNotSuitableVeh:
                    vState, vStateLvl = Vehicle.VEHICLE_STATE.NOT_SUITABLE, Vehicle.VEHICLE_STATE_LEVEL.WARNING
                rentInfoStr = RentLeftFormatter(vehicle.rentInfo, vehicle.isPremiumIGR).getRentLeftStr()
                vehData = self._getVehicleData(vehicle, vState, vStateLvl, rentInfoStr)
                multiselectionsData[intCD] = self.__packMultiselectionFlags(self.__multiselectionMode and vehicle.isFalloutSelected, self.__falloutCtrl.canSelectVehicle(vehicle), hasRequiredVehicles and hasEmptySlots or vehicle.isFalloutSelected)
            vehsData[intCD] = vehData

        LOG_DEBUG('Updating carousel vehicles: {0}'.format(vehsData if not isSet else 'full sync'))
        self.as_updateVehiclesS(vehsData, isSet)
        self.as_setMultiselectionButtonLabelsS(FALLOUT.TANKCAROUSELSLOT_ACTIVATEBUTTON, FALLOUT.TANKCAROUSELSLOT_DEACTIVATEBUTTON, self.__falloutCtrl.carouselSelectionButtonTooltip())
        self.as_updateMultiselectionDataS(multiselectionsData)
        isVehTypeLock = sum((len(v) for v in items.stats.vehicleTypeLocks.itervalues()))
        isGlobalVehLock = sum((len(v) for v in items.stats.globalVehicleLocks.itervalues()))
        if self.__updateVehiclesTimerId is None and (isVehTypeLock or isGlobalVehLock):
            self.__updateVehiclesTimerId = BigWorld.callback(_UPDATE_LOCKS_PERIOD, self.updateLockTimers)
            LOG_DEBUG('Lock timer updated')
        self._initializeFilters()
        if self.__multiselectionMode and updateFallout and not isSet:
            self._updateFallout()
        else:
            self.showVehicles()
        return

    def setVehicleSelected(self, vehicleInventoryId, isSelected):
        vehicleInventoryId = int(vehicleInventoryId)
        if isSelected:
            self.__falloutCtrl.addSelectedVehicle(vehicleInventoryId)
        else:
            self.__falloutCtrl.removeSelectedVehicle(vehicleInventoryId)

    def moveVehiclesSelectionSlot(self, vehicleInventoryId):
        self.__falloutCtrl.moveSelectedVehicle(int(vehicleInventoryId))

    def updateParams(self):
        items = g_itemsCache.items
        slots = items.stats.vehicleSlots
        vehicles = len(items.getVehicles(REQ_CRITERIA.INVENTORY))
        shopPrice = items.shop.getVehicleSlotsPrice(slots)
        defaultPrice = items.shop.defaults.getVehicleSlotsPrice(slots)
        selectedTankID = g_currentVehicle.item.intCD if g_currentVehicle.isPresent() else None
        action = None
        if shopPrice != defaultPrice:
            action = {'type': ACTION_TOOLTIPS_TYPE.ECONOMICS,
             'key': 'slotsPrices',
             'isBuying': True,
             'state': (None, ACTION_TOOLTIPS_STATE.DISCOUNT),
             'newPrice': (0, shopPrice),
             'oldPrice': (0, defaultPrice)}
        self.as_setParamsS({'slotPrice': (0, shopPrice),
         'freeSlots': slots - vehicles,
         'selectedTankID': selectedTankID,
         'slotPriceActionData': action})
        return

    def updateLockTimers(self):
        self.__updateVehiclesTimerId = None
        items = g_itemsCache.items
        if items.stats.globalVehicleLocks.get(CLAN_LOCK) is not None:
            vehicles = None
        else:
            vehicles = items.stats.vehicleTypeLocks.keys()
        self.updateVehicles(vehicles)
        return

    def getStringStatus(self, vState):
        statusStr = ''
        groupNotReadyStatuses = [Vehicle.VEHICLE_STATE.FALLOUT_BROKEN, Vehicle.VEHICLE_STATE.FALLOUT_MIN]
        if vState == Vehicle.VEHICLE_STATE.IN_PREMIUM_IGR_ONLY:
            icon = icons.premiumIgrSmall()
            statusStr = i18n.makeString('#menu:tankCarousel/vehicleStates/%s' % vState, icon=icon)
        elif vState not in groupNotReadyStatuses:
            statusStr = i18n.makeString('#menu:tankCarousel/vehicleStates/%s' % vState)
        return statusStr

    def _getVehicleData(self, vehicle, vState, vStateLvl, rentInfoStr):
        return {'id': vehicle.invID,
         'inventoryId': vehicle.invID,
         'label': vehicle.shortUserName if vehicle.isPremiumIGR else vehicle.userName,
         'image': vehicle.icon,
         'nation': vehicle.nationID,
         'level': vehicle.level,
         'stat': vState,
         'statStr': self.getStringStatus(vState),
         'stateLevel': vStateLvl,
         'doubleXPReceived': vehicle.dailyXPFactor,
         'compactDescr': vehicle.intCD,
         'favorite': vehicle.isFavorite,
         'clanLock': vehicle.clanLock,
         'elite': vehicle.isElite,
         'premium': vehicle.isPremium,
         'tankType': vehicle.type,
         'current': 0,
         'enabled': True,
         'rentLeft': rentInfoStr,
         'selectableForSlot': self.__multiselectionMode and vehicle.isFalloutAvailable and not vehicle.isDisabledInPremIGR}

    def __getMultiselectionSlots(self):
        result = []
        if not self.__multiselectionMode:
            return ()
        else:
            falloutCfg = self.__falloutCtrl.getConfig()
            selectedSlots = self.__falloutCtrl.getSelectedSlots()
            selectedSlotsNumber = len(selectedSlots)
            requiredSlots = self.__falloutCtrl.getRequiredSlots()
            mustSelectRequiredVehicle = self.__falloutCtrl.mustSelectRequiredVehicle()
            for slotIdx in range(falloutCfg.maxVehiclesPerPlayer):
                vehicle = None
                if slotIdx < selectedSlotsNumber:
                    vehicle = g_itemsCache.items.getVehicle(selectedSlots[slotIdx])
                if slotIdx in requiredSlots:
                    if mustSelectRequiredVehicle:
                        formattedStatusStr = alert(i18n.makeString(FALLOUT.MULTISELECTIONSLOT_DOMINATION_REQUIREDVEHICLENOTACTIVATED, level=int2roman(falloutCfg.vehicleLevelRequired)))
                    else:
                        formattedStatusStr = alert(FALLOUT.MULTISELECTIONSLOT_DOMINATION_VEHICLENOTACTIVATED)
                else:
                    formattedStatusStr = standard(FALLOUT.MULTISELECTIONSLOT_MULTITEAM_VEHICLENOTACTIVATED)
                data = {'indexStr': i18n.makeString(FALLOUT.MULTISELECTIONSLOT_INDEX, index=slotIdx + 1),
                 'isActivated': False,
                 'formattedStatusStr': formattedStatusStr,
                 'stateLevel': '',
                 'showAlert': slotIdx in requiredSlots,
                 'alertTooltip': TOOLTIPS.MULTISELECTION_ALERT}
                if vehicle is not None:
                    vState, vStateLvl = vehicle.getState()
                    data.update({'isActivated': True,
                     'formattedStatusStr': self.getStringStatus(vState),
                     'inventoryId': vehicle.invID,
                     'vehicleName': vehicle.shortUserName,
                     'vehicleIcon': vehicle.iconSmall,
                     'vehicleType': vehicle.type,
                     'vehicleLevel': vehicle.level,
                     'isElite': vehicle.isElite,
                     'stat': vState,
                     'stateLevel': vStateLvl,
                     'showAlert': False})
                result.append(data)

            return result

    def __getMultiselectionStatus(self):
        if self.__multiselectionMode:
            falloutCfg = self.__falloutCtrl.getConfig()
            messageTemplate = '#fallout:multiselectionSlot/{0}'.format(self.__falloutCtrl.getBattleType())
            if not falloutCfg.hasRequiredVehicles():
                levels = list(falloutCfg.allowedLevels)
                return (False, critical(i18n.makeString(messageTemplate + '/topTierVehicleRequired', level=toRomanRangeString(levels, 1), requiredLevel=int2roman(falloutCfg.vehicleLevelRequired))))
            if self.__falloutCtrl.getSelectedVehicles():
                return (True, middleTitle(i18n.makeString(FALLOUT.MULTISELECTIONSLOT_SELECTIONSTATUS)) + '\n' + main(i18n.makeString(FALLOUT.MULTISELECTIONSLOT_SELECTIONREQUIREMENTS, level=toRomanRangeString(list(falloutCfg.allowedLevels), 1))))
            if falloutCfg.getAllowedVehicles():
                levels = list(falloutCfg.allowedLevels)
                topLevel = levels[-1]
                header = highTitle(i18n.makeString(messageTemplate + '/descriptionTitle', topLevel=int2roman(topLevel)))
                body = main(i18n.makeString(messageTemplate + '/message', level=toRomanRangeString(levels, 1)))
                return (False, header + '\n' + body)
        return (False, '')

    def __updateMultiselectionData(self):
        falloutCfg = self.__falloutCtrl.getConfig()
        showSlots, msg = self.__getMultiselectionStatus()
        canDo, _ = self.prbDispatcher.canPlayerDoAction()
        data = {'multiSelectionIsEnabled': self.__multiselectionMode,
         'formattedMessage': msg,
         'showSlots': showSlots,
         'slots': self.__getMultiselectionSlots(),
         'indicatorIsEnabled': canDo,
         'vehicleTypes': middleTitle(i18n.makeString(FALLOUT.MULTISELECTIONSLOT_SELECTIONSTATUS)) + ' ' + main(i18n.makeString(FALLOUT.MULTISELECTIONSLOT_SELECTIONREQUIREMENTS, level=toRomanRangeString(list(falloutCfg.allowedLevels), 1))),
         'statusSrt': statInfo(FALLOUT.MULTISELECTIONSLOT_GROUPREADY) if canDo else critical(FALLOUT.MULTISELECTIONSLOT_GROUPNOTREADY)}
        self.as_setMultiselectionModeS(data)

    def __packMultiselectionFlags(self, selected, enabled, visible):
        value = 0
        idx = 0
        flags = (selected, enabled, visible)
        for flag in flags:
            if flag:
                value |= 1 << idx
            idx += 1

        return value

    def __onViewLoaded(self, view):
        if view is not None and view.settings is not None:
            if view.settings.alias == VIEW_ALIAS.TANK_CAROUSEL_FILTER_POPOVER:
                view.setTankCarousel(self)
        return


class TankCarouselOldFilter(TankCarousel):
    """ Legacy class that supports old filters.
    """

    def setVehiclesFilterOld(self, nation, vehicleType, favorite, gameMode):
        self._filter.update({'nation': int(nation),
         'vehicleType': int(vehicleType),
         'favoriteSelected': favorite,
         'gameModeSelected': gameMode})
        self.showVehicles()

    def _initializeFilters(self):
        self.as_initCarouselFilterOldS({'nations': self.__getNationsVO(),
         'vehicleTypes': self.__getVehicleTypesVO()})

    def _setupFilters(self, isMultiselectionMode):
        self._filter = createCarouselFilter(isMultiselectionMode, isLegacy=True)
        self.as_setCarouselFilterOldS(self._filter.getFilters(['nation',
         'vehicleType',
         'favoriteSelected',
         'gameModeSelected']))

    def __getVehicleTypesVO(self):
        result = [{'label': '#menu:carousel_tank_filter/all',
          'data': -1,
          'icon': getVehicleTypeAssetPath('all')}]
        for index, vehicleType in enumerate(VEHICLE_TYPES_ORDER):
            result.append({'label': '#menu:carousel_tank_filter/%s' % vehicleType,
             'data': index,
             'icon': getVehicleTypeAssetPath(vehicleType)})

        return result

    def __getNationsVO(self):
        result = [{'label': '#menu:nations/all',
          'data': -1,
          'icon': getNationsFilterAssetPath('all')}]
        if constants.IS_KOREA:
            result.append({'label': '#menu:carouselFilter/igr',
             'data': IGR_FILTER_ID,
             'icon': getNationsFilterAssetPath('igr')})
        for index, nation in enumerate(GUI_NATIONS):
            result.append({'label': '#menu:nations/%s' % nation,
             'data': index,
             'icon': getNationsFilterAssetPath(nation)})

        return result