# Embedded file name: scripts/client/gui/shared/tooltips/shell.py
from debug_utils import LOG_ERROR
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared import g_itemsCache
from gui.shared.items_parameters import params_helper, formatters as params_formatters, NO_DATA
from gui.shared.tooltips import formatters
from gui.shared.tooltips import getComplexStatus, TOOLTIP_TYPE
from gui.shared.tooltips.common import BlocksTooltipData, getCurrencySetting
from gui.shared.formatters import text_styles
from helpers.i18n import makeString as _ms
from BigWorld import wg_getIntegralFormat as _int
_TOOLTIP_MIN_WIDTH = 380
_TOOLTIP_MAX_WIDTH = 420
_AUTOCANNON_SHOT_DISTANCE = 400

class ShellBlockToolTipData(BlocksTooltipData):

    def __init__(self, context):
        super(ShellBlockToolTipData, self).__init__(context, TOOLTIP_TYPE.SHELL)
        self.item = None
        self._setContentMargin(top=0, left=0, bottom=20, right=20)
        self._setMargins(10, 15)
        self._setWidth(_TOOLTIP_MIN_WIDTH)
        return

    def _packBlocks(self, *args, **kwargs):
        self.item = self.context.buildItem(*args, **kwargs)
        items = super(ShellBlockToolTipData, self)._packBlocks()
        shell = self.item
        statsConfig = self.context.getStatsConfiguration(shell)
        paramsConfig = self.context.getParamsConfiguration(shell)
        statusConfig = self.context.getStatusConfiguration(shell)
        leftPadding = 20
        rightPadding = 20
        topPadding = 20
        lrPaddings = formatters.packPadding(left=leftPadding, right=rightPadding)
        blockTopPadding = -4
        blockPadding = formatters.packPadding(left=leftPadding, right=rightPadding, top=blockTopPadding)
        textGap = -2
        items.append(formatters.packBuildUpBlockData(HeaderBlockConstructor(shell, statsConfig, leftPadding, rightPadding).construct(), padding=formatters.packPadding(left=leftPadding, right=rightPadding, top=topPadding)))
        priceBlock, invalidWidth = PriceBlockConstructor(shell, statsConfig, 80, leftPadding, rightPadding).construct()
        if len(priceBlock) > 0:
            self._setWidth(_TOOLTIP_MAX_WIDTH if invalidWidth else _TOOLTIP_MIN_WIDTH)
            items.append(formatters.packBuildUpBlockData(priceBlock, padding=blockPadding, gap=textGap))
        items.append(formatters.packBuildUpBlockData(CommonStatsBlockConstructor(shell, paramsConfig, 80, leftPadding, rightPadding).construct(), padding=blockPadding, gap=textGap))
        statusBlock = StatusBlockConstructor(shell, statusConfig, leftPadding, rightPadding).construct()
        if len(statusBlock) > 0:
            items.append(formatters.packBuildUpBlockData(statusBlock, padding=lrPaddings))
        return items


class ShellTooltipBlockConstructor(object):

    def __init__(self, shell, configuration, leftPadding = 20, rightPadding = 20):
        self.shell = shell
        self.configuration = configuration
        self.leftPadding = leftPadding
        self.rightPadding = rightPadding

    def construct(self):
        return None


class HeaderBlockConstructor(ShellTooltipBlockConstructor):

    def __init__(self, shell, configuration, leftPadding, rightPadding):
        super(HeaderBlockConstructor, self).__init__(shell, configuration, leftPadding, rightPadding)

    def construct(self):
        shell = self.shell
        block = []
        title = shell.userName
        desc = '#item_types:shell/kinds/' + shell.type
        block.append(formatters.packImageTextBlockData(title=text_styles.highTitle(title), desc=text_styles.standard(desc), img=shell.icon, imgPadding=formatters.packPadding(left=7), txtGap=-4, txtOffset=100 - self.leftPadding))
        return block


