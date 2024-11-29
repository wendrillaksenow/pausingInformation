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
import wx
import addonHandler

addonHandler.initTranslation()

# List of control types
CONTROL_TYPE_NAMES = {
	controlTypes.Role.ALERT: _("alert"),
	controlTypes.Role.BUTTON: _("button"),
	controlTypes.Role.CHECKBOX: _("check box"),
	controlTypes.Role.CHECKMENUITEM: _("check menu item"),
	controlTypes.Role.COMBOBOX: _("combo box"),
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
	controlTypes.Role.TOGGLEBUTTON: _("toggle button"),
	controlTypes.Role.TOOLBAR: _("tool bar"),
	controlTypes.Role.TOOLTIP: _("tool tip"),
	controlTypes.Role.TREEVIEW: _("tree view"),
	controlTypes.Role.TREEVIEWITEM: _("tree view item"),
	controlTypes.Role.WINDOW: _("window"),
	# Add more types as needed
}

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
	"messageExtension": "integer(min=0,max=2,default=2)",
}

config.conf.spec["PausingInfo"] = confspec

# Settings category
class PausingInfoSettingsPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: The name of the panel in the NVDA settings dialog.
	title = _("Pausing Information")

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		
		# Translators: The label for a checkbox in the settings panel.
		self.useCustomTranslations = sHelper.addItem(wx.CheckBox(self, label=_("&Allow the add-on to translate the names of control types and states")))
		self.useCustomTranslations.SetValue(config.conf["PausingInfo"]["useCustomTranslations"])
		
		# Translators: The label for a radio button group in the settings panel.
		messageExtensionGroupLabel = _("Message Extension")
		messageExtensionGroup = gui.guiHelper.BoxSizerHelper(self, sizer=sHelper.addItem(wx.StaticBoxSizer(wx.VERTICAL, self, label=messageExtensionGroupLabel)))
		
		# Translators: The label for a radio button option in the settings panel.
		self.messageExtensionShort = messageExtensionGroup.addItem(wx.RadioButton(self, label=_("&Short"), style=wx.RB_GROUP))
		self.messageExtensionShort.SetValue(config.conf["PausingInfo"]["messageExtension"] == 0)
		
		# Translators: The label for a radio button option in the settings panel.
		self.messageExtensionMedium = messageExtensionGroup.addItem(wx.RadioButton(self, label=_("&Medium")))
		self.messageExtensionMedium.SetValue(config.conf["PausingInfo"]["messageExtension"] == 1)
		
		# Translators: The label for a radio button option in the settings panel.
		self.messageExtensionLong = messageExtensionGroup.addItem(wx.RadioButton(self, label=_("&Long")))
		self.messageExtensionLong.SetValue(config.conf["PausingInfo"]["messageExtension"] == 2)

	def onSave(self):
		config.conf["PausingInfo"]["useCustomTranslations"] = self.useCustomTranslations.GetValue()
		if self.messageExtensionShort.GetValue():
			config.conf["PausingInfo"]["messageExtension"] = 0
		elif self.messageExtensionMedium.GetValue():
			config.conf["PausingInfo"]["messageExtension"] = 1
		elif self.messageExtensionLong.GetValue():
			config.conf["PausingInfo"]["messageExtension"] = 2

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.originalSpeakObject = speech.speakObject
		speech.speakObject = self.customSpeakObject
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(PausingInfoSettingsPanel)
		self.last_announced_window = None
		self.in_task_switcher = False
		self.skip_next_speak = False

	def terminate(self):
		speech.speakObject = self.originalSpeakObject
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(PausingInfoSettingsPanel)
		super(GlobalPlugin, self).terminate()

	# Active window warning
	def event_foreground(self, obj, nextHandler):
		if config.conf["PausingInfo"]["messageExtension"] == 2:  # Message extension=Long
			if obj.role in [controlTypes.Role.PANE, controlTypes.Role.WINDOW] and obj.windowClassName == "TaskSwitcherWnd":
				if not self.in_task_switcher:
					# Avoid the repeated announcement of the last active window when switching tasks
					self.in_task_switcher = True
					nextHandler
			elif obj.role in [controlTypes.Role.DIALOG, controlTypes.Role.PANE, controlTypes.Role.WINDOW]:
				if obj.name != self.last_announced_window and not self.in_task_switcher:
					# Translators: Announced when any window or dialog is activated, including the Desktop
					message = _("Window activated: {name}").format(name=obj.name if obj.name != "Program Manager" else _("Desktop - list"))
					if obj.description:
						message += f" - {obj.description}"
					nextHandler()
					ui.message(message)
					self.last_announced_window = obj.name
					self.skip_next_speak = True
				self.in_task_switcher = False

	# nextHandler() remains commented out to avoid problems with the announcement

	def customSpeakObject(self, obj, *args, **kwargs):
		if self.in_task_switcher:
			# Suppress the announcement of the currently active window during task switching
			return

		if self.skip_next_speak:
			self.skip_next_speak = False
			return

		try:
			if obj.role in IGNORED_CONTROL_TYPES:
				self.originalSpeakObject(obj, *args, **kwargs)
				return

			description_parts = []

			# Object name
			if obj.name:
				# Ignore the list name "Desktop" if the window is "Program Manager"
				if obj.name and not (obj.role == controlTypes.Role.LIST and obj.parent and obj.parent.name == "Program Manager"):
					description_parts.append(obj.name)

			# Processing the combo boxes and hotkey fields
			if obj.role in [controlTypes.Role.COMBOBOX, controlTypes.Role.HOTKEYFIELD]:
				if obj.value:
					description_parts.append(obj.value)

			# Type of control
			control_type = None
			if config.conf["PausingInfo"]["useCustomTranslations"]:
				control_type = CONTROL_TYPE_NAMES.get(obj.role)
			if control_type is None:
				control_type = controlTypes.roleLabels.get(obj.role)
			if control_type:
				if config.conf["PausingInfo"]["messageExtension"] == 2 or obj.role not in [controlTypes.Role.LISTITEM, controlTypes.Role.TREEVIEWITEM, controlTypes.Role.MENUITEM]:
					description_parts.append(control_type)

			# Read the description of certain objects, where applicable
			if obj.role in [controlTypes.Role.ALERT, controlTypes.Role.BUTTON, controlTypes.Role.DIALOG, controlTypes.Role.GROUPING, controlTypes.Role.LISTITEM, controlTypes.Role.MENUBAR, controlTypes.Role.MENUBUTTON, controlTypes.Role.PROPERTYPAGE, controlTypes.Role.SCROLLBAR, controlTypes.Role.SPLITBUTTON, controlTypes.Role.TOGGLEBUTTON, controlTypes.Role.TOOLBAR]:
				if obj.description:
					description_parts.append(obj.description)

			# Processing sliders and scroll bars
			if obj.role in [controlTypes.Role.SCROLLBAR, controlTypes.Role.SLIDER]:
				if obj.value:
					if config.conf["PausingInfo"]["messageExtension"] > 0:
						# Translators: Announced before a slider value when the message extension is medium or higher
						description_parts.append(_("Value: {value}").format(value=obj.value))
					else:
						description_parts.append(str(obj.value))

			# Reading the contents of edit boxes and editable documents, where applicable
			if obj.role in [controlTypes.Role.DOCUMENT, controlTypes.Role.EDITABLETEXT]:
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

			# Check if the read-only status is relevant
			def is_read_only_relevant(obj):
				return obj.role in [controlTypes.Role.COMBOBOX, controlTypes.Role.DOCUMENT, controlTypes.Role.EDITABLETEXT, controlTypes.Role.SPINBUTTON]

			# Reading the value of the progress bars
			if obj.role == controlTypes.Role.PROGRESSBAR:
				if obj.value:
					description_parts.append(obj.value)

			# Relevant states (including negative ones)
			relevant_state = self.get_relevant_negative_state(obj)
			if relevant_state:
				description_parts.append(relevant_state)
			else:
				if config.conf["PausingInfo"]["useCustomTranslations"]:
					relevant_state = [
						STATE_NAMES.get(state) 
						for state in obj.states 
						if state in STATE_NAMES 
						and state not in IGNORED_STATES
						and (state != controlTypes.State.READONLY or is_read_only_relevant(obj))
					]
				else:
					relevant_state = [
						controlTypes.stateLabels.get(state) 
						for state in obj.states 
						if state in controlTypes.stateLabels 
						and state not in IGNORED_STATES
						and (state != controlTypes.State.READONLY or is_read_only_relevant(obj))
					]
				description_parts.extend(filter(None, relevant_state))

			# Processing the index and the level of items in the tree view, in lists and in other objects, where applicable
			if obj.role in [controlTypes.Role.BUTTON, controlTypes.Role.HEADING, controlTypes.Role.ICON, controlTypes.Role.LISTITEM, controlTypes.Role.MENUITEM, controlTypes.Role.TAB, controlTypes.Role.TREEVIEWITEM]:
				if obj.positionInfo:
					index = obj.positionInfo.get('indexInGroup')
					total = obj.positionInfo.get('similarItemsInGroup')
					level = obj.positionInfo.get('level')
					if index is not None and total is not None:
						# Translators: Used to announce the index number in lists and other objects
						description_parts.append(_("{index} of {total}").format(index=index, total=total))
					if level is not None:
						# Translators: Used to announce the level in the tree view and in other objects
						description_parts.append(_("Level{level}").format(level=level))

			# Announcement of shortcut keys
			if hasattr(obj, 'keyboardShortcut') and obj.keyboardShortcut:
				if config.conf["PausingInfo"]["messageExtension"] > 0:
					# Translators: Announced before the shortcut key of an object when the message extension is medium or higher
					description_parts.append(_("Shortcut: {shortcut}").format(shortcut=obj.keyboardShortcut))
				else:
					description_parts.append(str(obj.keyboardShortcut))

			# Finalize and announce the description
			final_description = " - ".join(filter(None, description_parts))
			if final_description:
				ui.message(final_description)

			# Reading selected text in edit boxes and editable documents
			if obj.role in [controlTypes.Role.DOCUMENT, controlTypes.Role.EDITABLETEXT]:
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

		except Exception as e:
			self.originalSpeakObject(obj, *args, **kwargs)

	# Processing negative states
	def get_relevant_negative_state(self, obj):
		if config.conf["PausingInfo"]["useCustomTranslations"]:
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
		# We don't call nextHandler() here to avoid duplicating the announcement
