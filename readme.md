# “Pausing Information” add-on for NVDA

## Description

The “Pausing Information” add-on for NVDA is an extension that provides a more detailed and paused reading of control and status information when the focus shifts between interface elements.

This feature was inspired by the Brazilian screen reader “Virtual Vision”, known for its paused way of announcing information, improving user comprehension.

This add-on is supposed to be used with the [DeltaTalk synthesizer](https://cld.pt/dl/download/2fbe0f2a-3a24-41f3-96f5-9ff9a5a88b07/DeltaTalk%20TTS.exe?dl=true) to ensure a full reading experience similar to that of Virtual Vision, but it is perfectly compatible with any other synthesizer being used by NVDA.

## Important note

Paused reading is based exclusively on the symbol level. Hyphens are added to pause the reading of information. If the symbol level is set to anything above “some”, the hyphens will be read aloud.

Likewise, if the symbols (specifically the hyphen) are not correctly adjusted in the punctuation/symbol pronunciation dialog, the pauses may not occur.

To ensure that pauses work as expected, go to the punctuation/symbol pronunciation dialog and make sure that the hyphen is set to be sent to the synthesizer when it is below the symbol level.

## Features

* Announcement of control types and states: The add-on announces the type of control (e.g. “checkbox”, “Radio button”, “menu”, “edit box”) and its status (e.g. “checked”, “pressed”, “unavailable”, “busy”).
* The announcement is made in a paused manner, similar to what was done by the Virtual Vision screen reader.

## Use

After installation, the add-on works automatically, allowing a more detailed and paused reading of information about the types and states of controls. No additional configuration is required.

### Configuration options

As mentioned, no additional configuration is required when using the add-on. The default settings provide a screen reading and Windows navigation experience very similar to that of Virtual Vision, especially when this add-on is used with the DeltaTalk synthesizer.

However, the following configuration options, which allow you to adjust the operation of the add-on to your liking or needs, are available from the “Pausing Information” category in the NVDA settings dialog:

* Enable paused reading of control types and states: If you uncheck this option, the add-on will be completely disabled and all other configuration options will be unavailable. You can also activate/deactivate the add-on using the NVDA+Shift+P shortcut. This shortcut can be modified from NVDA's “Input gestures” dialog, “Pausing Information” category.
* Allow the add-on to translate the names of control types and states: If this option is checked, the add-on will use an internal dictionary to translate the names of the types and states of the controls. Otherwise, NVDA's internal translations will be used.
Note: For now, this option only has a major impact on Portuguese languages. In English, there are no significant differences.
* Message length: This group of radio buttons controls the amount of information to be spoken.
    * Short: Only essential NVDA navigation information will be spoken.
    * Medium: In addition to NVDA's essential navigation information, some extra information will be added. For example, when an object has a shortcut key associated with it, you will hear the information “shortcut” before the shortcut key is announced. You will also hear the “value” information before announcing the value of the sliders and scroll bars.
    * Long: The add-on will add another set of information on top of the above. When you navigate through the items in a list, tree view or menus, you will hear the corresponding information according to the type of item. The add-on will also warn you whenever a window is activated. This is the default setting.
    * Custom: With this option, you can individually control all the information announced by the add-on.

#### Settings for the custom level

By setting the message extension level to “Custom”, you can individually adjust all the information announced by the add-on, for example, you can deactivate the information you don't want or don't need to be announced. You can do this via the “Configure” button. This button is only available when the custom message extension level is selected. Clicking this button opens a configuration dialog for the custom level, with the following options:

* Select the controls to be announced: In this list, you can activate or deactivate all the control types supported by the add-on. For deactivated controls, only the name and status (if applicable) will be announced.

* Other additional messages: This group of controls contains the following options:
    * Announce active windows: Announces whenever a window is activated.
    * Announce shortcut before object shortcut keys: When an object has an associated shortcut key, it announces the “shortcut” information before the corresponding shortcut key is announced.
    * Announce value before slider and scrollbar values: When focusing on a slider or scroll bar, it announces the “value” information before the value is announced.

## Known issues

* On web pages, the behavior of the add-on can be unpredictable. For now, paused reading doesn't always work as expected and objects are read repeatedly.
* In some cases, the announcement of states may fail or be incorrect.
    * When a checkbox is checked, unchecking it causes the “checked” state to be announced incorrectly.
    * When a toggle button is pressed or a list item is selected, deactivating the button or deselecting the item does not announce them.
    * This fault only occurs the first time you deselect a checkbox, deactivate a toggle button or deselect a list item with the Spacebar or Control+Spacebar.
    * To be sure, you can use the NVDA+Tab shortcut to have the information repeated by NVDA. In this case, the status will be announced correctly.
* In some types of menus, such as those in Thunderbird, the reading is a little strange. The information “submenu” is announced several times, even when it is not necessary. In these cases, until a solution to this problem is found, it is recommended to temporarily disable the add-on via the shortcut key when navigating through Thunderbird menus and other similar menus.
* In some types of dialog boxes that do not have an associated title, their content is not automatically read by the add-on.
* The announcement of active windows, in certain cases, causes this information to be announced incorrectly, for example, when opening a combo box with the Alt+Down Arrow shortcut or when opening a context menu such as the one in Google Chrome.

## Integration with DeltaTalk

The DeltaTalk synthesizer in dedicated format for NVDA is already fully developed, so the functionality of this add-on has been integrated into the synthesizer as a module called “Virtual Vision Mode”. So this will be the last independent version of this add-on.

Special thanks to Chat GPT for his exhaustive collaboration in the development of this add-on as an initial prototype, and also to Claude for his help with the additional tweaks that greatly improved the functionality, and to Groc for his help in fixing the last few bugs before the latest version was released.

Special thanks also to all the people who tried out this prototype and contributed with error reports and very valuable suggestions.

## Change history

### Version 0.5

* The “internal_link” status (which identifies links to the same page) has been added to the list of states to be announced.
* A few more controls have also been added to the list of control types to be announced.
* A logic has been created that checks for the presence of the old version of the add-on and removes it before installing this new version.
* The add-on is now available in the NVDA add-ons store. Just search for “Pausing Information”.
* Fixed an issue where Settings for the custom message extension level were lost when NVDA was restarted or when its language was changed.
* The code of the add-on has been simplified and unnecessary and repeated parts have been removed to make it easier to maintain.
* The add-on functionality has been integrated into DeltaTalk as “Virtual Vision Mode”, so this will be the last stand-alone version.

### Version 1.4

* Fixed an error with the announcement of active windows that caused the first item not to be announced when focusing on the taskbar or switching between tasks with the Alt+Tab shortcut. This problem also affected some items in normal windows, which were ignored.

### Version 1.3

* First official release version.
* A customized message extension level has been implemented, which allows you to individually control all the information announced by the add-on.
* A new configuration option has been created to completely disable the add-on.
* An enable/disable hotkey has also been implemented, which is especially useful for temporarily disabling the add-on in certain cases.

### Version 1.2

* Private test version, initially released as 1.1 and later updated to 1.2.
* A new configuration option has been created that allows you to choose whether or not the add-on should translate the names of the types and states of the controls.
* A logic of message extension levels has been implemented - long, medium and short. At the long level (default), all possible information will be spoken. At the medium level, some information will be suppressed and at the short level, only the essential information will be spoken.

### Version 1.1

* A new interface has been created for the add-on, with the first concept of configuration options.
* An error has been fixed in which the description of certain objects and the contents of some dialog boxes were not read.
* Fixed a bug where the value of progress bars was not read automatically.
* Fixed a bug where links contained in e-mail messages and web pages could not be focused correctly.
* A problem with reading Excel cells has been fixed.
* A logic has been created to check whether the read-only status is relevant, in order to avoid unnecessary announcements.

### Version 1.0

* Completely rewritten version from the initial prototype, with several error corrections.
* A complete dictionary has been created with the names of the control types and states, with their respective translations, which will be updated as necessary.
* The documentation has been rewritten and will be updated regularly.

### Version 0.1

* Initial prototype, created with very few resources and not yet very functional.
* Creation of the initial documentation.