class PriceBlockConstructor(ShellTooltipBlockConstructor):

    def __init__(self, shell, configuration, valueWidth, leftPadding, rightPadding):
        super(PriceBlockConstructor, self).__init__(shell, configuration, leftPadding, rightPadding)
        self._valueWidth = valueWidth

    def construct(self):
        block = []
        shell = self.shell
        configuration = self.configuration
        buyPrice = configuration.buyPrice
        sellPrice = configuration.sellPrice
        if buyPrice and sellPrice:
            LOG_ERROR('You are not allowed to use buyPrice and sellPrice at the same time')
            return
        else:
            creditsNeeded, goldNeeded = (0, 0)
            if buyPrice:
                credits, gold = g_itemsCache.items.stats.money
                price = shell.altPrice
                creditsNeeded = price[0] - credits if price[0] else 0
                goldNeeded = price[1] - gold if price[1] else 0
                need = (max(0, creditsNeeded), max(0, goldNeeded))
                defPrice = shell.defaultAltPrice or shell.defaultPrice
                block.append(self._makePriceBlock(price[0], 'buyCreditsPrice', need[0] if need[0] > 0 else None, defPrice[0] if defPrice[0] > 0 else None, percent=shell.actionPrc))
                if price[1] > 0:
                    block.append(formatters.packTextBlockData(text=text_styles.standard(TOOLTIPS.VEHICLE_TEXTDELIMITER_OR), padding=formatters.packPadding(left=81 + self.leftPadding)))
                    block.append(self._makePriceBlock(price[1], 'buyGoldPrice', need[1] if need[1] > 0 else None, defPrice[1] if defPrice[1] > 0 else None, percent=shell.actionPrc))
            if sellPrice:
                block.append(self._makePriceBlock(shell.sellPrice[0], 'sellPrice', oldPrice=shell.defaultSellPrice[0], percent=shell.sellActionPrc))
            inventoryCount = shell.inventoryCount
            if inventoryCount:
                block.append(formatters.packTextParameterBlockData(name=text_styles.main(TOOLTIPS.VEHICLE_INVENTORYCOUNT), value=text_styles.stats(inventoryCount), valueWidth=self._valueWidth, padding=formatters.packPadding(left=-5)))
            notEnoughMoney = creditsNeeded > 0 or goldNeeded > 0
            hasAction = shell.actionPrc > 0 or shell.sellActionPrc > 0
            return (block, notEnoughMoney or hasAction)

    def _makePriceBlock(self, price, settingsKey, neededValue = None, oldPrice = None, percent = 0):
        needFormatted = ''
        oldPriceText = ''
        hasAction = percent != 0
        settings = getCurrencySetting(settingsKey)
        if settings is None:
            return
        else:
            valueFormatted = settings.textStyle(_int(price))
            icon = settings.icon
            if neededValue is not None:
                needFormatted = settings.textStyle(_int(neededValue))
            if hasAction:
                oldPriceText = text_styles.concatStylesToSingleLine(icon, settings.textStyle(_int(oldPrice)))
            neededText = ''
            if neededValue is not None:
                neededText = text_styles.concatStylesToSingleLine(text_styles.main('('), text_styles.error(TOOLTIPS.VEHICLE_GRAPH_BODY_NOTENOUGH), ' ', needFormatted, ' ', icon, text_styles.main(')'))
            text = text_styles.concatStylesWithSpace(text_styles.main(settings.text), neededText)
            if hasAction:
                actionText = text_styles.main(_ms(TOOLTIPS.VEHICLE_ACTION_PRC, actionPrc=text_styles.stats(str(percent) + '%'), oldPrice=oldPriceText))
                text = text_styles.concatStylesToMultiLine(text, actionText)
                if settings.frame == ICON_TEXT_FRAMES.GOLD:
                    newPrice = (0, price)
                else:
                    newPrice = (price, 0)
                return formatters.packSaleTextParameterBlockData(name=text, saleData={'newPrice': newPrice,
                 'valuePadding': -8}, actionStyle='alignTop', padding=formatters.packPadding(left=61))
            return formatters.packTextParameterWithIconBlockData(name=text, value=valueFormatted, icon=settings.frame, valueWidth=self._valueWidth, padding=formatters.packPadding(left=-5))
            return


