# Embedded file name: scripts/client/gui/battle_control/arena_info/listeners.py
import weakref
import operator
from collections import namedtuple
import BigWorld
from constants import ARENA_PERIOD, FINISH_REASON
from debug_utils import LOG_DEBUG, LOG_NOTE, LOG_ERROR
from gui.battle_control.arena_info.invitations import SquadInvitationsFilter
from gui.battle_control.battle_constants import WinStatus
from gui.battle_control.arena_info.settings import ARENA_LISTENER_SCOPE as _SCOPE
from gui.battle_control.arena_info.settings import INVALIDATE_OP
from gui.prb_control.prb_helpers import prbInvitesProperty
from messenger.m_constants import USER_ACTION_ID, USER_TAG
from messenger.proto.events import g_messengerEvents

class _PeriodAdditionalInfo(namedtuple('_PeriodAdditionalInfo', ['winStatus', 'winnerTeam', 'finishReason'])):

    def getWinnerTeam(self):
        return self.winnerTeam

    def getWinStatus(self):
        return self.winStatus

    def isExtermination(self):
        return self.finishReason == FINISH_REASON.EXTERMINATION


def _getPeriodAdditionalInfo(arenaDP, period, additionalInfo):
    if period == ARENA_PERIOD.AFTERBATTLE:
        winnerTeam, finishReason = additionalInfo
        return _PeriodAdditionalInfo(WinStatus.fromWinnerTeam(winnerTeam, arenaDP.isAllyTeam(winnerTeam)), winnerTeam, finishReason)
    else:
        return None


class _Listener(object):
    __slots__ = ('_controllers', '_arena')

    def __init__(self):
        super(_Listener, self).__init__()
        self._arena = lambda : None
        self._controllers = set()

    def __del__(self):
        LOG_DEBUG('Deleted:', self)

    def addController(self, battleCtx, controller):
        controller.setBattleCtx(battleCtx)
        self._controllers.add(weakref.ref(controller))
        return True

    def removeController(self, controller):
        result = False
        controllerRef = weakref.ref(controller)
        if controllerRef in self._controllers:
            self._controllers.remove(controllerRef)
            result = True
        return result

    def clear(self):
        while len(self._controllers):
            ref = self._controllers.pop()
            ctrl = ref()
            if ctrl:
                ctrl.clear()

    def start(self, arena, **kwargs):
        self._arena = arena

    def stop(self):
        self.clear()
        arena = self._arena()
        self._arena = lambda : None
        return arena

    def _invokeListenersMethod(self, method, *args):
        caller = operator.methodcaller(method, *args)
        for ref in set(self._controllers):
            controller = ref()
            if controller is not None:
                caller(controller)

        return


