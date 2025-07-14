import globalPluginHandler
import controlTypes
import ui
import api
import textInfos
import speech
import config
import eventHandler
import winUser
import gui
from gui import guiHelper, nvdaControls
import wx
import addonHandler
from scriptHandler import script

addonHandler.initTranslation()

# List of control types
CONTROL_TYPE_NAMES = {
	controlTypes.Role.ALERT: _("alert"),
	controlTypes.Role.BUTTON: _("button"),
	controlTypes.Role.CHECKBOX: _("check box"),
	controlTypes.Role.CHECKMENUITEM: _("check menu item"),
	controlTypes.Role.COMBOBOX: _("combo box"),
	controlTypes.Role.DATAGRID: _("data grid"),
	controlTypes.Role.DIALOG: _("dialog"),
	controlTypes.Role.DOCUMENT: _("document"),
	controlTypes.Role.EDITABLETEXT: _("edit"),
	controlTypes.Role.FRAME: _("frame"),
	controlTypes.Role.GRAPHIC: _("graphic"),
	controlTypes.Role.GROUPING: _("grouping"),
	controlTypes.Role.HEADING: _("heading"),
	controlTypes.Role.HOTKEYFIELD: _("hot key field"),
	controlTypes.Role.ICON: _("icon"),
	controlTypes.Role.INDICATOR: _("indicator"),
	controlTypes.Role.LINK: _("link"),
	controlTypes.Role.LIST: _("list"),
	controlTypes.Role.LISTITEM: _("list item"),
	controlTypes.Role.MENUBAR: _("menu bar"),
	controlTypes.Role.MENUBUTTON: _("menu button"),
	controlTypes.Role.MENUITEM: _("menu item"),
	controlTypes.Role.POPUPMENU: _("menu"),
	controlTypes.Role.PROGRESSBAR: _("progress bar"),
	controlTypes.Role.PROPERTYPAGE: _("property page"),
	controlTypes.Role.RADIOBUTTON: _("radio button"),
	controlTypes.Role.RADIOMENUITEM: _("radio menu item"),
	controlTypes.Role.SCROLLBAR: _("scroll bar"),
	controlTypes.Role.SEPARATOR: _("separator"),
	controlTypes.Role.SLIDER: _("slider"),
	controlTypes.Role.SPLITBUTTON: _("split button"),
	controlTypes.Role.STATICTEXT: _("text"),
	controlTypes.Role.STATUSBAR: _("status bar"),
	controlTypes.Role.SWITCH: _("switch"),
	controlTypes.Role.TAB: _("tab"),
	controlTypes.Role.TABCONTROL: _("tab control"),
	controlTypes.Role.TABLE: _("table"),
	controlTypes.Role.TABLECOLUMNHEADER: _("colunn header"),
	controlTypes.Role.TERMINAL: _("terminal"),
	controlTypes.Role.TOGGLEBUTTON: _("toggle button"),
	controlTypes.Role.TOOLBAR: _("tool bar"),
	controlTypes.Role.TOOLTIP: _("tool tip"),
	controlTypes.Role.TREEVIEW: _("tree view"),
	controlTypes.Role.TREEVIEWITEM: _("tree view item"),
	controlTypes.Role.WINDOW: _("window"),
	# Add more types as needed
}

CONTROL_TYPE_NAMES_REVERSED = {value: key for key, value in CONTROL_TYPE_NAMES.items()}

# List of control states to be announced
STATE_NAMES = {
	controlTypes.State.AUTOCOMPLETE: _("has auto complete"),
	controlTypes.State.BUSY: _("busy"),
	controlTypes.State.CHECKED: _("checked"),
	controlTypes.State.CLICKABLE: _("clickable"),
	controlTypes.State.COLLAPSED: _("collapsed"),
	controlTypes.State.EXPANDED: _("expanded"),
	controlTypes.State.HALFCHECKED: _("half checked"),
	controlTypes.State.HALF_PRESSED: _("half pressed"),
	controlTypes.State.HASLONGDESC: _("has long description"),
	controlTypes.State.HASPOPUP: _("subMenu"),
	controlTypes.State.INTERNAL_LINK: _("same page"),
	controlTypes.State.INVALID_ENTRY: _("invalid entry"),
	controlTypes.State.MULTILINE: _("multi line"),
	controlTypes.State.ON: _("on"),
	controlTypes.State.PRESSED: _("pressed"),
	controlTypes.State.PROTECTED: _("protected"),
	controlTypes.State.READONLY: _("read only"),
	controlTypes.State.REQUIRED: _("required"),
	controlTypes.State.SORTED: _("sorted"),
	controlTypes.State.SORTED_ASCENDING: _("sorted ascending"),
	controlTypes.State.SORTED_DESCENDING: _("sorted descending"),
	controlTypes.State.UNAVAILABLE: _("unavailable"),
	controlTypes.State.VISITED: _("visited"),
	# Add more states as needed
}

