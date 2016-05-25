# Embedded file name: scripts/client/gui/battle_control/arena_info/__init__.py
import BigWorld
import constants
from gui import GUI_SETTINGS
from constants import ARENA_BONUS_TYPE_CAPS as caps
from debug_utils import LOG_WARNING

def getClientArena(avatar = None):
    if avatar is None:
        avatar = BigWorld.player()
    try:
        arena = avatar.arena
    except AttributeError:
        arena = None

    return arena


def getArenaType(avatar = None):
    return getattr(getClientArena(avatar), 'arenaType', None)


def getArenaTypeID(avatar = None):
    if avatar is None:
        avatar = BigWorld.player()
    try:
        arenaTypeID = avatar.arenaTypeID
    except AttributeError:
        arenaTypeID = 0

    return arenaTypeID


def getPlayerVehicleID():
    return getattr(BigWorld.player(), 'playerVehicleID', 0)


def isPlayerTeamKillSuspected():
    return bool(getattr(BigWorld.player(), 'tkillIsSuspected', 0))


def getArenaGuiType(arena = None):
    if arena is None:
        arena = getClientArena()
    return getattr(arena, 'guiType', constants.ARENA_GUI_TYPE.UNKNOWN)


def getArenaBonusType():
    return getattr(getClientArena(), 'bonusType', constants.ARENA_BONUS_TYPE.UNKNOWN)


def battleEndWarningEnabled():
    return GUI_SETTINGS.battleEndWarningEnabled and getArenaBonusType() != constants.ARENA_BONUS_TYPE.TUTORIAL


def getArenaGuiTypeLabel():
    arenaGuiType = getArenaGuiType()
    if arenaGuiType in constants.ARENA_GUI_TYPE_LABEL.LABELS:
        label = constants.ARENA_GUI_TYPE_LABEL.LABELS[arenaGuiType]
    else:
        label = ''
    return label


def isLowLevelBattle(arena = None):
    if arena is None:
        arena = getClientArena()
    if arena is not None:
        return 0 < arena.extraData.get('battleLevel') < 4
    else:
        return False
        return


def isRandomBattle(arena = None):
    return getArenaGuiType(arena=arena) == constants.ARENA_GUI_TYPE.RANDOM


def isEventBattle(arena = None):
    return getArenaGuiType(arena=arena) == constants.ARENA_GUI_TYPE.EVENT_BATTLES


def isFalloutBattle(arena = None):
    return getArenaGuiType(arena=arena) in constants.ARENA_GUI_TYPE.FALLOUT_RANGE


def isFalloutClassic(arena = None):
    return getArenaGuiType(arena=arena) == constants.ARENA_GUI_TYPE.FALLOUT_CLASSIC


def isFalloutMultiTeam(arena = None):
    return getArenaGuiType(arena=arena) == constants.ARENA_GUI_TYPE.FALLOUT_MULTITEAM


def isInSandboxBattle(arena = None):
    return getArenaGuiType(arena=arena) in constants.ARENA_GUI_TYPE.SANDBOX_RANGE


def makeClientTeamBaseID(team, baseID):
    if baseID is None:
        baseID = 0
    return (int(baseID) << 6) + team


def parseClientTeamBaseID(clientID):
    team = clientID & 63
    return (team, clientID >> 6)


def isArenaNotStarted():
    arena = getClientArena()
    result = False
    if arena is not None:
        try:
            result = arena.period in (constants.ARENA_PERIOD.WAITING, constants.ARENA_PERIOD.PREBATTLE)
        except AttributeError:
            pass

    return result


def isArenaInWaiting():
    arena = getClientArena()
    return arena is not None and arena.period == constants.ARENA_PERIOD.WAITING


def getArenaIconKey(arenaType = None, arenaGuiType = None):
    if arenaType is None:
        arena = getClientArena()
        if arena is None:
            return ''
        arenaType = arena.arenaType
    arenaGuiType = arenaGuiType or getArenaGuiType()
    arenaIcon = arenaType.geometryName
    if arenaGuiType in constants.ARENA_GUI_TYPE.FALLOUT_RANGE:
        return '%s_fallout' % arenaIcon
    else:
        return arenaIcon


def getArenaIcon(iconKey, arenaType = None, arenaGuiType = None):
    return iconKey % getArenaIconKey(arenaType, arenaGuiType)