class ArenaVehiclesListener(_Listener):
    __slots__ = ('__arenaDP', '__callbackID')

    def __init__(self):
        super(ArenaVehiclesListener, self).__init__()
        self.__arenaDP = None
        self.__callbackID = None
        return

    def start(self, arena, arenaDP = None):
        super(ArenaVehiclesListener, self).start(arena)
        if arenaDP is None:
            LOG_ERROR('Arena data provider is None')
            return
        else:
            arena = self._arena()
            self.__arenaDP = arenaDP
            self.__arenaDP.buildVehiclesData(arena.vehicles, arena.guiType)
            self.__arenaDP.buildStatsData(arena.statistics)
            arena.onNewVehicleListReceived += self.__arena_onNewVehicleListReceived
            arena.onVehicleAdded += self.__arena_onVehicleAdded
            arena.onVehicleUpdated += self.__arena_onVehicleUpdated
            arena.onVehicleKilled += self.__arena_onVehicleKilled
            arena.onAvatarReady += self.__arena_onAvatarReady
            arena.onNewStatisticsReceived += self.__arena_onNewStatisticsReceived
            arena.onVehicleStatisticsUpdate += self.__arena_onVehicleStatisticsUpdate
            arena.onTeamKiller += self.__arena_onTeamKiller
            arena.onInteractiveStats += self.__arena_onInteractiveStats
            return

    def stop(self):
        self.__clearCallback()
        if self.__arenaDP is not None:
            self.__arenaDP.clear()
            self.__arenaDP = None
        arena = super(ArenaVehiclesListener, self).stop()
        if arena is None:
            return
        else:
            arena.onNewVehicleListReceived -= self.__arena_onNewVehicleListReceived
            arena.onVehicleAdded -= self.__arena_onVehicleAdded
            arena.onVehicleUpdated -= self.__arena_onVehicleUpdated
            arena.onVehicleKilled -= self.__arena_onVehicleKilled
            arena.onAvatarReady -= self.__arena_onAvatarReady
            arena.onNewStatisticsReceived -= self.__arena_onNewStatisticsReceived
            arena.onVehicleStatisticsUpdate -= self.__arena_onVehicleStatisticsUpdate
            arena.onTeamKiller -= self.__arena_onTeamKiller
            arena.onInteractiveStats -= self.__arena_onInteractiveStats
            return

    def addController(self, battleCtx, controller):
        result = super(ArenaVehiclesListener, self).addController(battleCtx, controller)
        if result:
            if self.__isRequiredDataExists():
                if self.__callbackID is not None:
                    self.__clearCallback()
                    self._invokeListenersMethod('invalidateArenaInfo')
                else:
                    controller.invalidateArenaInfo()
            elif self.__callbackID is None:
                self.__setCallback()
        return result

    def removeController(self, controller):
        result = super(ArenaVehiclesListener, self).removeController(controller)
        if result:
            controller.setBattleCtx(None)
        return result

    def clear(self):
        while len(self._controllers):
            controller = self._controllers.pop()()
            if controller:
                controller.setBattleCtx(None)

        return

    def __arena_onNewVehicleListReceived(self):
        arena = self._arena()
        self.__arenaDP.buildVehiclesData(arena.vehicles, arena.guiType)
        self._invokeListenersMethod('invalidateVehiclesInfo', self.__arenaDP)

    def __arena_onVehicleAdded(self, vID):
        arena = self._arena()
        added, updated = self.__arenaDP.addVehicleInfo(vID, arena.vehicles[vID], arena.guiType)
        if added is not None:
            self._invokeListenersMethod('addVehicleInfo', added, self.__arenaDP)
        for flags, vo in updated:
            self._invokeListenersMethod('invalidateVehicleInfo', flags, vo, self.__arenaDP)

        return

    def __arena_onVehicleUpdated(self, vID):
        result = self.__arenaDP.updateVehicleInfo(vID, self._arena().vehicles[vID], self._arena().guiType)
        for flags, vo in result:
            self._invokeListenersMethod('invalidateVehicleInfo', flags, vo, self.__arenaDP)

    def __arena_onVehicleKilled(self, victimID, *args):
        flags, vo = self.__arenaDP.updateVehicleStatus(victimID, self._arena().vehicles[victimID])
        self._invokeListenersMethod('invalidateVehicleStatus', flags, vo, self.__arenaDP)

    def __arena_onAvatarReady(self, vID):
        flags, vo = self.__arenaDP.updateVehicleStatus(vID, self._arena().vehicles[vID])
        self._invokeListenersMethod('invalidateVehicleStatus', flags, vo, self.__arenaDP)

    def __arena_onNewStatisticsReceived(self):
        self.__arenaDP.buildStatsData(self._arena().statistics)
        self._invokeListenersMethod('invalidateStats', self.__arenaDP)

    def __arena_onVehicleStatisticsUpdate(self, vID):
        flags, vo = self.__arenaDP.updateVehicleStats(vID, self._arena().statistics[vID])
        self._invokeListenersMethod('invalidateVehicleStats', flags, vo, self.__arenaDP)

    def __arena_onTeamKiller(self, vID):
        flags, vo = self.__arenaDP.updatePlayerStatus(vID, self._arena().vehicles[vID])
        self._invokeListenersMethod('invalidatePlayerStatus', flags, vo, self.__arenaDP)

    def __arena_onInteractiveStats(self, stats):
        self.__arenaDP.updateVehicleInteractiveStats(stats)
        self._invokeListenersMethod('invalidateVehicleInteractiveStats')

    def __isRequiredDataExists(self):
        return self.__arenaDP is not None and self.__arenaDP.isRequiredDataExists()

    def __setCallback(self):
        self.__callbackID = BigWorld.callback(0.1, self.__handleCallback)

    def __clearCallback(self):
        if self.__callbackID is not None:
            BigWorld.cancelCallback(self.__callbackID)
            self.__callbackID = None
        return

    def __handleCallback(self):
        self.__callbackID = None
        if self.__isRequiredDataExists():
            self._invokeListenersMethod('invalidateArenaInfo')
        else:
            self.__setCallback()
        return