# List of negative states
NEGATIVE_STATE_NAMES = {
	controlTypes.State.CHECKED: _("not checked"),
	controlTypes.State.ON: _("off"),
	controlTypes.State.PRESSED: _("not pressed"),
	controlTypes.State.SELECTED: _("not selected"),
}

# Types of control to ignore
IGNORED_CONTROL_TYPES = {
controlTypes.Role.FRAME,
controlTypes.Role.PANE,
controlTypes.Role.TABLECELL,
controlTypes.Role.TABLEROW,
controlTypes.Role.UNKNOWN,
}

# States to ignore
IGNORED_STATES = {
	controlTypes.State.CHECKABLE,
	controlTypes.State.FOCUSABLE,
	controlTypes.State.FOCUSED,
	controlTypes.State.INVISIBLE,
	controlTypes.State.OFFSCREEN,
	controlTypes.State.SELECTABLE,
	controlTypes.State.SELECTED,
}

# Configuration customization options
confspec = {
	"useCustomTranslations": "boolean(default=True)",
	"messageExtension": "integer(min=0,max=3,default=2)",
	"enabled": "boolean(default=True)",
	"announceActiveWindows": "boolean(default=False)",
	"announceShortcutPrefix": "boolean(default=False)",
	"announceValuePrefix": "boolean(default=False)",
	"enabledControls": "string(default='')"  # Lista como string separada por vírgulas
}

config.conf.spec["pausingInfo"] = confspec