def hasFlags(arenaType = None, arenBonusType = None):
    if arenaType is None:
        arenaType = getArenaType()
    if arenBonusType is None:
        arenBonusType = getArenaBonusType()
    if arenaType is not None and arenBonusType is not None:
        return caps.get(arenBonusType) & caps.FLAG_MECHANICS > 0 and arenaType.flagSpawnPoints
    else:
        return False


def hasResourcePoints(arenaType = None, arenBonusType = None):
    if arenaType is None:
        arenaType = getArenaType()
    if arenBonusType is None:
        arenBonusType = getArenaBonusType()
    if arenaType is not None and arenBonusType is not None:
        return caps.get(arenBonusType) & caps.RESOURCE_POINTS > 0 and arenaType.resourcePoints
    else:
        return False


def hasRepairPoints(arenaType = None, arenBonusType = None):
    if arenaType is None:
        arenaType = getArenaType()
    if arenBonusType is None:
        arenBonusType = getArenaBonusType()
    if arenaType is not None and arenBonusType is not None:
        return caps.get(arenBonusType) & caps.REPAIR_MECHANICS > 0 and arenaType.repairPoints
    else:
        return False


def hasRespawns(arenBonusType = None):
    if arenBonusType is None:
        arenBonusType = getArenaBonusType()
    if arenBonusType is not None:
        return caps.get(arenBonusType) & caps.RESPAWN > 0
    else:
        return False


def hasRage(arenBonusType = None):
    if arenBonusType is None:
        arenBonusType = getArenaBonusType()
    if arenBonusType is not None:
        return caps.get(arenBonusType) & caps.RAGE_MECHANICS > 0
    else:
        return False


def hasGasAttack(arenBonusType = None):
    if arenBonusType is None:
        arenBonusType = getArenaBonusType()
    if arenBonusType is not None:
        return caps.get(arenBonusType) & caps.GAS_ATTACK_MECHANICS > 0 and isFalloutMultiTeam()
    else:
        return False


def getGasAttackSettings():
    if hasGasAttack():
        return getArenaType().gasAttackSettings
    else:
        return None


def getArenaVehicleExtras(vehicleID, avatar = None):
    extras = None
    arena = getClientArena(avatar=avatar)
    if arena is not None:
        try:
            extras = arena.vehicles[vehicleID]['vehicleType'].extras[:]
        except (KeyError, AttributeError):
            pass

    return extras


def getMaxTeamsOnArena(avatar = None, arenaType = None):
    if arenaType is None:
        arenaType = getArenaType(avatar=avatar)
    try:
        return arenaType.maxTeamsInArena
    except AttributeError:
        LOG_WARNING('Attribute "arenaType" or "maxTeamsInArena" is not found')

    return constants.TEAMS_IN_ARENA.MIN_TEAMS


def getTeamSpawnPoints(team, arena = None):
    if arena is None:
        arenaType = getArenaType()
    else:
        arenaType = arena.arenaType
    other = team - 1
    if isLowLevelBattle(arena) and other in arenaType.teamLowLevelSpawnPoints and len(arenaType.teamLowLevelSpawnPoints[other]):
        spawnPoints = arenaType.teamLowLevelSpawnPoints
    else:
        spawnPoints = arenaType.teamSpawnPoints or []
    for team, points in enumerate(spawnPoints, 1):
        for spawn, point in enumerate(points, 1):
            if len(points) > 1:
                number = spawn + 1
            else:
                number = 1
            yield (team, (point[0], 0, point[1]), number)

    return


def getTeamBasePositions(arena = None):
    if arena is None:
        arenaType = getArenaType()
    else:
        arenaType = arena.arenaType
    positions = arenaType.teamBasePositions or [] if arenaType else []
    for team, teamBasePoints in enumerate(positions, 1):
        for index, (base, point) in enumerate(teamBasePoints.items(), 1):
            if len(teamBasePoints) > 1:
                number = index
            else:
                number = 1
            yield (team, (point[0], 0, point[1]), number)

    return


def getControlPoints(arena = None):
    if arena is None:
        arenaType = getArenaType()
    else:
        arenaType = arena.arenaType
    controlPoints = arenaType.controlPoints or []
    for index, point in enumerate(controlPoints, 2):
        if len(controlPoints) > 1:
            number = index
        else:
            number = 1
        yield ((point[0], 0, point[1]), number)

    return


def getArenaPositions(arena = None):
    if arena is None:
        arena = getClientArena()
    try:
        positions = arena.positions
    except AttributeError:
        positions = {}

    return positions