_TAGS_TO_UPDATE = {USER_TAG.FRIEND, USER_TAG.IGNORED, USER_TAG.MUTED}

class ContactsListener(_Listener):
    __slots__ = ()

    def start(self, arena, **kwargs):
        super(ContactsListener, self).start(arena)
        g_messengerEvents.users.onUsersListReceived += self.__me_onUsersListReceived
        g_messengerEvents.users.onUserActionReceived += self.__me_onUserActionReceived

    def stop(self):
        g_messengerEvents.users.onUsersListReceived -= self.__me_onUsersListReceived
        g_messengerEvents.users.onUserActionReceived -= self.__me_onUserActionReceived
        super(ContactsListener, self).stop()

    def __me_onUsersListReceived(self, tags):
        if _TAGS_TO_UPDATE & tags:
            self._invokeListenersMethod('invalidateUsersTags')

    def __me_onUserActionReceived(self, actionID, user):
        if actionID in (USER_ACTION_ID.FRIEND_ADDED,
         USER_ACTION_ID.FRIEND_REMOVED,
         USER_ACTION_ID.IGNORED_ADDED,
         USER_ACTION_ID.IGNORED_REMOVED,
         USER_ACTION_ID.MUTE_SET,
         USER_ACTION_ID.MUTE_UNSET):
            self._invokeListenersMethod('invalidateUserTags', user)


class PersonalInvitationsListener(_Listener):
    __slots__ = ('__filter', '__arenaDP')

    def __init__(self):
        super(PersonalInvitationsListener, self).__init__()
        self.__filter = SquadInvitationsFilter()
        self.__arenaDP = None
        return

    @prbInvitesProperty
    def prbInvites(self):
        return None

    def start(self, arena, arenaDP = None, **kwargs):
        super(PersonalInvitationsListener, self).start(arena)
        if arenaDP is None:
            LOG_ERROR('Arena data provider is None')
            return
        else:
            self.__filter.setArenaUniqueID(self._arena().arenaUniqueID)
            self.__arenaDP = arenaDP
            invitesManager = self.prbInvites
            invitesManager.onReceivedInviteListModified += self.__im_onReceivedInviteModified
            invitesManager.onSentInviteListModified += self.__im_onSentInviteListModified
            return

    def stop(self):
        invitesManager = self.prbInvites
        invitesManager.onReceivedInviteListModified -= self.__im_onReceivedInviteModified
        invitesManager.onSentInviteListModified -= self.__im_onSentInviteListModified
        super(PersonalInvitationsListener, self).stop()

    def addController(self, battleCtx, controller):
        result = super(PersonalInvitationsListener, self).addController(battleCtx, controller)
        if result:
            self.__updateInvitationsStatuses()
        return result

    def __updateFilteredStatuses(self, filtered):
        update = self.__arenaDP.updateInvitationStatus
        vos = []
        for dbID, status in filtered:
            flags, vo = update(dbID, status)
            if vo is not None and flags != INVALIDATE_OP.NONE:
                vos.append(vo)

        if vos:
            self._invokeListenersMethod('invalidateInvitationsStatuses', vos, self.__arenaDP)
        return

    def __updateInvitationsStatuses(self):
        update = self.__arenaDP.updateInvitationStatus
        vos = []
        for invites in self.prbInvites.getInvites(incoming=True):
            flags, vo = update(*self.__filter.addReceivedInvite(invites))
            if vo is not None and flags != INVALIDATE_OP.NONE:
                vos.append(vo)

        for invites in self.prbInvites.getInvites(incoming=False):
            flags, vo = update(*self.__filter.addSentInvite(invites))
            if vo is not None and flags != INVALIDATE_OP.NONE:
                vos.append(vo)

        if vos:
            self._invokeListenersMethod('invalidateInvitationsStatuses', vos, self.__arenaDP)
        return

    def __im_onReceivedInviteModified(self, added, changed, deleted):
        filtered = self.__filter.filterReceivedInvites(self.prbInvites.getInvite, added, changed, deleted)
        self.__updateFilteredStatuses(filtered)

    def __im_onSentInviteListModified(self, added, changed, deleted):
        filtered = self.__filter.filterSentInvites(self.prbInvites.getInvite, added, changed, deleted)
        self.__updateFilteredStatuses(filtered)