# Settings category
class pausingInfoSettingsPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: The name of the panel in the NVDA settings dialog.
	title = _("Pausing Info")

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		
		# Translators: The label for a checkbox in the settings panel.
		self.enabledCheckbox = sHelper.addItem(wx.CheckBox(self, label=_("&Enable paused reading of control types and states")))
		self.enabledCheckbox.SetValue(config.conf["pausingInfo"]["enabled"])
		self.enabledCheckbox.Bind(wx.EVT_CHECKBOX, self.onEnabledCheckbox)

		# Translators: The label for a checkbox in the settings panel.
		self.useCustomTranslations = sHelper.addItem(wx.CheckBox(self, label=_("&Allow the add-on to translate the names of control types and states")))
		self.useCustomTranslations.SetValue(config.conf["pausingInfo"]["useCustomTranslations"])
		
		# Translators: The label for a radio button group in the settings panel.
		messageExtensionGroupLabel = _("Message Extension")
		messageExtensionGroup = gui.guiHelper.BoxSizerHelper(self, sizer=sHelper.addItem(wx.StaticBoxSizer(wx.VERTICAL, self, label=messageExtensionGroupLabel)))
		
		# Translators: The label for a radio button option in the settings panel.
		self.messageExtensionShort = messageExtensionGroup.addItem(wx.RadioButton(self, label=_("&Short"), style=wx.RB_GROUP))
		self.messageExtensionShort.SetValue(config.conf["pausingInfo"]["messageExtension"] == 0)
		
		# Translators: The label for a radio button option in the settings panel.
		self.messageExtensionMedium = messageExtensionGroup.addItem(wx.RadioButton(self, label=_("&Medium")))
		self.messageExtensionMedium.SetValue(config.conf["pausingInfo"]["messageExtension"] == 1)
		
		# Translators: The label for a radio button option in the settings panel.
		self.messageExtensionLong = messageExtensionGroup.addItem(wx.RadioButton(self, label=_("&Long")))
		self.messageExtensionLong.SetValue(config.conf["pausingInfo"]["messageExtension"] == 2)
		
		# Translators: The label for a radio button option in the settings panel.
		self.messageExtensionCustom = messageExtensionGroup.addItem(wx.RadioButton(self, label=_("&Custom")))
		self.messageExtensionCustom.SetValue(config.conf["pausingInfo"]["messageExtension"] == 3)
		
		# Translators: The label for a button in the settings panel.
		self.configureButton = wx.Button(self, label=_("Configure..."))
		sHelper.addItem(self.configureButton) 
		self.configureButton.Bind(wx.EVT_BUTTON, self.onConfigure) 

		self.configureButton.Enable(config.conf["pausingInfo"]["messageExtension"] == 3)

		self.messageExtensionShort.Bind(wx.EVT_RADIOBUTTON, self.updateConfigureButton)
		self.messageExtensionMedium.Bind(wx.EVT_RADIOBUTTON, self.updateConfigureButton)
		self.messageExtensionLong.Bind(wx.EVT_RADIOBUTTON, self.updateConfigureButton)
		self.messageExtensionCustom.Bind(wx.EVT_RADIOBUTTON, self.updateConfigureButton)

		self.updateControlState(config.conf["pausingInfo"]["enabled"])

	def onEnabledCheckbox(self, event):
		self.updateControlState(event.IsChecked())

	def updateControlState(self, enabled):
		for control in [self.useCustomTranslations, self.messageExtensionShort, self.messageExtensionMedium,
						self.messageExtensionLong, self.messageExtensionCustom]:
			control.Enable(enabled)

	def updateConfigureButton(self, event=None):
		self.configureButton.Enable(self.messageExtensionCustom.GetValue())

	def onConfigure(self, event):
		dlg = ConfigureDialog(self)
		dlg.ShowModal()
		dlg.Destroy()

	def onSave(self):
		config.conf["pausingInfo"]["enabled"] = self.enabledCheckbox.GetValue()
		config.conf["pausingInfo"]["useCustomTranslations"] = self.useCustomTranslations.GetValue()
		if self.messageExtensionShort.GetValue():
			config.conf["pausingInfo"]["messageExtension"] = 0
		elif self.messageExtensionMedium.GetValue():
			config.conf["pausingInfo"]["messageExtension"] = 1
		elif self.messageExtensionLong.GetValue():
			config.conf["pausingInfo"]["messageExtension"] = 2
		elif self.messageExtensionCustom.GetValue():
			config.conf["pausingInfo"]["messageExtension"] = 3

