#!/usr/bin/env python3
"""
Program : Alphabet Soup
Author  : Jon Freivald <jfreivald@brmedical.com>
        : Copyright (C) Blue Ridge Medical Center, 2023
        : License: GNU GPL Version 3
Date    : 2023-10-20
Purpose : Acronym Lookup Tool
        : Version change log at EoF.
"""

import openpyxl
import argparse
import PySimpleGUI as sg
import os
import pickle
from datetime import datetime
import pytz

progver = 'v 1.03(e)'
mainTheme = 'Kayak'
errorTheme = 'HotDogStand'
config_file = (f'{os.path.expanduser("~")}/as_config.dat')
tz_NY = pytz.timezone('America/New_York')

# --------------------------------------------------
def get_args():
	"""Process any command line arguments"""

	parser = argparse.ArgumentParser(
		description='Alphabet Soup (Acronym Lookup Tool)',
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument('-f',
		'--file',
		help='The soup. (source spreadsheet)',
		metavar='filename',
		type=str,
		default='//brmc-fs2012.int.brmedical.com/STAFF/Jon/Administrative/BRMC Acronyms.xlsx')

	args = parser.parse_args()

	return args

# --------------------------------------------------
def unique_list(list):
     
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    return(unique_list)

# --------------------------------------------------
def get_data(args):

    aList = [] # Acronyms
    dList = [] # Definitions
    theFile = openpyxl.load_workbook(args.file)

    m_dt = os.path.getmtime(args.file)
    updated = datetime.fromtimestamp(m_dt).strftime("%m/%d/%y @ %H:%M")
    
    currentSheet = theFile['AlphabetSoup']
    acronym = ''
    for row in range(5, currentSheet.max_row + 1): # start @ 5 because that's the first row with actual data
        cellA = (f'A{row}')
        cellB = (f'B{row}')
        if currentSheet[cellA].value != None: # We were pulling blank rows for some reason -- filter them out!
            if currentSheet[cellA].value != acronym:
                acronym = currentSheet[cellA].value
            definition = currentSheet[cellB].value
            aList.append(acronym)
            dList.append([acronym, definition])
    return unique_list(aList), dList, updated

# --------------------------------------------------
def filter_data(acronym, dList):
    tList = [] # Temp List
    for i in dList:
        if i[0] == acronym:
            tList.append(i[1])
    return tList

# --------------------------------------------------
def get_user_settings():

    user_config = {}

    try:
        with open(config_file, 'rb') as fp:
            user_config = pickle.load(fp)
        fp.close()
    except:
        user_config['Theme'] = mainTheme

    return user_config

# --------------------------------------------------
def write_user_settings(user_config):

    try:
        with open(config_file, 'wb') as fp:
            pickle.dump(user_config, fp)
        fp.close()
    except:
        sg.theme(errorTheme)
        layout = [ [sg.Text(f'File or data error: {config_file}. Updates NOT saved!')],
					[sg.Button('Quit')] ]
        window = sg.Window('FILE ERROR!', layout, finalize=True)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Quit'): # if user closes window or clicks quit
                window.close()
                return


# --------------------------------------------------
def check_theme(theme, user_config, winLoc):
    
    list1 = ['AAA', 'BBB', 'IRS']
    list2 = ['American Automobile Association', 'Better Business Bureau', 'Internal Revenue Serivce']

    sg.theme(theme)
    layout = [ [sg.Text('Themes take effect immediately.')],
                [sg.Listbox(values = list1, size=(5, 3), key='folks', default_values=list1[0]), sg.Listbox(values = list2, size=(25, 3), key='places', default_values=list1[0])],
                [sg.Button('Keep'), sg.Button('Cancel')] ]
    window = sg.Window('Theme sampler', layout, location=winLoc, element_justification='center', finalize=True)
    window.BringToFront()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Cancel'): # if user closes window or clicks cancel
            break
        if event == 'Keep':
            user_config['Theme'] = theme
            write_user_settings(user_config)
            break
    
    window.close()

# --------------------------------------------------
def time_warning(quit_time, user_config):

    sg.theme(errorTheme)
    layout = [ [sg.Text(f'Program auto-closing at {quit_time}')],
                [sg.Button('Cancel', bind_return_key=True)] ]
    window = sg.Window('Error Message', layout, location=user_config['winLoc'], modal=True, finalize=True)
    while True:
        event, values = window.read(timeout=500)
        now = datetime.now(tz_NY)
        if event in (sg.WIN_CLOSED, 'Cancel'): # if user closes window or clicks abort
            window.close()
            return False
        if now.strftime("%H:%M") == quit_time:
            return True

# --------------------------------------------------
def find_acronym():

    args = get_args()
    user_config = get_user_settings()
    if 'winLoc' in user_config:
        winLoc = user_config['winLoc']
    else:
        winLoc = (2, 2)
    warn_time = '21:25'
    quit_time = '21:30'
    quit_now = False
    now = datetime.now(tz_NY)
    input_width = 20
    num_items_to_show = 5
    num_defs_to_show = 3

    menu_def = [
                ['&Theme', [sg.theme_list()]],
                [user_config['Theme'], []]
                ]
    menu_dispatcher = {}
    for t in sg.theme_list():
        menu_dispatcher[t] = check_theme
    
    aList = [] # Acronym List
    dList = [] # Definition List
    fList = [] # Filtered List
    aList, dList, updated = get_data(args)

    sg.theme(user_config['Theme'])
    
    layout = [  [sg.Menu(menu_def, text_color='black', font='SYSTEM_DEFAULT', pad=(10,10))],
                [sg.Input(size=(input_width, 1), enable_events=True, key='-IN-'), sg.Listbox(values = fList, size=(100, num_defs_to_show), key='-OUT-')],
                [sg.pin(sg.Col([[sg.Listbox(values=[], size=(input_width, num_items_to_show), enable_events=True, key='-BOX-',
                                    select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)]],
                       key='-BOX-CONTAINER-', pad=(0, 0), visible=False))],
                [sg.Button('Quit'), sg.Push(), sg.Text('Copyright (C) Blue Ridge Medical Center, 2023')] ]
    
    window = sg.Window(f'Alphabet Soup Acronym Lookup Tool {progver}', layout, return_keyboard_events=True, location=winLoc, finalize=True)

    list_element:sg.Listbox = window.Element('-BOX-')           # store listbox element for easier access and to get to docstrings
    prediction_list, input_text, sel_item = [], "", 0
    window['-IN-'].set_focus()
    window.BringToFront()

    while True:
        # Force everyone out once per night so we can do updates as needed.
        # This only works if the users system does not sleep! Publish the need to log out on the user group!
        now = datetime.now(tz_NY)
        if now.strftime("%H:%M") == warn_time:
            quit_now = time_warning(quit_time, user_config)
        if quit_now:
            break
        try:
            if updated != datetime.fromtimestamp(os.path.getmtime(args.file)).strftime("%m/%d/%y @ %H:%M"):
                aList, dList, updated = get_data(args)
                fList = []
        except:
            pass
            
        event, values = window.read(timeout=5000)
        winLoc = window.CurrentLocation()

        if event in (sg.WINDOW_CLOSED, 'Quit'): # if user closes window
            if event == 'Quit':     # If they "x-out" of the window, there is an error trying to get window.CurrentLocation()
                user_config['winLoc'] = winLoc
                write_user_settings(user_config)
            break
        elif event.startswith('Escape'):
            window['-IN-'].update('')
            window['-BOX-CONTAINER-'].update(visible=False)
            window['-OUT-'].update('')
            
        elif event.startswith('Down') and len(prediction_list):
            sel_item = (sel_item + 1) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
            
        elif event.startswith('Up') and len(prediction_list):
            sel_item = (sel_item + (len(prediction_list) -1)) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
            
        elif event == '\r' or event.startswith('Return'):
            if len(values['-BOX-']) > 0:
                window['-IN-'].update(value=values['-BOX-'])
                window['-BOX-CONTAINER-'].update(visible=False)
                fList = filter_data(str(values['-BOX-'][0]), dList)
                window['-OUT-'].update(sorted(fList))
            
        elif event == '-IN-':
            text = values['-IN-'].lower()
            if text == input_text:
                continue
            else:
                input_text = text
            prediction_list = []
            if text:
                prediction_list = [item for item in aList if item.lower().startswith(text)]
            
            list_element.update(values=prediction_list)
            sel_item = 0
            list_element.update(set_to_index=sel_item)

            if len(prediction_list) > 0:
                window['-BOX-CONTAINER-'].update(visible=True)
            else:
                window['-BOX-CONTAINER-'].update(visible=False)
            
        elif event == '-BOX-':
            window['-IN-'].update(value=values['-BOX-'])
            window['-BOX-CONTAINER-'].update(visible=False)
            
        elif event in menu_dispatcher:
            old_theme = user_config['Theme']
            menu_dispatcher[event](event, user_config, winLoc)
            if old_theme != user_config['Theme']:
                menu_def = [
                    ['&Theme', [sg.theme_list()]],
                    [user_config['Theme'], []]
                    ]
                sg.theme(user_config['Theme'])
                layout = [  [sg.Menu(menu_def, text_color='black', font='SYSTEM_DEFAULT', pad=(10,10))],
                    [sg.Input(size=(input_width, 1), enable_events=True, key='-IN-'), sg.Listbox(values = fList, size=(100, num_defs_to_show), key='-OUT-')],
                    [sg.pin(sg.Col([[sg.Listbox(values=[], size=(input_width, num_items_to_show), enable_events=True, key='-BOX-',
                                        select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)]],
                        key='-BOX-CONTAINER-', pad=(0, 0), visible=False))],
                    [sg.Button('Quit'), sg.Push(), sg.Text('Copyright (C) Blue Ridge Medical Center, 2023')] ]
                window.close()
                window = sg.Window(f'Alphabet Soup Acronym Lookup Tool {progver}', layout, return_keyboard_events=True, location=winLoc, finalize=True)
                list_element:sg.Listbox = window.Element('-BOX-')           # store listbox element for easier access and to get to docstrings
                prediction_list, input_text, sel_item = [], "", 0
                window.BringToFront()
                window['-OUT-'].update("")
                window['-IN-'].set_focus()
                
    
    window.close()

# --------------------------------------------------
if __name__ == '__main__':
	find_acronym()
        
"""Change log:

    v 1.0           : Yeah, that. Based on IQT v1.1(b) and the PySimpleGui typeahead demo code.
    v 1.01          : VPN latency was causing the program to crash if it couldn't see the source file
                    :   to check for update. Placed that section of code into a try/except block. It
                    :   still needs to see the file on start-up.
    v 1.02          : Changed button from 'Done' to 'Quit' to alleviate user confusion.
    v 1.02(a)       : Minor layout tweaks.
    v 1.02(b)       : Minor refactoring.
    v 1.03          : Completely redid Theme menu -- now pulls all available themes from PySimpleGui
                    :   as options for the users to choose.
    v 1.03(a)       : Added display of currently selected theme to menu bar.
    v 1.03(b)       : Change theme now takes effect immediately.
    v 1.03(c)       : Minor tweak to dynamic theme scheme. Window will only respawn if theme was actually changed.
    v 1.03(d)       : Fixed bug in window respawn scheme.
    v 1.03(e)       : Updated event capturing return key to perform cross-platform.
				    : 231205	: Added date to comments, because I always forget to update it in the header.
"""