class ArenaSpaceLoadListener(_Listener):
    MAX_PROGRESS_VALUE = 1.0
    SPACE_INVALIDATION_PERIOD = 0.5
    INFLUX_INVALIDATION_PERIOD = 0.5

    def __init__(self):
        super(ArenaSpaceLoadListener, self).__init__()
        self.__progress = 0.0
        self.__spaceLoadCB = None
        self.__influxDrawCB = None
        return

    def start(self, arena, **kwargs):
        super(ArenaSpaceLoadListener, self).start(arena)
        self.__onSpaceLoadStarted()
        self.__loadSpaceCallback()

    def stop(self):
        self.__clearSpaceCallback()
        self.__clearInfluxCallback()
        super(ArenaSpaceLoadListener, self).stop()

    def __loadSpaceCallback(self):
        self.__clearSpaceCallback()
        progress = 1.0
        import BattleReplay
        if not BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            progress = BigWorld.spaceLoadStatus()
        if progress > self.__progress:
            self.__progress = progress
            self.__onSpaceLoadUpdated(progress)
        if progress < self.MAX_PROGRESS_VALUE:
            self.__spaceLoadCB = BigWorld.callback(self.SPACE_INVALIDATION_PERIOD, self.__loadSpaceCallback)
            BigWorld.SetDrawInflux(False)
        else:
            self.__onSpaceLoadCompleted()
            BigWorld.SetDrawInflux(True)
            self.__loadInfluxCallback()

    def __loadInfluxCallback(self):
        self.__clearInfluxCallback()
        if BigWorld.worldDrawEnabled():
            self.__onArenaLoadCompleted()
        else:
            self.__influxDrawCB = BigWorld.callback(self.SPACE_INVALIDATION_PERIOD, self.__loadInfluxCallback)

    def __clearSpaceCallback(self):
        if self.__spaceLoadCB is not None:
            BigWorld.cancelCallback(self.__spaceLoadCB)
            self.__spaceLoadCB = None
        return

    def __clearInfluxCallback(self):
        if self.__influxDrawCB is not None:
            BigWorld.cancelCallback(self.__influxDrawCB)
            self.__influxDrawCB = None
        return

    def __onSpaceLoadUpdated(self, progress):
        self._invokeListenersMethod('updateSpaceLoadProgress', progress)

    def __onSpaceLoadStarted(self):
        self._invokeListenersMethod('spaceLoadStarted')

    def __onSpaceLoadCompleted(self):
        self._invokeListenersMethod('spaceLoadCompleted')

    def __onArenaLoadCompleted(self):
        self._invokeListenersMethod('arenaLoadCompleted')


class ArenaTeamBasesListener(_Listener):
    __slots__ = ('__baseIDs', '__points')

    def __init__(self):
        super(ArenaTeamBasesListener, self).__init__()

    def start(self, arena, **kwargs):
        super(ArenaTeamBasesListener, self).start(arena, **kwargs)
        arena = self._arena()
        arena.onTeamBasePointsUpdate += self.__arena_onTeamBasePointsUpdate
        arena.onTeamBaseCaptured += self.__arena_onTeamBaseCaptured
        arena.onPeriodChange += self.__arena_onPeriodChange

    def stop(self):
        arena = super(ArenaTeamBasesListener, self).stop()
        if arena is None:
            return
        else:
            arena.onTeamBasePointsUpdate -= self.__arena_onTeamBasePointsUpdate
            arena.onTeamBaseCaptured -= self.__arena_onTeamBaseCaptured
            arena.onPeriodChange -= self.__arena_onPeriodChange
            return

    def __arena_onTeamBasePointsUpdate(self, team, baseID, points, timeLeft, invadersCnt, capturingStopped):
        self._invokeListenersMethod('invalidateTeamBasePoints', team, baseID, points, timeLeft, invadersCnt, capturingStopped)

    def __arena_onTeamBaseCaptured(self, team, baseID):
        self._invokeListenersMethod('invalidateTeamBaseCaptured', team, baseID)

    def __arena_onPeriodChange(self, period, *args):
        if period == ARENA_PERIOD.AFTERBATTLE:
            self._invokeListenersMethod('removeTeamsBases')