# Settings dialog for the custom level
class ConfigureDialog(wx.Dialog):
	def __init__(self, parent):
		# Translators: The name of the custom level settings dialog.
		super(ConfigureDialog, self).__init__(parent, title=_("Settings for the custom message extension level"))
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: The instruction text for the custom level settings dialog.
		sHelper.addItem(wx.StaticText(self, label=_("You can individually adjust all the information announced by the add-on")))

		# Translators: The label for a group of controls in the custom level settings dialog.
		controlsGroupSizer = wx.StaticBoxSizer(wx.VERTICAL, self, label=_("Types of control"))
		controlsGroupHelper = gui.guiHelper.BoxSizerHelper(self, sizer=controlsGroupSizer)

		# Use enums as fixed values, dynamically translated for display
		self.controlChoices = list(CONTROL_TYPE_NAMES.keys())  # List of enums Role

		controlDisplayNames = [CONTROL_TYPE_NAMES[role] for role in self.controlChoices]  # Translated names


		self.controlsList = controlsGroupHelper.addLabeledControl(
			# Translators: The label for a custom check list box in the custom level settings dialog.
			_("Select the controls to be announced:"),
			nvdaControls.CustomCheckListBox,
			choices=controlDisplayNames
		)

		# Load the controls activated from the configuration as integers
		enabledControlsStr = config.conf["pausingInfo"].get("enabledControls", "")
		enabledControls = [int(role) for role in enabledControlsStr.split(",")] if enabledControlsStr else []

		# Map the integer values to the indexes in controlChoices
		self.controlsList.CheckedItems = [
			i for i, role in enumerate(self.controlChoices) if role.value in enabledControls
		]

		sHelper.addItem(controlsGroupSizer, flag=wx.EXPAND)

		# Translators: The label for a group of controls in the custom level settings dialog.
		messagesGroupSizer = wx.StaticBoxSizer(wx.VERTICAL, self, label=_("Other additional messages"))
		messagesGroupHelper = gui.guiHelper.BoxSizerHelper(self, sizer=messagesGroupSizer)

		self.announceActiveWindowsCheckbox = messagesGroupHelper.addItem(
			# Translators: The label for a checkbox in the custom level settings dialog.
			wx.CheckBox(self, label=_("Announce active windows"))
		)
		self.announceActiveWindowsCheckbox.SetValue(config.conf["pausingInfo"]["announceActiveWindows"])

		self.prefixShortcutCheckbox = messagesGroupHelper.addItem(
			# Translators: The label for a checkbox in the custom level settings dialog.
			wx.CheckBox(self, label=_("Announce shortcut before object shortcut keys"))
		)
		self.prefixShortcutCheckbox.SetValue(config.conf["pausingInfo"]["announceShortcutPrefix"])

		self.prefixValueCheckbox = messagesGroupHelper.addItem(
			# Translators: The label for a checkbox in the custom level settings dialog.
			wx.CheckBox(self, label=_("Announce value before slider and scrollbar values"))
		)
		self.prefixValueCheckbox.SetValue(config.conf["pausingInfo"]["announceValuePrefix"])

		sHelper.addItem(messagesGroupSizer, flag=wx.EXPAND)
		sHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))

		mainSizer.Add(sHelper.sizer, border=10, flag=wx.ALL)
		self.SetSizer(mainSizer)
		mainSizer.Fit(self)
		self.CenterOnScreen()

		self.Bind(wx.EVT_BUTTON, self.OnOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.OnCancel, id=wx.ID_CANCEL)
		# Sets the initial focus in the list of controls
		wx.CallAfter(self.controlsList.SetFocus)

	def GetSelections(self):
		# Get the integer values of the selected enums
		selectedControls = [self.controlChoices[i].value for i in self.controlsList.CheckedItems]

		# Save other settings
		config.conf["pausingInfo"]["announceActiveWindows"] = self.announceActiveWindowsCheckbox.GetValue()
		config.conf["pausingInfo"]["announceShortcutPrefix"] = self.prefixShortcutCheckbox.GetValue()
		config.conf["pausingInfo"]["announceValuePrefix"] = self.prefixValueCheckbox.GetValue()

		# Return as list of integers (will be converted to string in OnOk)
		return selectedControls

	def OnOk(self, event):
		try:
			# Convert the list of integers into a comma-separated string
			selectedControls = self.GetSelections()
			config.conf["pausingInfo"]["enabledControls"] = ",".join(str(role) for role in selectedControls)
			config.conf.save()
		except Exception as e:
			wx.MessageBox(f"Error saving settings: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)
		finally:
			self.EndModal(wx.ID_OK)

	def OnCancel(self, event):
		self.EndModal(wx.ID_CANCEL)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.originalSpeakObject = speech.speakObject
		speech.speakObject = self.customSpeakObject
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(pausingInfoSettingsPanel)
		self.last_announced_window = None

	def terminate(self):
		speech.speakObject = self.originalSpeakObject
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(pausingInfoSettingsPanel)
		super(GlobalPlugin, self).terminate()

	@script(
		# Translators: The description for the toggle script.
		description=_("Toggles Pausing Info on and off"),
		# Translators: Name of the section in "Input gestures" dialog.
		category=_("Pausing Information"),
		gesture="kb:NVDA+shift+p"
	)
	def script_togglepausingInfo(self, gesture):
		config.conf["pausingInfo"]["enabled"] = not config.conf["pausingInfo"]["enabled"]
		# Translators: Message announced when Pausing Info is enabled or disabled.
		message = _("Pausing Info enabled") if config.conf["pausingInfo"]["enabled"] else _("Pausing Info disabled")
		ui.message(message)

	# Active window warning
	def event_foreground(self, obj, nextHandler):
		# Check if the add-on is activated or if the announcement of active windows is deactivated on custom message extension level
		if not config.conf["pausingInfo"]["enabled"]:
			nextHandler()
			return

		message_extension = config.conf["pausingInfo"]["messageExtension"]
		announce_active_windows = config.conf["pausingInfo"].get("announceActiveWindows", False)
		
		if message_extension == 3 and not announce_active_windows:
				nextHandler()
				return
		elif message_extension < 2:  # Short and medium levels
			nextHandler()
			return

		# Announce active windows, respecting the settings
		elif obj.role in [controlTypes.Role.DIALOG, controlTypes.Role.PANE, controlTypes.Role.WINDOW]:
			if obj.name != self.last_announced_window:
				# Translators: Announced when any window or dialog is activated
				message = _("Window activated: {name}").format(name=obj.name if obj.name != "Program Manager" else " ")  # For the Desktop, the character string is empty to avoid duplication of the announcement by NVDA. There could be a better solution!
				if obj.description:
					message += f" - {obj.description}"
				nextHandler()
				ui.message(message)
				self.last_announced_window = obj.name

	# nextHandler() remains commented out to avoid problems with the announcement

	def build_description_parts(self, obj, message_extension, enabledControls=None):
		description_parts = []

		if obj.role in IGNORED_CONTROL_TYPES:
			self.originalSpeakObject(obj, *args, **kwargs)
			return

		# Always announce the name of the object, if available
		if obj.name:
			description_parts.append(obj.name)

		# Announce the value of the combo boxes
		if obj.role in [controlTypes.Role.COMBOBOX, controlTypes.Role.HOTKEYFIELD]:
			if obj.value:
				description_parts.append(obj.value)

		# Announce the control type if enabled or according to the message extension level
		if message_extension == 3 and enabledControls and obj.role.value in enabledControls:
			description_parts.append(self.get_control_type(obj))
		elif message_extension == 2:  # Long
			description_parts.append(self.get_control_type(obj))
		elif message_extension in [0, 1] and obj.role not in [controlTypes.Role.LISTITEM, controlTypes.Role.TREEVIEWITEM, controlTypes.Role.MENUITEM]:
			description_parts.append(self.get_control_type(obj))

		# Announce the description of the objects that have it
		if obj.role in [controlTypes.Role.ALERT, controlTypes.Role.BUTTON, controlTypes.Role.COMBOBOX, controlTypes.Role.DIALOG, controlTypes.Role.EDITABLETEXT, controlTypes.Role.GROUPING, controlTypes.Role.LINK, controlTypes.Role.LISTITEM, controlTypes.Role.MENUBAR, controlTypes.Role.MENUBUTTON, controlTypes.Role.PROPERTYPAGE, controlTypes.Role.SCROLLBAR, controlTypes.Role.SPLITBUTTON, controlTypes.Role.STATICTEXT, controlTypes.Role.TERMINAL, controlTypes.Role.TOGGLEBUTTON, controlTypes.Role.TOOLBAR]:
			if obj.description:
				description_parts.append(obj.description)

		# Announce relevant states
		relevant_states = self.get_relevant_states(obj, None)
		description_parts.extend(relevant_states)

		# Announce the value for sliders and scrollbars, with or without prefix
		if obj.role in [controlTypes.Role.SLIDER, controlTypes.Role.SCROLLBAR] and obj.value:
			if message_extension == 3:  # Custom level
				if config.conf["pausingInfo"]["announceValuePrefix"]:
					# Translators: Announced before a slider value when the Announce value before slider and scrollbar values is enabled
					description_parts.append(_("Value: {value}").format(value=obj.value))
				else:
					description_parts.append(str(obj.value))
			elif message_extension > 0:
				# Translators: Announced before a slider value when the message extension is medium or higher
				description_parts.append(_("Value: {value}").format(value=obj.value))
			else:
				description_parts.append(str(obj.value))

		# Announce the shortcut, with or without prefix
		if hasattr(obj, 'keyboardShortcut') and obj.keyboardShortcut:
			if message_extension == 3:  # Custom level
				if config.conf["pausingInfo"]["announceShortcutPrefix"]:
					# Translators: Announced before the shortcut key of an object when the Announce shortcut before object shortcut keys is enabled
					description_parts.append(_("Shortcut: {shortcut}").format(shortcut=obj.keyboardShortcut))
				else:
					description_parts.append(str(obj.keyboardShortcut))
			elif message_extension > 0:
				# Translators: Announced before the shortcut key of an object when the message extension is medium or higher
				description_parts.append(_("Shortcut: {shortcut}").format(shortcut=obj.keyboardShortcut))
			else:
				description_parts.append(str(obj.keyboardShortcut))

		# Announce position information, when applicable
		if obj.role in [controlTypes.Role.BUTTON, controlTypes.Role.HEADING, controlTypes.Role.ICON, controlTypes.Role.LISTITEM, controlTypes.Role.MENUITEM, controlTypes.Role.SLIDER, controlTypes.Role.TAB, controlTypes.Role.TOGGLEBUTTON, controlTypes.Role.TREEVIEWITEM]:
			position_info = self.get_position_info(obj)
			if position_info:
				description_parts.extend(position_info)

		# Announce the contents of edit boxes and editable documents
		if obj.role in [controlTypes.Role.DOCUMENT, controlTypes.Role.EDITABLETEXT, controlTypes.Role.STATICTEXT, controlTypes.Role.TERMINAL]:
			self.add_document_content(obj, description_parts)

		# Announce the value of the progress bars and certain list items that have it
		if obj.role in [controlTypes.Role.LISTITEM, controlTypes.Role.PROGRESSBAR] and obj.value:
			description_parts.append(obj.value)

		return description_parts

	def customSpeakObject(self, obj, *args, **kwargs):
		if not config.conf["pausingInfo"]["enabled"]:
			self.originalSpeakObject(obj, *args, **kwargs)
			return

		if obj.role in [controlTypes.Role.DIALOG, controlTypes.Role.PANE, controlTypes.Role.WINDOW] and obj.name == self.last_announced_window:
			self.last_announced_window = None
			return

		try:
			message_extension = config.conf["pausingInfo"]["messageExtension"]
			enabledControls = [int(role) for role in config.conf["pausingInfo"].get("enabledControls", "").split(",")] if config.conf["pausingInfo"].get("enabledControls", "") else []

			# Finalize and announce the description
			description_parts = self.build_description_parts(obj, message_extension, enabledControls if message_extension == 3 else None)
			final_description = " - ".join(filter(None, description_parts))
			if final_description:
				ui.message(final_description)

			# Announce selected text in edit boxes and editable documents
			if obj.role in [controlTypes.Role.DOCUMENT, controlTypes.Role.EDITABLETEXT]:
				self.announce_selected_text(obj)
		except Exception as e:
			self.originalSpeakObject(obj, *args, **kwargs)

	# Auxiliary function for obtaining the relevant statuses
	def get_relevant_states(self, obj, enabledControls):
		relevant_states = []
		use_custom_translations = config.conf["pausingInfo"]["useCustomTranslations"]
		
		last_obj = getattr(self, 'last_menu_item', None)
		last_states = getattr(self, 'last_menu_states', [])

		for state in obj.states:
			if state not in IGNORED_STATES:
				state_name = STATE_NAMES.get(state) if use_custom_translations else controlTypes.stateLabels.get(state)
				if state_name:
					# Avoid announcing "subMenu" for the collapsed menu items
					if state == controlTypes.State.HASPOPUP and controlTypes.State.COLLAPSED in obj.states and obj.role == controlTypes.Role.MENUITEM:
						continue
					# Avoid repeating "unavailable" or "checked" in sequence
					if state in [controlTypes.State.UNAVAILABLE, controlTypes.State.CHECKED] and obj.role == controlTypes.Role.MENUITEM:
						if last_obj and last_obj.role == controlTypes.Role.MENUITEM and state_name in last_states:
							continue
					if enabledControls is None or state_name in enabledControls:
						if state == controlTypes.State.READONLY:
							if self.is_read_only_relevant(obj):
								relevant_states.append(state_name)
						else:
							relevant_states.append(state_name)

		negative_state = self.get_relevant_negative_state(obj)
		if negative_state and (enabledControls is None or negative_state in enabledControls):
			relevant_states.append(negative_state)

		if obj.role == controlTypes.Role.MENUITEM:
			self.last_menu_item = obj
			self.last_menu_states = relevant_states
		else:
			self.last_menu_item = None
			self.last_menu_states = []

		return relevant_states

	# Auxiliary function to check if the read-only status is relevant
	def is_read_only_relevant(self, obj):
		return obj.role in [controlTypes.Role.COMBOBOX, controlTypes.Role.DOCUMENT, controlTypes.Role.EDITABLETEXT, controlTypes.Role.SPINBUTTON]

	# Auxiliary function for obtaining position information
	def get_position_info(self, obj):
		position_info = []
		if obj.positionInfo:
			index = obj.positionInfo.get('indexInGroup')
			total = obj.positionInfo.get('similarItemsInGroup')
			level = obj.positionInfo.get('level')
			if index is not None and total is not None:
				# Translators: Used to announce the index number in lists and other objects
				position_info.append(_("{index} of {total}").format(index=index, total=total))
			if level is not None:
				# Translators: Used to announce the level in the tree view and in other objects
				position_info.append(_("Level {level}").format(level=level))
		return position_info

	# Auxiliary function to announce the selected text
	def announce_selected_text(self, obj):
		try:
			info = obj.makeTextInfo(textInfos.POSITION_SELECTION)
			if not info.isCollapsed:
				selected_text = info.text
				if selected_text:
					if len(selected_text) > 512:
						# Translators: Announced when the selected text is longer than 512 characters
						ui.message(_("{chars} characters selected").format(chars=len(selected_text)))
					else:
						# Translators: Announced before reading the selected text
						ui.message(_("Selected {text}").format(text=selected_text))
		except:
			pass

	# Auxiliary function to obtain the type of control
	def get_control_type(self, obj):
		if config.conf["pausingInfo"]["useCustomTranslations"]:
			return CONTROL_TYPE_NAMES.get(obj.role)
		return controlTypes.roleLabels.get(obj.role)

	# Auxiliary function for reading the contents of edit boxes and editable documents
	def add_document_content(self, obj, description_parts):
		try:
			info = obj.makeTextInfo(textInfos.POSITION_SELECTION)
			if info.isCollapsed:  # Checks that there is no text selected
				info = obj.makeTextInfo(textInfos.POSITION_CARET)
				info.expand(textInfos.UNIT_LINE)
				if info.text:
					description_parts.append(info.text)
		except:
			if obj.value:
				description_parts.append(obj.value)

	# Auxiliary function to obtain the relevant negative states
	def get_relevant_negative_state(self, obj):
		if config.conf["pausingInfo"]["useCustomTranslations"]:
			if obj.role == controlTypes.Role.CHECKBOX:
				return NEGATIVE_STATE_NAMES[controlTypes.State.CHECKED] if controlTypes.State.CHECKED not in obj.states else None
			elif obj.role == controlTypes.Role.RADIOBUTTON:
				return NEGATIVE_STATE_NAMES[controlTypes.State.CHECKED] if controlTypes.State.CHECKED not in obj.states else None
			elif obj.role == controlTypes.Role.TOGGLEBUTTON:
				return NEGATIVE_STATE_NAMES[controlTypes.State.PRESSED] if controlTypes.State.PRESSED not in obj.states else None
			elif obj.role == controlTypes.Role.SWITCH:
				return NEGATIVE_STATE_NAMES[controlTypes.State.ON] if controlTypes.State.ON not in obj.states else None
			elif obj.role in [controlTypes.Role.LISTITEM, controlTypes.Role.TAB, controlTypes.Role.TREEVIEWITEM]:
				return NEGATIVE_STATE_NAMES[controlTypes.State.SELECTED] if controlTypes.State.SELECTED not in obj.states else None
		else:
			if obj.role == controlTypes.Role.CHECKBOX:
				return controlTypes.negativeStateLabels[controlTypes.State.CHECKED] if controlTypes.State.CHECKED not in obj.states else None
			elif obj.role == controlTypes.Role.RADIOBUTTON:
				return controlTypes.negativeStateLabels[controlTypes.State.CHECKED] if controlTypes.State.CHECKED not in obj.states else None
			elif obj.role == controlTypes.Role.TOGGLEBUTTON:
				return controlTypes.negativeStateLabels[controlTypes.State.PRESSED] if controlTypes.State.PRESSED not in obj.states else None
			elif obj.role == controlTypes.Role.SWITCH:
				return controlTypes.negativeStateLabels[controlTypes.State.ON] if controlTypes.State.ON not in obj.states else None
			elif obj.role in [controlTypes.Role.LISTITEM, controlTypes.Role.TAB, controlTypes.Role.TREEVIEWITEM]:
				return controlTypes.negativeStateLabels[controlTypes.State.SELECTED] if controlTypes.State.SELECTED not in obj.states else None
		return None

	# Call up the personalized reading method by gaining focus
	def customEventGainFocus(self, obj, nextHandler):
		self.customSpeakObject(obj)
		nextHandler()