class CommonStatsBlockConstructor(ShellTooltipBlockConstructor):

    def __init__(self, shell, configuration, valueWidth, leftPadding, rightPadding):
        super(CommonStatsBlockConstructor, self).__init__(shell, configuration, leftPadding, rightPadding)
        self._valueWidth = valueWidth

    def construct(self):
        block = []
        shell = self.shell
        vehicle = self.configuration.vehicle
        vDescr = vehicle.descriptor if vehicle is not None else None
        params = params_helper.getParameters(shell, vDescr)
        piercingPower = params.pop('piercingPower')
        piercingPowerTable = params.pop('piercingPowerTable')
        maxShotDistance = params.pop('maxShotDistance') if 'maxShotDistance' in params else None
        formattedParameters = params_formatters.getFormattedParamsList(shell.descriptor, params)
        block.append(formatters.packTitleDescBlock(title=text_styles.middleTitle(_ms(TOOLTIPS.TANKCARUSEL_MAINPROPERTY)), padding=formatters.packPadding(bottom=8)))
        for paramName, paramValue in formattedParameters:
            block.append(self.__packParameterBlock(_ms('#menu:moduleInfo/params/' + paramName), paramValue, params_formatters.measureUnitsForParameter(paramName)))

        piercingUnits = _ms(params_formatters.measureUnitsForParameter('piercingPower'))
        if isinstance(piercingPowerTable, list):
            block.append(formatters.packTitleDescBlock(title=text_styles.standard(_ms(MENU.MODULEINFO_PARAMS_PIERCINGDISTANCEHEADER)), padding=formatters.packPadding(bottom=8, top=8)))
            for distance, value in piercingPowerTable:
                if maxShotDistance is not None and distance == _AUTOCANNON_SHOT_DISTANCE:
                    piercingUnits += '*'
                block.append(self.__packParameterBlock(_ms(MENU.MODULEINFO_PARAMS_PIERCINGDISTANCE, dist=distance), params_formatters.baseFormatParameter('piercingPower', value), piercingUnits))

            if maxShotDistance is not None:
                block.append(formatters.packTitleDescBlock(title=text_styles.standard(_ms(MENU.MODULEINFO_PARAMS_MAXSHOTDISTANCE_FOOTNOTE)), padding=formatters.packPadding(top=8)))
        else:
            if piercingPowerTable != NO_DATA:
                piercingUnits += '*'
            block.append(self.__packParameterBlock(_ms(MENU.MODULEINFO_PARAMS_PIERCINGPOWER), params_formatters.baseFormatParameter('piercingPower', piercingPower), piercingUnits))
            if piercingPowerTable != NO_DATA:
                title = _ms(MENU.MODULEINFO_PARAMS_NOPIERCINGDISTANCE_FOOTNOTE)
                distanceNote = ''
                if maxShotDistance is not None:
                    distanceNote = _ms(MENU.MODULEINFO_PARAMS_NOPIERCINGDISTANCE_FOOTNOTE_MAXDISTANCE)
                title = title % distanceNote
                block.append(formatters.packTitleDescBlock(title=text_styles.standard(title), padding=formatters.packPadding(top=8)))
        return block

    def __packParameterBlock(self, name, value, measureUnits):
        return formatters.packTextParameterBlockData(name=text_styles.main(name) + text_styles.standard(measureUnits), value=text_styles.stats(value), valueWidth=self._valueWidth, padding=formatters.packPadding(left=-5))


class StatusBlockConstructor(ShellTooltipBlockConstructor):

    def __init__(self, shell, configuration, leftPadding, rightPadding):
        super(StatusBlockConstructor, self).__init__(shell, configuration, leftPadding, rightPadding)

    def construct(self):
        shell = self.shell
        configuration = self.configuration
        block = []
        status = None
        checkBuying = configuration.checkBuying
        if checkBuying:
            couldBeBought, reason = shell.mayPurchase(g_itemsCache.items.stats.money)
            if not couldBeBought:
                status = '#tooltips:shellFits/%s' % reason
        statusHeader, statusText = getComplexStatus(status)
        if statusHeader is not None or statusText is not None:
            block.append(formatters.packTitleDescBlock(title=text_styles.middleTitle(statusHeader if statusHeader is not None else ''), desc=text_styles.main(statusText if statusText is not None else '')))
        return block