class ArenaPeriodListener(_Listener):

    def __init__(self):
        super(ArenaPeriodListener, self).__init__()
        self._dataProvider = None
        return

    def start(self, arena, arenaDP = None):
        super(ArenaPeriodListener, self).start(arena)
        self._dataProvider = arenaDP
        self.__setPeriodInfo(controller=None)
        arena = self._arena()
        arena.onPeriodChange += self.__arena_onPeriodChange
        return

    def stop(self):
        arena = super(ArenaPeriodListener, self).stop()
        self._dataProvider = None
        if arena is None:
            return
        else:
            arena.onPeriodChange -= self.__arena_onPeriodChange
            return

    def addController(self, battleCtx, controller):
        result = super(ArenaPeriodListener, self).addController(battleCtx, controller)
        if result:
            self.__setPeriodInfo(controller)
        return result

    def __setPeriodInfo(self, controller = None):
        arena = self._arena()
        if arena is not None and self._dataProvider is not None:
            periodAddInfo = _getPeriodAdditionalInfo(self._dataProvider, arena.period, arena.periodAdditionalInfo)
            if controller is not None:
                controller.setPeriodInfo(arena.period, arena.periodEndTime, arena.periodLength, periodAddInfo, arena.arenaType.battleCountdownTimerSound)
            else:
                self._invokeListenersMethod('setPeriodInfo', arena.period, arena.periodEndTime, arena.periodLength, periodAddInfo, arena.arenaType.battleCountdownTimerSound)
        return

    def __arena_onPeriodChange(self, period, endTime, length, additionalInfo):
        self._invokeListenersMethod('invalidatePeriodInfo', period, endTime, length, _getPeriodAdditionalInfo(self._dataProvider, period, additionalInfo))


class ArenaRespawnListener(_Listener):

    def start(self, arena, **kwargs):
        super(ArenaRespawnListener, self).start(arena, **kwargs)
        arena = self._arena()
        arena.onRespawnAvailableVehicles += self.__arena_onRespawnAvailableVehicles
        arena.onRespawnCooldowns += self.__arena_onRespawnCooldowns
        arena.onRespawnRandomVehicle += self.__arena_onRespawnRandomVehicle
        arena.onRespawnResurrected += self.__arena_onRespawnResurrected

    def stop(self):
        arena = super(ArenaRespawnListener, self).stop()
        if arena is None:
            return
        else:
            arena.onRespawnAvailableVehicles -= self.__arena_onRespawnAvailableVehicles
            arena.onRespawnCooldowns -= self.__arena_onRespawnCooldowns
            arena.onRespawnRandomVehicle -= self.__arena_onRespawnRandomVehicle
            arena.onRespawnResurrected -= self.__arena_onRespawnResurrected
            return

    def __arena_onRespawnAvailableVehicles(self, vehsList):
        self._invokeListenersMethod('updateRespawnVehicles', vehsList)

    def __arena_onRespawnCooldowns(self, cooldowns):
        self._invokeListenersMethod('updateRespawnCooldowns', cooldowns)

    def __arena_onRespawnRandomVehicle(self, respawnInfo):
        self._invokeListenersMethod('updateRespawnInfo', respawnInfo)

    def __arena_onRespawnResurrected(self, respawnInfo):
        self._invokeListenersMethod('updateRespawnRessurectedInfo', respawnInfo)


