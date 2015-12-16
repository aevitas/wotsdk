# Embedded file name: scripts/client/tutorial/gui/Scaleform/TutorialLayout.py
import GUI, weakref
from debug_utils import LOG_DEBUG, LOG_CURRENT_EXCEPTION, LOG_ERROR, LOG_WARNING
from gui import WindowsManager, SystemMessages
from gui.Scaleform.CommandArgsParser import CommandArgsParser
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.windows import UIInterface
from tutorial.gui import GUIProxy, GUIEvent
from tutorial.gui.Scaleform.TutorialConfig import TutorialConfig
from tutorial.gui.Scaleform.TutorialDispatcher import TutorialDispatcher

class TutorialLayout(GUIProxy, UIInterface):

    def __init__(self):
        super(TutorialLayout, self).__init__()
        self.config = TutorialConfig()
        self._guiRef = None
        self._dispatcherRef = None
        return

    def __del__(self):
        LOG_DEBUG('TutorialLayout deleted')

    def populateUI(self, proxy):
        super(TutorialLayout, self).populateUI(proxy)
        self.uiHolder.addFsCallbacks({'Tutorial.MouseClicked': self.__dispatchMouseClickEvent})
        self.uiHolder.addExternalCallbacks({'Loader.LoadStart': self.__dispatchPageChangingEvent,
         'Tutorial.GetScreenSize': self.__onGetScreenSize})

    def dispossessUI(self):
        self.uiHolder.removeFsCallbacks('Tutorial.MouseClicked')
        self.uiHolder.removeExternalCallback('Loader.LoadStart', function=self.__dispatchPageChangingEvent)
        self.uiHolder.removeExternalCallback('Tutorial.GetScreenSize')
        super(TutorialLayout, self).dispossessUI()

    def init(self):
        try:
            window = WindowsManager.g_windowsManager.window
            self._guiRef = weakref.ref(window)
            proxy = window.proxy
            dispatcher = window.tutorialDispatcher
            if dispatcher is None:
                dispatcher = TutorialDispatcher()
                dispatcher.populateUI(proxy)
                window.tutorialDispatcher = dispatcher
            self._dispatcherRef = weakref.ref(dispatcher)
        except AttributeError:
            LOG_CURRENT_EXCEPTION()
            return False

        self.populateUI(proxy)
        try:
            movie = self.uiHolder.movie
            movie.invoke(('_root.tutorialLoader.loadTutorial', ['TutorialLayout.swf']))
            LOG_DEBUG("load 'TutorialLayout.swf'")
            self.setTrainingRunMode()
            self.call('common.closeAllWindows')
        except Exception:
            LOG_CURRENT_EXCEPTION()
            return False

        return True

    def clear(self):
        if self._guiRef is not None and self._guiRef() is not None:
            self.clearChapterInfo()
            self.call('Tutorial.Effects.Stop')
            self.call('Tutorial.Areas.Destroy', [False, True])
            self.call('Tutorial.Items.ResetAll')
            self.call('common.closeAllWindows')
        return

    def fini(self):
        self.eManager.clear()
        if self._guiRef is None or self._guiRef() is None:
            return
        else:
            try:
                self.call('common.closeAllWindows')
                movie = self.uiHolder.movie
                movie.invoke(('_root.tutorialLoader.unloadTutorial', []))
                LOG_DEBUG("unload 'TutorialLayout.swf'")
            except Exception:
                LOG_CURRENT_EXCEPTION()
                return False

            self.dispossessUI()
            return

    def loadConfig(self, filePath):
        self.config.loadConfig(filePath)

    def reloadConfig(self, filePath):
        self.config.reloadConfig(filePath)

    def updateLockedAreas(self, areas):
        getter = self.config.getArea
        args = []
        for area in areas:
            areaID = area.getID()
            props = getter(areaID)
            if props['path'] is None:
                LOG_ERROR('TUTORIAL. Target path for locked area not found ', areaID)
                continue
            args.extend([areaID,
             props['path'],
             props['lockedSymbol'],
             props['position'][0],
             props['position'][1],
             props['size'][0],
             props['size'][1],
             props['changeSize'],
             props['lockedPopUp']])

        self.call('Tutorial.LockedAreas.Update', args)
        return

    def updateActiveAreas(self, areas):
        areaGetter = self.config.getArea
        itemGetter = self.config.getItem
        args = []
        for area in areas:
            areaID = area.getID()
            props = areaGetter(area.getID())
            path = props['path']
            targetID = props['targetID']
            if path is None or targetID is None:
                targetID = area.getTargetID()
                item = itemGetter(targetID)
                if item is not None:
                    path = item['path']
                else:
                    LOG_ERROR('TUTORIAL. Target path for active area not found', areaID)
                    continue
            if targetID is None or path is None:
                LOG_WARNING('TUTORIAL. Target path or ID for active area not found', areaID, targetID, path)
                continue
            action = area.getAction(targetID)
            if action is not None:
                actionType = action.getType()
            else:
                actionType = 0
            args.extend([areaID,
             targetID,
             path,
             props['position'][0],
             props['position'][1],
             props['size'][0],
             props['size'][1],
             area.isUseMask(),
             area.getHideMaskMode(),
             props['changeSize'],
             actionType])

        self.call('Tutorial.ActiveAreas.Update', args)
        return

    def getSceneID(self):
        result = None
        if not Waiting.isVisible():
            guiPage = self.uiHolder.currentInterface
            result = self.config.getSceneID(guiPage)
        return result

    def goToScene(self, sceneID):
        method = self.config.getGoToSceneMethod(sceneID)
        if method is not None:
            self.uiHolder.movie.invoke((method,))
        return

    def playEffect(self, effectName, args, itemRef = None, containerRef = None):
        if itemRef is not None:
            item = self.config.getItem(itemRef)
            if item is None:
                LOG_ERROR('TUTORIAL. GUI Item not found', effectName, itemRef)
                return
            if args is None:
                args = []
            args.append(item['path'])
        if containerRef is not None:
            container = self.config.getItem(containerRef)
            if container is None:
                LOG_ERROR('TUTORIAL. GUI Item not found', effectName, containerRef)
                return
            if args is None:
                args = []
            args.append(container['path'])
        self.call('Tutorial.Effects.{0:>s}.Play'.format(effectName), args)
        return

    def stopEffect(self, effectName, effectID):
        self.call('Tutorial.Effects.{0:>s}.Stop'.format(effectName), [effectID])

    def showWaiting(self, messageID, isSingle = False):
        Waiting.show('tutorial-{0:>s}'.format(messageID), isSingle=isSingle)

    def hideWaiting(self, messageID):
        if Waiting.isVisible():
            Waiting.hide('tutorial-{0:>s}'.format(messageID))

    def showErrorMessage(self, key, *args, **kwargs):
        kwargs['type'] = SystemMessages.SM_TYPE.Error
        SystemMessages.g_instance.pushI18nMessage(key, *args, **kwargs)

    def setItemProps(self, itemRef, props, revert = False):
        item = self.config.getItem(itemRef)
        if item is None:
            LOG_ERROR('TUTORIAL. GUI Item not found', itemRef)
            return
        else:
            args = [itemRef, item['path'], revert]
            for name, value in props.iteritems():
                args.extend([name, value])

            self.call('Tutorial.Items.SetProps', args)
            return

    def isGuiDialogDisplayed(self):
        result = False
        try:
            result = self.uiHolder.movie.invoke(('_root.tutorialLoader.isGuiDialogDisplayed', []))
        except Exception:
            LOG_CURRENT_EXCEPTION()

        return result

    def isTutorialDialogDisplayed(self, dialogID):
        result = True
        try:
            result = self.uiHolder.movie.invoke(('_root.tutorialLoader.isTutorialDialogDisplayed', [dialogID]))
        except Exception:
            LOG_CURRENT_EXCEPTION()

        return result

    def findItem(self, itemID, criteria):
        itemPath = None
        if criteria is None:
            item = self.config.getItem(itemID)
            locked = True
            valuePath = None
            value = None
        else:
            parentID, valuePath, value = criteria
            item = self.config.getItem(parentID)
            locked = False
        try:
            itemPath = self.uiHolder.movie.invoke(('_root.tutorialLoader.findItem', [item['path'], valuePath, value]))
            if not locked:
                if itemPath is not None:
                    self.config.addItem(itemID, itemPath)
                else:
                    self.config.removeItem(itemID)
        except Exception:
            LOG_CURRENT_EXCEPTION()

        return itemPath

    def invokeCommand(self, command):
        name, args = command
        self.uiHolder.call(name, args[:])

    def getGuiRoot(self):
        try:
            root = WindowsManager.g_windowsManager.window
        except AttributeError:
            LOG_CURRENT_EXCEPTION()
            root = None

        return root

    @classmethod
    def defineDispatcher(cls):
        dispatcher = None
        try:
            window = WindowsManager.g_windowsManager.window
            dispatcher = getattr(window, 'tutorialDispatcher', None)
            if dispatcher is None and window is not None:
                dispatcher = TutorialDispatcher()
                dispatcher.populateUI(window.proxy)
                window.tutorialDispatcher = dispatcher
        except AttributeError:
            LOG_CURRENT_EXCEPTION()

        return dispatcher

    def setChapterInfo(self, title, description):
        if self._dispatcherRef() is not None:
            self._dispatcherRef().setChapterInfo(title, description)
        else:
            LOG_ERROR('TUTORIAL. Tutorial dispatcher is not defined.')
        return

    def clearChapterInfo(self):
        if self._dispatcherRef() is not None:
            self._dispatcherRef().clearChapterInfo()
        else:
            LOG_ERROR('TUTORIAL. Tutorial dispatcher is not defined.')
        return

    def setTrainingRestartMode(self):
        if self._dispatcherRef() is not None:
            self._dispatcherRef().setTrainingRestartMode()
        else:
            LOG_ERROR('TUTORIAL. Tutorial dispatcher is not defined.')
        return

    def setTrainingRunMode(self):
        if self._dispatcherRef() is not None:
            self._dispatcherRef().setTrainingRunMode()
        else:
            LOG_ERROR('TUTORIAL. Tutorial dispatcher is not defined.')
        return

    def __dispatchMouseClickEvent(self, targetID):
        self.onMouseClicked(GUIEvent(None, targetID))
        return

    def __dispatchPageChangingEvent(self, _, pageName):
        sceneID = self.config.getSceneID(pageName)
        if sceneID is None:
            self.clear()
            LOG_DEBUG('TUTORIAL. Scene alias not found, page:', pageName)
        else:
            self.call('Tutorial.Effects.Stop')
            self.onPageChanging(sceneID)
        return

    def __onGetScreenSize(self, *args):
        parser = CommandArgsParser(self.__onGetScreenSize.__name__)
        parser.parse(*args)
        parser.addArgs(list(GUI.screenResolution()))
        self.uiHolder.respond(parser.args())