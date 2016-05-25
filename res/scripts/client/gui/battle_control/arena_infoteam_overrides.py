# Embedded file name: scripts/client/gui/battle_control/arena_info/team_overrides.py
from account_helpers.settings_core import g_settingsCore
from account_helpers.settings_core.settings_constants import SOUND
from constants import IS_CHINA
from gui.battle_control import avatar_getter, arena_info
from gui.battle_control.arena_info.arena_vos import VehicleActions
from gui.battle_control.arena_info.settings import PLAYER_STATUS
from gui.battle_control.arena_info.settings import INVITATION_DELIVERY_STATUS

class DefaultTeamOverrides(object):
    __slots__ = ('team', 'personal', 'prebattleID', 'isReplayPlaying')

    def __init__(self, team, personal, prebattleID = 0, isReplayPlaying = False):
        super(DefaultTeamOverrides, self).__init__()
        self.team = team
        self.personal = personal
        self.prebattleID = prebattleID
        self.isReplayPlaying = isReplayPlaying

    def isPlayerSelected(self, vo):
        return False

    def isPersonalSquad(self, vo):
        return False

    def isTeamKiller(self, vo):
        return False

    def getAction(self, vo):
        return VehicleActions.getBitMask(vo.events)

    def getPlayerStatus(self, vo):
        playerStatus = PLAYER_STATUS.DEFAULT
        if vo.isActionsDisabled() or self.isReplayPlaying:
            playerStatus |= PLAYER_STATUS.IS_ACTION_DISABLED
        if vo.isSquadMan():
            playerStatus |= PLAYER_STATUS.IS_SQUAD_MAN
            if self.isPersonalSquad(vo):
                playerStatus |= PLAYER_STATUS.IS_SQUAD_PERSONAL
        if self.isTeamKiller(vo):
            playerStatus |= PLAYER_STATUS.IS_TEAM_KILLER
        if self.isPlayerSelected(vo) and not self.personal.isOtherSelected() or self.isPostmortemView(vo):
            playerStatus |= PLAYER_STATUS.IS_PLAYER_SELECTED
        return playerStatus

    def isPostmortemView(self, vo):
        return vo.vehicleID == self.personal.selectedID

    def getInvitationDeliveryStatus(self, vo):
        return INVITATION_DELIVERY_STATUS.FORBIDDEN

    def getColorScheme(self):
        return 'vm_enemy'

    def clear(self):
        self.personal = None
        return


class PlayerTeamOverrides(DefaultTeamOverrides):
    __slots__ = ()

    def isPlayerSelected(self, vo):
        return vo.vehicleID == self.personal.vehicleID

    def isPersonalSquad(self, vo):
        return vo.isSquadMan(prebattleID=self.prebattleID)

    def isTeamKiller(self, vo):
        if self.isPlayerSelected(vo):
            return self.personal.teamKillSuspected or vo.isTeamKiller(playerTeam=self.team)
        return vo.isTeamKiller(playerTeam=self.team)

    def getAction(self, vo):
        return 0

    def getPlayerStatus(self, vo):
        status = super(PlayerTeamOverrides, self).getPlayerStatus(vo)
        if self.personal.vehicleID == vo.vehicleID and vo.isSquadMan() and arena_info.isRandomBattle() and not g_settingsCore.getSetting(SOUND.VOIP_ENABLE) and not IS_CHINA:
            status |= PLAYER_STATUS.IS_VOIP_DISABLED
        return status

    def getInvitationDeliveryStatus(self, vo):
        return vo.invitationDeliveryStatus

    def getColorScheme(self):
        return 'vm_ally'


class PersonalInfo(object):
    __slots__ = ('vehicleID', 'selectedID', 'teamKillSuspected')

    def __init__(self):
        super(PersonalInfo, self).__init__()
        self.vehicleID = avatar_getter.getPlayerVehicleID()
        self.selectedID = self.vehicleID
        self.teamKillSuspected = arena_info.isPlayerTeamKillSuspected()

    def changeSelected(self, selectedID):
        previousID, self.selectedID = self.selectedID, selectedID
        return previousID

    def isOtherSelected(self):
        return self.vehicleID != self.selectedID


def makeOverrides(isEnemy, team, personal, prebattleID = 0, isReplayPlaying = False):
    if isEnemy:
        ctx = DefaultTeamOverrides(team, personal, isReplayPlaying=isReplayPlaying)
    else:
        ctx = PlayerTeamOverrides(team, personal, prebattleID=prebattleID, isReplayPlaying=isReplayPlaying)
    return ctx