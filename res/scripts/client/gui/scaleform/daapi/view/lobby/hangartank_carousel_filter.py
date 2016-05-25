# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/tank_carousel_filter.py
import constants
import nations
from account_helpers.AccountSettings import AccountSettings, CAROUSEL_FILTER, FALLOUT_CAROUSEL_FILTER, CAROUSEL_FILTER_1, CAROUSEL_FILTER_2, FALLOUT_CAROUSEL_FILTER_1, FALLOUT_CAROUSEL_FILTER_2
from account_helpers.settings_core.SettingsCore import g_settingsCore
from gui import GUI_NATIONS
from gui.prb_control.settings import VEHICLE_LEVELS
from gui.shared.utils.requesters import REQ_CRITERIA
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER
IGR_FILTER_ID = 100
FILTER_VEHICLE_LEVELS = [ 'level_%d' % level for level in VEHICLE_LEVELS ]

def createCarouselFilter(isFallout = False, isLegacy = False):
    """ Factory method for creating of carousel filter.
    
    :param isFallout: flag indicating whether filter is intended for fallout
    :param isLegacy: flag indicating whether the old filters should be used
    :return an instance of on of Carousel{Fallout|}Filter{Old|} class.
    """
    if not isLegacy:
        if isFallout:
            carouselFilter = CarouselFalloutFilter(FALLOUT_CAROUSEL_FILTER_1, FALLOUT_CAROUSEL_FILTER_2)
        else:
            carouselFilter = CarouselFilter(CAROUSEL_FILTER_1, CAROUSEL_FILTER_2)
    elif isFallout:
        carouselFilter = CarouselFalloutFilterOld(FALLOUT_CAROUSEL_FILTER)
    else:
        carouselFilter = CarouselFilterOld(CAROUSEL_FILTER)
    return carouselFilter


def _filterDict(dictionary, keys, invert = False):
    """ Filter dict leaving only acceptable keys.
    
    :param dictionary: dictionary to be filtered
    :param keys: list of acceptable keys
    :param invert: optionally invert the values
    :return a new dict with only acceptable keys
    """
    return {key:(not value if invert else value) for key, value in dictionary.items() if key in keys}


class _CarouselFilter(object):
    """ Base class for tank carousel filters.
    """

    def __init__(self, *sections):
        self._sections = sections
        self._filters = {}
        self._load()

    def getCriteria(self):
        """ Get a criteria suitable for item requester.
        This request criteria is composed according to current state of the filters.
        
        :return an instance of RequestCriteria.
        """
        raise NotImplementedError

    def getDefaultCriteria(self):
        """ Get a default request criteria for the current game mode.
        
        :return: an instance of RequestCriteria.
        """
        return REQ_CRITERIA.INVENTORY | ~REQ_CRITERIA.VEHICLE.ONLY_FOR_FALLOUT

    def getFilters(self, keys = None):
        """ Get filters and their params.
        If there are overrides, they're returned instead of real filter params.
        
        :param keys: if specified, gathers only filters listed in this parameter.
        :return a dict.
        """
        if keys is not None:
            filters = _filterDict(self._filters, keys)
        else:
            filters = self._filters.copy()
        return filters

    def isDefault(self, keys = None):
        """ Check whether filters are in default state or not.
        
        :param keys: if specified, check only the filters listed in this parameter.
        :return: True if filters are in default state, False otherwise.
        """
        defaultFilters = AccountSettings.getFilterDefaults(self._sections)
        if keys is None:
            keys = defaultFilters.keys()
        for key in keys:
            if self._filters[key] != defaultFilters[key]:
                return False

        return True

    def reset(self, keys = None, save = True):
        """ Reset filters to their default state.
        
        :param keys: if specified, resets only the filters listed in this parameter.
        :param save: flag that determines whether filters should be saved immediately.
        """
        defaultFilters = AccountSettings.getFilterDefaults(self._sections)
        if keys is not None:
            defaultFilters = _filterDict(defaultFilters, keys)
        self.update(defaultFilters, save)
        return

    def switch(self, keys, save = True):
        """ Switch the state of boolean filter (True -> False).
        
        :param keys: switches values in the filters listed in this parameter.
        :param save: flag that determines whether filters should be saved immediately.
        """
        self.update(_filterDict(self._filters, keys, invert=True), save)

    def update(self, params, save = True):
        """ Update values of the specified filters.
        
        :param params: dict containing new parameters of filters.
        :param save: flag that determines whether filters should be saved immediately.
        """
        for key, value in params.items():
            raise key in self._filters or AssertionError
            self._filters[key] = value

        if save:
            self.save()

    def _load(self):
        """ Load filters from server.
        """
        raise NotImplementedError

    def save(self):
        """ Save filters to server.
        """
        raise NotImplementedError


