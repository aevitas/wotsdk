# Embedded file name: scripts/client/gui/battle_control/BattleSessionProvider.py
from collections import namedtuple
import weakref
from PlayerEvents import g_playerEvents
from debug_utils import LOG_DEBUG
from adisp import async
from gui.battle_control import consumables, vehicle_state_ctrl
from gui.battle_control.avatar_stats_controller import AvatarStatsController
from gui.battle_control.BattleContext import BattleContext
from gui.battle_control.RespawnsController import RespawnsController
from gui.battle_control.NotificationsController import NotificationsController
from gui.battle_control.arena_info import getClientArena
from gui.battle_control.avatar_getter import leaveArena
from gui.battle_control.battle_constants import BATTLE_CTRL, VIEW_COMPONENT_RULE
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from gui.battle_control.battle_feedback import createFeedbackAdaptor
from gui.battle_control.battle_msgs_ctrl import createBattleMessagesCtrl
from gui.battle_control.battle_period_ctrl import createPeriodCtrl
from gui.battle_control.battle_team_bases_ctrl import createTeamsBasesCtrl
from gui.battle_control.ChatCommandsController import ChatCommandsController
from gui.battle_control.ArenaLoadController import ArenaLoadController
from gui.battle_control.DRRScaleController import DRRScaleController
from gui.battle_control.RepairController import RepairController
from gui.battle_control.arena_info.ArenaDataProvider import ArenaDataProvider
from gui.battle_control.arena_info.listeners import ListenersCollection
from gui.battle_control.dyn_squad_functional import DynSquadFunctional
from gui.battle_control.gas_attack_controller import GasAttackController
from gui.battle_control.hit_direction_ctrl import HitDirectionController
from gui.battle_control.requests import AvatarRequestsController
from gui.battle_control.debug_ctrl import DebugController
from gui.battle_control.view_components import createComponentsBridge
BattleSessionProviderStartCtx = namedtuple('BattleSessionProviderStartCtx', ('avatar', 'replayCtrl', 'gasAttackMgr'))
BattleSessionProviderStartCtx.__new__.__defaults__ = (None, None, None)