class PositionsListener(_Listener):
    __slots__ = ('__arenaDP',)

    def __init__(self):
        super(PositionsListener, self).__init__()
        self.__arenaDP = None
        return

    def start(self, arena, arenaDP = None, **kwargs):
        super(PositionsListener, self).start(arena, **kwargs)
        arena = self._arena()
        arena.onPositionsUpdated += self.__arena_onPositionsUpdated
        self.__arenaDP = arenaDP

    def stop(self):
        self.__arenaDP = None
        arena = super(PositionsListener, self).stop()
        if arena is None:
            return
        else:
            arena.onPositionsUpdated -= self.__arena_onPositionsUpdated
            return

    def __arena_onPositionsUpdated(self):
        positions = self._arena().positions
        if self.__arenaDP:
            getter = self.__arenaDP.getVehicleInfo
        else:

            def getter(_):
                return None

        def _iterator():
            for vehicleID, position in positions.iteritems():
                yield (getter(vehicleID), position)

        self._invokeListenersMethod('updatePositions', _iterator)


class ListenersCollection(_Listener):
    __slots__ = ('__vehicles', '__teamsBases', '__loader', '__contacts', '__period', '__respawn', '__invitations', '__positions')

    def __init__(self):
        super(ListenersCollection, self).__init__()
        self.__vehicles = ArenaVehiclesListener()
        self.__teamsBases = ArenaTeamBasesListener()
        self.__contacts = ContactsListener()
        self.__loader = ArenaSpaceLoadListener()
        self.__period = ArenaPeriodListener()
        self.__respawn = ArenaRespawnListener()
        self.__invitations = PersonalInvitationsListener()
        self.__positions = PositionsListener()

    def addController(self, battleCtx, controller):
        result = False
        try:
            scope = controller.getCtrlScope()
        except AttributeError:
            LOG_ERROR('Controller is not valid', controller)
            return False

        if scope & _SCOPE.LOAD > 0:
            result |= self.__loader.addController(battleCtx, controller)
        if scope & _SCOPE.VEHICLES > 0:
            result |= self.__vehicles.addController(battleCtx, controller)
            result |= self.__contacts.addController(battleCtx, controller)
        if scope & _SCOPE.PERIOD > 0:
            result |= self.__period.addController(battleCtx, controller)
        if scope & _SCOPE.TEAMS_BASES > 0:
            result |= self.__teamsBases.addController(battleCtx, controller)
        if scope & _SCOPE.RESPAWN > 0:
            result |= self.__respawn.addController(battleCtx, controller)
        if scope & _SCOPE.INVITATIONS > 0:
            result |= self.__invitations.addController(battleCtx, controller)
        if scope & _SCOPE.POSITIONS > 0:
            result |= self.__positions.addController(battleCtx, controller)
        return result

    def removeController(self, controller):
        result = self.__vehicles.removeController(controller)
        result |= self.__teamsBases.removeController(controller)
        result |= self.__contacts.removeController(controller)
        result |= self.__loader.removeController(controller)
        result |= self.__period.removeController(controller)
        result |= self.__respawn.removeController(controller)
        result |= self.__invitations.removeController(controller)
        result |= self.__positions.removeController(controller)
        return result

    def start(self, arena, **kwargs):
        if arena is None:
            LOG_NOTE('ClientArena is not found')
            return
        else:
            ref = weakref.ref(arena)
            self.__vehicles.start(ref, **kwargs)
            self.__teamsBases.start(ref, **kwargs)
            self.__contacts.start(ref, **kwargs)
            self.__loader.start(ref, **kwargs)
            self.__period.start(ref, **kwargs)
            self.__respawn.start(ref, **kwargs)
            self.__invitations.start(ref, **kwargs)
            self.__positions.start(ref, **kwargs)
            return

    def stop(self):
        self.__vehicles.stop()
        self.__teamsBases.stop()
        self.__contacts.stop()
        self.__loader.stop()
        self.__period.stop()
        self.__respawn.stop()
        self.__invitations.stop()
        self.__positions.stop()

    def clear(self):
        self.__vehicles.clear()
        self.__teamsBases.clear()
        self.__contacts.clear()
        self.__loader.clear()
        self.__period.clear()
        self.__respawn.clear()
        self.__invitations.clear()
        self.__positions.clear()