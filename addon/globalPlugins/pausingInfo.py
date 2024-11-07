import globalPluginHandler
import controlTypes
import ui
import api
import textInfos
import speech
import config
import eventHandler
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

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.originalSpeakObject = speech.speakObject
		speech.speakObject = self.customSpeakObject

	def terminate(self):
		speech.speakObject = self.originalSpeakObject
		super(GlobalPlugin, self).terminate()

	def customSpeakObject(self, obj, **kwargs):
		try:
			if obj.role in IGNORED_CONTROL_TYPES:
				self.originalSpeakObject(obj, **kwargs)
				return

			description_parts = []

			# Object name
			if obj.name:
				description_parts.append(obj.name)

			# Processing the combo boxes
			if obj.role == controlTypes.Role.COMBOBOX:
				if obj.value:
					description_parts.append(obj.value)

			# Type of control
			control_type = CONTROL_TYPE_NAMES.get(obj.role, controlTypes.roleLabels.get(obj.role))
			if control_type:
				description_parts.append(control_type)

			# Read the description of certain object types, where applicable
			if obj.role in [controlTypes.Role.ALERT, controlTypes.Role.BUTTON, controlTypes.Role.DIALOG, controlTypes.Role.GROUPING, controlTypes.Role.MENUBUTTON, controlTypes.Role.SPLITBUTTON]:
				if obj.description:
					description_parts.append(obj.description)

# Processing the slider controls
			if obj.role == controlTypes.Role.SLIDER:
				if obj.value:
					# Translators: Announced before a slider value
					description_parts.append(_("Value: {value}").format(value=obj.value))

			# Relevant states
			relevant_states = [STATE_NAMES.get(state, controlTypes.stateLabels.get(state))
							   for state in obj.states
							   if state in STATE_NAMES]
			description_parts.extend(relevant_states)

			# Processes the index and level of items in tree views, in lists and other objects, where applicable
			if obj.role in [controlTypes.Role.LISTITEM, controlTypes.Role.TREEVIEWITEM, controlTypes.Role.ICON, controlTypes.Role.BUTTON, controlTypes.Role.MENUITEM]:
				if obj.positionInfo:
					index = obj.positionInfo.get('indexInGroup')
					total = obj.positionInfo.get('similarItemsInGroup')
					level = obj.positionInfo.get('level')
					if index is not None and total is not None:
						# Translators: Used to announce the index number in lists and other objects
						description_parts.append(_("{index} of {total}").format(index=index, total=total))
					if level is not None:
						# Translators: Used to announce the level in the tree view and in other objects
						description_parts.append(_("Level {level}").format(level=level))

			# Announcement of shortcut keys
			if hasattr(obj, 'keyboardShortcut') and obj.keyboardShortcut:
				# Translators: Announced before the shortcut key of an object
				description_parts.append(_("Shortcut: {shortcut}").format(shortcut=obj.keyboardShortcut))

			# Finalize and announce the description
			final_description = " - ".join(filter(None, description_parts))

			if final_description:
				ui.message(final_description)

			# Reading selected text in edit boxes
			if obj.role in [controlTypes.Role.EDITABLETEXT, controlTypes.Role.DOCUMENT]:
				try:
					info = obj.makeTextInfo(textInfos.POSITION_SELECTION)
					if not info.isCollapsed:
						selected_text = info.text
						if selected_text:
							# Translators: Announced before reading the selected text
							ui.message(_("Selected {text}").format(text=selected_text))
				except:
					pass

		except Exception as e:
			self.originalSpeakObject(obj, **kwargs)
		# Call up the personalized reading method by gaining focus
	def customEventGainFocus(self, obj, nextHandler):
		self.customSpeakObject(obj)
		# We don't call nextHandler() here to avoid duplication
