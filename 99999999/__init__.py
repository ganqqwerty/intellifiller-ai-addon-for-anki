from aqt import mw
from aqt.qt import *
from aqt.gui_hooks import editor_did_init_buttons
from aqt.editor import EditorMode, Editor
from aqt.browser import Browser
from aqt.editcurrent import EditCurrent
from aqt.addcards import AddCards
from anki.hooks import addHook
import os

from .settings_editor import SettingsWindow
from .process_notes import process_notes, generate_for_single_note
from .run_prompt_dialog import RunPromptDialog


ADDON_NAME = 'IntelliFiller'


def create_run_prompt_dialog_from_browser(browser, prompt_config):
    dialog = RunPromptDialog(browser, browser.selectedNotes(), prompt_config)
    if dialog.exec_() == QDialog.DialogCode.Accepted:
        updated_prompt_config = dialog.get_result()
        process_notes(browser, updated_prompt_config)

def create_run_prompt_dialog_from_editor(editor: Editor, prompt_config):
    '''parentWindow can be either Browser (when we are viewing the list of cards) or EditCurrent when we click edit
    button while we are reviewing cards. See EditorMode for details '''
    if editor.editorMode == EditorMode.BROWSER:
        browser: Browser = editor.parentWindow
        dialog = RunPromptDialog(browser, browser.selectedNotes(), prompt_config)
        if dialog.exec_() == QDialog.DialogCode.Accepted:
            updated_prompt_config = dialog.get_result()
            process_notes(browser, updated_prompt_config)
        return
    if editor.editorMode == EditorMode.EDIT_CURRENT:
        editCurrentWindow: EditCurrent = editor.parentWindow
        dialog = RunPromptDialog(editCurrentWindow, [editor.note.id], prompt_config )
        if dialog.exec_() == QDialog.DialogCode.Accepted:
            updated_prompt_config = dialog.get_result()
            generate_for_single_note(editor, updated_prompt_config)
        return
    if editor.editorMode == EditorMode.ADD_CARDS:
        addCardsWindow: AddCards
        pass



def add_context_menu_items(browser, menu):
    submenu = QMenu(ADDON_NAME, menu)
    menu.addMenu(submenu)
    config = mw.addonManager.getConfig(__name__)

    for prompt_config in config['prompts']:
        action = QAction(prompt_config["promptName"], browser)
        action.triggered.connect(lambda _, br=browser, pc=prompt_config: create_run_prompt_dialog_from_browser(br, pc))
        submenu.addAction(action)


def open_settings():
    window = SettingsWindow(mw)
    window.exec_()


def on_editor_button(editor):
    prompts = mw.addonManager.getConfig(__name__).get('prompts', [])

    menu = QMenu(editor.widget)
    for i, prompt in enumerate(prompts):
        action = QAction(f'Prompt {i + 1}: {prompt["promptName"]}', menu)
        action.triggered.connect(lambda _, p=prompt: create_run_prompt_dialog_from_editor(editor, p))
        menu.addAction(action)

    menu.exec_(editor.widget.mapToGlobal(QPoint(0, 0)))


def on_setup_editor_buttons(buttons, editor):
    icon_path = os.path.join(os.path.dirname(__file__), "icon.svg")
    btn = editor.addButton(
        icon=icon_path,
        cmd="run_prompt",
        func=lambda e=editor: on_editor_button(e),
        tip=ADDON_NAME,
        keys=None,
        disables=False
    )
    buttons.append(btn)
    return buttons


addHook("browser.onContextMenu", add_context_menu_items)
mw.addonManager.setConfigAction(__name__, open_settings)
editor_did_init_buttons.append(on_setup_editor_buttons)
