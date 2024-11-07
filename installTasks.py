import gui
import wx
import addonHandler

addonHandler.initTranslation()

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.name == "Pausing Information":
			result = gui.messageBox(
				# Translators: Displays a message to the user asking if they want to uninstall the previous version of the add-on
				_("Due to a technical error, the internal name of the previous version of this add-on was incorrect, which makes it incompatible with this new version. For the add-on to work properly, this version must be uninstalled. Do you want to uninstall the previous version now?"),
				# Translators: question title
				_("Previous version found"),
				wx.YES_NO|wx.ICON_QUESTION, gui.mainFrame)
			if result == wx.YES:
				addon.requestRemove()
			else:
				raise Exception(_("Installation canceled by the user."))