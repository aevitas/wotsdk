# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/__init__.py
from gui import GUI_SETTINGS
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, GroupedViewSettings, ViewTypes, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.managers.context_menu import ContextMenuManager
from gui.Scaleform.daapi.view.lobby.hangar.filter_popover import FilterPopover
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES
ContextMenuManager.registerHandler(CONTEXT_MENU_HANDLER_TYPE.CREW, 'gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers', 'CrewContextMenuHandler')
ContextMenuManager.registerHandler(CONTEXT_MENU_HANDLER_TYPE.VEHICLE, 'gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers', 'VehicleContextMenuHandler')
ContextMenuManager.registerHandler(CONTEXT_MENU_HANDLER_TYPE.TECHNICAL_MAINTENANCE, 'gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers', 'TechnicalMaintenanceCMHandler')

def getViewSettings():
    from AmmunitionPanel import AmmunitionPanel
    from Crew import Crew
    from CrewAboutDogWindow import CrewAboutDogWindow
    from Hangar import Hangar
    from ResearchPanel import ResearchPanel
    from SwitchModePanel import SwitchModePanel
    from TechnicalMaintenance import TechnicalMaintenance
    from TmenXpPanel import TmenXpPanel
    from gui.Scaleform.daapi.view.lobby.hangar.VehicleParameters import VehicleParameters
    if GUI_SETTINGS.useNewCarouselFilters:
        from TankCarousel import TankCarousel
    else:
        from TankCarousel import TankCarouselOldFilter as TankCarousel
    return (ViewSettings(VIEW_ALIAS.LOBBY_HANGAR, Hangar, 'hangar.swf', ViewTypes.LOBBY_SUB, VIEW_ALIAS.LOBBY_HANGAR, ScopeTemplates.LOBBY_SUB_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.CREW_ABOUT_DOG_WINDOW, CrewAboutDogWindow, 'simpleWindow.swf', ViewTypes.WINDOW, 'aboutDogWindow', None, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.TECHNICAL_MAINTENANCE, TechnicalMaintenance, 'technicalMaintenance.swf', ViewTypes.WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.TANK_CAROUSEL_FILTER_POPOVER, FilterPopover, 'filtersPopoverView.swf', ViewTypes.WINDOW, VIEW_ALIAS.TANK_CAROUSEL_FILTER_POPOVER, VIEW_ALIAS.TANK_CAROUSEL_FILTER_POPOVER, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(HANGAR_ALIASES.AMMUNITION_PANEL, AmmunitionPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(HANGAR_ALIASES.RESEARCH_PANEL, ResearchPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.SWITCH_MODE_PANEL, SwitchModePanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(HANGAR_ALIASES.TANK_CAROUSEL, TankCarousel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(HANGAR_ALIASES.TMEN_XP_PANEL, TmenXpPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(HANGAR_ALIASES.VEHICLE_PARAMETERS, VehicleParameters, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(HANGAR_ALIASES.CREW, Crew, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (HangarPackageBusinessHandler(),)


class HangarPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = ((VIEW_ALIAS.TANK_CAROUSEL_FILTER_POPOVER, self.loadViewByCtxEvent),
         (VIEW_ALIAS.CREW_ABOUT_DOG_WINDOW, self.loadViewByCtxEvent),
         (VIEW_ALIAS.LOBBY_HANGAR, self.loadViewByCtxEvent),
         (VIEW_ALIAS.TECHNICAL_MAINTENANCE, self.loadViewByCtxEvent))
        super(HangarPackageBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)