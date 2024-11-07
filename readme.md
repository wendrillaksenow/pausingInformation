## “Pausing Information” add-on for NVDA

## Description

The “Pausing Information” add-on for NVDA is an extension that provides a more detailed and paused reading of control and status information when the focus shifts between interface elements.

This feature was inspired by the Brazilian screen reader “Virtual Vision”, known for its paused way of announcing information, improving user comprehension.

## Features

* Announcement of control types and states: The add-on announces the type of control (e.g. “checkbox”, “Radio button”, “menu”, “edit box”) and its status (e.g. “checked”, “pressed”, “unavailable”, “busy”).
* The announcement is made in a paused manner, similar to what was done by the Virtual Vision screen reader.

## Use

After installation, the add-on works automatically, allowing a more detailed and paused reading of information about the types and states of controls. No additional configuration is required.

## Notes

* The reading of the selected text is not fully functional and may fail in some cases. However, adjustments have been made to improve operation.
* In some cases, the control status is not announced, for example when a checkbox is not checked or a toggle button is not pressed. Some further adjustments will be made to try to correct this problem.
* On web pages, the behavior of the add-on can be unpredictable. for now, paused reading doesn't always work as expected and objects are read repeatedly.
* Paused reading is based exclusively on the punctuation level, since hyphens are added to pause the reading of information. If the punctuation level is set to anything above “some”, the hyphens will be read aloud.
* Likewise, if the symbols (specifically the hyphen) are not correctly adjusted in the punctuation/symbol pronunciation dialog, the pauses may not occur.
* To ensure that pauses work as expected, go to the punctuation/symbol pronunciation dialog and make sure that the hyphen is set to be sent to the synthesizer when it is below the symbol level.
* For very advanced users: If you don't want to hear the phrase “list item”, “tree view item” and “menu item” when scrolling through the respective items, simply open the code for the extra in “globalPlugins\pausingInfo.py” and modify the lines for “ListItem”, “TreeViewItem” and “MenuItem”, replacing the phrases in quotes with a space and restart NVDA after saving the file. Please note that this should only be done by very experienced users! The possibility of implementing a settings dialog in the future is being considered, which will allow the user to customize the add-on according to their tastes or needs.

## Future Development

This add-on was created as a prototype. When the DeltaTalk synthesizer add-on for NVDA is fully developed, the functionality of this prototype will be included as part of the add-on.

Special thanks to Chat GPT for his exhaustive collaboration in the development of this prototype, and also to Claude for his help with the additional tweaks that greatly improved functionality.

## Change history

### Version 1.0

* Completely rewritten version from the initial prototype, with several error corrections.
* A complete dictionary has been created with the names of the control types and states, with their respective translations, which will be updated as necessary.
* The documentation has been rewritten and will be updated regularly.

### Version 0.1

* Initial prototype, created with very few resources and not yet very functional.
* Creation of the initial documentation.