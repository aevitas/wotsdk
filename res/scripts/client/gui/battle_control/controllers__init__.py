# Embedded file name: scripts/client/gui/battle_control/controllers/__init__.py
from gui.battle_control.controllers.repositories import BattleSessionSetup
from gui.battle_control.controllers.repositories import SharedControllersLocator
from gui.battle_control.controllers.repositories import DynamicControllersLocator
from gui.battle_control.controllers.repositories import ClassicControllersRepository
from gui.battle_control.controllers.repositories import FalloutControllersRepository
from gui.battle_control.controllers.repositories import SharedControllersRepository
__all__ = ('createShared', 'createDynamic', 'BattleSessionSetup', 'SharedControllersLocator', 'DynamicControllersLocator')

def createShared(setup):
    raise isinstance(setup, BattleSessionSetup) or AssertionError
    return SharedControllersLocator(SharedControllersRepository.create(setup))


def createDynamic(setup):
    if not isinstance(setup, BattleSessionSetup):
        raise AssertionError
        guiVisitor = setup.arenaVisitor.gui
        repository = guiVisitor.isFalloutBattle() and FalloutControllersRepository.create(setup)
    elif not guiVisitor.isTutorialBattle():
        repository = ClassicControllersRepository.create(setup)
    else:
        repository = None
    return DynamicControllersLocator(repository=repository)