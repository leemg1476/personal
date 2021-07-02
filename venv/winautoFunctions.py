from pywinauto import Application
import pywinauto
from pywinauto import keyboard
import re


def close_all_window():

    n = len(pywinauto.findwindows.find_elements())
    for i in range(n//2):
        tab = '{TAB}'
        keyboard.send_keys('%{TAB}')
        keyboard.send_keys('%{F4}')


def shutdown_computer():

    keyboard.send_keys('{LWIN down}''{x down}''{LWIN up}''{x up}')
    keyboard.send_keys('{u}{u}')


def search_keyword(s,window):

    textbox=window['앱 바'].child_window(control_type='Edit')
    textbox.set_edit_text(s)
    keyboard.send_keys('{ENTER}')

if __name__ == '__main__':
    pass



