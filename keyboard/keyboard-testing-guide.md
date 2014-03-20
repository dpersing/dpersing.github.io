# Keyboard testing guide

Quick and dirty guide for testing keyboard-only support for native controls in up-to-date browser versions on Windows and OSX.

_Last test date: March 20, 2014_

Please let me know if you find mistakes.

**All interactive elements should receive keyboard focus with the Tab key. To move backwards to the previous element, use Shift + Tab.**

Most browers receive the same keystrokes for manipulation, with a few gnarly exceptions:

## Links

Fire a link with the **Enter** key.

##Buttons

Fire a button with the **Enter** _or_ **Spacebar** key. (Browsers receive both; native OS buttons take a Spacebar.)

## Checkboxes

Individual checkboxes should receive keyboard focus with **Tab**/**Shift + Tab**.

To check/uncheck a box, use the **Spacebar**.

## Radio buttons

### Everything except Firefox on Windows

Once a radio button set receives focus, move the selection of a radio button within a set with the **up and down arrow keys**.

Use **Tab/Shift + Tab** to move to the next/previous interactive element after you've set the selected radio button.

### Firefox on Windows

The above works, but individual radio buttons can also receive Tab/Shift + Tab focus for some reason.

## Text inputs

Text fields should be able to accept regular typing once they have focus.

## Textareas

Textareas should be able to receive regular typing once they have focus.

## Select elements

These are quite different in different browsers.

### Internet Explorer and Chrome on Windows

There are two options. After the select box has focus, either:

* Use the **up and down arrow keys** to navigate through the list of options like a spinner, then use **Tab/Shift + Tab** to navigate away, _or_
* Use the **Spacebar** to open the select element, use the **up and down arrow keys** to choose an option, then close the select element with the **Enter** key

Personally I think the first option is easier.

### Safari and Chrome on OSX

Use the **up and down arrow keys** to navigate to an option. The options will pop up automatically. (Accordingly, VoiceOver on OSX calls these elements "popup buttons".)

Use the **Spacebar** to close the opened select element.

### Firefox on Windows and OSX

Use the **up and down arrow keys** to navigate to an option. The select element will spin through the options, like in IE. Use **Tab/Shift + Tab** to move away after your selection has been made.
    
