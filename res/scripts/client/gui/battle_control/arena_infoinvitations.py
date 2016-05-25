# Embedded file name: scripts/client/gui/battle_control/arena_info/invitations.py
from adisp import process
from constants import PREBATTLE_TYPE, INVITATION_TYPE
from gui.battle_control.arena_info.settings import INVITATION_DELIVERY_STATUS
from gui.battle_control.requests.context import SendInvitesCtx
from gui.prb_control.prb_helpers import prbInvitesProperty
from unit_roster_config import SquadRoster
_DELIVERY_STATUS = INVITATION_DELIVERY_STATUS

class SquadInvitationsFilter(object):
    __slots__ = ('__arenaUniqueID', '__isReceivingProhibited', '__isSendingProhibited', '__received', '__sent')

    def __init__(self):
        super(SquadInvitationsFilter, self).__init__()
        self.__arenaUniqueID = 0
        self.__isReceivingProhibited = False
        self.__isSendingProhibited = False
        self.__received = {}
        self.__sent = {}

    def setArenaUniqueID(self, arenaUniqueID):
        self.__arenaUniqueID = arenaUniqueID

    def isReceivingProhibited(self):
        return self.__isReceivingProhibited

    def isSendingProhibited(self):
        return self.__isSendingProhibited

    def updatePersonalInfo(self, arenaDP):
        vInfoVO = arenaDP.getVehicleInfo()
        playerInfo = vInfoVO.player
        self.__isReceivingProhibited = playerInfo.forbidInBattleInvitations
        self.__isSendingProhibited = False
        if vInfoVO.isInSquad():
            if playerInfo.isPrebattleCreator:
                count = arenaDP.getVehiclesCountInPrebattle(vInfoVO.team, vInfoVO.prebattleID)
                self.__isSendingProhibited = count >= SquadRoster.MAX_SLOTS
            else:
                self.__isSendingProhibited = True

    def addReceivedInvite(self, invite):
        if not self.__isInviteValid(invite):
            return (0, _DELIVERY_STATUS.NONE)
        self.__received[invite.creatorDBID] = invite.clientID
        return (invite.creatorDBID, _DELIVERY_STATUS.RECEIVED_FROM)

    def addSentInvite(self, invite):
        if not self.__isInviteValid(invite):
            return (0, _DELIVERY_STATUS.NONE)
        self.__sent[invite.receiverDBID] = invite.clientID
        return (invite.receiverDBID, _DELIVERY_STATUS.RECEIVED_FROM)

    def filterReceivedInvites(self, getter, added, changed, deleted):
        for clientID in added:
            invite = getter(clientID)
            if invite is None:
                continue
            if not self.__isInviteValid(invite):
                continue
            self.__received[invite.creatorDBID] = invite.clientID
            yield (invite.creatorDBID, _DELIVERY_STATUS.RECEIVED_FROM)

        for clientID in changed:
            invite = getter(clientID)
            if invite is None:
                continue
            if not self.__isInviteValid(invite) and self.__received.pop(invite.creatorDBID, None) is not None:
                yield (invite.creatorDBID, _DELIVERY_STATUS.INACTIVE)

        inverted = dict(zip(self.__received.values(), self.__received.keys()))
        for clientID in deleted:
            if clientID not in inverted:
                continue
            accountDBID = inverted[clientID]
            if self.__received.pop(accountDBID, None) is not None:
                yield (accountDBID, _DELIVERY_STATUS.INACTIVE)

        return

    def filterSentInvites(self, getter, added, changed, deleted):
        for clientID in added:
            invite = getter(clientID)
            if invite is None:
                continue
            if not self.__isInviteValid(invite):
                continue
            self.__sent[invite.receiverDBID] = invite.clientID
            yield (invite.receiverDBID, _DELIVERY_STATUS.SENT_TO)

        for clientID in changed:
            invite = getter(clientID)
            if invite is None:
                continue
            if not self.__isInviteValid(invite) and self.__sent.pop(invite.receiverDBID, None) is not None:
                yield (invite.receiverDBID, _DELIVERY_STATUS.INACTIVE)

        inverted = dict(zip(self.__sent.values(), self.__sent.keys()))
        for clientID in deleted:
            if clientID not in inverted:
                continue
            accountDBID = inverted[clientID]
            if self.__sent.pop(accountDBID, None) is not None:
                yield (accountDBID, _DELIVERY_STATUS.INACTIVE)

        return

    def __isInviteValid(self, invite):
        if invite.type != PREBATTLE_TYPE.SQUAD:
            return False
        if not invite.isSameBattle(self.__arenaUniqueID):
            return False
        if not invite.isActive():
            return False
        return True


class SquadInvitationsHandler(object):
    __slots__ = ()

    @prbInvitesProperty
    def prbInvites(self):
        return None

    def send(self, playerID):
        self.__onSendInviteToSquad(playerID)

    def accept(self, playerID):
        inviteID = self.__getInviteID(playerID, True, True)
        if inviteID is not None:
            self.prbInvites.acceptInvite(inviteID)
        return

    def reject(self, playerID):
        inviteID = self.__getInviteID(playerID, True, True)
        if inviteID is not None:
            self.prbInvites.declineInvite(inviteID)
        return

    @process
    def __onSendInviteToSquad(self, playerID):
        from gui.battle_control import g_sessionProvider
        yield g_sessionProvider.sendRequest(SendInvitesCtx(databaseIDs=(playerID,)))

    def __getInviteID(self, playerID, isCreator, incomingInvites):
        invites = self.prbInvites.getInvites(incoming=incomingInvites, onlyActive=True)
        if isCreator:
            getter = lambda i: i.creatorDBID
        else:
            getter = lambda i: i.receiverDBID
        for invite in invites:
            if invite.type == INVITATION_TYPE.SQUAD and getter(invite) == playerID:
                return invite.clientID

        return None