class BattleSessionProvider(object):
    __slots__ = ('__ammoCtrl', '__equipmentsCtrl', '__optDevicesCtrl', '__vehicleStateCtrl', '__chatCommands', '__drrScaleCtrl', '__feedback', '__ctx', '__arenaDP', '__arenaListeners', '__arenaLoadCtrl', '__respawnsCtrl', '__notificationsCtrl', '__arenaTeamsBasesCtrl', '__periodCtrl', '__messagesCtrl', '__repairCtrl', '__hitDirectionCtrl', '__requestsCtrl', '__avatarStatsCtrl', '__dynSquadFunctional', '__weakref__', '__gasAttackCtrl', '__debugCtrl', '__viewComponentsBridge')

    def __init__(self):
        super(BattleSessionProvider, self).__init__()
        self.__ctx = BattleContext()
        self.__ammoCtrl = None
        self.__equipmentsCtrl = None
        self.__optDevicesCtrl = None
        self.__vehicleStateCtrl = None
        self.__chatCommands = None
        self.__drrScaleCtrl = None
        self.__feedback = None
        self.__messagesCtrl = None
        self.__hitDirectionCtrl = None
        self.__requestsCtrl = None
        self.__arenaDP = None
        self.__arenaLoadCtrl = None
        self.__arenaTeamsBasesCtrl = None
        self.__periodCtrl = None
        self.__respawnsCtrl = None
        self.__notificationsCtrl = None
        self.__repairCtrl = None
        self.__dynSquadFunctional = None
        self.__avatarStatsCtrl = None
        self.__arenaListeners = None
        self.__gasAttackCtrl = None
        self.__debugCtrl = None
        self.__viewComponentsBridge = None
        return

    def getCtx(self):
        """
        Gets instance of ammo controller.
        :return: instance of AmmoController.
        """
        return self.__ctx

    def getAmmoCtrl(self):
        """
        Gets instance of ammo controller.
        :return: instance of AmmoController.
        """
        return self.__ammoCtrl

    def getEquipmentsCtrl(self):
        """
        Gets instance of equipments controller.
        :return: instance of EquipmentsController.
        """
        return self.__equipmentsCtrl

    def getOptDevicesCtrl(self):
        """
        Gets instance of optional devices controller.
        :return: instance of OptionalDevicesController.
        """
        return self.__optDevicesCtrl

    def getVehicleStateCtrl(self):
        """
        Gets instance of vehicle state controller.
        :return: instance of VehicleStateController.
        """
        return self.__vehicleStateCtrl

    def getChatCommands(self):
        """
        Gets instance of chat commands controller.
        :return: instance of ChatCommandsController.
        """
        return self.__chatCommands

    def getDrrScaleCtrl(self):
        """
        Gets instance of DRR scale controller.
        :return: instance of DRRScaleController.
        """
        return self.__drrScaleCtrl

    def getRespawnsCtrl(self):
        """
        Gets instance of respawns controller.
        :return: instance of RespawnsController.
        """
        return self.__respawnsCtrl

    def getNotificationsCtrl(self):
        """
        Gets instance of notification controller.
        :return: instance of NotificationController.
        """
        return self.__notificationsCtrl

    def getRepairCtrl(self):
        """
        Gets instance of repair controller.
        :return: instance of RepairController.
        """
        return self.__repairCtrl

    def getFeedback(self):
        """
        Gets instance of feedback adaptor to notify GUI about some events that
        needs to show response on player(s) actions.
        :return: instance of BattleFeedbackAdaptor.
        """
        return self.__feedback

    def getBattleMessagesCtrl(self):
        """
        Gets instance of messages controller to show messages in a battle.
        :return: instance of BattleMessagesController.
        """
        return self.__messagesCtrl

    def getHitDirectionCtrl(self):
        """
        Gets instance of hit direction controller to show damage indicator.
        :return: instance of HitDirectionController.
        """
        return self.__hitDirectionCtrl

    def getAvatarStatsCtrl(self):
        """
        Gets instance of avatar stats controller to track stats changes.
        :return: instance of AvatarStatsController.
        """
        return self.__avatarStatsCtrl

    def getArenaTeamsBasesCtrl(self):
        """
        Gets instance of arena team bases controller to track bases changes.
        :return: instance of BattleTeamsBasesController.
        """
        return self.__arenaTeamsBasesCtrl

    def getPeriodCtrl(self):
        """
        Gets instance of period controller to track time changes.
        :return: instance of ArenaPeriodController.
        """
        return self.__periodCtrl

    def getGasAttackCtrl(self):
        """
        Gets instance of gas attack controller.
        :return: instance of GasAttackController.
        """
        return self.__gasAttackCtrl

    def getDynSquadFunctional(self):
        """
        Gets instance of dynamic squad functional.
        :return: instance of DynSquadFunctional.
        """
        return self.__dynSquadFunctional

    @async
    def sendRequest(self, ctx, callback, allowDelay = None):
        """
        Sends request to the server.
        :param ctx: avatar request context object,
            @see gui.battle_control.request.context.
        :param callback: function that is invoked when response is received.
        :param allowDelay: bool.
        """
        self.__requestsCtrl.request(ctx, callback=callback, allowDelay=allowDelay)

    def setPlayerVehicle(self, vID, vDesc):
        self.__ammoCtrl.setGunSettings(vDesc.gun)
        self.__vehicleStateCtrl.setPlayerVehicle(vID)
        self.__feedback.setPlayerVehicle(vID)
        self.__respawnsCtrl.spawnVehicle(vID)

    def setAimOffset(self, offset):
        if self.__hitDirectionCtrl is not None:
            self.__hitDirectionCtrl.setOffset(offset)
        return

    def setAimPositionUpdated(self, mode, x, y):
        if self.__feedback is not None:
            self.__feedback.setAimPositionUpdated(mode, x, y)
        return

    def getArenaDP(self):
        """
        Gets instance of arena data provider.
        :return: instance of ArenaDataProvider.
        """
        return self.__arenaDP

    def addArenaCtrl(self, controller):
        """
        Adds arena controller. For additional information see
            gui.arena_info.IArenaController.
        :param controller: object extends IArenaController
        """
        if self.__arenaListeners is not None:
            self.__arenaListeners.addController(weakref.proxy(self.__ctx), controller)
        return

    def removeArenaCtrl(self, controller):
        """
        Removes arena controller.
        :param controller: object extends IArenaController.
        """
        if self.__arenaListeners is not None:
            self.__arenaListeners.removeController(controller)
        return

    def start(self, startCtx = None):
        """
        Battle session is started.
        :param startCtx: instance of BattleSessionProviderStartCtx.
        :return:
        """
        isReplayRecording = startCtx.replayCtrl.isRecording
        isReplayPlaying = startCtx.replayCtrl.isPlaying
        self.__arenaDP = ArenaDataProvider(avatar=startCtx.avatar)
        self.__ctx.start(self.__arenaDP)
        self.__ammoCtrl = consumables.createAmmoCtrl(isReplayPlaying, isReplayRecording)
        self.__equipmentsCtrl = consumables.createEquipmentCtrl(isReplayPlaying)
        self.__optDevicesCtrl = consumables.createOptDevicesCtrl()
        self.__vehicleStateCtrl = vehicle_state_ctrl.createCtrl(isReplayRecording)
        self.__arenaLoadCtrl = ArenaLoadController()
        self.__arenaTeamsBasesCtrl = createTeamsBasesCtrl(isReplayPlaying)
        self.__periodCtrl = createPeriodCtrl(isReplayPlaying, isReplayRecording)
        self.__respawnsCtrl = RespawnsController(startCtx)
        self.__repairCtrl = RepairController()
        self.__dynSquadFunctional = DynSquadFunctional(isReplayPlaying)
        self.__notificationsCtrl = NotificationsController(self.__arenaDP)
        self.__gasAttackCtrl = GasAttackController(startCtx)
        ctx = weakref.proxy(self.__ctx)
        self.__arenaListeners = ListenersCollection()
        self.__arenaListeners.addController(ctx, self.__arenaLoadCtrl)
        self.__arenaListeners.addController(ctx, self.__arenaTeamsBasesCtrl)
        self.__arenaListeners.addController(ctx, self.__periodCtrl)
        self.__arenaListeners.addController(ctx, self.__respawnsCtrl)
        self.__arenaListeners.addController(ctx, self.__dynSquadFunctional)
        self.__arenaListeners.start(startCtx.avatar.arena, arenaDP=self.__arenaDP)
        self.__feedback = createFeedbackAdaptor(isReplayPlaying)
        self.__feedback.start(self.__arenaDP)
        self.__messagesCtrl = createBattleMessagesCtrl(isReplayPlaying)
        self.__messagesCtrl.start(ctx)
        self.__drrScaleCtrl = DRRScaleController()
        self.__drrScaleCtrl.start(self.__messagesCtrl)
        self.__hitDirectionCtrl = HitDirectionController()
        self.__hitDirectionCtrl.start()
        g_playerEvents.onBattleResultsReceived += self.__pe_onBattleResultsReceived
        self.__chatCommands = ChatCommandsController()
        self.__chatCommands.start(self.__arenaDP, self.__feedback)
        self.__requestsCtrl = AvatarRequestsController()
        self.__avatarStatsCtrl = AvatarStatsController()
        self.__debugCtrl = DebugController()
        self.__debugCtrl.start()
        self.__viewComponentsBridge = createComponentsBridge()
        self.__viewComponentsBridge.registerControllers((BATTLE_CTRL.PERIOD, self.__periodCtrl), (BATTLE_CTRL.TEAM_BASES, self.__arenaTeamsBasesCtrl), (BATTLE_CTRL.DEBUG, self.__debugCtrl), (BATTLE_CTRL.HIT_DIRECTION, self.__hitDirectionCtrl))

    def stop(self):
        g_playerEvents.onBattleResultsReceived -= self.__pe_onBattleResultsReceived
        if self.__viewComponentsBridge is not None:
            self.__viewComponentsBridge.clear()
            self.__viewComponentsBridge = None
        if self.__requestsCtrl is not None:
            self.__requestsCtrl.fini()
            self.__requestsCtrl = None
        if self.__ammoCtrl is not None:
            self.__ammoCtrl.clear()
            self.__ammoCtrl = None
        if self.__equipmentsCtrl is not None:
            self.__equipmentsCtrl.clear()
            self.__equipmentsCtrl = None
        if self.__optDevicesCtrl is not None:
            self.__optDevicesCtrl.clear()
            self.__optDevicesCtrl = None
        if self.__vehicleStateCtrl is not None:
            self.__vehicleStateCtrl.clear()
            self.__vehicleStateCtrl = None
        if self.__arenaListeners is not None:
            self.__arenaListeners.stop()
            self.__arenaListeners = None
        if self.__drrScaleCtrl is not None:
            self.__drrScaleCtrl.stop()
            self.__drrScaleCtrl = None
        if self.__feedback is not None:
            self.__feedback.stop()
            self.__feedback = None
        if self.__messagesCtrl is not None:
            self.__messagesCtrl.stop()
            self.__messagesCtrl = None
        if self.__hitDirectionCtrl is not None:
            self.__hitDirectionCtrl.stop()
            self.__hitDirectionCtrl = None
        if self.__arenaDP is not None:
            self.__arenaDP.clear()
            self.__arenaDP = None
        if self.__chatCommands is not None:
            self.__chatCommands.stop()
            self.__chatCommands = None
        if self.__debugCtrl is not None:
            self.__debugCtrl.stop()
            self.__debugCtrl = None
        self.__arenaLoadCtrl = None
        self.__arenaTeamsBasesCtrl = None
        self.__periodCtrl = None
        self.__respawnsCtrl = None
        self.__notificationsCtrl = None
        self.__repairCtrl = None
        self.__gasAttackCtrl = None
        self.__dynSquadFunctional = None
        if self.__avatarStatsCtrl is not None:
            self.__avatarStatsCtrl.stop()
            self.__avatarStatsCtrl = None
        self.__ctx.stop()
        return

    def registerViewComponents(self, *data):
        """
        Sets view component data to find that components in routines
            addViewComponent, removeViewComponent.
        :param data: tuple((BATTLE_CTRL.*, (componentID, ...)), ...)
        """
        if self.__viewComponentsBridge is not None:
            self.__viewComponentsBridge.registerViewComponents(*data)
        return

    def addViewComponent(self, componentID, component, rule = VIEW_COMPONENT_RULE.PROXY):
        """
        View component has been created.
        :param componentID: string containing unique component ID.
        :param component: instance of component.
        :param rule: one of VIEW_COMPONENT_RULE.*.
        """
        if self.__viewComponentsBridge is not None:
            self.__viewComponentsBridge.addViewComponent(componentID, component, rule=rule)
        return

    def removeViewComponent(self, componentID):
        """
        View component has been removed.
        :param componentID: string containing unique component ID.
        """
        if self.__viewComponentsBridge is not None:
            self.__viewComponentsBridge.removeViewComponent(componentID)
        return

    def switchToPostmortem(self):
        """
        Player's vehicle is destroyed, switchers GUI to postmortem mode.
        """
        self.__ammoCtrl.clear()
        self.__equipmentsCtrl.clear()
        self.__optDevicesCtrl.clear()
        self.__gasAttackCtrl.clear()
        self.__feedback.setPlayerVehicle(0L)
        self.__vehicleStateCtrl.switchToPostmortem()

    def useLoaderIntuition(self):
        """
        Loader intuition was used.
        """
        self.__messagesCtrl.showVehicleMessage('LOADER_INTUITION_WAS_USED')
        self.__ammoCtrl.useLoaderIntuition()

    def movingToRespawnBase(self):
        """
        Player's avatar is moving to the respawn.
        """
        self.__ammoCtrl.clear(False)
        self.__equipmentsCtrl.clear(False)
        self.__optDevicesCtrl.clear(False)
        self.__vehicleStateCtrl.movingToRespawn()
        self.__respawnsCtrl.movingToRespawn()

    def invalidateVehicleState(self, state, value, vehicleID = 0):
        """
        State of player's vehicle (health, fire, state of device, etc.) is
        changed, notifies GUI about it.
        :param state: one of VEHICLE_VIEW_STATE.*.
        :param value: value of state.
        :param vehicleID: vehicle ID or zero.
        """
        self.__vehicleStateCtrl.invalidate(state, value, vehicleID)
        if state == VEHICLE_VIEW_STATE.DESTROYED:
            self.__ammoCtrl.clear(False)
            self.__equipmentsCtrl.clear(False)

    def repairPointAction(self, repairPointIndex, action, nextActionTime):
        self.__repairCtrl.action(repairPointIndex, action, nextActionTime)

    def updateAvatarPrivateStats(self, stats):
        self.__avatarStatsCtrl.update(stats)

    def addHitDirection(self, hitDirYaw, isDamage):
        self.__hitDirectionCtrl.addHit(hitDirYaw, isDamage)

    def startVehicleVisual(self, vProxy, isImmediate = False):
        self.__feedback.startVehicleVisual(vProxy, isImmediate)
        self.__debugCtrl.startVehicleVisual(vProxy.id)

    def stopVehicleVisual(self, vehicleID, isPlayerVehicle):
        self.__feedback.stopVehicleVisual(vehicleID, isPlayerVehicle)
        self.__debugCtrl.stopVehicleVisual(vehicleID)

    def handleShortcutChatCommand(self, key):
        self.__chatCommands.handleShortcutChatCommand(key)

    def __pe_onBattleResultsReceived(self, isActiveVehicle, _):
        """
        It's listener of event _PlayerEvents.onBattleResultsReceived.
        :param isActiveVehicle: bool.
        """
        if isActiveVehicle:
            arena = getClientArena()
            LOG_DEBUG('Try to exit from arena', arena)
            if arena:
                self.__ctx.lastArenaUniqueID = arena.arenaUniqueID
            leaveArena()