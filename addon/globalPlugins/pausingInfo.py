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
	"announceListItems": "boolean(default=True)",
	"announceTreeViewItems": "boolean(default=True)",
	"announceMenuItems": "boolean(default=True)",
	"announceValuePrefix": "boolean(default=True)",
	"announceShortcutPrefix": "boolean(default=True)",
}

config.conf.spec["PausingInfo"] = confspec

# Settings category
class PausingInfoSettingsPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: The name of the panel in the NVDA settings dialog.
	title = _("Pausing Information")

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		
		# Translators: The label for a checkbox in the settings panel.
		self.announceListItems = sHelper.addItem(wx.CheckBox(self, label=_("Announce list items")))
		self.announceListItems.SetValue(config.conf["PausingInfo"]["announceListItems"])
		
		# Translators: The label for a checkbox in the settings panel.
		self.announceTreeViewItems = sHelper.addItem(wx.CheckBox(self, label=_("Announce tree view items")))
		self.announceTreeViewItems.SetValue(config.conf["PausingInfo"]["announceTreeViewItems"])
		
		# Translators: The label for a checkbox in the settings panel.
		self.announceMenuItems = sHelper.addItem(wx.CheckBox(self, label=_("Announce menu items")))
		self.announceMenuItems.SetValue(config.conf["PausingInfo"]["announceMenuItems"])
		
		# Translators: The label for a checkbox in the settings panel.
		self.announceValuePrefix = sHelper.addItem(wx.CheckBox(self, label=_('Announce "value" before slider values')))
		self.announceValuePrefix.SetValue(config.conf["PausingInfo"]["announceValuePrefix"])
		
		# Translators: The label for a checkbox in the settings panel.
		self.announceShortcutPrefix = sHelper.addItem(wx.CheckBox(self, label=_('Announce "shortcut" before object shortcuts')))
		self.announceShortcutPrefix.SetValue(config.conf["PausingInfo"]["announceShortcutPrefix"])

	def onSave(self):
		config.conf["PausingInfo"]["announceListItems"] = self.announceListItems.GetValue()
		config.conf["PausingInfo"]["announceTreeViewItems"] = self.announceTreeViewItems.GetValue()
		config.conf["PausingInfo"]["announceMenuItems"] = self.announceMenuItems.GetValue()
		config.conf["PausingInfo"]["announceValuePrefix"] = self.announceValuePrefix.GetValue()
		config.conf["PausingInfo"]["announceShortcutPrefix"] = self.announceShortcutPrefix.GetValue()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.originalSpeakObject = speech.speakObject
		speech.speakObject = self.customSpeakObject
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(PausingInfoSettingsPanel)

	def terminate(self):
		speech.speakObject = self.originalSpeakObject
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(PausingInfoSettingsPanel)
		super(GlobalPlugin, self).terminate()

	def customSpeakObject(self, obj, *args, **kwargs):
		try:
			if obj.role in IGNORED_CONTROL_TYPES:
				self.originalSpeakObject(obj, *args, **kwargs)
				return

			description_parts = []

			# Object name
			if obj.name:
					description_parts.append(obj.name)

			# Processing combo boxes and shortcut key fields
			if obj.role in [controlTypes.Role.COMBOBOX, controlTypes.Role.HOTKEYFIELD]:
				if obj.value:
					description_parts.append(obj.value)

			# Type of control
			control_type = CONTROL_TYPE_NAMES.get(obj.role)
			if control_type:
				if obj.role == controlTypes.Role.LISTITEM and not config.conf["PausingInfo"]["announceListItems"]:
					control_type = " "
				elif obj.role == controlTypes.Role.TREEVIEWITEM and not config.conf["PausingInfo"]["announceTreeViewItems"]:
					control_type = " "
				elif obj.role == controlTypes.Role.MENUITEM and not config.conf["PausingInfo"]["announceMenuItems"]:
					control_type = " "
				description_parts.append(control_type)

			# Read the description of certain objects, where applicable
			if obj.role in [controlTypes.Role.ALERT, controlTypes.Role.BUTTON, controlTypes.Role.DIALOG, controlTypes.Role.GROUPING, controlTypes.Role.LISTITEM, controlTypes.Role.MENUBAR, controlTypes.Role.MENUBUTTON, controlTypes.Role.PROPERTYPAGE, controlTypes.Role.SCROLLBAR, controlTypes.Role.SPLITBUTTON, controlTypes.Role.TOGGLEBUTTON, controlTypes.Role.TOOLBAR]:
				if obj.description:
					description_parts.append(obj.description)

			# Processing sliders and scroll bars
			if obj.role in [controlTypes.Role.SCROLLBAR, controlTypes.Role.SLIDER]:
				if obj.value:
					if config.conf["PausingInfo"]["announceValuePrefix"]:
						# Translators: Announced before a slider value when the "announce value" option is enabled.
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
				relevant_state = [
					STATE_NAMES.get(state) 
					for state in obj.states 
					if state in STATE_NAMES 
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
				if config.conf["PausingInfo"]["announceShortcutPrefix"]:
					# Translators: Announced before a shortcut when the "announce shortcut" option is enabled.
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
		return None

		# Call the personalized reading method gaining focus
	def customEventGainFocus(self, obj, nextHandler):
		self.customSpeakObject(obj)
		# We don't call nextHandler() here to avoid duplicating the announcement