class CarouselFilter(_CarouselFilter):

    def getCriteria(self):
        criteria = self.getDefaultCriteria()
        selectedNationsIds = []
        for nation, nId in nations.INDICES.items():
            if self._filters[nation]:
                selectedNationsIds.append(nId)

        if selectedNationsIds:
            criteria |= REQ_CRITERIA.NATIONS(selectedNationsIds)
        selectedVehiclesIds = []
        for vehicleType, vId in constants.VEHICLE_CLASS_INDICES.items():
            if self._filters[vehicleType]:
                selectedVehiclesIds.append(vehicleType)

        if selectedVehiclesIds:
            criteria |= REQ_CRITERIA.VEHICLE.CLASSES(selectedVehiclesIds)
        selectedLevels = []
        for level in VEHICLE_LEVELS:
            if self._filters['level_%d' % level]:
                selectedLevels.append(level)

        if selectedLevels:
            criteria |= REQ_CRITERIA.VEHICLE.LEVELS(selectedLevels)
        if self._filters['elite'] and not self._filters['premium']:
            criteria |= REQ_CRITERIA.VEHICLE.ELITE | ~REQ_CRITERIA.VEHICLE.PREMIUM
        elif self._filters['elite'] and self._filters['premium']:
            criteria |= REQ_CRITERIA.VEHICLE.ELITE
        elif self._filters['premium']:
            criteria |= REQ_CRITERIA.VEHICLE.PREMIUM
        if self._filters['igr'] and constants.IS_KOREA:
            criteria |= REQ_CRITERIA.VEHICLE.IS_PREMIUM_IGR
        if self._filters['hideRented']:
            criteria |= ~REQ_CRITERIA.VEHICLE.RENT
        if self._filters['bonus']:
            criteria |= REQ_CRITERIA.VEHICLE.HAS_XP_FACTOR
        if self._filters['favorite']:
            criteria |= REQ_CRITERIA.VEHICLE.FAVORITE
        return criteria

    def update(self, params, save = True):
        if 'igr' in params and params['igr']:
            params['hideRented'] = False
        super(CarouselFilter, self).update(params, save)

    def save(self):
        g_settingsCore.serverSettings.setSections(self._sections, self._filters)

    def _load(self):
        defaultFilters = AccountSettings.getFilterDefaults(self._sections)
        savedFilters = g_settingsCore.serverSettings.getSections(self._sections, defaultFilters)
        for key, value in defaultFilters.items():
            savedFilters[key] = type(value)(savedFilters[key])

        self._filters = savedFilters


class CarouselFalloutFilter(CarouselFilter):

    def getCriteria(self):
        criteria = super(CarouselFalloutFilter, self).getCriteria()
        if self._filters['gameMode']:
            criteria |= REQ_CRITERIA.VEHICLE.FALLOUT.AVAILABLE
        return criteria

    def getDefaultCriteria(self):
        return REQ_CRITERIA.INVENTORY


class CarouselFilterOld(_CarouselFilter):

    def getCriteria(self):
        criteria = self.getDefaultCriteria()
        if self._filters['nation'] != -1 and self._filters['nation'] != IGR_FILTER_ID:
            nationIndex = nations.INDICES.get(GUI_NATIONS[self._filters['nation']])
            criteria |= REQ_CRITERIA.NATIONS([nationIndex])
        if self._filters['nation'] == IGR_FILTER_ID:
            criteria |= REQ_CRITERIA.VEHICLE.IS_PREMIUM_IGR
        if self._filters['vehicleType'] != -1:
            vehicleIndex = constants.VEHICLE_CLASS_INDICES.get(VEHICLE_TYPES_ORDER[self._filters['vehicleType']])
            criteria |= REQ_CRITERIA.VEHICLE.CLASSES([constants.VEHICLE_CLASSES[vehicleIndex]])
        if self._filters['favoriteSelected']:
            criteria |= REQ_CRITERIA.VEHICLE.FAVORITE
        return criteria

    def save(self):
        savedFilters = {'nation': abs(self._filters['nation']),
         'nationIsNegative': self._filters['nation'] < 0,
         'vehicleType': abs(self._filters['vehicleType']),
         'vehicleTypeIsNegative': self._filters['vehicleType'] < 0,
         'favoriteSelected': self._filters['favoriteSelected'],
         'gameModeSelected': self._filters['gameModeSelected']}
        g_settingsCore.serverSettings.setSections(self._sections, savedFilters)

    def _load(self):
        defaultFilters = AccountSettings.getFilterDefaults(self._sections)
        savedFilters = g_settingsCore.serverSettings.getSections(self._sections, defaultFilters)
        isNationNegative = savedFilters['nationIsNegative']
        isVehicleTypeNegative = savedFilters['vehicleTypeIsNegative']
        if isNationNegative:
            nation = -savedFilters['nation']
        else:
            nation = savedFilters['nation']
        if isVehicleTypeNegative:
            vehicleType = -savedFilters['vehicleType']
        else:
            vehicleType = savedFilters['vehicleType']
        self._filters = {'nation': nation,
         'vehicleType': vehicleType,
         'favoriteSelected': bool(savedFilters['favoriteSelected']),
         'gameModeSelected': bool(savedFilters['gameModeSelected'])}


class CarouselFalloutFilterOld(CarouselFilterOld):

    def getCriteria(self):
        criteria = super(CarouselFalloutFilterOld, self).getCriteria()
        if self._filters['gameModeSelected']:
            criteria |= REQ_CRITERIA.VEHICLE.FALLOUT.AVAILABLE
        return criteria

    def getDefaultCriteria(self):
        return REQ_CRITERIA.INVENTORY