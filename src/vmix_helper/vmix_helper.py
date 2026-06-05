#################################################Options section
version = '0.9.5'
registered_modifiers = []
vmix_process_name = 'vmix64.exe'
vmix_port = 8088
http_file_server_port = 80
menu_settings = {'enable_auto_powerpoint_pause':True,
                 'enable_change_layers_input_shortcuts':True,
                 'enable_framing_layout_on_click_output_window':True
                }

font_family = 'Segoe UI'
font_size = 10
font_weight = 'normal'

options = {
    vmix_process_name: {
        'call_functions': True,
        'send_key_stroks_to_vmix': False,
        'need_to_activate': False,
        'make_sure_its_always_on_top': False,
        'send_keys_to_first_match': True,
        'send_wm_keyup_also': True,
        'window_title_contain': ['vmix', 'find control'],
        'window_title_not_contain': ['screen'],
        'window_class_contain': ['windowsforms10'],
        'dont_activate_if_window_class_exist': [],
        'dont_activate_if_process_exist': [],
        'keys': {
            'page down': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'nextitem',
                            'input': 'active',
                            'call_same_function_to_layers_input': True,
                            'call_only_if_vmix_foreground': False
                        }
                    ]
                },
                'send_key_stroks_to_vmix': {
                    '': 'page down',
                    '.': '1'
                }
            },
            'page up': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'previousitem',
                            'input': 'active',
                            'call_same_function_to_layers_input': True,
                            'call_only_if_vmix_foreground': False
                        }
                    ]
                },
                'send_key_stroks_to_vmix': {
                    '': 'page up',
                    '.': '2'
                }
            },
            'f5': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'selectindex',
                            'input': 'active',
                            'value':'1',
                            'call_same_function_to_layers_input': True,
                            'call_only_if_vmix_foreground': False
                        }
                    ]
                },
                'send_key_stroks_to_vmix': {
                    '': 'f5',
                    '.': '3'
                }
            },
            'esc': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'selectindex',
                            'input': 'active',
                            'value':'1',
                            'call_same_function_to_layers_input': True,
                            'call_only_if_vmix_foreground': False
                        }
                    ]
                },
                'send_key_stroks_to_vmix': {
                    '': 'f5',
                    '.': '4'
                }
            },
        }
    },
    'powerpnt.exe': {
        'enable':True,
        'need_to_activate':True,
        'make_sure_its_always_on_top':True,
        'send_keys_to_first_match':True,
        'send_wm_keyup_also':True,
        'window_title_contain':[],
        'window_title_not_contain': [],
        'window_class_contain':['screenclass'],
        'dont_activate_if_window_class_exist':[],
        'dont_activate_if_process_exist':[],
        'keys':{
            'page down':{
                '':'page down',
            },
            'page up':{
                '':'page up',
            },
            'f5':{
                '':'home',
            },
            'esc':{
                '':'home',
            }
        }
    },
    'foreground': {
        'enable':True,
        'need_to_activate':True,
        'make_sure_its_always_on_top':False,
        'send_wm_keyup_also':True,
        'dont_activate_if_window_class_exist':[],
        'dont_activate_if_process_exist':['powerpnt.exe']
    }
}

layers_options = {
            'alt+a': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'setmultiviewoverlay',
                            'input': 'active',
                            'value':'1,preview',
                            'call_same_function_to_layers_input': False,
                            'call_only_if_vmix_foreground': True
                        }
                    ]
                }
            },
            'alt+s': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'setmultiviewoverlay',
                            'input': 'active',
                            'value':'2,preview',
                            'call_same_function_to_layers_input': False,
                            'call_only_if_vmix_foreground': True
                        }
                    ]
                }
            },
            'alt+d': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'setmultiviewoverlay',
                            'input': 'active',
                            'value':'3,preview',
                            'call_same_function_to_layers_input': False,
                            'call_only_if_vmix_foreground': True
                        }
                    ]
                }
            },
            'alt+f': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'setmultiviewoverlay',
                            'input': 'active',
                            'value':'4,preview',
                            'call_same_function_to_layers_input': False,
                            'call_only_if_vmix_foreground': True
                        }
                    ]
                }
            },
            'alt+z': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'setmultiviewoverlay',
                            'input': 'active',
                            'value':'1,',
                            'call_same_function_to_layers_input': False,
                            'call_only_if_vmix_foreground': True
                        }
                    ]
                }
            },
            'alt+x': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'setmultiviewoverlay',
                            'input': 'active',
                            'value':'2,',
                            'call_same_function_to_layers_input': False,
                            'call_only_if_vmix_foreground': True
                        }
                    ]
                }
            },
            'alt+c': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'setmultiviewoverlay',
                            'input': 'active',
                            'value':'3,',
                            'call_same_function_to_layers_input': False,
                            'call_only_if_vmix_foreground': True
                        }
                    ]
                }
            },
            'alt+v': {
                'call_functions': {
                    '': [
                        {
                            'function_name': 'setmultiviewoverlay',
                            'input': 'active',
                            'value':'4,',
                            'call_same_function_to_layers_input': False,
                            'call_only_if_vmix_foreground': True
                        }
                    ]
                }
            }
        }
#################################################Options section
#################################################translation section
####################english translation
translation_dict = {
    'About':
        'About',
    'Update python required modules':
        'Update python required modules',
    'Run on startup':
        'Run on startup',
    'FFmpeg/Gstreamer (Test)':
        'FFmpeg/Gstreamer (Test)',
    'Save PDF as images':
        'Save PDF as images',
    'HTTP file server to receive files':
        'HTTP file server to receive files',
    'Restart free trial':
        'Restart free trial',
    'Tools to install':
        'Tools to install',
    'Virtual Display Driver':
        'Virtual Display Driver',
    'VB-CABLE Virtual Audio Device':
        'VB-CABLE Virtual Audio Device',
    'FFmpeg':
        'FFmpeg',
    'K-Lite Codec Pack':
        'K-Lite Codec Pack',
    'Gstreamer':
        'Gstreamer',
    'VLC':
        'VLC',
    'MediaMTX':
        'MediaMTX',
    'Windhawk':
        'Windhawk',
    'Media Foundation Codecs For Windows 10 and 11':
        'Media Foundation Codecs For Windows 10 and 11',
    'Fullscreen':
        'Fullscreen',
    'Patch vMix settings':
        'Patch vMix settings',
    'Video downloader (YouTube/TikTok/etc)':
        'Video downloader (YouTube/TikTok/etc)',
    'Enable Virtual Display':
        'Enable Virtual Display',
    'Stop powerpoint input from autoplay':
        'Stop powerpoint input from autoplay',
    'Enable change layers input shortcuts':
        'Enable change layers input shortcuts',
    'Enable layers selection by mouse':
        'Enable layers selection by mouse',
    'Exit':
        'Exit',
    'Make sure python and pip is added to system environment variable PATH.':
        'Make sure python and pip is added to system environment variable PATH.',
    'vMix Helper && echo Please update python to version ^>=3.11':
        'vMix Helper && echo Please update python to version ^>=3.11',
    'vMix Helper installing required python module':
        'vMix Helper installing required python module',
    'PLEASE_INSTALL_GSTREAMER':
        'PLEASE_INSTALL_GSTREAMER',
    'vMix Helper version':
        'vMix Helper version',
    'Do you want to check for update?':
        'Do you want to check for update?',
    'Go to "Tools to install" Submenu to install.':
        'Go to "Tools to install" Submenu to install.',
    'ffmpeg not found!!.':
        'ffmpeg not found!!.',
    'Enter URL: ':
        'Enter URL: ',
    'Invalid URL! Please enter valid URL like "https://www.youtube.com/watch?v=ZJKLVXlPJfY".':
        'Invalid URL! Please enter valid URL like "https://www.youtube.com/watch?v=ZJKLVXlPJfY".',
    'Audio only':
        'Audio only',
    'Enter Number: ':
        'Enter Number: ',
    'Invalid choice! Please enter a number between 1 and 7.':
        'Invalid choice! Please enter a number between 1 and 7.',
    'Invalid choice! Please enter a number between 1 and 3.':
        'Invalid choice! Please enter a number between 1 and 3.',
    'Do you want to pause after finesh?':
        'Do you want to pause after finesh?',
    'Yes':
        'Yes',
    'No':
        'No',
    'Hit ENTER to exit...':
        'Hit ENTER to exit...',
    'Error':
        'Error',
    'Not able to enable Virtual Screen Make sure you installed the driver.':
        'Not able to enable Virtual Screen Make sure you installed the driver.',
    'Not able to disable Virtual Screen, try to disable it from Device manager.':
        'Not able to disable Virtual Screen, try to disable it from Device manager.',
    'Confirmation':
        'Confirmation',
    'Are you sure you want to patch vMix settings?':
        'Are you sure you want to patch vMix settings?',
    'PATCH_SETTINGS':
        '''
        These settings will be affected and set to:
        Hide Cursor = True
        On Top = True
        Video Renderer = EVR
        Application Priority = High
        High Output Performance Mode = True
        FFmpeg Extensions = *.here
        Direct Show Settings = Auto
        Web Controler = Enabled
        Web Controler Port = 8088
        External Output:
            External 1 => vMix Video / Streaming = Enable
            External 2 => vMix Video / Streaming = Enable
            External 3 => vMix Video / Streaming = Enable
            External 4 => vMix Video / Streaming = Enable
    ''',
    'Info':
        'Info',
    'Main Output':
        'Main Output',
    'Output 2':
        'Output 2',
    'Output 3':
        'Output 3',
    'Output 4':
        'Output 4',
    'Stretch it':
        'Stretch it',
    'None':
        'None',
    'Settings file patched successfully please restart vMix to take affect.':
        'Settings file patched successfully please restart vMix to take affect.',
    'here!':
        'here!',
    'PDF to image':
        'PDF to image',
    'Save settinges :':
        'Save settinges :',
    'File : ':
        'File : ',
    'Browse':
        'Browse',
    'Save Folder : ':
        'Save Folder : ',
    'DPI : ':
        'DPI : ',
    'Rotation : ':
        'Rotation : ',
    'Flip horizontal.':
        'Flip horizontal.',
    'Flip vertical.':
        'Flip vertical.',
    'Save':
        'Save',
    'Open file:':
        'Open file:',
    'Save folder:':
        'Save folder:',
    'Convert':
        'Convert',
    'Convert And Import to vMix':
        'Convert And Import to vMix',
    'Download and extract and run VDD.Control.*.zip.':
        'Download and extract and run VDD.Control.*.zip.',
    'Download and extract and run VBCABLE_Driver_Pack*.zip.':
        'Download and extract and run VBCABLE_Driver_Pack*.zip.',
    'Download ffmpeg-master-latest-win64-gpl.zip and extract it to C:\\ffmpeg and add it to system variable PATH. see https://www.youtube.com/watch?v=rWVaxSWvxUQ':
        'Download ffmpeg-master-latest-win64-gpl.zip and extract it to C:\\ffmpeg and add it to system variable PATH. see https://www.youtube.com/watch?v=rWVaxSWvxUQ',
    'Remove haali splitter first and download and install the mega version.':
        'Remove haali splitter first and download and install the mega version.',
    'Go to download section on the bottom.':
        'Go to download section on the bottom.',
    'Download and install MinGW 64-bit version runtime installer.':
        'Download and install MinGW 64-bit version runtime installer.',
    'Download and install VLC then copy folder "C:\\Program Files\\VideoLAN\\VLC" to "C:\\ProgramData\\vMix" and rename it to vlc64':
        'Download and install VLC then copy folder "C:\\Program Files\\VideoLAN\\VLC" to "C:\\ProgramData\\vMix" and rename it to vlc64',
    'Download and extract mediamtx_v*_windows_amd64.zip':
        'Download and extract mediamtx_v*_windows_amd64.zip',
    'Number of running processes':
        'Number of running processes',
    'Stopped running.':
        'Stopped running.',
    'ffplay is not installed. Please install ffmpeg and add it to system environment variable PATH.':
        'ffplay is not installed. Please install ffmpeg and add it to system environment variable PATH.',
    'Close all full screens':
        'Close all full screens',
    'Upload':
        'Upload',
    'Choose Files':
        'Choose Files',
    'Add More Files':
        'Add More Files',
    'Upload Files':
        'Upload Files',
    'No Chosen Files':
        'No Chosen Files',
    'Faild Uploads:':
        'Faild Uploads:',
    'No Errors':
        'No Errors',
    'Upload More Files':
        'Upload More Files',
    'Not found':
        'Not found',
    'Fatal error':
        'Fatal error',
    'Server may already running.':
        'Server may already running.',
    'Failed to get local ip address.\nMake sure you are connected to a network.':
        'Failed to get local ip address.\nMake sure you are connected to a network.',
    'Server is running on':
        'Server is running on',
    'All uploaded files will be saved to desktop folder.':
        'All uploaded files will be saved to desktop folder.',
    'Click OK to close the server.':
        'Click OK to close the server.',
    'Content-Type must be multipart/form-data':
        'Content-Type must be multipart/form-data',
    "Content doesn't begin with boundary":
        "Content doesn't begin with boundary",
    'Streaming Error:':
        'Streaming Error:',
    'Upload Results':
        'Upload Results',
    'Cut':
        'Cut',
    'Copy':
        'Copy',
    'Paste':
        'Paste',
    'Profiles:':
        'Profiles:',
    'Profile: ':
        'Profile: ',
    'Profile settinges :':
        'Profile settinges :',
    'Destination preset: ':
        'Destination preset: ',
    'Destination: ':
        'Destination: ',
    'Input video device: ':
        'Input video device: ',
    'Input audio device: ':
        'Input audio device: ',
    'Video encoder: ':
        'Video encoder: ',
    'Encoder preset: ':
        'Encoder preset: ',
    'Encoder profile: ':
        'Encoder profile: ',
    'Output video dimension: ':
        'Output video dimension: ',
    'Output video bitrate (kbps): ':
        'Output video bitrate (kbps): ',
    'Numbers of threads: ':
        'Numbers of threads: ',
    'Output video frame rate (fps): ':
        'Output video frame rate (fps): ',
    'Output audio encoder and settings: ':
        'Output audio encoder and settings: ',
    'Output audio bitrate (kbps): ':
        'Output audio bitrate (kbps): ',
    'Input buffer settings: ':
        'Input buffer settings: ',
    'Output buffer size (packets): ':
        'Output buffer size (packets): ',
    'Enable output buffer flush immediately.':
        'Enable output buffer flush immediately.',
    'Show console window.':
        'Show console window.',
    'Enable experimental (Required for AV1 encoding for stream).':
        'Enable experimental (Required for AV1 encoding for stream).',
    'Enable output audio.':
        'Enable output audio.',
    'Command :':
        'Command :',
    'The command':
        'The command',
    'Command template for one destination':
        'Command template for one destination',
    'Command template for multiple destinations':
        'Command template for multiple destinations',
    'Remove This Profile':
        'Remove This Profile',
    'Restore default':
        'Restore default',
    'Get address':
        'Get address',
    'Close all processes':
        'Close all processes',
    'Save Settings':
        'Save Settings',
    'Sart':
        'Sart',
    'Change settings profile name.':
        'Change settings profile name.',
    'Set a name for destination preset.':
        'Set a name for destination preset.',
    'Settings saved successful in':
        'Settings saved successful in',
    'Successful':
        'Successful',
    'Failed':
        'Failed',
    'Failed to delete this profile':
        'Failed to delete this profile',
    'Save file as:':
        'Save file as:',
    'Closing processes in progress please wait and try again.':
        'Closing processes in progress please wait and try again.',
    'Successfully started. You will get a messsage if process stoped.':
        'Successfully started. You will get a messsage if process stoped.',
    'NEW_PROFILE (KEEP_PREVIOUS_SETTINGS)':
        'NEW_PROFILE (KEEP_PREVIOUS_SETTINGS)',
    'NEW_PROFILE (DEFAULT_SETTINGS)':
        'NEW_PROFILE (DEFAULT_SETTINGS)',
    'Save to file':
        'Save to file',
    'Save to file (Open file browser)':
        'Save to file (Open file browser)',
    'Intel GPU, Not all GPU supports':
        'Intel GPU, Not all GPU supports',
    'Nvidia GPU, Not all GPU supports':
        'Nvidia GPU, Not all GPU supports',
    'AMD GPU, Not all GPU supports':
        'AMD GPU, Not all GPU supports',
    'CPU':
        'CPU',
    'All Available':
        'All Available',
    'HLS Template 3 Resolutions':
        'HLS Template 3 Resolutions',
    'Gstreamer send stream webrtc h264':
        'Gstreamer send stream webrtc h264',
    'Send to webrtc server (Gstreamer)':
        'Send to webrtc server (Gstreamer)',
    'Gstreamer receive webrtc h264 stream to srt listen mode on http://127.0.0.1:1234)':
        'Gstreamer receive webrtc h264 stream to srt listen mode on http://127.0.0.1:1234)',
    'Gstreamer webrtc server (Gstreamer) signaller and info':
        'Gstreamer webrtc server (Gstreamer) signaller and info',
    'Send to rtsp tcp server':
        'Send to rtsp tcp server',
    'Send to rtsp udp server':
        'Send to rtsp udp server',
    'ffmpeg as a SRT server (accept one client)':
        'ffmpeg as a SRT server (accept one client)',
    'ffmpeg as a SRT server (accept one client) and save to file (Mutiple destinations)':
        'ffmpeg as a SRT server (accept one client) and save to file (Mutiple destinations)',
    'Send to youtube live':
        'Send to youtube live',
    'Send to YouTube Live and save to file (Mutiple destinations)':
        'Send to YouTube Live and save to file (Mutiple destinations)',
    'Gstreamer webrtc server (Gstreamer) signaller and info':
        'Gstreamer webrtc server (Gstreamer) signaller and info',
    'Please select file input.':
        'Please select file input.',
    'Primary':
        'Primary',
    'Convert PDF to Pictures':
        'Convert PDF to Pictures'
}
#################################################translation section
def t(string):
    if string in translation_dict and translation_dict[string]!='':
        return translation_dict[string]
    return string

import os
import subprocess
import sys

if sys.version_info.major != 3 or sys.version_info.minor < 8:
    subprocess.Popen(f'cmd.exe /k "echo {t("vMix Helper && echo Please update python to version ^>=3.8")}"',creationflags=subprocess.CREATE_NEW_CONSOLE)
    os._exit(1)
    
import psutil

def is_already_running():
    pidfile = os.environ.get('TEMP', '') + '\\vmix-helper.pid'
    pid = 0
    try:
        if os.path.exists(pidfile):
            with open(pidfile, 'r') as f:
                pid = int(f.read().strip())
            if psutil.pid_exists(pid):
                process = psutil.Process(pid)
                if 'python' in process.name().lower():
                    return True
    except:
        pass
        
    try:    
        with open(pidfile, 'w') as f:
            f.write(str(os.getpid()))
        return False
    except:
        return False

if is_already_running():
    os._exit(0)
    
import time
import ctypes
import pystray
import keyboard
import requests
import mouse
import win32gui
import tkinter as tk
from PIL import Image, ImageTk
import base64
from io import BytesIO
import win32process
import win32con
import win32api
import threading
import ctypes
from ctypes import Array, Structure, Union, _Pointer, _SimpleCData, wintypes
import xml.etree.ElementTree as ET
import glob
from win32api import MapVirtualKey
from random import randint
import pickle
from collections import OrderedDict
import copy
import re
from tkinter import ttk, StringVar, IntVar, BooleanVar, messagebox, PhotoImage, filedialog
import signal
from datetime import datetime
import win32com.shell.shell as shell
import random
import string
########################################Globals section######################################################################################################################################################################

icon_base64 = 'AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAMqZAADKmQAAAAAAAAAAAAAZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPpsAML/AL14JKe9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JLO7diIAvXgkbL14JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+mwAwv8AvXgkp714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgks7t2IgC9eCRsvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6bADC/wC9eCSnvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCSzu3YiAL14JGy9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPpsAML/AL14JKe9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JLO7diIAvXgkbL14JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+mwAwv8AvXgkp714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgks7t2IgC9eCRsvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6bADC/wC9eCSnvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCSzu3YiAL14JGy9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPpsAML/AL14JKe9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JLO7diIAvXgkbL14JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+mwAwv8AvXgkp714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgks7t2IgC9eCRsvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6/xmk+v8ZpPr/GaT6bADC/wC9eCSnvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCSzu3YiAb14JGy9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP8YpPtsGKT7bBik+2wYpPtsGKT7bBik+2wYpPtsGKT7bBik+20YpPsuAMH/AL14JEe9eCRuvXgkbL14JGy9eCRsvXgkbL14JGy9eCRsvXgkbr14JEy7diIAvXgkLr14JG29eCRsvXgkbL14JGy9eCRsvXgkbL14JGy9eCRsvXgkbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAvXgks714JLO9eCSzvXgks714JLO9eCSzvXgks714JLO9eCS0vXgkTL15JAC9eCR1vXgktr14JLO9eCSzvXgks714JLO9eCSzvXgks714JLa9eCR+u3YiAL14JEy9eCS0vXgks714JLO9eCSzvXgks714JLO9eCSzvXgks714JLO9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCRsvXkkAL14JKe9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JLO7diIBvXgkbL14JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JGy9eSQAvXgkp714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgks7t2IgC9eCRsvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgkbL15JAC9eCSnvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCSzu3YiAL14JGy9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCRsvXkkAL14JKe9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JLO7diIAvXgkbL14JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JGy9eSQAvXgkp714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgks7t2IgC9eCRsvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgkbL15JAC9eCSnvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCSzu3YiAL14JGy9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCRsvXkkAL14JKe9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JLO7diIAvXgkbL14JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JGy9eSQAvXgkp714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgks7t2IgG9eCRsvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgkp714JKe9eCSnvXgkp714JKe9eCSnvXgkp714JKe9eCSovXgkR715JAC9eCRuvXgkqr14JKe9eCSnvXgkp714JKe9eCSnvXgkp714JKq9eCR1u3YiAL14JEe9eCSovXgkp714JKe9eCSnvXgkp714JKe9eCSnvXgkp714JKcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL14JGy9eCRsvXgkbL14JGy9eCRsvXgkbL14JGy9eCRsvXgkbb14JC69eSQAvXgkR714JG69eCRsvXgkbL14JGy9eCRsvXgkbL14JGy9eCRuvXgkTP8AAABJtkEuSbZBbUm2QWxJtkFsSbZBbEm2QWxJtkFsSbZBbEm2QWxJtkFsvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgkbL15JAC9eCSnvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCSz/wAAAUm2QWxJtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCRsvXkkAL14JKe9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JLP/AAAASbZBbEm2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JGy9eSQAvXgkp714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgks/8AAABJtkFsSbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgkbL15JAC9eCSnvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCSz/wAAAEm2QWxJtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCRsvXkkAL14JKe9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JLP/AAAASbZBbEm2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JGy9eSQAvXgkp714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgks/8AAABJtkFsSbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgkbL15JAC9eCSnvXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCSz/wAAAEm2QWxJtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCRsvXkkAL14JKe9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JLP/AAAASbZBbEm2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JGy9eSQAvXgkp714JP+9eCT/vXgk/714JP+9eCT/vXgk/714JP+9eCT/vXgks/8AAABJtkFsSbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/SbZB/0m2Qf9JtkH/ACAEAAAgBAAAIAQAACAEAAAgBAAAIAQAACAEAAAgBAAAIAAAACAEAP////8AIAQAACAAAAAgBAAAIAQAACAEAAAgBAAAIAQAACAEAAAgAAAAIAQA/////wAgBAAAIAAAACAEAAAgBAAAIAQAACAEAAAgBAAAIAQAACAEAAAgBAA='
icon = Image.open(BytesIO(base64.b64decode(icon_base64)))
modifier = ''
ffmpeg_processes = []
enable_startup = False
ffmpeg_processes_closing_is_running = False
vmix_process_name = vmix_process_name.lower()
keys_add_to_hotkey = []
modifiers_add_to_hotkey = []
frame_thread_1 = None
options_backup = None
layers_keys_add_to_hotkey = []
settings_window_is_up = False
power_point_thread = None
tk_settings_window = None
tk_pdf2png_window = None
tk_fullscreen_window = None
virtual_audio_device_id = t("PLEASE_INSTALL_GSTREAMER")
systray = None
old_all_monitors = []
fullscreen_ffplay = {}
key_codes = {
    'backspace':0x08,'tab':0x09,'clear':0x0C,'enter':0x0D,'shift':0x10,'ctrl':0x11,'alt':0x12,'pause':0x13,'caps lock':0x14,'esc':0x1B,'space':0x20,'page up':0x21,'page down':0x22,'end':0x23,'home':0x24,'left':0x25,'up':0x26,
    'right':0x27,'down':0x28,'select':0x29,'print':0x2A,'execute':0x2B,'print screen':0x2C,'insert':0x2D,'delete':0x2E,'help':0x2F,
    '0':0x30,'1':0x31,'2':0x32,'3':0x33,'4':0x34,'5':0x35,'6':0x36,'7':0x37,'8':0x38,'9':0x39,
    'a':0x41,'b':0x42,'c':0x43,'d':0x44,'e':0x45,'f':0x46,'g':0x47,'h':0x48,'i':0x49,'j':0x4A,'k':0x4B,'l':0x4C,'m':0x4D,'n':0x4E,'o':0x4F,'p':0x50,'q':0x51,'r':0x52,'s':0x53,'t':0x54,'u':0x55,'v':0x56,'w':0x57,'x':0x58,'y':0x59,'z':0x5A,
    'left windows':0x5B,'right windows':0x5C,
    'applications':0x5D,'sleep':0x5F,
    'numpad 0':0x60,'numpad 1':0x61,'numpad 2':0x62,'numpad 3':0x63,'numpad 4':0x64,'numpad 5':0x65,'numpad 6':0x66,'numpad 7':0x67,'numpad 8':0x68,'numpad 9':0x69,
    '*':0x6A,'+':0x6B,'separator':0x6C,'-':0x6D,'decimal':0x6E,'/':0x6F,
    'f1':0x70,'f2':0x71,'f3':0x72,'f4':0x73,'f5':0x74,'f6':0x75,'f7':0x76,'f8':0x77,'f9':0x78,'f10':0x79,'f11':0x7A,'f12':0x7B,'f13':0x7C,'f14':0x7D,'f15':0x7E,'f16':0x7F,'f17':0x80,'f18':0x81,'f19':0x82,'f20':0x83,'f21':0x84,'f22':0x85,'f23':0x86,'f24':0x87,
    'num lock':0x90,'scroll lock':0x91,
    'left shift':0xA0,'right shift':0xA1,'left ctrl':0xA2,'right ctrl':0xA3,
    'left alt':0xA4,'right alt':0xA5,
    'browser back':0xA6,'browser forward':0xA7,'browser refresh':0xA8,'browser stop':0xA9,'browser search key':0xAA,'browser favorites':0xAB,'browser start and home':0xAC,
    'volume mute':0xAD,'volume down':0xAE,'volume up':0xAF,
    'next track':0xB0,'previous track':0xB1,'stop media':0xB2,'play/pause media':0xB3,'select media':0xB5,'start mail':0xB4,
    'start application 1':0xB6,'start application 2':0xB7,
    '+':0xBB,',':0xBC,'-':0xBD,'.':0xBE,'`':0xC0,'[':0xDB,'\\':0xDC,']':0xDD,'\'':0xDE,
    'ime process':0xE5,'attn':0xF6,'crsel':0xF7,'exsel':0xF8,'erase eof':0xF9,
    'play':0xFA,'zoom':0xFB,'reserved ':0xFC,'pa1':0xFD,'clear':0xFE
}

shell32 = ctypes.windll.shell32
user32 = ctypes.windll.user32
AttachThreadInput = user32.AttachThreadInput
AttachThreadInput.argtypes = [
    ctypes.wintypes.DWORD,
    ctypes.wintypes.DWORD,
    ctypes.wintypes.BOOL
]
AttachThreadInput.restype = ctypes.wintypes.BOOL

WM_DROPFILES = 0x0233
GWL_WNDPROC = -4
LRESULT = ctypes.c_ssize_t
WNDPROC_TYPE = ctypes.WINFUNCTYPE(LRESULT, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)
try:
    SetWindowLongPtr = user32.SetWindowLongPtrW
    SetWindowLongPtr.restype = WNDPROC_TYPE
    SetWindowLongPtr.argtypes = [wintypes.HWND, ctypes.c_int, WNDPROC_TYPE]
except AttributeError:
    SetWindowLongPtr = user32.SetWindowLongW
    SetWindowLongPtr.restype = WNDPROC_TYPE
    SetWindowLongPtr.argtypes = [wintypes.HWND, ctypes.c_int, WNDPROC_TYPE]
user32.CallWindowProcW.restype = LRESULT
user32.CallWindowProcW.argtypes = [WNDPROC_TYPE, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
shell32.DragQueryFileW.restype = wintypes.UINT
shell32.DragQueryFileW.argtypes = [wintypes.WPARAM, wintypes.UINT, wintypes.LPWSTR, wintypes.UINT]
shell32.DragFinish.restype = None
shell32.DragFinish.argtypes = [wintypes.WPARAM]
shell32.DragAcceptFiles.restype = None
shell32.DragAcceptFiles.argtypes = [wintypes.HWND, wintypes.BOOL]

class LUID(ctypes.Structure):
    _fields_ = [
        ('LowPart', wintypes.DWORD),
        ('HighPart', wintypes.LONG),
    ]

class DISPLAYCONFIG_RATIONAL(ctypes.Structure):
    _fields_ = [
        ('Numerator', wintypes.UINT),
        ('Denominator', wintypes.UINT),
    ]

class DISPLAYCONFIG_PATH_SOURCE_INFO(ctypes.Structure):
    _fields_ = [
        ('adapterId', LUID),
        ('id', wintypes.UINT),
        ('modeInfoIdx', wintypes.UINT),
        ('statusFlags', wintypes.UINT),
    ]

class DISPLAYCONFIG_PATH_TARGET_INFO(ctypes.Structure):
    _fields_ = [
        ('adapterId', LUID),
        ('id', wintypes.UINT),
        ('modeInfoIdx', wintypes.UINT),
        ('outputTechnology', wintypes.UINT),
        ('rotation', wintypes.UINT),
        ('scaling', wintypes.UINT),
        ('refreshRate', DISPLAYCONFIG_RATIONAL),
        ('scanLineOrdering', wintypes.UINT),
        ('targetAvailable', wintypes.BOOL),
        ('statusFlags', wintypes.UINT),
    ]

class DISPLAYCONFIG_PATH_INFO(ctypes.Structure):
    _fields_ = [
        ('sourceInfo', DISPLAYCONFIG_PATH_SOURCE_INFO),
        ('targetInfo', DISPLAYCONFIG_PATH_TARGET_INFO),
        ('flags', wintypes.UINT),
    ]

class DISPLAYCONFIG_2DREGION(ctypes.Structure):
    _fields_ = [('cx', wintypes.UINT), ('cy', wintypes.UINT)]

class DISPLAYCONFIG_VIDEO_SIGNAL_INFO(ctypes.Structure):
    _fields_ = [
        ('pixelRate', ctypes.c_uint64),
        ('hSyncFreq', DISPLAYCONFIG_RATIONAL),
        ('vSyncFreq', DISPLAYCONFIG_RATIONAL),
        ('activeSize', DISPLAYCONFIG_2DREGION),
        ('totalSize', DISPLAYCONFIG_2DREGION),
        ('videoStandard', wintypes.UINT),
        ('scanLineOrdering', wintypes.UINT),
    ]

class DISPLAYCONFIG_TARGET_MODE(ctypes.Structure):
    _fields_ = [('targetVideoSignalInfo', DISPLAYCONFIG_VIDEO_SIGNAL_INFO)]

class POINTL(ctypes.Structure):
    _fields_ = [('x', wintypes.LONG), ('y', wintypes.LONG)]

class DISPLAYCONFIG_SOURCE_MODE(ctypes.Structure):
    _fields_ = [
        ('width', wintypes.UINT),
        ('height', wintypes.UINT),
        ('pixelFormat', wintypes.UINT),
        ('position', POINTL),
    ]

class DISPLAYCONFIG_MODE_INFO_UNION(ctypes.Union):
    _fields_ = [
        ('targetMode', DISPLAYCONFIG_TARGET_MODE),
        ('sourceMode', DISPLAYCONFIG_SOURCE_MODE),
    ]

class DISPLAYCONFIG_MODE_INFO(ctypes.Structure):
    _fields_ = [
        ('infoType', wintypes.UINT),
        ('id', wintypes.UINT),
        ('adapterId', LUID),
        ('modeInfo', DISPLAYCONFIG_MODE_INFO_UNION),
    ]

class DISPLAYCONFIG_DEVICE_INFO_HEADER(ctypes.Structure):
    _fields_ = [
        ('type', wintypes.UINT),
        ('size', wintypes.UINT),
        ('adapterId', LUID),
        ('id', wintypes.UINT),
    ]

class DISPLAYCONFIG_TARGET_DEVICE_NAME(ctypes.Structure):
    _fields_ = [
        ('header', DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('flags', wintypes.UINT),
        ('outputTechnology', wintypes.UINT),
        ('edidManufactureId', wintypes.USHORT),
        ('edidProductCodeId', wintypes.USHORT),
        ('connectorInstance', wintypes.UINT),
        ('monitorFriendlyDeviceName', wintypes.WCHAR * 64),
        ('monitorDevicePath', wintypes.WCHAR * 128),
    ]
########################################Globals section########################################################################################################################################################################

def make_lparam(vk, scan_code, extended=False, previous_state=0, transition=0):
    repeat_count = 1
    extended_bit = 1 if extended else 0
    lparam = (
        (repeat_count & 0xFFFF) |
        ((scan_code & 0xFF) << 16) |
        (extended_bit << 24) |
        (previous_state << 30) |
        (transition << 31)
    )
    return lparam
    
def on_systray_click_exit(tray, item):
    close_all_full_screens()
    close_ffmpeg_thread(False)
    os._exit(0)

class power_point_thread_class(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            try:
                time.sleep(0.8)
                
                windows = []
                windows = get_windows_by_process(vmix_process_name)
                if len(windows)==0:
                    time.sleep(1)
                    continue
                
                page = f'http://127.0.0.1:{str(vmix_port)}/api/'
                try:
                    response = requests.get(page, timeout=0.2)
                except:
                    continue
                xmlDoc = ET.fromstring(response.text)
                activeNode = xmlDoc.find('./active')
                
                if activeNode is None:
                    activeNode = ''
                
                inputNode = xmlDoc.find(f'./inputs/input[@number=\'{activeNode.text}\']')
                if inputNode is None:
                    continue
                else:
                    active_type = inputNode.get('type').lower()
                    pause_types = ['powerpoint', 'photos']
                    if (active_type in pause_types):
                        send = f'http://127.0.0.1:{str(vmix_port)}/api/?Function=pause&input={activeNode.text}'
                        try:
                            response = requests.get(send, timeout=0.2)
                        except:
                            continue
                    for overlayNode in inputNode:
                        overlay_node = xmlDoc.find(f'./inputs/input[@key=\'{overlayNode.get("key")}\']')
                        overlay_type = overlay_node.get('type').lower()
                        if (overlay_type in pause_types):
                            send = f'http://127.0.0.1:{str(vmix_port)}/api/?Function=pause&input={overlay_node.get("number")}'
                            try:
                                response = requests.get(send, timeout=0.2)
                            except:
                                continue
            except:continue
    def stop(self):
        self._stop_event.set()

    
def on_systray_click_disable_powerpoint_play():
    global menu_settings
    global power_point_thread
    menu_settings['enable_auto_powerpoint_pause'] = not menu_settings['enable_auto_powerpoint_pause']
    if menu_settings['enable_auto_powerpoint_pause']:
        power_point_thread = power_point_thread_class()
        power_point_thread.start()
    else:
        power_point_thread.stop()
    save_settings_tofile()
    
def on_systray_click_enable_layers():
    global menu_settings
    global options
    global options_backup
    global layers_keys_add_to_hotkey
    menu_settings['enable_change_layers_input_shortcuts'] = not menu_settings['enable_change_layers_input_shortcuts']
    if menu_settings['enable_change_layers_input_shortcuts']:
        options_backup = options
        options[vmix_process_name]['keys'].update(layers_options)
        for key, value in layers_options.items():
            if (key not in keys_add_to_hotkey and key not in modifiers_add_to_hotkey):
                keyboard.add_hotkey(key, on_key_press, args=(key,), suppress=True)
                layers_keys_add_to_hotkey.append(key)
    else:
        options=options_backup
        for layer_key_add_to_hotkey in layers_keys_add_to_hotkey:
            keyboard.remove_hotkey(layer_key_add_to_hotkey)
        layers_keys_add_to_hotkey = []
        options_backup = None
    save_settings_tofile()

def on_systray_click_about():
    global version
    response = messagebox.askyesno('Success', f'{t("vMix Helper version")} {version}\n{t("Do you want to check for update?")}')
    if response:
        open_web('vmix-helper')
    
def on_systray_click_enable_framing_layers():
    global menu_settings
    global frame_thread_1
    try:
        menu_settings['enable_framing_layout_on_click_output_window'] = not menu_settings['enable_framing_layout_on_click_output_window']
        if menu_settings['enable_framing_layout_on_click_output_window']:
            frame_window_layout = frame_layout(root)
            frame_thread_1 = frame_thread(frame_window_layout)
            frame_thread_1.start()
        else:
            frame_thread_1.stop()
    except:
        pass
    save_settings_tofile()
        
def get_vdd_status():
    process = subprocess.Popen(['pnputil', '/enum-devices', '/instanceid', 'ROOT\\DISPLAY\\0000'], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
    stdout, stderr = process.communicate()
    try:
        status_line = [line for line in stdout.split('\n') if 'Status:' in line][0]
        status = status_line.split('Status:')[1].strip()
        return True if (status=='Enabled' or status=='Started') else False
    except:
        return False
    
enable_vdd = get_vdd_status()

def start_yt_dlp():
    dlp_script = f'''
@echo off
chcp 65001 > nul
where ffmpeg >nul
if %errorlevel% neq 0 (
    cls
    echo {t('ffmpeg not found!!.')}
    echo {t('Go to "Tools to install" Submenu to install.')}
    goto End
)

cls
:AskURL
set /p "url={t('Enter URL: ')}"
echo "%url%" | findstr /R "^""http[s]*://[a-z-A-Z-0-9.]*" >nul
if %errorlevel% equ 0 (
    cls
    goto AskQuality
) else (
    echo.
    echo {t('Invalid URL! Please enter valid URL like "https://www.youtube.com/watch?v=ZJKLVXlPJfY."')}
    echo.
    goto AskURL
)


:AskQuality
echo Select quality.
echo 1.480p
echo 2.720p
echo 3.1080p
echo 4.1440p
echo 5.2160p
echo 6.4320p
echo 7.{t('Audio only')}
echo.

set /p "op={t('Enter Number: ')}"

if "%op%"=="1" set "quality=480" && cls && goto SaveFolder
if "%op%"=="2" set "quality=720" && cls && goto SaveFolder
if "%op%"=="3" set "quality=1080" && cls && goto SaveFolder
if "%op%"=="4" set "quality=1440" && cls && goto SaveFolder
if "%op%"=="5" set "quality=2160" && cls && goto SaveFolder
if "%op%"=="6" set "quality=4320" && cls && goto SaveFolder
if "%op%"=="7" cls && goto SaveFolder
echo.
echo {t('Invalid choice! Please enter a number between 1 and 7.')}
echo.
goto AskQuality

:SaveFolder
echo Select Save Folder.
echo 1.Desktop
echo 2.Documents
echo 3.Videos
echo.

set /p "dest={t('Enter Number: ')}"

if "%dest%"=="1" set "destination=/Desktop" && cls && goto Final
if "%dest%"=="2" set "destination=/Documents" && cls && goto Final
if "%dest%"=="3" set "destination=/Videos" && cls && goto Final
echo.
echo {t('Invalid choice! Please enter a number between 1 and 3.')}
echo.
goto SaveFolder


:Final
echo {t('Do you want to pause after finesh?')}
echo y.{t('Yes')}
echo n.{t('No')}
set /p "pause=(y or n): "
if "%op%"=="7" goto AUDIOONLY

yt-dlp --windows-filenames --force-overwrites -S "+height:%quality%" -f "bv*+ba/b" -o ~%destination%/%%(title)s.%%(ext)s "%url%"
if "%pause%"=="y" goto End
goto End2

:AUDIOONLY
yt-dlp --windows-filenames --force-overwrites -f "ba" -o ~%destination%/%%(title)s.%%(ext)s "%url%"
if "%pause%"=="y" goto End
goto End2

:End
pause

:End2
    '''
    batfile = os.environ.get('TEMP', '') + '\\vmix-helper.bat'
    try:
        with open(batfile, 'w', encoding="utf-8") as f:
            f.write(dlp_script)
        import winreg
        os.environ['PATH']=os.path.expandvars(winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'System\CurrentControlSet\Control\Session Manager\Environment', 0, winreg.KEY_READ), 'Path')[0])
        subprocess.Popen(f'cmd.exe /c "{batfile}"',creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NEW_PROCESS_GROUP, env=os.environ.copy())
    except Exception as e:
        messagebox.showerror(t('Error'), e)

def on_systray_click_enable_vdd():
    global enable_vdd
    global systray
    if not enable_vdd:
        try:
            commands = '-NoProfile -ExecutionPolicy Bypass -Command "Get-PnpDevice -InstanceId \\"ROOT\\DISPLAY\\0000\\" | Enable-PnpDevice -Confirm:$false"'
            if shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters=commands):
                time.sleep(2)
                enable_vdd = get_vdd_status()
                systray.update_menu()
        except:
            messagebox.showerror(t('Error'), t('Not able to enable Virtual Screen Make sure you installed the driver.'))
    else:
        try:
            commands = '-NoProfile -ExecutionPolicy Bypass -Command "Get-PnpDevice -InstanceId \\"ROOT\\DISPLAY\\0000\\" | Disable-PnpDevice -Confirm:$false"'
            if shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters=commands):
                time.sleep(2)
                enable_vdd = get_vdd_status()
                systray.update_menu()
        except:
            messagebox.showerror(t('Error'), t('Not able to disable Virtual Screen, try to disable it from Device manager.'))

def preserve_namespaces(element):
    if 'ArrayOfString' in element.tag:
        element.set('xmlns:xsd', 'http://www.w3.org/2001/XMLSchema')
        element.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        
def on_systray_click_patch_settings():
    import html
    global root
    settings_is_changed = False
    CustomMessageBox(root,title=t('Info'),message=t('PATCH_SETTINGS'))
    response = messagebox.askyesno(t('Confirmation'), t('Are you sure you want to patch vMix settings?'))
    if response:
        folders = []
        config_file_name = []
        folders.append(r'%USERPROFILE%\\AppData\\Local\\StudioCoast_Pty_Ltd\\vMix64*\\*')
        folders.append(r'%ALLUSERSPROFILE%\\vMix\\settingbackups')
        config_file_name.append('user.config')
        config_file_name.append('current.config')
        
        for i in range(2):
            pattern = os.path.expandvars(folders[i])
            matches_folders = glob.glob(pattern)
            if matches_folders:
                for folder_path in matches_folders:
                    config_files = glob.glob(os.path.join(folder_path, config_file_name[i]))
                    for config_file in config_files:
                        try:
                            with open(config_file, 'r', encoding='utf-8') as file:
                                xmlDoc = ET.ElementTree(ET.fromstring(file.read().strip()))
                                xml_root = xmlDoc.getroot()
                        except Exception as e:
                            CustomMessageBox(root,msg_type='error',title=t('Error'),message=e)
                        OutputsExternal = '&lt;VirtualFrameRate&gt;333667&lt;/VirtualFrameRate&gt;&lt;VirtualFrameRateInterlaced&gt;0&lt;/VirtualFrameRateInterlaced&gt;&lt;ExternalFrameRate&gt;333667&lt;/ExternalFrameRate&gt;&lt;ExternalFrameRateInterlaced&gt;0&lt;/ExternalFrameRateInterlaced&gt;&lt;Overlay0&gt;1&lt;/Overlay0&gt;&lt;Overlay1&gt;1&lt;/Overlay1&gt;&lt;Overlay2&gt;1&lt;/Overlay2&gt;&lt;Overlay3&gt;1&lt;/Overlay3&gt;&lt;Overlay4&gt;1&lt;/Overlay4&gt;&lt;Overlay5&gt;1&lt;/Overlay5&gt;&lt;Overlay6&gt;1&lt;/Overlay6&gt;&lt;Overlay7&gt;1&lt;/Overlay7&gt;&lt;Overlay8&gt;1&lt;/Overlay8&gt;&lt;Overlay9&gt;1&lt;/Overlay9&gt;&lt;Overlay10&gt;1&lt;/Overlay10&gt;&lt;Overlay11&gt;1&lt;/Overlay11&gt;&lt;Overlay12&gt;1&lt;/Overlay12&gt;&lt;Overlay13&gt;1&lt;/Overlay13&gt;&lt;Overlay14&gt;1&lt;/Overlay14&gt;&lt;Overlay15&gt;1&lt;/Overlay15&gt;&lt;Input&gt;0&lt;/Input&gt;&lt;Mix&gt;0&lt;/Mix&gt;&lt;Display&gt;0&lt;/Display&gt;&lt;SRTEnabled&gt;0&lt;/SRTEnabled&gt;&lt;ExternalSize&gt;1920x1080&lt;/ExternalSize&gt;&lt;VirtualSize&gt;1280x720&lt;/VirtualSize&gt;&lt;ExternalDevice&gt;&lt;/ExternalDevice&gt;&lt;ExternalAudioDevice&gt;&lt;/ExternalAudioDevice&gt;&lt;ExternalAudioDelay&gt;0&lt;/ExternalAudioDelay&gt;&lt;Virtual&gt;1&lt;/Virtual&gt;&lt;External&gt;0&lt;/External&gt;&lt;ExternalPort&gt;0&lt;/ExternalPort&gt;&lt;ExternalAudioChannel&gt;0&lt;/ExternalAudioChannel&gt;&lt;ExternalAlphaChannel&gt;0&lt;/ExternalAlphaChannel&gt;&lt;VirtualUseStreaming&gt;1&lt;/VirtualUseStreaming&gt;&lt;ExternalUseDisplay&gt;1&lt;/ExternalUseDisplay&gt;'
                        settings_elments = {
                            'ProcessPriority':'128',
                            'OutputHideCursor':'True',
                            'OutputAlwaysOnTop':'True',
                            'VideoRenderer':'1',
                            'HighPerformanceOutput':'True',
                            'WebServerPort':'8088',
                            'WebServerEnabled':'True',
                            'ScreenSettings':'&lt;Screen0&gt;1&lt;/Screen0&gt;&lt;OutputHideCursor0&gt;1&lt;/OutputHideCursor0&gt;&lt;OutputAlwaysOnTop0&gt;1&lt;/OutputAlwaysOnTop0&gt;',
                            'OutputsExternal':OutputsExternal,
                            'OutputsExternal2':OutputsExternal,
                            'OutputsExternal3':OutputsExternal,
                            'OutputsExternal4':OutputsExternal
                        }
                        target_parent = xml_root.find(".//vMix.My.MySettings")
                        for key, value in settings_elments.items():
                            elm = xml_root.find(f".//setting[@name='{key}']")
                            if elm is not None:
                                elm.find('value').text = html.unescape(value)
                            else:
                                ET.SubElement(ET.SubElement(target_parent, 'setting', {'name': key, 'serializeAs': 'String'}), 'value').text = html.unescape(value)
                                ET.indent(xml_root, space="    ", level=0)
                        ffmpeg_extensions = xml_root.find(".//setting[@name='FFMpegExtensions']")
                        if ffmpeg_extensions is not None:
                            array_of_string = ffmpeg_extensions.find('.//ArrayOfString')
                            if array_of_string is not None:
                                array_of_string.clear()
                                preserve_namespaces(array_of_string)
                                new_string = ET.SubElement(array_of_string, 'string').text = '*.here'

                        my_settings = xml_root.find('.//vMix.My.MySettings')
                        MpegVideoDecoder = my_settings.find(".//setting[@name='MpegVideoDecoder']")
                        if MpegVideoDecoder is not None:
                            my_settings.remove(MpegVideoDecoder)
                        MpegAudioDecoder = my_settings.find(".//setting[@name='MpegAudioDecoder']")
                        if MpegAudioDecoder is not None:
                            my_settings.remove(MpegAudioDecoder)
                        H264VideoDecoder = my_settings.find(".//setting[@name='H264VideoDecoder']")
                        if H264VideoDecoder is not None:
                            my_settings.remove(H264VideoDecoder)
                            
                        for array in xml_root.findall('.//ArrayOfString'):
                            preserve_namespaces(array)
                        try:
                            with open(config_file, 'w', encoding='utf-8') as file:
                                file.write('<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(xml_root, encoding='unicode'))
                                settings_is_changed = True
                        except Exception as e:
                            CustomMessageBox(root,msg_type='error',title=t('Error'),message=e)
        if settings_is_changed:
            CustomMessageBox(root,title=t('Info'),message=t('Settings file patched successfully please restart vMix to take affect.'))

def vmix_thread(key_pressed):
    windows = []
    windows = get_windows_by_process(vmix_process_name)
    if len(windows)==0:return
    
    page = f'http://127.0.0.1:{str(vmix_port)}/api/'
    try:
        response = requests.get(page,timeout=0.2)
    except:
        return
    xmlDoc = ET.fromstring(response.text)
    activeNode = xmlDoc.find('./active')
    previewNode = xmlDoc.find('./preview')
    
    if activeNode is None:activeNode=''
    if previewNode is None:previewNode=''
    calls = []
    for call_function in options[vmix_process_name]['keys'][key_pressed]['call_functions'][(modifier if modifier in options[vmix_process_name]['keys'][key_pressed] else '')]:
        if call_function['call_only_if_vmix_foreground'] :
            active_window_hwnd = win32gui.GetForegroundWindow()
            active_process_name = psutil.Process(win32process.GetWindowThreadProcessId(active_window_hwnd)[1]).name().lower()
            active_process_title = win32gui.GetWindowText(active_window_hwnd).lower()
            active_class_name = win32gui.GetClassName(active_window_hwnd).lower()
            if (active_process_name != vmix_process_name or not any(keyword in active_process_title for keyword in options[vmix_process_name]['window_title_contain']) or not any(keyword in active_class_name for keyword in options[vmix_process_name]['window_class_contain'])):
                continue
        arguments = ''
        for key, value in call_function.items():
            if (key=='function_name' or key=='call_same_function_to_layers_input' or key=='call_only_if_vmix_foreground'):continue
            arguments = arguments + f'&{key}={value.replace("active",activeNode.text).replace("preview",previewNode.text)}'
        send = f'http://127.0.0.1:{str(vmix_port)}/api/?Function={call_function["function_name"]}{arguments}'
        try:
            if send not in calls:
                response = requests.get(send, timeout=0.2)
                calls.append(send)
        except:
            continue
        if call_function['call_same_function_to_layers_input']:
            inputNode = xmlDoc.find(f'./inputs/input[@number=\'{activeNode.text}\']')
            if inputNode is None:
                return
            else:
                for overlayNode in inputNode:
                    input_num = xmlDoc.find(f'./inputs/input[@key=\'{overlayNode.get("key")}\']').get("number")
                    arguments = ''
                    for key, value in call_function.items():
                        if (key=='function_name' or key=='call_same_function_to_layers_input' or key=='call_only_if_vmix_foreground'):continue
                        if key=='input': arguments = arguments + f'&{key}={input_num}'
                        else:
                            arguments = arguments + f'&{key}={value.replace("active",activeNode.text).replace("preview",previewNode.text)}'
                    send = f'http://127.0.0.1:{str(vmix_port)}/api/?Function={call_function["function_name"]}{arguments}'
                    try:
                        if send not in calls:
                            response = requests.get(send, timeout=0.2)
                            calls.append(send)
                    except:
                        continue

def on_key_modifier_press(key):
    global modifier
    if key != modifier: modifier=key
    else: modifier=''
    return True

def on_key_press(key_pressed):
    if key_pressed in registered_modifiers:on_key_modifier_press(key_pressed)
    if key_pressed in options[vmix_process_name]['keys']:
        tmp_mod = modifier if modifier in options[vmix_process_name]['keys'][key_pressed]['call_functions'] else ''
        if options[vmix_process_name]['keys'][key_pressed]['call_functions'][tmp_mod][0]['call_only_if_vmix_foreground']:
            active_window_hwnd = win32gui.GetForegroundWindow()
            active_process_name = psutil.Process(win32process.GetWindowThreadProcessId(active_window_hwnd)[1]).name().lower()
            if active_process_name!=vmix_process_name:
                return True
    
    target_thread_id, target_process_id = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
    AttachThreadInput(threading.current_thread().native_id, target_thread_id, True)
    active_control_hwnd = win32gui.GetFocus()
    AttachThreadInput(threading.current_thread().native_id, target_thread_id, False)
    thread = threading.Thread(target=on_key_press_thread, args=(key_pressed,active_control_hwnd))
    thread.start()
    return False
    
def on_key_press_thread(key_pressed,active_control_hwnd):
    global modifier
    
    active_window_hwnd = win32gui.GetForegroundWindow()
    active_process_name = psutil.Process(win32process.GetWindowThreadProcessId(active_window_hwnd)[1]).name().lower()
    active_window_title = win32gui.GetWindowText(active_window_hwnd).lower()
    active_window_class = win32gui.GetClassName(active_window_hwnd).lower()
    
    windows = []
    processes_found = []
    classes_found = []
    list_of_hwnd__we_sent_key_stroks = []
    
    for key, value in options.items():
        if((key!='foreground') and (key_pressed not in value['keys'])):continue
        if ((key==vmix_process_name and not value['call_functions'] and not value['send_key_stroks_to_vmix']) or (key!=vmix_process_name and not value['enable'])):
            continue
        elif key==vmix_process_name and value['call_functions']:
            thread = threading.Thread(target=vmix_thread, args=(key_pressed,))
            thread.start()
            if not value['send_key_stroks_to_vmix']:
                continue
        if key!='foreground':
            windows = get_windows_by_process(key)
        else:
            if active_window_hwnd in list_of_hwnd__we_sent_key_stroks:
                continue
            windows.clear()
            windows.append({
                'hwnd': active_window_hwnd,
                'active_control_hwnd':active_control_hwnd,
                'class_name':active_window_class,
                'title': active_window_title
            })
        if len(windows)>0:
            if key!='foreground': processes_found.append(key)
            for window in windows:
                classes_found.append(window['class_name'])
                if 'window_title_contain' in value and len(value['window_title_contain'])>0:
                    if not any(keyword in window['title'] for keyword in value['window_title_contain']):
                        continue
                    else:
                        if 'window_title_not_contain' in value and len(value['window_title_not_contain'])>0:
                            if any(keyword in window['title'] for keyword in value['window_title_not_contain']):
                                continue
                if 'window_class_contain' in value and len(value['window_class_contain'])>0:
                    if not any(keyword in window['class_name'] for keyword in value['window_class_contain']):
                        continue
                if 'need_to_activate' in value and value['need_to_activate']:
                    if len(set(processes_found).intersection(set(value['dont_activate_if_process_exist']))) == 0 and len(set(classes_found).intersection(set(value['dont_activate_if_window_class_exist']))) == 0:
                        if window['hwnd'] != win32gui.GetForegroundWindow():
                            for i in range(2):
                                try:
                                    win32gui.SetForegroundWindow(window['hwnd'])
                                    time.sleep(0.05)
                                except:
                                    pass
                if key=='foreground':
                    key_code1 = key_codes[key_pressed.split('+',1)[0]] if key_pressed!='+' else '+'
                    try:key_code2 = key_codes[key_pressed.split('+',1)[1]]
                    except:key_code2=None
                elif key==vmix_process_name:
                    if 'send_key_stroks_to_vmix' in value['keys'][key_pressed]:
                        key_code1 = key_codes[value['keys'][key_pressed]['send_key_stroks_to_vmix'][(modifier if modifier in value['keys'][key_pressed]['send_key_stroks_to_vmix'] else '')]] if key_pressed in value['keys'] else key_codes[(key_pressed.split('+')[0] if key_pressed!='+' else '+')]
                        try:key_code2 = key_codes[value['keys'][key_pressed]['send_key_stroks_to_vmix'][(modifier if modifier in value['keys'][key_pressed]['send_key_stroks_to_vmix'] else '')]] if key_pressed in value['keys'] else key_codes[key_pressed.split('+')[1]]
                        except:key_code2=None
                    else:
                        key_code1 = key_codes[key_pressed.split('+',1)[0]] if key_pressed!='+' else '+'
                        try:key_code2 = key_codes[key_pressed.split('+',1)[1]]
                        except:key_code2=None
                else:
                    key_code1 = key_codes[value['keys'][key_pressed][(modifier if modifier in value['keys'][key_pressed] else '')]] if key_pressed in value['keys'] else key_codes[(key_pressed.split('+')[0] if key_pressed!='+' else '+')]
                    try:key_code2 = key_codes[value['keys'][key_pressed][(modifier if modifier in value['keys'][key_pressed] else '')]] if key_pressed in value['keys'] else key_codes[key_pressed.split('+')[1]]
                    except:key_code2=None
                if key_code1==key_code2:key_code2=None
                if key=='foreground' and window['class_name'] == 'podiumparent' and active_process_name=='powerpnt.exe':continue
                if key=='foreground' and window['class_name'] == 'podiumparent' and active_process_name=='powerpnt.exe':continue
                win32gui.PostMessage(window['hwnd'] if key!='foreground' else window['active_control_hwnd'], win32con.WM_KEYDOWN, key_code1, make_lparam(key_code1, MapVirtualKey(key_code1, 0)))
                if key_code2 is not None:
                    win32gui.PostMessage(window['hwnd'] if key!='foreground' else window['active_control_hwnd'], win32con.WM_KEYDOWN, key_code2, make_lparam(key_code2, MapVirtualKey(key_code2, 0)))
                time.sleep(0.05)
                list_of_hwnd__we_sent_key_stroks.append(window['hwnd'])
                if value['send_wm_keyup_also']:
                    if key_code2 is not None:
                        win32gui.PostMessage(window['hwnd'] if key!='foreground' else window['active_control_hwnd'], win32con.WM_KEYUP, key_code2, make_lparam(key_code2, MapVirtualKey(key_code2, 0), previous_state=1, transition=1))
                    win32gui.PostMessage(window['hwnd'] if key!='foreground' else window['active_control_hwnd'], win32con.WM_KEYUP, key_code1, make_lparam(key_code1, MapVirtualKey(key_code1, 0), previous_state=1, transition=1))
                time.sleep(0.05)
                if 'make_sure_its_always_on_top' in value and value['make_sure_its_always_on_top']:
                    try:
                        win32gui.SetWindowPos(window['hwnd'],win32con.HWND_TOPMOST,0, 0, 0, 0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
                    except:
                        pass
                if 'send_keys_to_first_match' in value and value['send_keys_to_first_match']:
                    break
    return False
def get_windows_by_pid(target_process_pid):
    windows = []
    
    def callback(hwnd, extra):
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        
        try:
            if target_process_pid == pid:
                class_name = win32gui.GetClassName(hwnd)
                window_title = win32gui.GetWindowText(hwnd)
                windows.append({
                    'hwnd': hwnd,
                    'pid': pid,
                    'class_name': class_name.lower(),
                    'title': window_title.lower(),
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
        return True
    
    win32gui.EnumWindows(callback, None)
    return windows
    
def get_windows_by_process(target_process_name):
    windows = []
    
    def callback(hwnd, extra):
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        
        try:
            process = psutil.Process(pid)
            if process.name().lower() == target_process_name.lower():
                class_name = win32gui.GetClassName(hwnd)
                window_title = win32gui.GetWindowText(hwnd)
                windows.append({
                    'hwnd': hwnd,
                    'pid': pid,
                    'class_name': class_name.lower(),
                    'title': window_title.lower(),
                    'process_path': process.exe().lower(),
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
        return True
    
    win32gui.EnumWindows(callback, None)
    return windows

def lowercase_dict_keys_and_values(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = key.lower() if isinstance(key, str) else key
            new_value = lowercase_dict_keys_and_values(value)
            new_dict[new_key] = new_value
        return new_dict
    elif isinstance(data, list):
        return [lowercase_dict_keys_and_values(item) for item in data]
    elif isinstance(data, str):
        return data.lower()
    else:
        return data
        
options = lowercase_dict_keys_and_values(options)

class frame_layout():
    def __init__(self,root):
        self.root = tk.Toplevel(root)
        self.root.withdraw()
        self.visible = False
        self.root.overrideredirect(True)
        self.root.attributes('-transparentcolor', 'white')
        self.root.attributes('-topmost', True)
        self.width = 1
        self.height = 1
        self.x_pos = 0
        self.y_pos = 0
        self.selected_layer = '0'
        self.root.geometry(f'{self.width}x{self.height}+{self.x_pos}+{self.y_pos}')

        self.canvas = tk.Canvas(
            self.root,
            width=self.width,
            height=self.height,
            bg='white',
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.frame_id = self.canvas.create_rectangle(
            0, 0, self.width-1, self.height-1,
            outline='red',
            width=3
        )

        self.here_button = tk.Button(
            self.root, text=t('here!'), command=self.here_button_click,
            bg='red', activebackground='red', padx=1, pady=1
        )
        self.here_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.close_button = tk.Button(
            self.root, text='X', command=self.close_frame,
            bg='red', activebackground='red', padx=1, pady=1
        )
        self.close_button.place(relx=1.0, x=-5, y=5, anchor=tk.NE)
        
    def here_button_click(self): 
        page = f'http://127.0.0.1:{str(vmix_port)}/api/'
        try:
            response = requests.get(page,timeout=0.2)
        except:
            return
        xmlDoc = ET.fromstring(response.text)
        
        activeNode = xmlDoc.find('./active')
        previewNode = xmlDoc.find('./preview')

        if activeNode is None or previewNode is None:return
        try:
            send = f'http://127.0.0.1:{str(vmix_port)}/api/?Function=setmultiviewoverlay&input={activeNode.text}&value={str(int(self.selected_layer)+1)},{previewNode.text}'
            response = requests.get(send, timeout=0.2)
        except:
            return
        
    def show_frame(self, width, height, x, y, selected_layer):
        if self.visible == False or self.width != width or self.height != height or self.x_pos != x or self.y_pos != y:
            self.root.geometry(f'{width}x{height}+{x}+{y}')
            self.canvas.config(width=width, height=height)
            self.canvas.coords(self.frame_id, 0, 0, width-1, height-1)
            self.root.attributes('-transparentcolor', 'white')
            self.root.deiconify()
            self.width = width
            self.height = height
            self.x_pos = x
            self.y_pos = y
            self.selected_layer = selected_layer
            self.visible = True
        
    def hide_frame(self):
        self.root.withdraw()
        self.visible = False
        
    def close_frame(self):
        time.sleep(0.05)
        self.root.withdraw()
        self.visible = False

    def frame_is_visible(self):
        return self.visible
        
    def get_hwnd(self):
        return win32gui.GetParent(self.root.winfo_id())
        
    def exit(self):
        self.root.destroy()

class CustomMessageBox:
    class right_click_menu:
        def __init__(self, e):
            commands = ['Copy']
            menu = tk.Menu(None, tearoff=0, takefocus=0)

            for txt in commands:
                menu.add_command(label=t(txt), command=lambda e=e,txt=txt:self.click_command(e,txt))

            menu.tk_popup(e.x_root, e.y_root, entry='0')

        def click_command(self, e, cmd):
            e.widget.event_generate(f'<<{cmd}>>')
            
    def __init__(self, parent, wait=True, msg_type='info', title='Message', message='', button_text='OK', _font=None, wrap=80):
        from tkinter import font as tkfont
        self.top = tk.Toplevel(parent)
        self.top.withdraw()
        self.top.attributes('-topmost', True)
        self.top.title(title)
        self.top.iconphoto(False, ImageTk.PhotoImage(icon))
        self.top.resizable(False, False)
        
        main_frame = tk.Frame(self.top, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.X)
        font = (font_family,font_size,font_weight) if _font is None else _font
        icon_symbol, icon_color = self.get_icon_properties(msg_type)
        icon_font = tkfont.Font(family=font[0], size=26, weight='bold')
        icon_label = tk.Label(
            content_frame,
            text=icon_symbol,
            font=icon_font,
            fg=icon_color,
            bg=main_frame.cget('bg')
        )
        icon_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.wrap = wrap
        
        h_scroll = ttk.Scrollbar(content_frame, orient='horizontal')
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
    
        self.msg_label = tk.Text(content_frame, font=font, width=(wrap if wrap>0 else 80),
            wrap=('char' if wrap else 'none'),
            bg=main_frame.cget('bg'),
            xscrollcommand=h_scroll.set,
            padx=5, pady=5
        )
        self.msg_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.msg_label.insert('1.0', message)
        self.auto_height()
        self.msg_label.bind('<Button-3>', self.right_click_menu)
        self.msg_label.config(state='disabled')
        
        h_scroll.config(command=self.msg_label.xview)
        
        close_btn = ttk.Button(main_frame,text=button_text,command=self.close)
        close_btn.pack(pady=(10, 0))

        self.top.deiconify()
        self.top.update_idletasks()
        
        width = self.top.winfo_width()
        height = self.top.winfo_height()
        
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        self.top.geometry(f'+{(screen_width-width)//2}+{(screen_height-height)//2}')
        if wait:
            self.top.wait_window(self.top)
        
    def auto_height(self,event=None):
        chars = self.msg_label.get('1.0', 'end-1c')
        lines = (chars.count('\n')+(int(len(chars)/self.wrap) if self.wrap>0 else 0)+2)
        self.msg_label.config(height=lines)
    
    def get_icon_properties(self, msg_type):
        icons_s = {
            'info': ('✔', 'blue'),
            'warning': ('⚠', 'orange'),
            'error': ('✖', 'red'),
            'question': ('❓', 'green')
        }
        return icons_s.get(msg_type.lower(), ('✔', 'blue'))
    
    def center_window(self):
        self.top.update_idletasks()
        width = self.top.winfo_width()
        height = self.top.winfo_height()
        
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        self.top.geometry(f'+{x}+{y}')
        
    def close(self):
        self.top.grab_release()
        self.top.destroy()
        
class fullscreen_window:
    def __init__(self, root):
        self.controls_list = {}
        self.font = (font_family,font_size,font_weight)
        self.settings = {}
        self.root = tk.Toplevel(root)
        self.root.withdraw()
        self.root.iconphoto(False, ImageTk.PhotoImage(icon))
        self.root.title(t('Fullscreen'))
        self.root.geometry("1180x650")  # Size of the control window
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)
        self.main_frame = ttk.Frame(self.root, padding='0')
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        self.root.update_idletasks()
        self.root.minsize(
            self.main_frame.winfo_reqwidth() + 10,
            self.main_frame.winfo_reqheight() + 10
        )
        self.root.deiconify()
        
    def fullscreen(self,in_device,monitor_name):
        global fullscreen_ffplay
        global old_all_monitors
        
        if monitor_name in fullscreen_ffplay:
            try:
                os.kill(fullscreen_ffplay[monitor_name]['process'].pid,signal.SIGINT)
            except:
                pass
            del fullscreen_ffplay[monitor_name]
        if in_device != t('None'):
            stretch = False
            if t('Main Output') in in_device:vmix_in_device = 'vMix Video'
            if t('Output 2') in in_device:vmix_in_device = 'vMix Video External 2'
            if t('Output 3') in in_device:vmix_in_device = 'vMix Video External 3'
            if t('Output 4') in in_device:vmix_in_device = 'vMix Video External 4'
            if t('Stretch it') in in_device:stretch=True
            for monitor in old_all_monitors:
                if monitor['name'] == monitor_name:
                    try:
                        import winreg
                        os.environ['PATH']=os.path.expandvars(winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'System\CurrentControlSet\Control\Session Manager\Environment', 0, winreg.KEY_READ), 'Path')[0])
                        tmp_process = subprocess.Popen(f'ffplay.exe -f dshow -i "video={vmix_in_device}" -left {monitor["x"]} -top {monitor["y"]} -x {monitor["width"]} -y {monitor["height"]} -fs -noborder -alwaysontop' + (f' -vf "scale={monitor["width"]}:{monitor["height"]}"' if stretch else ''), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
                        time.sleep(0.5)
                        try:
                            stdout, stderr = tmp_process.communicate(timeout=1)
                            if stderr:
                                messagebox.showerror(t('Failed'), stderr)
                                return
                        except:
                            pass
                        fullscreen_ffplay[monitor['name']]={'process':tmp_process,'last_seen':int(time.time()),'in_device':in_device}
                        parent = psutil.Process(fullscreen_ffplay[monitor_name]['process'].pid)
                        children = parent.children(recursive=True)
                        windows = [parent]+children
                        for window in windows:
                            wins = get_windows_by_pid(window.pid)
                            for win in wins:
                                style = win32gui.GetWindowLong(win['hwnd'], win32con.GWL_EXSTYLE)
                                win32gui.SetWindowLong(win['hwnd'], win32con.GWL_EXSTYLE, style | win32con.WS_EX_TOOLWINDOW)
                    except FileNotFoundError:
                        messagebox.showerror(t('Failed'), t('ffmpeg is not installed. Please install ffmpeg from Tools to install submenu.'))
                    except Exception as e:
                        messagebox.showerror(t('Failed'), e)
                    return
    def option_click(self,event,moniter_name):
        selected_value = event.widget.get() 
        self.fullscreen(selected_value,moniter_name)

    def create_widgets(self):
        global fullscreen_ffplay
        global old_all_monitors
        all_monitors = get_all_screens_connected()
        if all_monitors != old_all_monitors:
            old_all_monitors = copy.deepcopy(all_monitors)
        min_x = min(s['x'] for s in old_all_monitors)
        min_y = min(s['y'] for s in old_all_monitors)
        max_x = max(s['x'] + s['width'] for s in old_all_monitors)
        max_y = max(s['y'] + s['height'] for s in old_all_monitors)

        total_width = max_x - min_x
        total_height = max_y - min_y

        max_allowed_w = 1080
        max_allowed_h = 550

        scale_x = max_allowed_w / total_width
        scale_y = max_allowed_h / total_height
        scale = min(scale_x, scale_y)

        margin_x = 50
        margin_y = 50

        combo_options = [t('None'), t('Main Output'), t('Output 2'),t('Output 3'),t('Output 4'), f'{t("Main Output")} ({t("Stretch it")})', f'{t("Output 2")} ({t("Stretch it")})',f'{t("Output 3")} ({t("Stretch it")})',f'{t("Output 4")} ({t("Stretch it")})']
        for screen in old_all_monitors:
            local_x = int((screen['x'] - min_x) * scale) + margin_x
            local_y = int((screen['y'] - min_y) * scale) + margin_y
            local_w = int(screen['width'] * scale)
            local_h = int(screen['height'] * scale)
            self.screen_box = tk.Frame(
                self.root, 
                bg='#ff4d4d',
                highlightbackground='#b30000', 
                highlightthickness=2
            )
            self.screen_box.place(x=local_x, y=local_y, width=local_w, height=local_h)

            self.lbl = tk.Label(
                self.screen_box, 
                text=f'{screen["name_string"]}\n{screen["monitor_name"]}\n({screen["width"]}x{screen["height"]}){("\n" + t("Primary")) if screen["is_primary"] else ""}', 
                bg='#ff4d4d', 
                fg='white',
                font=(self.font[0], 9, 'bold')
            )
            
            self.lbl.pack(side='top', fill='x', pady=(5, 2))
            self.controls_list[f'combobox_{screen["name"]}'] = ttk.Combobox(self.screen_box, values=combo_options, state='readonly')
            if screen['name'] in fullscreen_ffplay:
                self.controls_list[f'combobox_{screen["name"]}'].set(fullscreen_ffplay[screen['name']]['in_device'])
            else:
                self.controls_list[f'combobox_{screen["name"]}'].set(combo_options[0])
            self.controls_list[f'combobox_{screen["name"]}'].pack(side='bottom', pady=(0, 5), padx=5, fill='x')
            self.controls_list[f'combobox_{screen["name"]}'].bind('<<ComboboxSelected>>', lambda event, moniter_name=screen['name']: self.option_click(event, moniter_name))
            
class pdf2png_window:
    class right_click_menu:
        def __init__(self, e):
            commands = ['Cut','Copy','Paste']
            menu = tk.Menu(None, tearoff=0, takefocus=0)

            for txt in commands:
                menu.add_command(label=t(txt), command=lambda e=e,txt=txt:self.click_command(e,txt))

            menu.tk_popup(e.x_root, e.y_root, entry='0')

        def click_command(self, e, cmd):
            e.widget.event_generate(f'<<{cmd}>>')
            
    def on_drop_files(self,hwnd, msg, wp, lp):
        if msg == WM_DROPFILES:
            length = shell32.DragQueryFileW(wp, 0, None, 0)
            buffer = ctypes.create_unicode_buffer(length + 1)
            shell32.DragQueryFileW(wp, 0, buffer, length + 1)
            shell32.DragFinish(wp)
            self.settings['entry_file'].set(buffer.value)
            return 0
        return user32.CallWindowProcW(self.original_wndproc, hwnd, msg, wp, lp)
        
    def __init__(self, root):
        self.controls_list = {}
        self.initialdir_in = os.path.expanduser('~')
        self.initialdir_out = os.path.expanduser('~')
        self.font = (font_family,font_size,font_weight)
        self.settings = {}
        self.root = tk.Toplevel(root)
        self.root.withdraw()
        self.root.iconphoto(False, ImageTk.PhotoImage(icon))
        self.root.title(t('PDF to pictures'))
        self.root.resizable(False, False)
        self.main_frame = ttk.Frame(self.root, padding='0')
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        self.root.update_idletasks()
        self.root.minsize(
            self.main_frame.winfo_reqwidth() + 10,
            self.main_frame.winfo_reqheight() + 10
        )
        self.root.deiconify()
        
    def create_widgets(self):
        frame = ttk.LabelFrame(self.main_frame, text=t('Settinges :'), padding='0')
        frame.grid(row=0, column=0, sticky='ew', padx=10, pady=5)

        ttk.Label(frame, text=t('File : '),font=self.font).grid(row=0, column=0, sticky='e')
        self.settings['entry_file'] = StringVar(value='')
        self.controls_list['entry_file'] = ttk.Entry(
                frame, 
                textvariable=self.settings['entry_file'],
                width=50,
                font=self.font
            )
        self.controls_list['entry_file'].grid(row=0, column=1, sticky='w', padx=3, pady=2)
        self.controls_list['entry_file'].bind('<Button-3>', self.right_click_menu)
        tk.Button(frame, text=t('Browse'), command=self.browse_file,font=self.font).grid(row=0, column=2, padx=1, sticky='e')

        ttk.Label(frame, text=t('Save Folder : '),font=self.font).grid(row=1, column=0, sticky='e')
        new_path = re.sub(r'%[YmdHMS%-]+',lambda m: datetime.now().strftime(m.group(0)),r'' + '%USERPROFILE%\\Desktop\\PDF_%Y-%m-%d_%H-%M-%S')
        expanded_path = os.path.expandvars(new_path)
        expanded_path = os.path.expanduser(expanded_path)
        self.settings['entry_folder'] = StringVar(value=expanded_path)
        self.controls_list['entry_folder'] = ttk.Entry(
                frame, 
                textvariable=self.settings['entry_folder'],
                width=50,
                font=self.font
            )
        self.controls_list['entry_folder'].grid(row=1, column=1, sticky='w', padx=3, pady=2)
        self.controls_list['entry_folder'].bind('<Button-3>', self.right_click_menu)
        tk.Button(frame, text=t('Browse'), command=self.browse_folder,font=self.font).grid(row=1, column=2, padx=1, sticky='e')

        ttk.Label(frame, text=t('DPI : '),font=self.font).grid(row=2, column=0, sticky='e')
        self.settings['combobox_dpi'] = StringVar(value='200')
        self.controls_list['combobox_dpi'] = ttk.Combobox(
                frame, 
                textvariable=self.settings['combobox_dpi'],
                values=['100','200','300','400'],
                width=50,
                font=self.font
            )
        self.controls_list['combobox_dpi'].grid(row=2, column=1, sticky='w', padx=3, pady=2)

        ttk.Label(frame, text=t('Rotation : '),font=self.font).grid(row=3, column=0, sticky='e')
        self.settings['combobox_rotation'] = StringVar(value='0')
        self.controls_list['combobox_rotation'] = ttk.Combobox(
                frame, 
                textvariable=self.settings['combobox_rotation'],
                width=50,
                values=['0','90','180','270'],
                font=self.font
            )
        self.controls_list['combobox_rotation'].grid(row=3, column=1, sticky='w', padx=3, pady=2)

        self.settings['Checkbutton_flip_h'] = BooleanVar(value=False)
        self.controls_list['Checkbutton_flip_h'] = tk.Checkbutton(
                frame, 
                text=t('Flip horizontal.'),
                variable=self.settings['Checkbutton_flip_h'],
                font=self.font
            )
        self.controls_list['Checkbutton_flip_h'].grid(row=4, column=1, sticky='w', padx=3, pady=2)

        self.settings['Checkbutton_flip_v'] = BooleanVar(value=False)
        self.controls_list['Checkbutton_flip_v'] = tk.Checkbutton(
                frame, 
                text=t('Flip vertical.'),
                variable=self.settings['Checkbutton_flip_v'],
                font=self.font
            )
        self.controls_list['Checkbutton_flip_v'].grid(row=5, column=1, sticky='w', padx=3, pady=2)

        frame3 = ttk.Frame(self.main_frame)
        frame3.grid(row=1, column=0, sticky='e', pady=10)
        self.controls_list['save_import_button'] = tk.Button(frame3, text=t('Convert And Import to vMix'), command=self.save_import,font=self.font)
        self.controls_list['save_import_button'].grid(row=0, column=2, padx=5, sticky='e')
        self.controls_list['save_button'] = tk.Button(frame3, text='   ' + t('Convert') + '   ', command=self.save,font=self.font)
        self.controls_list['save_button'].grid(row=0, column=1, padx=5, sticky='e')

        self.controls_list['progress'] = ttk.Label(frame3, text='',font=self.font)
        self.controls_list['progress'].grid(row=0, column=0, sticky='e')
        self.root.update()
        hwnd = self.root.winfo_id()
        shell32.DragAcceptFiles(hwnd, True)
        self.new_wndproc = WNDPROC_TYPE(self.on_drop_files)
        self.original_wndproc = SetWindowLongPtr(hwnd, GWL_WNDPROC, self.new_wndproc)
        
    def browse_file(self):
        filepath = filedialog.askopenfilename(
                    initialdir=self.initialdir_in,
                    title=t('Open file:'),
                    filetypes=(('PDF file', '*.pdf'),),
                    defaultextension='.pdf',
                    parent=self.root
                )
        if filepath:
            self.settings['entry_file'].set(filepath.replace('/','\\'))
            self.initialdir_in = os.path.dirname(self.settings['entry_file'].get())
    
    def browse_folder(self):
        folderpath = filedialog.askdirectory(
                    initialdir=self.initialdir_out,
                    title=t('Save folder:'),
                    parent=self.root
                )
        if folderpath:
            self.settings['entry_folder'].set(folderpath.replace('/','\\'))
            self.initialdir_out = os.path.dirname(self.settings['entry_folder'].get())
            
    def save_import(self):
        self.save(True)
        
    def save(self,import_vmix=False):
        if not os.path.exists(self.settings['entry_file'].get()):
            self.controls_list['progress'].config(text=t('Please select file input.'))
            return
        self.controls_list['save_button']['state']= tk.DISABLED
        self.controls_list['save_import_button']['state']= tk.DISABLED
        save_thread = threading.Thread(target=self.save_pdf, args=(
            import_vmix,
            self.settings['entry_file'].get(),
            self.settings['entry_folder'].get(),
            self.settings['combobox_dpi'].get(),
            self.settings['combobox_rotation'].get(),
            self.settings['Checkbutton_flip_h'].get(),
            self.settings['Checkbutton_flip_v'].get(),
            self.root,
            self.controls_list['progress'],
            self.controls_list['save_button'],
            self.controls_list['save_import_button']
        ))
        save_thread.start()
        
    def save_pdf(self,import_vmix,srcfile,target_folder,dpi=200,rotation='0',flip_h=False,flip_v=False,window=None,progress_text=None,savebutton=None,save_importbutton=None):
        try:
            import pymupdf
        except:
            process = subprocess.Popen([
                'powershell.exe', 
                '-Command',
                '''
                Write-host "`nvMix Helper. Staring Installation of Microsoft Visual C++ 2015-2022 x64"
                $vcRedistUrl = "https://aka.ms/vs/17/release/vc_redist.x64.exe"
                $installerPath = "$env:TEMP\\vc_redist.x64.exe"
                try {
                    Invoke-WebRequest -Uri $vcRedistUrl -OutFile $installerPath -UseBasicParsing -ErrorAction Stop
                    Start-Process -FilePath $installerPath -ArgumentList "/passive", "/norestart" -Wait
                    Remove-Item $installerPath -Force
                }
                catch {
                    Write-Error "Failed to install VC++ Redistributable:" $_.Exception.Message
                    exit 1
                }
                '''
            ], creationflags=subprocess.CREATE_NEW_CONSOLE)
            process.wait()
            try:
                import pymupdf
            except Exception as e:
                progress_text.config(text=e)
                window.update_idletasks()
                savebutton['state']= tk.NORMAL
                save_importbutton['state']= tk.NORMAL
                return
        try:
            doc = pymupdf.open(srcfile)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            mat = pymupdf.Matrix(int(dpi) / 72, int(dpi) / 72)
            if rotation == '90':
                mat = mat * pymupdf.Matrix(0, 1, -1, 0, 0, 0)
            if rotation == '180':
                mat = mat * pymupdf.Matrix(-1, 0, 0, -1, 0, 0)
            if rotation == '270':
                mat = mat * pymupdf.Matrix(0, -1, 1, 0, 0, 0)
            if flip_h or flip_v:
                mat = mat * pymupdf.Matrix((-1 if flip_h else 1), 0, 0, (1 if flip_h and not flip_v else -1), 0, 0)

            for page_num in range(len(doc)):
                progress_text.config(text=f'{str(round((((page_num+1)/len(doc))*100),1))}%')
                window.update_idletasks()
                page = doc.load_page(page_num)
                pix = page.get_pixmap(matrix=mat)
                output_image_path = os.path.join(target_folder, f'page_{(page_num+1):04d}.png')
                pix.save(output_image_path)
            doc.close()
            pymupdf.TOOLS.store_shrink(100)
            if import_vmix:
                page = f'http://127.0.0.1:{str(vmix_port)}/api/?Function=AddInput&Value=Photos|{target_folder}'
                try:
                    response = requests.get(page, timeout=1)
                except:
                    pass
            new_path = re.sub(r'%[YmdHMS%-]+',lambda m: datetime.now().strftime(m.group(0)),r'' + self.initialdir_out + '\\PDF_%Y-%m-%d_%H-%M-%S')
            expanded_path = os.path.expandvars(new_path)
            expanded_path = os.path.expanduser(expanded_path)
            self.settings['entry_folder'].set(expanded_path.replace('\\\\','\\'))
        except Exception as e:
            progress_text.config(text=e)
            window.update_idletasks()
            
        savebutton['state']= tk.NORMAL
        save_importbutton['state']= tk.NORMAL
        
class settings_window:
    ffmpeg_default_settings = {
        'ffmpeg_settings_profile':{
            'selection':t('NEW_PROFILE (DEFAULT_SETTINGS)'),
            'profiles':{
                t('NEW_PROFILE (KEEP_PREVIOUS_SETTINGS)'):{},
                t('NEW_PROFILE (DEFAULT_SETTINGS)'):{
                    'ffmpeg_destination_preset':t('Save to file'),
                    'ffmpeg_destination':'%USERPROFILE%\\Desktop\\%Y-%m-%d_%H-%M-%S.mp4',
                    'ffmpeg_vmix_video_device':'vMix Video',
                    'ffmpeg_vmix_audio_device':'vMix Audio',
                    'ffmpeg_encoder':f'hevc_qsv ({t("Intel GPU, Not all GPU supports")})',
                    'ffmpeg_preset':'veryfast',
                    'ffmpeg_profile':'main',
                    'ffmpeg_dimension':'1920x1080',
                    'ffmpeg_video_bitrate':'3000',
                    'ffmpeg_threads':t('All Available'),
                    'ffmpeg_output_frame_rate':'30',
                    'ffmpeg_audio_codec':'aac -profile:a aac_low -aac_coder twoloop -async 15',
                    'ffmpeg_audio_bitrate':'128',
                    'ffmpeg_input_buffer':'-rtbufsize 128M',
                    'ffmpeg_fifo_queue_size':'240',
                    'ffmpeg_output_flush_packets':True,
                    'ffmpeg_show_window':True,
                    'ffmpeg_enable_experiment':False,
                    'ffmpeg_enable_sound':True,
                    'ffmpeg_template_one':'ffmpeg.exe -y {ffmpeg_input_buffer} -err_detect ignore_err {ffmpeg_hwaccel} -f dshow -i "video={ffmpeg_vmix_video_device}:audio={ffmpeg_vmix_audio_device}" -codec:v {ffmpeg_encoder} -pix_fmt yuv420p -s:v {ffmpeg_dimension} -r {ffmpeg_output_frame_rate} -g {ffmpeg_output_frame_rate} -threads {ffmpeg_threads} -bufsize:v {ffmpeg_video_maxbitrate} -profile:v {ffmpeg_profile} -bf 0 -preset:v {ffmpeg_preset} -tune zerolatency -b:v {ffmpeg_video_bitrate} -maxrate:v {ffmpeg_video_maxbitrate} -low_power 1 -async_depth 1 {ffmpeg_enable_sound} -codec:a {ffmpeg_audio_codec} -b:a {ffmpeg_audio_bitrate} -ar 48000 -ac 2 -bufsize:a 1024k -fps_mode cfr {experimental} -flush_packets {ffmpeg_output_flush_packets} -f fifo -fifo_format {ffmpeg_destination_a} -attempt_recovery 1 -drop_pkts_on_overflow 1 -max_recovery_attempts 10 -queue_size {ffmpeg_fifo_queue_size} -map 0:v -map 0:a "{ffmpeg_destination_b}"',
                    'ffmpeg_template_multiple':'ffmpeg.exe -y {ffmpeg_input_buffer} -err_detect ignore_err {ffmpeg_hwaccel} -f dshow -i "video={ffmpeg_vmix_video_device}:audio={ffmpeg_vmix_audio_device}" -codec:v {ffmpeg_encoder} -pix_fmt yuv420p -s:v {ffmpeg_dimension} -r {ffmpeg_output_frame_rate} -g {ffmpeg_output_frame_rate} -threads {ffmpeg_threads} -bufsize:v {ffmpeg_video_maxbitrate} -profile:v {ffmpeg_profile} -bf 0 -preset:v {ffmpeg_preset} -tune zerolatency -b:v {ffmpeg_video_bitrate} -maxrate:v {ffmpeg_video_maxbitrate} -low_power 1 -async_depth 1 {ffmpeg_enable_sound} -codec:a {ffmpeg_audio_codec} -b:a {ffmpeg_audio_bitrate} -ar 48000 -ac 2 -bufsize:a 1024k -fps_mode cfr {experimental} -flush_packets {ffmpeg_output_flush_packets} -f tee -use_fifo 1 -fifo_options "attempt_recovery=1:drop_pkts_on_overflow=1:max_recovery_attempts=10:queue_size={ffmpeg_fifo_queue_size}" -map 0:v -map 0:a "{loop_destinations}"'
                },
                f'{t("NEW_PROFILE (DEFAULT_SETTINGS)")}({t("HLS Template 3 Resolutions")})':{
                    'ffmpeg_destination_preset':t('Save to file (Open file browser)'),
                    'ffmpeg_destination':'%USERPROFILE%\\Desktop\\master.m3u8',
                    'ffmpeg_vmix_video_device':'vMix Video',
                    'ffmpeg_vmix_audio_device':'vMix Audio',
                    'ffmpeg_encoder':f'hevc_qsv ({t("Intel GPU, Not all GPU supports")})',
                    'ffmpeg_preset':'veryfast',
                    'ffmpeg_profile':'main',
                    'ffmpeg_dimension':'1920x1080',
                    'ffmpeg_video_bitrate':'3000',
                    'ffmpeg_threads':t('All Available'),
                    'ffmpeg_output_frame_rate':'30',
                    'ffmpeg_audio_codec':'aac -profile:a aac_low -aac_coder twoloop -async 15',
                    'ffmpeg_audio_bitrate':'128',
                    'ffmpeg_input_buffer':'-rtbufsize 128M',
                    'ffmpeg_fifo_queue_size':'240',
                    'ffmpeg_output_flush_packets':True,
                    'ffmpeg_show_window':True,
                    'ffmpeg_enable_experiment':False,
                    'ffmpeg_enable_sound':True,
                    'ffmpeg_template_one':'ffmpeg.exe -y {ffmpeg_input_buffer} -err_detect ignore_err {ffmpeg_hwaccel} -f dshow -i "video={ffmpeg_vmix_video_device}:audio={ffmpeg_vmix_audio_device}" -map 0:v:0 -map 0:a:0 -map 0:v:0 -map 0:a:0 -map 0:v:0 -map 0:a:0 -c:v {ffmpeg_encoder} -pix_fmt yuv420p -r {ffmpeg_output_frame_rate} -g {ffmpeg_output_frame_rate} -profile:v {ffmpeg_profile} -bf 0 -tune zerolatency -low_power 1 -async_depth 1 {ffmpeg_enable_sound} -codec:a {ffmpeg_audio_codec} -b:a {ffmpeg_audio_bitrate} -ar 48000 -bufsize:a 1024k -fps_mode cfr -flush_packets {ffmpeg_output_flush_packets} -preset {ffmpeg_preset} -threads {ffmpeg_threads} -filter:v:0 scale={ffmpeg_dimension_0} -maxrate:v:0 {ffmpeg_video_maxbitrate_0} -b:v:0 {ffmpeg_video_bitrate_0} -filter:v:1 scale={ffmpeg_dimension_1} -maxrate:v:1 {ffmpeg_video_maxbitrate_1} -b:v:1 {ffmpeg_video_bitrate_1} -filter:v:2 scale={ffmpeg_dimension_2} -maxrate:v:2 {ffmpeg_video_maxbitrate_2} -b:v:2 {ffmpeg_video_bitrate_2} -var_stream_map "v:0,a:0,name:{ffmpeg_dimension_h_0}p v:1,a:1,name:{ffmpeg_dimension_h_1}p v:2,a:2,name:{ffmpeg_dimension_h_2}p" -f hls -hls_time 1 -hls_list_size 3 -hls_delete_threshold 1 -hls_flags split_by_time+independent_segments+delete_segments -master_pl_name "{ffmpeg_destination_c}" -y "{ffmpeg_destination_c_folder}{ffmpeg_destination_d}"',
                    'ffmpeg_template_multiple':'ffmpeg.exe -y {ffmpeg_input_buffer} -err_detect ignore_err {ffmpeg_hwaccel} -f dshow -i "video={ffmpeg_vmix_video_device}:audio={ffmpeg_vmix_audio_device}" -map 0:v:0 -map 0:a:0 -map 0:v:0 -map 0:a:0 -map 0:v:0 -map 0:a:0 -c:v {ffmpeg_encoder} -pix_fmt yuv420p -r {ffmpeg_output_frame_rate} -g {ffmpeg_output_frame_rate} -profile:v {ffmpeg_profile} -bf 0 -tune zerolatency -low_power 1 -async_depth 1 {ffmpeg_enable_sound} -codec:a {ffmpeg_audio_codec} -b:a {ffmpeg_audio_bitrate} -ar 48000 -bufsize:a 1024k -fps_mode cfr -flush_packets {ffmpeg_output_flush_packets} -preset {ffmpeg_preset} -threads {ffmpeg_threads} -filter:v:0 scale={ffmpeg_dimension_0} -maxrate:v:0 {ffmpeg_video_maxbitrate_0} -b:v:0 {ffmpeg_video_bitrate_0} -filter:v:1 scale={ffmpeg_dimension_1} -maxrate:v:1 {ffmpeg_video_maxbitrate_1} -b:v:1 {ffmpeg_video_bitrate_1} -filter:v:2 scale={ffmpeg_dimension_2} -maxrate:v:2 {ffmpeg_video_maxbitrate_2} -b:v:2 {ffmpeg_video_bitrate_2} -var_stream_map "v:0,a:0,name:{ffmpeg_dimension_h_0}p v:1,a:1,name:{ffmpeg_dimension_h_1}p v:2,a:2,name:{ffmpeg_dimension_h_2}p" -f hls -hls_time 1 -hls_list_size 3 -hls_delete_threshold 1 -hls_flags split_by_time+independent_segments+delete_segments -master_pl_name "{ffmpeg_destination_c}" -y "{ffmpeg_destination_c_folder}{ffmpeg_destination_d}"'
                },
                f'{t("NEW_PROFILE (DEFAULT_SETTINGS)")}({t("Gstreamer send stream webrtc h264")})':{
                    'ffmpeg_destination_preset':t('Send to webrtc server (Gstreamer)'),
                    'ffmpeg_destination':'"ws://SIGNALLER_IP:SIGNALLER_PORT" meta="meta,name=STREAM_ID"',
                    'ffmpeg_vmix_video_device':'vMix Video',
                    'ffmpeg_vmix_audio_device':'CABLE Output (VB-Audio Virtual Cable)',
                    'ffmpeg_encoder':f'hevc_qsv ({t("Intel GPU, Not all GPU supports")})',
                    'ffmpeg_preset':'veryfast',
                    'ffmpeg_profile':'main',
                    'ffmpeg_dimension':'1920x1080',
                    'ffmpeg_video_bitrate':'3000',
                    'ffmpeg_threads':t('All Available'),
                    'ffmpeg_output_frame_rate':'30',
                    'ffmpeg_audio_codec':'aac -profile:a aac_low -aac_coder twoloop -async 15',
                    'ffmpeg_audio_bitrate':'128',
                    'ffmpeg_input_buffer':'-rtbufsize 128M',
                    'ffmpeg_fifo_queue_size':'240',
                    'ffmpeg_output_flush_packets':True,
                    'ffmpeg_show_window':True,
                    'ffmpeg_enable_experiment':False,
                    'ffmpeg_enable_sound':True,
                    'ffmpeg_template_one':'gst-launch-1.0 webrtcsink name=ws signaller::uri={ffmpeg_destination_b} mfvideosrc device-name="{ffmpeg_vmix_video_device}" ! video/x-raw, format=UYVY ! videoconvert ! queue ! videoscale ! "video/x-raw,width={gstreamer_width},height={gstreamer_height}" ! videorate ! "video/x-raw,framerate={gstreamer_framerate}" ! openh264enc bitrate={gstreamer_video_bitrate} ! h264parse ! ws. {gstreamer_audio_device} ! queue ! audioconvert ! audioresample ! opusenc bitrate={gstreamer_audio_bitrate} perfect-timestamp=true ! ws.',
                    'ffmpeg_template_multiple':'gst-launch-1.0 webrtcsink name=ws signaller::uri={ffmpeg_destination_b} mfvideosrc device-name="{ffmpeg_vmix_video_device}" ! video/x-raw, format=UYVY ! videoconvert ! queue ! videoscale ! "video/x-raw,width={gstreamer_width},height={gstreamer_height}" ! videorate ! "video/x-raw,framerate={gstreamer_framerate}" ! openh264enc bitrate={gstreamer_video_bitrate} ! h264parse ! ws. {gstreamer_audio_device} ! queue ! audioconvert ! audioresample ! opusenc bitrate={gstreamer_audio_bitrate} perfect-timestamp=true ! ws.'
                },
                f'{t("NEW_PROFILE (DEFAULT_SETTINGS)")}({t("Gstreamer receive webrtc h264 stream to srt listen mode on http://127.0.0.1:1234)")}':{
                    'ffmpeg_destination_preset':t('Gstreamer webrtc server (Gstreamer) signaller and info'),
                    'ffmpeg_destination':'"ws://SIGNALLER_IP:SIGNALLER_PORT" meta="meta,name=STREAM_ID"',
                    'ffmpeg_vmix_video_device':'vMix Video',
                    'ffmpeg_vmix_audio_device':'CABLE Output (VB-Audio Virtual Cable)',
                    'ffmpeg_encoder':f'hevc_qsv ({t("Intel GPU, Not all GPU supports")})',
                    'ffmpeg_preset':'veryfast',
                    'ffmpeg_profile':'main',
                    'ffmpeg_dimension':'1920x1080',
                    'ffmpeg_video_bitrate':'3000',
                    'ffmpeg_threads':t('All Available'),
                    'ffmpeg_output_frame_rate':'30',
                    'ffmpeg_audio_codec':'aac -profile:a aac_low -aac_coder twoloop -async 15',
                    'ffmpeg_audio_bitrate':'128',
                    'ffmpeg_input_buffer':'-rtbufsize 128M',
                    'ffmpeg_fifo_queue_size':'240',
                    'ffmpeg_output_flush_packets':True,
                    'ffmpeg_show_window':True,
                    'ffmpeg_enable_experiment':False,
                    'ffmpeg_enable_sound':True,
                    'ffmpeg_template_one':'gst-launch-1.0 mpegtsmux name=flvmux ! srtserversink uri=srt://:1234 webrtcsrc name=whep connect-to-first-producer=true signaller::uri={ffmpeg_destination_b} ! rtpopusdepay ! queue ! flvmux. whep. ! rtph264depay ! h264parse ! queue ! flvmux.',
                    'ffmpeg_template_multiple':'gst-launch-1.0 mpegtsmux name=flvmux ! srtserversink uri=srt://:1234 webrtcsrc name=whep connect-to-first-producer=true signaller::uri={ffmpeg_destination_b} ! rtpopusdepay ! queue ! flvmux. whep. ! rtph264depay ! h264parse ! queue ! flvmux.'
                }
            }
        },
        'ffmpeg_destination_preset':{
                '':[],
                t('Send to rtsp tcp server'):['','rtsp_tcp://MEDIASERVER_IP:MEDIASERVER_PORT/mystream'],
                t('Send to rtsp udp server'):['','rtsp_udp://MEDIASERVER_IP:MEDIASERVER_PORT/mystream'],
                t('Save to file (Open file browser)'):[''],
                t('Save to file'):['','%USERPROFILE%\\Desktop\\%Y-%m-%d_%H-%M-%S.mp4'],
                t('ffmpeg as a SRT server (accept one client)'):['','srt://0.0.0.0:1234?mode=listener&latency=100&congestion=live'],
                t('ffmpeg as a SRT server (accept one client) and save to file (Mutiple destinations)'):['','[srt://0.0.0.0:1234?mode=listener&latency=100&transtype=live&congestion=live][%USERPROFILE%\\Desktop\\%Y-%m-%d_%H-%M-%S.mp4]'],
                t('Send to youtube live'):['','rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY_HERE'],
                t('Send to YouTube Live and save to file (Mutiple destinations)'):['','[rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY_HERE][%USERPROFILE%\\Desktop\\%Y-%m-%d_%H-%M-%S.mp4]'],
                t('Gstreamer webrtc server (Gstreamer) signaller and info'):['','"ws://SIGNALLER_IP:SIGNALLER_PORT" meta="meta,name=STREAM_ID"'],
        },
        'ffmpeg_vmix_video_device':['','vMix Video','vMix Video External 2','vMix Video External 3','vMix Video External 4'],
        'ffmpeg_vmix_audio_device':['','vMix Audio','vMix Audio - 16Ch','vMix Audio - Bus A','vMix Audio - Bus B','vMix Audio - Bus C','vMix Audio - Bus D','vMix Audio - Bus E','vMix Audio - Bus F','vMix Audio - Bus G','vMix Audio - M A','vMix Audio - M A B','vMix Audio - M A B C 8Ch','vMix Audio - F G','CABLE Output (VB-Audio Virtual Cable)', 'Gstreamer system sound output', 'Gstreamer system sound input'],
        'ffmpeg_fifo_queue_size':['','60','120','240','480','600'],
        'ffmpeg_encoder':[
            '',f'libx264 ({t("CPU")})',f'libx265 ({t("CPU")})',f'h264_qsv ({t("Intel GPU, Not all GPU supports")})',f'{t("hevc_qsv (Intel GPU, Not all GPU supports")})',
                        f'av1_qsv ({t("Intel GPU, Not all GPU supports")})',f'h264_nvenc ({t("Nvidia GPU, Not all GPU supports")})',f'hevc_nvenc ({t("Nvidia GPU, Not all GPU supports")})',
                        f'av1_nvenc ({t("Nvidia GPU, Not all GPU supports")})',f'h264_amf ({t("AMD GPU, Not all GPU supports")})',f'hevc_amf ({t("AMD GPU, Not all GPU supports")})',f'av1_amf ({t("AMD GPU, Not all GPU supports")})'
        ],
        'ffmpeg_preset':['','ultrafast','veryfast','fast'],
        'ffmpeg_profile':['','baseline','main','main10'],
        'ffmpeg_dimension':['','854x480','1280x720','1920x1080','2560x1440','3840x2160'],
        'ffmpeg_video_bitrate':['','500','750','1000','1500','2000','3000','4000','6000','8000','16000','32000'],
        'ffmpeg_threads':['','1','2','3','4','5','6','7','8',t('All Available')],
        'ffmpeg_output_frame_rate':['','25','29.97','30','60'],
        'ffmpeg_audio_codec':['','aac -profile:a aac_low -aac_coder twoloop -async 15','libopus -frame_duration 80 -application lowdelay -compression_level 3 -async 15'],
        'ffmpeg_audio_bitrate':['','64','96','128','256'],
        'ffmpeg_input_buffer':['','-fflags +flush_packets+nobuffer','-rtbufsize 128M','-rtbufsize 256M']
    }
    class right_click_menu:
        def __init__(self, e):
            commands = ['Cut','Copy','Paste']
            menu = tk.Menu(None, tearoff=0, takefocus=0)

            for txt in commands:
                menu.add_command(label=t(txt), command=lambda e=e,txt=txt:self.click_command(e,txt))

            menu.tk_popup(e.x_root, e.y_root, entry='0')

        def click_command(self, e, cmd):
            e.widget.event_generate(f'<<{cmd}>>')
            
    def __init__(self, root):
        global settings_window_is_up
        try:
            with open(os.path.expanduser('~\\vmix-helper.conf'), 'rb') as f:
                ffmpeg_settings = pickle.load(f)
        except:
            ffmpeg_settings = copy.deepcopy(self.ffmpeg_default_settings)
        self.settings = {}
        
        self.ffmpeg_settings = ffmpeg_settings
        self.controls_list = {}
        self.font = (font_family,font_size,font_weight)
        self.initialdir_out=os.path.expanduser('~')
        self.root = tk.Toplevel(root)
        self.root.withdraw()
        self.root.iconphoto(False, ImageTk.PhotoImage(icon))
        self.root.title('FFmpeg/Gstreamer (Test)')
        self.root.resizable(False, False)
        self.main_frame = ttk.Frame(self.root, padding='0')
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        self.root.update_idletasks()
        self.root.minsize(
            self.main_frame.winfo_reqwidth() + 10,
            self.main_frame.winfo_reqheight() + 10
        )
        self.process_command()
        settings_window_is_up = True
        self.root.deiconify()
        
    def create_widgets(self):
        global ffmpeg_processes
        frame = ttk.LabelFrame(self.main_frame, text=t('Profiles:'), padding='0')
        frame.grid(row=0, column=0, sticky='ew', padx=10, pady=5)
        frame.bind('<Button-1>', self.on_value_change)
        ttk.Label(frame, text=t('Profile: '),font=(self.font[0], 12, 'bold')).grid(row=0, column=0, sticky='e')
        self.settings['ffmpeg_settings_profile'] = StringVar(value=self.ffmpeg_settings['ffmpeg_settings_profile']['selection'])
        self.controls_list['ffmpeg_settings_profile_combobox'] = ttk.Combobox(
            frame, 
            textvariable=self.settings['ffmpeg_settings_profile'],
            values=list(self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'].keys()), 
            width=75,
            font=(self.font[0], 12, 'bold')
        )
        self.controls_list['ffmpeg_settings_profile_combobox'].grid(row=0, column=1, sticky='w', padx=3, pady=2)
        self.controls_list['ffmpeg_settings_profile_combobox'].bind('<<ComboboxSelected>>', self.on_settings_profile_change)
        self.controls_list['ffmpeg_settings_profile_combobox'].bind('<Button-3>', self.right_click_menu)
        
        self.controls_list['ffmpeg_number_processes'] = ttk.Label(frame, text=f'{t("Number of running processes")} : {str(len(ffmpeg_processes))}',font=(self.font[0], 12, 'bold'))
        self.controls_list['ffmpeg_number_processes'].grid(row=0, column=2, sticky='w')
        
        frame = ttk.LabelFrame(self.main_frame, text=t('Profile settinges :'), padding='0')
        frame.grid(row=1, column=0, sticky='ew', padx=10, pady=5)
        frame.bind('<Button-1>', self.on_value_change)
        
        labels = [t('Destination preset: '),t('Destination: '),t('Input video device: '),t('Input audio device: '),t('Video encoder: '),t('Encoder preset: '),t('Encoder profile: '),
        t('Output video dimension: '),t('Output video bitrate (kbps): '),t('Numbers of threads: '),t('Output video frame rate (fps): '),t('Output audio encoder and settings: '),
        t('Output audio bitrate (kbps): '),t('Input buffer settings: '),t('Output buffer size (packets): '),t('Enable output buffer flush immediately.'),t('Show console window.'),
        t('Enable experimental (Required for AV1 encoding for stream).'),t('Enable output audio.')]
        ind = 0
        profile_selecetd = self.ffmpeg_settings['ffmpeg_settings_profile']['selection']
        for key, value in self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd].items():
            if key == 'ffmpeg_template_one':break
            if isinstance(value, bool):
                self.settings[key] = BooleanVar(value=self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd][key])
                self.controls_list[f'{key}_checkbutton'] = tk.Checkbutton(frame, text=labels[ind], variable=self.settings[key], command=self.on_value_change, font=self.font)
                self.controls_list[f'{key}_checkbutton'].grid(row=ind+1, column=0, columnspan=3, sticky='w', padx=3, pady=1)
                ind+=1
                continue
            ttk.Label(frame, text=labels[ind],font=self.font).grid(row=ind+1, column=0, sticky='e')
            self.settings[key] = StringVar(value=self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd][key])
            self.controls_list[f'{key}_combobox'] = ttk.Combobox(
                frame, 
                textvariable=self.settings[key],
                values=(list(self.ffmpeg_settings['ffmpeg_destination_preset'].keys()) if key == 'ffmpeg_destination_preset' else (self.ffmpeg_settings['ffmpeg_destination_preset'][self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd]['ffmpeg_destination_preset']] if key == 'ffmpeg_destination' else self.ffmpeg_settings[key])),
                width=(110 if 'destination' in key else 40),
                font=self.font
            )
            self.controls_list[f'{key}_combobox'].grid(row=ind+1, column=1, sticky='w', padx=3, pady=2)
            self.controls_list[f'{key}_combobox'].bind('<<ComboboxSelected>>', self.on_value_change if key != 'ffmpeg_destination_preset' else self.on_destination_preset_change)
            self.controls_list[f'{key}_combobox'].bind('<FocusOut>', self.on_value_change if key != 'ffmpeg_destination_preset' else self.on_destination_preset_change)
            self.controls_list[f'{key}_combobox'].bind('<Button-3>', self.right_click_menu)
            ind+=1
            
        frame2 = ttk.LabelFrame(self.main_frame, text=t('Command :'), padding='10')
        frame2.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
        self.tab_control = ttk.Notebook(frame2)
        labels3 = [t('The command'),t('Command template for one destination'),t('Command template for multiple destinations')]
        for i in range(3):
            self.controls_list[f'tab{i}'] = ttk.Frame(self.tab_control)
            self.controls_list[f'tab{i}_textbox'] = tk.Text(self.controls_list[f'tab{i}'], font=(self.font[0], 12, 'bold' if i ==0 else 'normal'), height=6, width=100, wrap=tk.WORD)
            self.controls_list[f'tab{i}_textbox'].grid(row=0, column=0, sticky='nsew', padx=3, pady=2)

            self.controls_list[f'tab{i}_scroll'] = ttk.Scrollbar(self.controls_list[f'tab{i}'], orient='vertical', command=self.controls_list[f'tab{i}_textbox'].yview)
            self.controls_list[f'tab{i}_textbox'].configure(yscrollcommand=self.controls_list[f'tab{i}_scroll'].set)
            self.controls_list[f'tab{i}_scroll'].grid(row=0, column=1, sticky='ns')
            self.controls_list[f'tab{i}'].grid_rowconfigure(0, weight=1)
            self.controls_list[f'tab{i}'].grid_columnconfigure(0, weight=1)
            self.controls_list[f'tab{i}'].grid_columnconfigure(1, weight=0)
            self.controls_list[f'tab{i}_textbox'].insert('1.0', '' if i == 0 else (self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd]['ffmpeg_template_one'] if i==1 else self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd]['ffmpeg_template_multiple']))
            self.controls_list[f'tab{i}_textbox'].bind('<Button-3>', self.right_click_menu)
            self.tab_control.add(self.controls_list[f'tab{i}'], text=labels3[i])
        self.tab_control.pack(expand=True, fill='both')
        
        frame3 = ttk.Frame(self.main_frame)
        frame3.grid(row=3, column=0, sticky='e', pady=10)
        tk.Button(frame3, text=t('Remove This Profile'), command=self.remove_profile,font=self.font).grid(row=0, column=0, padx=5, sticky='e')
        tk.Button(frame3, text=t('Restore default'), command=self.restore_default,font=self.font).grid(row=0, column=1, padx=5, sticky='e')
        tk.Button(frame3, text=t('Get address'), command=self.get_ffmpeg_url,font=self.font).grid(row=0, column=2, padx=5, sticky='e')
        tk.Button(frame3, text=t('Close all processes'), command=self.close_ffmpeg,font=self.font).grid(row=0, column=3, padx=5, sticky='e')
        tk.Button(frame3, text=t('Save Settings'), command=self.save_settings,font=self.font).grid(row=0, column=4, padx=5, sticky='e')
        tk.Button(frame3, text=f'    {t("Sart")}    ', command=self.start_ffmpeg,font=self.font).grid(row=0, column=5, padx=5, sticky='e')
        
    def save_settings(self, ignore_name=False):
        if not ignore_name:
            profile_name = self.settings['ffmpeg_settings_profile'].get()
            if (profile_name == '') or (profile_name in list(self.ffmpeg_default_settings['ffmpeg_settings_profile']['profiles'].keys())):
                messagebox.showerror(t('Failed'), t('Change settings profile name.'))
                return
            if self.settings['ffmpeg_destination_preset'].get() == '':
                messagebox.showerror(t('Failed'), t('Set a name for destination preset.'))
                return
        selected_profile = ''
        selected_destination_profile = ''
        for key, value in self.settings.items():
            val = value.get()
            if key=='ffmpeg_settings_profile':
                selected_profile = val
                self.ffmpeg_settings['ffmpeg_settings_profile']['selection'] = val
                if val not in list(self.ffmpeg_settings[key]['profiles'].keys()):
                    self.ffmpeg_settings[key]['profiles'].update({val:{}})
                    self.controls_list['ffmpeg_settings_profile_combobox']['values'] = list(self.ffmpeg_settings[key]['profiles'].keys())
                continue
            elif key=='ffmpeg_destination_preset':
                selected_destination_profile = val;
                if val not in list(self.ffmpeg_settings[key].keys()):
                    self.ffmpeg_settings[key].update({val:['']})
                    self.controls_list['ffmpeg_destination_preset_combobox']['values'] = list(self.ffmpeg_settings[key].keys())
            elif key == 'ffmpeg_destination':
                if self.settings['ffmpeg_destination_preset'].get() != t('Save to file (Open file browser)'):
                    if val not in self.ffmpeg_settings['ffmpeg_destination_preset'][selected_destination_profile]:
                        self.ffmpeg_settings['ffmpeg_destination_preset'][selected_destination_profile].append(val)
                        self.controls_list['ffmpeg_destination_combobox']['values'] = self.ffmpeg_settings['ffmpeg_destination_preset'][selected_destination_profile]
            elif isinstance(val, bool) == False and val not in self.ffmpeg_settings[key]:
                self.ffmpeg_settings[key].append(val)
                self.controls_list[f'{key}_combobox']['values'] = self.ffmpeg_settings[key]
            self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][selected_profile][key]=val
        self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][selected_profile]['ffmpeg_template_one'] = self.controls_list[f'tab1_textbox'].get('1.0', tk.END).strip()
        self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][selected_profile]['ffmpeg_template_multiple'] = self.controls_list[f'tab2_textbox'].get('1.0', tk.END).strip()
        try:
            with open(os.path.expanduser('~\\vmix-helper.conf'), 'wb') as f:
                pickle.dump(self.ffmpeg_settings, f)
                self.process_command()
        except Exception as e:
            messagebox.showerror('Failed', e)
        messagebox.showinfo(t('Successful'), f'{t("Settings saved successful in")} {f.name}')

    def restore_default(self):
        self.ffmpeg_settings = copy.deepcopy(self.ffmpeg_default_settings)
        profile_selecetd = self.ffmpeg_settings['ffmpeg_settings_profile']['selection']
        for key, value in self.settings.items():
            if key == 'ffmpeg_settings_profile':
                self.settings['ffmpeg_settings_profile'].set(profile_selecetd)
                self.controls_list[f'ffmpeg_settings_profile_combobox']['values'] = list(self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'].keys())
                continue
            self.settings[key].set(self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd][key])
            if not isinstance(value.get(), bool):
                self.controls_list[f'{key}_combobox']['values'] = list(self.ffmpeg_settings['ffmpeg_destination_preset'].keys()) if key == 'ffmpeg_destination_preset' else (self.ffmpeg_settings['ffmpeg_destination_preset'][self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd]['ffmpeg_destination_preset']] if key == 'ffmpeg_destination' else self.ffmpeg_settings[key])

        self.controls_list['tab1_textbox'].delete('1.0', tk.END)
        self.controls_list['tab2_textbox'].delete('1.0', tk.END)
        self.controls_list['tab1_textbox'].insert('1.0', self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd]['ffmpeg_template_one'])
        self.controls_list['tab2_textbox'].insert('1.0', self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd]['ffmpeg_template_multiple'])
        self.process_command()
        self.save_settings(ignore_name=True)
        
    def on_settings_profile_change(self,event):
        profile_selecetd = self.settings['ffmpeg_settings_profile'].get()
        if (profile_selecetd == t('NEW_PROFILE (KEEP_PREVIOUS_SETTINGS)')) or (profile_selecetd not in list(self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'].keys())):
            return
        for key, value in self.settings.items():
            if key == 'ffmpeg_settings_profile':
                continue
            self.settings[key].set(self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd][key])
        for i in range(1,3):
            self.controls_list[f'tab{i}_textbox'].delete('1.0', tk.END)
            self.controls_list[f'tab{i}_textbox'].insert('1.0', self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_selecetd]['ffmpeg_template_one' if i==1 else 'ffmpeg_template_multiple'])
        if event.type == '35':
            if profile_selecetd in list(self.ffmpeg_default_settings['ffmpeg_settings_profile']['profiles'].keys()):
                self.on_destination_preset_change(event,defaultextension='.m3u8',filetypes=(('HLS file', '*.m3u8'), ('MP4 file', '*.mp4'), ('MKV file', '*.mkv'), ('TS file', '*.ts')))
            else:
                self.on_destination_preset_change(None,defaultextension='.m3u8',filetypes=(('HLS file', '*.m3u8'), ('MP4 file', '*.mp4'), ('MKV file', '*.mkv'), ('TS file', '*.ts')))
        self.process_command()
        
    def remove_profile(self):
        profile_name = self.settings['ffmpeg_settings_profile'].get()
        if (profile_name == '') or (profile_name in list(self.ffmpeg_default_settings['ffmpeg_settings_profile']['profiles'].keys())):
            messagebox.showerror(t('Failed'), t('Failed to delete this profile'))
            return
        if (profile_name in list(self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'].keys())):
            del self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'][profile_name]
            self.settings['ffmpeg_settings_profile'].set(t('NEW_PROFILE (DEFAULT_SETTINGS)'))
            self.controls_list['ffmpeg_settings_profile_combobox']['values'] = list(self.ffmpeg_settings['ffmpeg_settings_profile']['profiles'].keys())
            self.on_settings_profile_change(None)
            self.settings['ffmpeg_settings_profile'].set(t('NEW_PROFILE (DEFAULT_SETTINGS)'))
            self.process_command()
            self.save_settings(ignore_name=True)
        
    def on_destination_preset_change(self, event, defaultextension='.mp4',filetypes=(('MP4 file', '*.mp4'), ('HLS file', '*.m3u8'), ('MKV file', '*.mkv'), ('TS file', '*.ts'))):
        if event is not None and event.type == '35':
            if (self.settings['ffmpeg_destination_preset'].get() != '') and (self.settings['ffmpeg_destination_preset'].get() in list(self.ffmpeg_settings['ffmpeg_destination_preset'].keys())):
                self.controls_list['ffmpeg_destination_combobox']['values'] = self.ffmpeg_settings['ffmpeg_destination_preset'][self.settings['ffmpeg_destination_preset'].get()]
                if(self.settings['ffmpeg_destination_preset'].get() != t('Save to file (Open file browser)')):
                    try:
                        self.settings['ffmpeg_destination'].set(self.ffmpeg_settings['ffmpeg_destination_preset'][self.settings['ffmpeg_destination_preset'].get()][1])
                    except:
                        self.settings['ffmpeg_destination'].set(self.ffmpeg_settings['ffmpeg_destination_preset'][self.settings['ffmpeg_destination_preset'].get()][0])
            else:
                self.controls_list['ffmpeg_destination_combobox']['values'] = list(OrderedDict.fromkeys([item for sublist in self.ffmpeg_settings['ffmpeg_destination_preset'].values() for item in sublist]))
                
            if self.settings['ffmpeg_destination_preset'].get() == t('Save to file (Open file browser)'):
                filepath = filedialog.asksaveasfilename(
                    initialdir=self.initialdir_out,
                    title=t('Save file as:'),
                    filetypes=filetypes,
                    defaultextension=defaultextension,
                    parent=self.root
                )
                if filepath:
                    self.settings['ffmpeg_destination'].set(filepath.replace('/','\\'))
                else:
                    self.settings['ffmpeg_destination'].set(f'%USERPROFILE%\\Desktop\\%Y-%m-%d_%H-%M-%S{defaultextension}')
                self.initialdir_out = os.path.dirname(self.settings['ffmpeg_destination'].get())
            self.on_value_change(event)
        
    def on_value_change(self, event = None):
        self.process_command()

    def get_file_name(self,destination_str):
        new_path = re.sub(r'%[YmdHMS%-]+',lambda m: datetime.now().strftime(m.group(0)),r'' + destination_str)
        expanded_path = os.path.expandvars(new_path)
        expanded_path = os.path.expanduser(expanded_path)
        if os.path.isabs(expanded_path) and expanded_path[0]!='/':
            return {'is_file':True,'path':expanded_path}
        else:
            return {'is_file':False,'path':destination_str}
            
    def get_format(self,is_file,path,is_multiple):
        from urllib.parse import urlparse
        if is_file:
            ext = os.path.splitext(path)[1]
        else:
            ext = re.findall(r'^(.*?):\/\/', path)[0]
        
        strict = (':strict=experimental' if self.settings['ffmpeg_enable_experiment'].get() else '')
        
        if ext=='.mp4':
            if is_multiple:return 'mp4:movflags=+faststart+frag_keyframe' + strict
            else:return 'mp4 -format_opts movflags=+faststart+frag_keyframe' + strict
        if ext=='.mkv':
            return 'mkv'
        if ext=='srt':
            return 'mpegts'
        if ext=='udp':
            return 'mpegts'
        if ext=='rtmp':
            return 'flv' + strict
        if ext=='rtsp':
            if is_multiple:return 'rtsp:rtsp_transport=tcp' + strict
            else:return 'rtsp -format_opts rtsp_transport=tcp' + strict
        if ext=='rtsp_udp':
            if is_multiple:return 'rtsp:rtsp_transport=udp' + strict
            else:return 'rtsp -format_opts rtsp_transport=udp' + strict
        if ext=='rtsp_tcp':
            if is_multiple:return 'rtsp:rtsp_transport=tcp' + strict
            else:return 'rtsp -format_opts rtsp_transport=tcp' + strict
        if ext=='.ts':
            return 'mpegts'
        if ext=='.m3u8':
            if is_multiple:return 'hls:hls_time=4:hls_list_size=0' + strict
            else:return 'hls -format_opts hls_time=4:hls_list_size=0' + strict
        return ''
        
    def process_destinations(self,destination_str):
        if len(destination_str)==0:return {'is_multiple':False,'ffmpeg_destination_a':'','ffmpeg_destination_b':'','ffmpeg_destination':''}
        try:
            is_multiple = True if destination_str[0] == '[' else False
            if is_multiple:
                final_str = ''
                destinations = re.findall(r'(?<!\\)\[(.*?)(?<!\\)\]', destination_str)
                set_pipe = False
                for destination in destinations:
                    dest = self.get_file_name(destination)
                    if dest['is_file']:
                        final_str = f'{final_str}{("|" if set_pipe else "")}[f={self.get_format(dest["is_file"],dest["path"],True)}]' + dest["path"].replace("\\","\\\\")
                        set_pipe = True
                for destination in destinations:
                    dest = self.get_file_name(destination)
                    if not dest['is_file']:
                        final_str = f'{final_str}{("|" if set_pipe else "")}[f={self.get_format(dest["is_file"],dest["path"],True)}]' + dest["path"].replace("\\","\\\\").replace("rtsp_udp://","rtsp://").replace("rtsp_tcp://","rtsp://")
                        set_pipe = True
                return {'is_multiple':True,'ffmpeg_destination':final_str}
            else:
                dest = self.get_file_name(destination_str)
                return {'is_multiple':False,'ffmpeg_destination_a':self.get_format(dest['is_file'],dest['path'],False),'ffmpeg_destination_b':dest['path'].replace('rtsp_udp://','rtsp://').replace('rtsp_tcp://','rtsp://')}
        except:
            return {'is_multiple':False,'ffmpeg_destination_a':'','ffmpeg_destination_b':destination_str,'ffmpeg_destination':destination_str}
        
    def process_command(self):
        global virtual_audio_device_id
        from datetime import datetime
        from pathlib import Path
        is_multi_output = True if (len(self.settings['ffmpeg_destination'].get())>0 and '[' in self.settings['ffmpeg_destination'].get()[0]) else False
        template = self.controls_list[f'tab2_textbox'].get('1.0', tk.END).strip() if is_multi_output else self.controls_list[f'tab1_textbox'].get('1.0', tk.END).strip()

        template = template.replace('{ffmpeg_input_buffer}',self.settings['ffmpeg_input_buffer'].get()).replace('{ffmpeg_vmix_video_device}',self.settings['ffmpeg_vmix_video_device'].get())
        template = template.replace('{ffmpeg_vmix_audio_device}',self.settings['ffmpeg_vmix_audio_device'].get()).replace('{ffmpeg_encoder}',self.settings['ffmpeg_encoder'].get().split(' (')[0])
        template = template.replace('{ffmpeg_dimension}',self.settings['ffmpeg_dimension'].get()).replace('{ffmpeg_output_frame_rate}',self.settings['ffmpeg_output_frame_rate'].get())
        template = template.replace('{ffmpeg_threads}',self.settings['ffmpeg_threads'].get().replace(t('All Available'),'0')).replace('{ffmpeg_profile}',self.settings['ffmpeg_profile'].get())
        template = template.replace('{ffmpeg_preset}',self.settings['ffmpeg_preset'].get()).replace('{ffmpeg_video_bitrate}',self.settings['ffmpeg_video_bitrate'].get() + 'k')
        template = template.replace('{ffmpeg_enable_sound}',('' if self.settings['ffmpeg_enable_sound'].get() else '-an')).replace('{ffmpeg_audio_codec}',self.settings['ffmpeg_audio_codec'].get())
        template = template.replace('{ffmpeg_audio_bitrate}',self.settings['ffmpeg_audio_bitrate'].get() + 'k').replace('{experimental}',('-strict experimental' if self.settings['ffmpeg_enable_experiment'].get() else ''))
        template = template.replace('{ffmpeg_output_flush_packets}',str(int(self.settings['ffmpeg_output_flush_packets'].get()))).replace('{ffmpeg_fifo_queue_size}',self.settings['ffmpeg_fifo_queue_size'].get())
        template = template.replace('{ffmpeg_hwaccel}',self.get_hwaccel(self.settings['ffmpeg_encoder'].get())).replace('{ffmpeg_video_maxbitrate}',str(int(int(self.settings['ffmpeg_video_bitrate'].get())*1.5)) + 'k')
        
        template = template.replace('{gstreamer_width}',self.settings['ffmpeg_dimension'].get().split('x')[0] if len(self.settings['ffmpeg_dimension'].get().split('x'))>1 else '')
        template = template.replace('{gstreamer_height}',self.settings['ffmpeg_dimension'].get().split('x')[1] if len(self.settings['ffmpeg_dimension'].get().split('x'))>1 else '')
        template = template.replace('{gstreamer_framerate}',self.settings['ffmpeg_output_frame_rate'].get() + '/1')
        template = template.replace('{gstreamer_video_bitrate}',self.settings['ffmpeg_video_bitrate'].get() + '000')
        template = template.replace('{gstreamer_audio_bitrate}',self.settings['ffmpeg_audio_bitrate'].get() + '000')
        if self.settings['ffmpeg_vmix_audio_device'].get()=='Gstreamer system sound output':
            template = template.replace('{gstreamer_audio_device}','wasapisrc loopback=true')
        elif self.settings['ffmpeg_vmix_audio_device'].get()=='Gstreamer system sound input':
            template = template.replace('{gstreamer_audio_device}','directsoundsrc')
        else:
            template = template.replace('{gstreamer_audio_device}',virtual_audio_device_id)
        destination = self.process_destinations(self.settings['ffmpeg_destination'].get())
        if destination['is_multiple']:
            template = template.replace('{loop_destinations}',destination['ffmpeg_destination'])
        else:
            template = template.replace('{ffmpeg_destination_a}',destination['ffmpeg_destination_a'])
            template = template.replace('-fifo_format ',('' if destination['ffmpeg_destination_a'] == '' else '-fifo_format '))
            template = template.replace('{ffmpeg_destination_b}',destination['ffmpeg_destination_b'])
        if not is_multi_output:
            new_dimension = [int(self.settings['ffmpeg_dimension'].get().split('x')[0]),int(self.settings['ffmpeg_dimension'].get().split('x')[1]),
                        int(self.settings['ffmpeg_dimension'].get().split('x')[0])/int(self.settings['ffmpeg_dimension'].get().split('x')[1])]
            new_bitrate = int(self.settings['ffmpeg_video_bitrate'].get())
            new_max_bitrate = int(new_bitrate*1.5)
            path = self.get_file_name(self.settings['ffmpeg_destination'].get())
            if path['is_file']:
                directory = os.path.dirname(path['path']) + ('\\' if os.path.dirname(path['path'])[-1] != '\\' else '')
                directory = directory.replace('\\','\\\\')
                res = [4320,2160,1440,1080,720,480,320]
                for i in range(4):
                    template = template.replace('{ffmpeg_dimension_' + str(i) + '}',f'w={new_dimension[0]}:h={new_dimension[1]}').replace('{ffmpeg_dimension_h_' + str(i) + '}',f'{new_dimension[1]}')
                    template = template.replace('{ffmpeg_video_bitrate_' + str(i) + '}',f'{new_bitrate}k').replace('{ffmpeg_video_maxbitrate_' + str(i) + '}',f'{new_max_bitrate}k')
                    template = template.replace('{ffmpeg_destination_c_folder}',directory).replace('{ffmpeg_destination_c}',Path(path['path']).name)
                    template = template.replace('{ffmpeg_destination_d}',Path(path['path']).name.replace('.m3u8','-%v.m3u8'))
                    if res.index(new_dimension[1])+1<len(res):
                        new_new_res = res[res.index(new_dimension[1])+1]
                    else:
                        new_new_res = res[res.index(new_dimension[1])]
                    new_bitrate = int(new_bitrate / (new_dimension[1]/new_new_res))
                    new_max_bitrate = int(new_bitrate*1.5)
                    new_dimension[1] = new_new_res
                    new_dimension[0] = int(new_dimension[1]*new_dimension[2])

        self.controls_list['tab0_textbox'].delete('1.0', tk.END)
        self.controls_list['tab0_textbox'].insert('1.0', template)
        
    def get_hwaccel(self,encoder):
        if 'nvenc' in encoder:return '-hwaccel cuda -hwaccel_output_format cuda'
        if 'qsv' in encoder:return '-hwaccel qsv -hwaccel_output_format qsv'
        if 'amf' in encoder:return '-hwaccel d3d11va -hwaccel_output_format d3d11'
        return ''

    def start_ffmpeg(self):
        global ffmpeg_processes
        global ffmpeg_processes_closing_is_running
        if ffmpeg_processes_closing_is_running:
            messagebox.showerror(t('Failed'), t('Closing processes in progress please wait and try again.'))
            return
        ffmpeg_command_line = self.controls_list['tab0_textbox'].get('1.0', tk.END).strip()
        try:
            import winreg
            os.environ['PATH']=os.path.expandvars(winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'System\CurrentControlSet\Control\Session Manager\Environment', 0, winreg.KEY_READ), 'Path')[0])
            if self.settings['ffmpeg_show_window'].get():
                process = subprocess.Popen(f'cmd.exe /k "{ffmpeg_command_line}"', creationflags=subprocess.CREATE_NEW_CONSOLE, env=os.environ.copy())
            else:
                process = subprocess.Popen(f'cmd.exe /c "{ffmpeg_command_line}"',stdin=subprocess.PIPE,creationflags=subprocess.CREATE_NO_WINDOW, env=os.environ.copy())
            tmp_info = f'{t("Profile: ")}{self.settings["ffmpeg_settings_profile"].get()}\r\n\r\n{t("Command : ")}{ffmpeg_command_line}'
            CustomMessageBox(root, wait=False ,msg_type='info',title=t('Success'),message=f'{tmp_info}\r\n\r\n {t("Successfully started. You will get a messsage if process stoped.")}')
            ffmpeg_processes.append({'process':process,'show_console':self.settings['ffmpeg_show_window'].get(),'time_add':int(time.time()),'ffmpeg_command_line':tmp_info})
            self.controls_list['ffmpeg_number_processes']['text'] = f'{t("Number of running processes")} : {str(len(ffmpeg_processes))}'
        except Exception as e:
            CustomMessageBox(root, wait=False ,msg_type='error',title=t('Failed'),message=e)
        return True
        
    def close_ffmpeg(self):
        global ffmpeg_processes_closing_is_running
        if ffmpeg_processes_closing_is_running:return
        ffmpeg_processes_closing_is_running = True
        threading.Thread(target=close_ffmpeg_thread, args=()).start()
          
    def get_ffmpeg_url(self):
        destination_str = self.settings['ffmpeg_destination'].get()
        is_multiple = True if destination_str[0] == '[' else False
        final_str = ''
        local_ip = None
        if is_multiple:
            destinations = re.findall(r'(?<!\\)\[(.*?)(?<!\\)\]', destination_str)
            for destination in destinations:
                dest = self.get_file_name(destination)
                final_str = final_str + ('' if final_str=='' else '\r\n\r\n') + dest['path']
                if 'srt://' in dest['path']:
                    try:
                        res_r = re.findall(r'^srt:\/\/(.*?):([0-9]{4,5})?', dest['path'])
                        res = f'IP={res_r[0][0]}   PORT={res_r[0][1]}'
                        final_str = f'{final_str}\r\n{res}'
                    except:
                        continue
        else:
            dest = self.get_file_name(destination_str)
            final_str = dest['path']
            if 'srt://' in dest['path']:
                try:
                    res_r = re.findall(r'^srt:\/\/(.*?):([0-9]{4,5})?', dest['path'])
                    res = f'IP={res_r[0][0]}   PORT={res_r[0][1]}'
                    final_str = f'{final_str}\r\n{res}'
                except:
                    pass
        import socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            local_ip = s.getsockname()[0]
            s.close()
        except:
            local_ip = None
        
        if local_ip is not None:
            final_str = final_str.replace('localhost',local_ip).replace('127.0.0.1',local_ip).replace('0.0.0.0',local_ip)
        if 'srt://' in final_str:
            final_str = final_str.replace('mode=listener','mode=caller')
        final_str = final_str.replace('rtsp_udp://','rtsp://').replace('rtsp_tcp://','rtsp://')
       
        CustomMessageBox(
            self.root,
            wait=False,
            msg_type='info',
            title=t('Success'),
            message=final_str,
            _font=(font_family, 12,'bold'),
            wrap=False
        )

def send_q_key_to_childs(parent_hwnd):
    def callback(hwnd, extra):
        try:
            win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x51, make_lparam(0x51, MapVirtualKey(0x51, 0)))
            win32gui.PostMessage(hwnd, win32con.WM_KEYUP, 0x51, make_lparam(0x51, MapVirtualKey(0x51, 0)))
        except:
            pass
        return True
    win32gui.EnumChildWindows(parent_hwnd, callback, None)
    return True

def send_q_key():
    def callback(hwnd, extra):
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            process = psutil.Process(pid)
            window_title = win32gui.GetWindowText(hwnd)
            if 'windowsterminal.exe' in process.exe().lower() and 'cmd.exe' in window_title:
                send_q_key_to_childs(hwnd)
                win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x51, make_lparam(0x51, MapVirtualKey(0x51, 0)))
                win32gui.PostMessage(hwnd, win32con.WM_KEYUP, 0x51, make_lparam(0x51, MapVirtualKey(0x51, 0)))
        except:
            pass
        return True
    win32gui.EnumWindows(callback, None)
    return True
        
def close_ffmpeg_thread(wait=True):
    try:
        global ffmpeg_processes
        if len(ffmpeg_processes)==0:return
        global ffmpeg_processes_closing_is_running
        if not ffmpeg_processes:
            ffmpeg_processes_closing_is_running = False
            return
        for i in range(len(ffmpeg_processes)):
            if int(time.time()) - ffmpeg_processes[i]['time_add']<3:time.sleep(3-(int(time.time()) - ffmpeg_processes[i]['time_add']))
            try:
                if ffmpeg_processes[i]['show_console']:
                    send_q_key()
                else:
                    ffmpeg_processes[i]['process'].stdin.write(b'q')
                    ffmpeg_processes[i]['process'].stdin.flush()
            except:continue
        if wait:
            time.sleep(3)
        for i in range(len(ffmpeg_processes)):
            try:
                parent = psutil.Process(ffmpeg_processes[i]['process'].pid)
                children = parent.children(recursive=True)
                try:
                    for proc in children:
                        os.kill(proc.pid,signal.SIGINT)
                    time.sleep(1)
                    os.kill(parent.pid,signal.SIGINT)
                except:continue
            except:continue
        ffmpeg_processes.clear()
        ffmpeg_processes_closing_is_running = False
        return
    except:
        ffmpeg_processes_closing_is_running = False
        return
            
class frame_thread(threading.Thread):
    def __init__(self,_layout_frame_window):
        super().__init__()
        self._stop_event = threading.Event()
        mouse.on_click(self.on_mouse_click)
        self.layout_frame_window = _layout_frame_window
        self.selected_layer_input = ''
        self.vmix_hwnd=0
        self.output_hwnd=0
        self.vmix_resolution={'width':0,'height':0}
        self.show_frame = False

    def run(self):
        self.show_frame_func()

    def get_output_window(self,active_window_hwnd):
        output_window = {}
        if active_window_hwnd != self.vmix_hwnd:
            client_left, client_top = win32gui.ClientToScreen(active_window_hwnd, (0, 0))
            windows = self.list_child_windows(active_window_hwnd)
            tmp_left = 0
            for window in windows:
                if window['rect_window'][1]-client_top == 54:
                    if window['client_left']>tmp_left:
                        tmp_left = window['client_left']
                        output_window = window
                        self.vmix_hwnd = active_window_hwnd
                        self.output_hwnd = output_window['hwnd']
        else:
            rect_window = win32gui.GetWindowRect(self.output_hwnd)
            rect_client = win32gui.GetClientRect(self.output_hwnd)
            client_left, client_top = win32gui.ClientToScreen(self.output_hwnd, (0, 0))
            output_window = {
                'hwnd': self.output_hwnd,
                'rect_window':rect_window,
                'rect_client':rect_client,
                'client_left':client_left,
                'client_top':client_top
            }
        return output_window
        
    def show_frame_func(self):
        while not self._stop_event.is_set():
            try:
                time.sleep(0.1)
                if self.show_frame:
                    self.selected_layer_input = ''
                if self.show_frame or self.layout_frame_window.frame_is_visible():
                    self.show_frame = False
                    active_window_hwnd = win32gui.GetForegroundWindow()
                    active_process_name = psutil.Process(win32process.GetWindowThreadProcessId(active_window_hwnd)[1]).name().lower()
                    if active_process_name == 'vmix64.exe':
                        active_window_title = win32gui.GetWindowText(active_window_hwnd).lower()
                        if 'vmix' in active_window_title and 'screen' not in active_process_name:
                            output_window = self.get_output_window(active_window_hwnd)
                            if not output_window:continue
                            mouse_x = mouse.get_position()[0]
                            mouse_y = mouse.get_position()[1]
                            window_w = output_window['rect_client'][2]
                            window_h = output_window['rect_client'][3]
                            window_x = output_window['rect_window'][0]
                            window_y = output_window['rect_window'][1]
                            result = self.get_layer_position_and_number(mouse_x-window_x,mouse_y-window_y,window_w,window_h,self.selected_layer_input)
                            if result is None and self.layout_frame_window.frame_is_visible():
                                self.layout_frame_window.hide_frame()
                            elif result is not None:
                                self.layout_frame_window.show_frame(result['w'],result['h'],result['x']+window_x,result['y']+window_y,result['number'])
                                self.selected_layer_input = result['number']
                        elif self.layout_frame_window.frame_is_visible():
                            self.layout_frame_window.hide_frame()
                    elif active_window_hwnd != self.layout_frame_window.get_hwnd() and self.layout_frame_window.frame_is_visible():
                        self.layout_frame_window.hide_frame()
            except:
                pass
        if self.layout_frame_window.frame_is_visible():
            self.layout_frame_window.hide_frame()
        
    def on_mouse_click(self):
        try:
            active_window_hwnd = win32gui.GetForegroundWindow()
            time.sleep(0.05)
            if active_window_hwnd != win32gui.GetForegroundWindow():
                return
            active_process_name = psutil.Process(win32process.GetWindowThreadProcessId(active_window_hwnd)[1]).name().lower()
            if active_process_name == 'vmix64.exe':
                active_window_title = win32gui.GetWindowText(active_window_hwnd).lower()
                if 'vmix' in active_window_title and 'screen' not in active_process_name:
                    output_window = self.get_output_window(active_window_hwnd)
                    mouse_x = mouse.get_position()[0]
                    mouse_y = mouse.get_position()[1]
                    window_w = output_window['rect_client'][2]
                    window_h = output_window['rect_client'][3]
                    window_x = output_window['rect_window'][0]
                    window_y = output_window['rect_window'][1]
                    if ((mouse_x > window_x and mouse_x < (window_x+window_w)) and (mouse_y > window_y and mouse_y < (window_y+window_h))):
                        self.show_frame = True
        except:
            pass        
    def stop(self):
        mouse.unhook_all()
        self._stop_event.set()
        
    def list_child_windows(self,parent_hwnd):
        children = []
        
        def callback(hwnd, extra):
            rect_window = win32gui.GetWindowRect(hwnd)
            rect_client = win32gui.GetClientRect(hwnd)
            client_left, client_top = win32gui.ClientToScreen(hwnd, (0, 0))
            children.append({
                'hwnd': hwnd,
                'rect_window':rect_window,
                'rect_client':rect_client,
                'client_left':client_left,
                'client_top':client_top
            })
            return True
        
        win32gui.EnumChildWindows(parent_hwnd, callback, None)
        return children
        
    def get_vmix_resolution(self,vmix_version):
        if self.vmix_resolution['width'] !=0 :return self.vmix_resolution
        base_dir = f'{os.environ.get("LOCALAPPDATA", "")}\\StudioCoast_Pty_Ltd'
        vmix_folders = glob.glob(os.path.join(base_dir, 'vMix64.exe_Url_*'))
        
        if not vmix_folders:
            return self.vmix_resolution

        dynamic_folder = vmix_folders[0]
        config_path = os.path.join(dynamic_folder, vmix_version, 'user.config')
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    xmlDoc = ET.fromstring(f.read().strip())
                    output_size_setting = xmlDoc.find(".//setting[@name='OutputSize']")
                    if output_size_setting is not None:
                        value = output_size_setting.find('value').text
                        self.vmix_resolution['width'] = int(value.split('x')[0])
                        self.vmix_resolution['height'] = int(value.split('x')[1])
                        return self.vmix_resolution
                    else:
                        return self.vmix_resolution
            except:
                return self.vmix_resolution
                
    def get_layer_position_and_number(self,mouse_x,mouse_y,window_w,window_h,selected_layer_input):
        topmost_layer = {}
        topmost_layer['number'],topmost_layer['y'],topmost_layer['x'],topmost_layer['w'],topmost_layer['h'] = ['-1',0,0,int(window_w),int(window_h)]
        if selected_layer_input == '-1':
            return topmost_layer
        page = f'http://127.0.0.1:{str(vmix_port)}/api/'
        try:
            response = requests.get(page,timeout=0.2)
        except:
            return topmost_layer
        xmlDoc = ET.fromstring(response.text)
        
        activeNode = xmlDoc.find('./active')
        if activeNode is None:
            return topmost_layer
        activeNode = activeNode.text
        inputNode = xmlDoc.find(f'./inputs/input[@number=\'{activeNode}\']')
        if inputNode is None:
            return topmost_layer
        else:
            for overlayNode in inputNode:
                if selected_layer_input !='' and overlayNode.get('index') != selected_layer_input:
                    continue
                positionNode = overlayNode.find('position')
                width_is_negative = False
                height_is_negative = False
                layout_is_90 = False
                if positionNode is not None:
                    
                    panX = float(positionNode.attrib['panX']) if 'panX' in positionNode.attrib else 0.0
                    panY = float(positionNode.attrib['panY']) if 'panY' in positionNode.attrib else 0.0
                    zoomX = float(positionNode.attrib['zoomX']) if 'zoomX' in positionNode.attrib else 1.0
                    zoomY = float(positionNode.attrib['zoomY']) if 'zoomY' in positionNode.attrib else 1.0
                    width = float(positionNode.attrib['width']) if 'width' in positionNode.attrib else 1.0
                    height = float(positionNode.attrib['height']) if 'height' in positionNode.attrib else 1.0
                    
                    if (width<0 and height>0) or (width>0 and height<0):
                        layout_is_90 = True
                    if not layout_is_90:
                        layout_x = int(((panX+1.0)*(window_w/2)) - ((zoomX*window_w)/2))
                        layout_y = int((window_h) - (((panY+1.0)*(window_h/2)) - ((zoomY*window_h)/2)) - (zoomY*window_h))
                        layout_w = int((zoomX*window_w) - ((layout_x*-1) if layout_x<0 else 0))
                        layout_h = int((zoomY*window_h) - ((layout_y*-1) if layout_y<0 else 0))
                    else:
                        resolustion = self.get_vmix_resolution(xmlDoc.find('version').text)
                        vmix_res_w=resolustion['width']
                        vmix_res_h=resolustion['height']
                        
                        layout_w = int(window_w / (vmix_res_w / ((vmix_res_h / (vmix_res_w/vmix_res_h))*zoomY)))
                        layout_h = int(zoomX*window_h)
                        layout_y = int((window_h) - (((panY+1.0)*(window_h/2)) - ((zoomX*window_h)/2)) - (zoomX*window_h))
                        layout_x = int(((panX+1.0)*(window_w/2)) - (layout_w/2))
                        
                        layout_w = layout_w - ((layout_x*-1) if layout_x<0 else 0)
                        layout_h = layout_h - ((layout_y*-1) if layout_y<0 else 0)

                    if layout_x<0:layout_x=0
                    if layout_y<0:layout_y=0
                    if (layout_x+layout_w)>window_w:
                        layout_w = window_w - layout_x
                    if (layout_y+layout_h)>window_h:
                        layout_h = window_h - layout_y
                    if (selected_layer_input !='') or ((mouse_x > layout_x and mouse_x < (layout_x+layout_w)) and (mouse_y > layout_y and mouse_y < (layout_y+layout_h))):
                        topmost_layer['number'] = overlayNode.get('index')
                        topmost_layer['x'],topmost_layer['y'],topmost_layer['w'],topmost_layer['h'] = [int(layout_x),int(layout_y),int(layout_w),int(layout_h)]
                        continue
                else:
                    topmost_layer['number'] = overlayNode.get('index')
                    topmost_layer['x'],topmost_layer['y'],topmost_layer['w'],topmost_layer['h'] = [0,0,int(window_w),int(window_h)]
            if selected_layer_input!='' and topmost_layer['number']!=selected_layer_input:
                return None
            else:
                return topmost_layer

def show_settings_window_tray():
    global tk_settings_window
    tk_settings_window = settings_window(root)

def show_fullscreen_window_tray():
    global tk_fullscreen_window
    tk_fullscreen_window = fullscreen_window(root)
    
def show_pdf2png_window_tray():
    global tk_pdf2png_window
    tk_pdf2png_window = pdf2png_window(root)
    
def open_web(item):
    import webbrowser
    if item=='vdd':
        response = messagebox.askyesno(t('Confirmation'), t('Are you sure you want to install Virtual Display Driver ?'))
        if response:
            commands = '''-NoProfile -ExecutionPolicy Bypass -Command "
            winget install -e --id VirtualDrivers.Virtual-Display-Driver --scope machine --accept-source-agreements --accept-package-agreements --force;
            if ($LASTEXITCODE -eq 0) {
                $env:Path = [System.Environment]::ExpandEnvironmentVariables([System.Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [System.Environment]::GetEnvironmentVariable('Path','User'))
                $wsh = New-Object -ComObject WScript.Shell;
                $s = $wsh.CreateShortcut($env:USERPROFILE + '\\Desktop\\VDD Control.lnk');
                $s.TargetPath = (Get-Item (Get-Command 'VDD Control.exe' -ErrorAction SilentlyContinue).Source).Target[0];
                $s.Save();
                $installPath = $env:TEMP + '\\silent-install.ps1';
                Invoke-WebRequest -Uri https://raw.githubusercontent.com/VirtualDrivers/Virtual-Display-Driver/master/Community%20Scripts/silent-install.ps1 -OutFile $installPath;
                & $installPath;
                exit 0;
            }
            pause;
			exit 1;
            "'''
            shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters=commands, nShow=win32con.SW_SHOWNORMAL)
    if item=='vad':
        webbrowser.open('https://vb-audio.com/Cable/index.htm', new=1)
        CustomMessageBox(root,wait=False,title=t('Info'),message=t('Download and extract and run VBCABLE_Driver_Pack*.zip.'))
    if item=='ffmpeg':
        response = messagebox.askyesno(t('Confirmation'), t('Are you sure you want to install ffmpeg ?'))
        if response:
            commands = '-NoProfile -ExecutionPolicy Bypass -Command "winget install -e --id Gyan.FFmpeg --scope machine --accept-source-agreements --accept-package-agreements --force"'
            shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters=commands, nShow=win32con.SW_SHOWNORMAL)
    if item=='klcp':
        response = messagebox.askyesno(t('Confirmation'), t('Are you sure you want to install K-Lite Codec Pack (Mega) ?'))
        if response:
            commands = '-NoProfile -ExecutionPolicy Bypass -Command "winget install -e --id CodecGuide.K-LiteCodecPack.Mega --scope machine --accept-source-agreements --accept-package-agreements --force"'
            shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters=commands, nShow=win32con.SW_SHOWNORMAL)
    if item=='mfc':
        response = messagebox.askyesno(t('Confirmation'), t('Are you sure you want to install Media Foundation Codecs ?'))
        if response:
            commands = '''-NoProfile -ExecutionPolicy Bypass -Command "
            $zipPath = $env:TEMP + '\\mf.zip';
            $extrPath = $env:TEMP + '\\mf_Codecs';
            curl.exe -L https://raw.githubusercontent.com/aymanqama/vmix-helper/refs/heads/main/mf/mf.bin -o $zipPath;
            if ($LASTEXITCODE -eq 0) {
                Install-Module -Name 7Zip4Powershell
                Expand-7Zip -ArchiveFileName $zipPath -TargetPath $env:TEMP -Password abcdefghijklmnopqrstuvwxyz
                Get-ChildItem -Path $extrPath -Filter '*.Appx*' | ForEach-Object {
                    try {
                        Write-Host 'Trying to install' $_.FullName -ForegroundColor Green;
                        Add-AppxPackage -Path $_.FullName -ErrorAction Stop;
                        Write-Host 'installed successfully' -ForegroundColor Green;
                    } catch {
                        Write-Host 'Failed to install' -ForegroundColor Red;
                        Write-Host $_.Exception.Message -ForegroundColor Red;
                    }
                }
                exit 0;
            }
            pause;
			exit 1;
            "'''
            shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters=commands, nShow=win32con.SW_SHOWNORMAL)
    if item=='gst':
        response = messagebox.askyesno(t('Confirmation'), t('Are you sure you want to install Gstreamer ?'))
        if response:
            commands = '''-NoProfile -ExecutionPolicy Bypass -Command "
            winget install -e --id gstreamerproject.gstreamer --location 'C:\\gstreamer' --scope machine --accept-source-agreements --accept-package-agreements --force;
            if ($LASTEXITCODE -eq 0) {
                $var = $env:Path.TrimEnd(';') + ';C:\\gstreamer\\bin';
                setx /m PATH $var;
            }
            "'''
            shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters=commands, nShow=win32con.SW_SHOWNORMAL)
    if item=='vlc':
        response = messagebox.askyesno(t('Confirmation'), t('Are you sure you want to install VLC media player ?'))
        if response:
            commands = '-NoProfile -ExecutionPolicy Bypass -Command "winget install -e --id VideoLAN.VLC --scope machine --accept-source-agreements --accept-package-agreements --force"'
            shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters=commands, nShow=win32con.SW_SHOWNORMAL)
    if item=='mmtx':
        response = messagebox.askyesno(t('Confirmation'), t('Are you sure you want to install mediamtx ?'))
        if response:
            commands = '-NoProfile -ExecutionPolicy Bypass -Command "winget install -e --id bluenviron.mediamtx --scope machine --accept-source-agreements --accept-package-agreements --force"'
            shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters=commands, nShow=win32con.SW_SHOWNORMAL)
    if item=='wndh':
        response = messagebox.askyesno(t('Confirmation'), t('Are you sure you want to install Windhawk ?'))
        if response:
            commands = '-NoProfile -ExecutionPolicy Bypass -Command "winget install -e --id RamenSoftware.Windhawk --scope machine --accept-source-agreements --accept-package-agreements --force"'
            shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters=commands, nShow=win32con.SW_SHOWNORMAL)
    if item=='vmix-helper':
        webbrowser.open('https://github.com/aymanqama/vmix-helper', new=1)

def check_startup():
    global enable_startup
    enable_startup = os.path.exists(os.path.join(os.environ['APPDATA'], 
                               'Microsoft', 'Windows', 'Start Menu', 
                               'Programs', 'Startup','vmix-helper.lnk'))
    
def enable_startup_shortcut():
    global enable_startup
    enable_startup = not enable_startup
    if enable_startup:
        create_startup_shortcut()
    else:
        delete_startup_shortcut()

def create_startup_shortcut():
    ps_script = f'''
    $targetFile = "vmix-helper.exe"
    $shortcutName = "vmix-helper.lnk"
    $startupFolder = [System.Environment]::GetFolderPath("Startup")
    $WScriptShell = New-Object -ComObject WScript.Shell
    $shortcut = $WScriptShell.CreateShortcut("$startupFolder\\$shortcutName")
    $shortcut.TargetPath = $targetFile
    $shortcut.Save()
    Write-Output "Shortcut created at $startupFolder\\$shortcutName"
    '''
    process = subprocess.Popen(['powershell', '-Command', ps_script],creationflags=subprocess.CREATE_NO_WINDOW)

def delete_startup_shortcut():
    ps_script = f'''
    $shortcutName = "vmix-helper.lnk"
    $startupFolder = [System.Environment]::GetFolderPath("Startup")
    Remove-Item -Path "$startupFolder\\$shortcutName"
    '''
    process = subprocess.Popen(['powershell', '-Command', ps_script],creationflags=subprocess.CREATE_NO_WINDOW)

def save_settings_tofile():
    global menu_settings
    global virtual_audio_device_id
    try:
        with open(os.path.expanduser('~\\vmix-helper.set'), 'wb') as f:
            pickle.dump({'menu_settings':menu_settings,'virtual_audio_device_id':virtual_audio_device_id}, f)
    except:
        pass
        
def load_settings_fromfile():
    global menu_settings
    global virtual_audio_device_id
    try:
        with open(os.path.expanduser('~\\vmix-helper.set'), 'rb') as f:
            tmp_settings = pickle.load(f)
        menu_settings = copy.deepcopy(tmp_settings['menu_settings'])
        virtual_audio_device_id = tmp_settings['virtual_audio_device_id']
    except:
        pass
        
def get_virtual_audio_device_id():
    global virtual_audio_device_id
    device_name = 'CABLE Output (VB-Audio Virtual Cable)'
    try:
        import winreg
        os.environ['PATH']=os.path.expandvars(winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'System\CurrentControlSet\Control\Session Manager\Environment', 0, winreg.KEY_READ), 'Path')[0])
        process = subprocess.Popen(['gst-device-monitor-1.0.exe', 'Audio/Source'], 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        stdout, stderr = process.communicate()
    except:
        return
    device_start=0
    device_end=0
    while True:
        device_start = stdout.find(f'name  : {device_name}',device_end)
        if device_start == -1:
            virtual_audio_device_id = ''
            save_settings_tofile()
            return
        device_end = stdout.find('...',device_start)
        if device_end == -1:
            virtual_audio_device_id = ''
            save_settings_tofile()
            return
        strid_start = stdout.find('device.strid = ',device_start,device_end)
        if strid_start ==-1:continue
        strid_start = strid_start + len('device.strid = ')
        strid_end = stdout.find('\n', strid_start)
        virtual_audio_device_id = f'wasapisrc device={stdout[strid_start:strid_end].strip()}'
        save_settings_tofile()
        return
    virtual_audio_device_id = ''
    save_settings_tofile()

def monitor_ffmpeg_processes():
    global root
    global ffmpeg_processes
    global tk_settings_window
    global settings_window_is_up
    global ffmpeg_processes_closing_is_running
    while True:
        try:
            if tk_settings_window is not None and settings_window_is_up:
                try:tk_settings_window.controls_list['ffmpeg_number_processes']['text'] = f'{t("Number of running processes")} : {str(len(ffmpeg_processes))}'
                except:settings_window_is_up = False
            if not ffmpeg_processes or ffmpeg_processes_closing_is_running:
                time.sleep(2)
                continue
            time.sleep(0.5)
            if not ffmpeg_processes or ffmpeg_processes_closing_is_running:
                continue
            for i in range(len(ffmpeg_processes)):
                if int(time.time()) - ffmpeg_processes[i]['time_add']<3:time.sleep(3-(int(time.time()) - ffmpeg_processes[i]['time_add']))
                process_is_up = False
                parent_is_up = False
                for n in range(2):
                    try:
                        parent = psutil.Process(ffmpeg_processes[i]['process'].pid)
                        parent_is_up = True
                        break
                    except:
                        continue
                if parent_is_up:
                    children = parent.children(recursive=True)
                    all_procs = children + [parent]
                    for n in range(2):
                        for proc in all_procs:
                            if [line for line in ffmpeg_processes[i]['ffmpeg_command_line'].split('\n') if 'Command : ' in line][0].split('Command : ')[1].split()[0] in proc.name():
                                process_is_up = True
                                break
                if not process_is_up:
                    if tk_settings_window is not None and settings_window_is_up:
                        try:tk_settings_window.controls_list['ffmpeg_number_processes']['text'] = f'{t("Number of running processes")} : {str(len(ffmpeg_processes)-1)}'
                        except:settings_window_is_up = False
                    CustomMessageBox(root,msg_type='error',title=t('Failed'),message=f'{ffmpeg_processes[i]["ffmpeg_command_line"]}\r\n\r\n {t("Stopped running.")}')
                    del ffmpeg_processes[i]
                    continue
        except:
            continue
def get_all_screens_basic():
    all_monitors = []
    
    try:
        monitor_handles = win32api.EnumDisplayMonitors()
        
        for i, (hMonitor, hdcMonitor, rect) in enumerate(monitor_handles):
            info = win32api.GetMonitorInfo(hMonitor)
            monitor_rect = info['Monitor']
                
            width = monitor_rect[2] - monitor_rect[0]
            height = monitor_rect[3] - monitor_rect[1]
            
            all_monitors.append(f'{monitor_rect[0]}x{monitor_rect[1]}x{width}x{height}')
    except:
        pass
    
    return all_monitors
    
def get_all_screens_connected():
    
    def get_monitor_name_string(device_name):
        i = 0
        while True:
            try:
                display_device = win32api.EnumDisplayDevices(None, i, 0)
                if display_device.DeviceName == device_name:
                    return display_device.DeviceString
                i += 1
            except:
                break
        return ''
        
    def get_monitor_friendly_name(adapter_id, target_id):
        device_name = DISPLAYCONFIG_TARGET_DEVICE_NAME()
        device_name.header.size = ctypes.sizeof(DISPLAYCONFIG_TARGET_DEVICE_NAME)
        device_name.header.type = 2
        device_name.header.adapterId = adapter_id
        device_name.header.id = target_id
        
        error = ctypes.windll.user32.DisplayConfigGetDeviceInfo(ctypes.byref(device_name))
        if error != 0:
            return f"Unknown (Error: {error})"
        return device_name.monitorFriendlyDeviceName
        
    def gpu_info(x,y):
        try:
            info = win32api.GetMonitorInfo(win32api.MonitorFromPoint((x+1, y+1), 2))
            return info['Flags'] & win32con.MONITORINFOF_PRIMARY,get_monitor_name_string(info['Device'])
        except:
            return 0,''
            
    path_count = wintypes.UINT()
    mode_count = wintypes.UINT()
    
    error = ctypes.windll.user32.GetDisplayConfigBufferSizes(
        0x00000002, 
        ctypes.byref(path_count), 
        ctypes.byref(mode_count)
    )
    if error != 0:
        raise ctypes.WinError(error)

    paths = (DISPLAYCONFIG_PATH_INFO * path_count.value)()
    modes = (DISPLAYCONFIG_MODE_INFO * mode_count.value)()

    error = ctypes.windll.user32.QueryDisplayConfig(
        0x00000002,
        ctypes.byref(path_count),
        paths,
        ctypes.byref(mode_count),
        modes,
        None
    )
    if error != 0:
        raise ctypes.WinError(error)

    all_scr = []
    friendly_name = ''
    for i in range(mode_count.value):
        if modes[i].infoType == 2:
            friendly_name = get_monitor_friendly_name(modes[i].adapterId, modes[i].id)
        else:
            name = f'{modes[i].modeInfo.sourceMode.position.x}x{modes[i].modeInfo.sourceMode.position.y}x{modes[i].modeInfo.sourceMode.width}x{modes[i].modeInfo.sourceMode.height}'
            is_primary,gpu_name = gpu_info(modes[i].modeInfo.sourceMode.position.x,modes[i].modeInfo.sourceMode.position.y)
            all_scr.append({
                'name': name,
                'name_string': gpu_name,
                'width': modes[i].modeInfo.sourceMode.width,
                'height': modes[i].modeInfo.sourceMode.height,
                'x': modes[i].modeInfo.sourceMode.position.x,
                'y': modes[i].modeInfo.sourceMode.position.y,
                'is_primary': is_primary,
                'monitor_name':friendly_name
            })
    return all_scr
    
def update_python_modules():
    import sys
    mods = ['psutil','pystray','keyboard','requests','yt-dlp','mouse','pymupdf','pywin32']
    for mod in mods:
        process = subprocess.Popen(f'cmd.exe /c "echo {t("vMix Helper installing required python module")} {mod} && pip install --upgrade {mod}"',creationflags=subprocess.CREATE_NEW_CONSOLE)
        process.wait()
    subprocess.Popen([sys.executable, __file__])
    os._exit(0)
        
def close_all_full_screens():
    global fullscreen_ffplay
    for monitor in list(fullscreen_ffplay.keys()):
        try:
            os.kill(fullscreen_ffplay[monitor]['process'].pid,signal.SIGINT)
        except:
            pass
        del fullscreen_ffplay[monitor]
    windows = get_windows_by_process('ffplay.exe')
    if len(windows)>0:
        for window in windows:
            try:
                os.kill(window['pid'],signal.SIGINT)
            except:continue

def on_systray_click_editscript():
    subprocess.Popen(["notepad.exe", __file__])

def build_menu():
    global icon
    global version
    global systray
    try:
        systray.stop()
        systray = None
    except:
        pass
    systray = pystray.Icon(
        f'vMix Helper {version}',
        icon,
        f'vMix Helper {version}',
        menu=pystray.Menu(
            pystray.MenuItem(t('About'), on_systray_click_about),
            pystray.MenuItem(t('Edit the script code'), on_systray_click_editscript),
            pystray.MenuItem(t('Update python required modules'), update_python_modules),
            pystray.MenuItem(t('Run on startup'),enable_startup_shortcut,checked=lambda item: enable_startup),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(t('FFmpeg/Gstreamer (Test)'), show_settings_window_tray),
            pystray.MenuItem(t('Convert PDF to Pictures'), show_pdf2png_window_tray),
            pystray.MenuItem(t('HTTP file server to receive files'), run_server),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(t('Tools to install'), pystray.Menu(
                pystray.MenuItem(t('Virtual Display Driver'), lambda: open_web('vdd')),
                pystray.MenuItem(t('VB-CABLE Virtual Audio Device'), lambda: open_web('vad')),
                pystray.MenuItem(t('FFmpeg'), lambda: open_web('ffmpeg')),
                pystray.MenuItem(t('K-Lite Codec Pack'), lambda: open_web('klcp')),
                pystray.MenuItem(t('Gstreamer'), lambda: open_web('gst')),
                pystray.MenuItem(t('VLC'), lambda: open_web('vlc')),
                pystray.MenuItem(t('MediaMTX'), lambda: open_web('mmtx')),
                pystray.MenuItem(t('Windhawk'), lambda: open_web('wndh')),
                pystray.MenuItem(t('Media Foundation Codecs For Windows 10 and 11'), lambda: open_web('mfc'))
            )),
            pystray.MenuItem(t('Fullscreen'), pystray.Menu(
                pystray.MenuItem(t('Fullscreen'),show_fullscreen_window_tray),
                pystray.MenuItem(t('Close all full screens'),close_all_full_screens)
            )),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(t('Patch vMix settings'), on_systray_click_patch_settings),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(t('Video downloader (YouTube/TikTok/etc)'), start_yt_dlp),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(t('Enable Virtual Display'), on_systray_click_enable_vdd,checked=lambda item: enable_vdd),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(t('Stop Powerpoint/Photos input from autoplay'), on_systray_click_disable_powerpoint_play,checked=lambda item: menu_settings['enable_auto_powerpoint_pause']),
            pystray.MenuItem(t('Enable change layers input shortcuts'), on_systray_click_enable_layers,checked=lambda item: menu_settings['enable_change_layers_input_shortcuts']),
            pystray.MenuItem(t('Enable layers selection by mouse'), on_systray_click_enable_framing_layers,checked=lambda item: menu_settings['enable_framing_layout_on_click_output_window']),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(t('Exit'), on_systray_click_exit)
        )
    )
    systray.run_detached()
        
def run_server():
    threading.Thread(target=run_server_thread_1, args=()).start()
    
def run_server_thread_1():
    import http.server
    import socketserver
    import urllib.parse
    class MultiFileUploadHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            pass
        def do_GET(self):
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                html = f'''
                <!DOCTYPE html>
                <html>
                <head>
                    <title>{t("Upload")}</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=2.0">
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 40px; }}
                        .success {{ color: green; }}
                        .error {{ color: red; }}
                        .file-list {{ margin: 10px 0; padding: 10px; border: 1px solid #ddd; }}
                    </style>
                </head>
                <body>
                    <h2>{t("Upload")}</h2>
                    
                    <form method="post" enctype="multipart/form-data" id="uploadForm">
                        <input type="file" name="files" title={t("Choose Files")} multiple required>
                        <br><br>
                        <input type="submit" value={t("Upload Files")}>
                        <button type="button" onclick="addMoreFiles()">{t("Add More Files")}</button>
                    </form>
                    
                    <script>
                        function addMoreFiles() {{
                            const input = document.createElement('input');
                            input.type = 'file';
                            input.name = 'files';
                            input.multiple = true;
                            input.style.marginTop = '10px';
                            document.getElementById('uploadForm').insertBefore(input, document.querySelector('br'));
                        }}
                    </script>
                </body>
                </html>
                '''
                html = f'''
                <!DOCTYPE html>
                <html>
                <head>
                    <title>{t("Upload")}</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=2.0">
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 40px; }}
                        .success {{ color: green; }}
                        .error {{ color: red; }}
                        .file-list {{ margin: 10px 0; padding: 10px; border: 1px solid #ddd; }}
                    </style>
                </head>
                <body>
                    <h2>{t("Upload")}</h2>
                    
                    <form method="post" enctype="multipart/form-data" id="uploadForm">
                        <button type="button" onclick="document.getElementById('filesid').click()" style="font-size: 24px;">{t("Choose Files")}</button>
                        <input type="file" name="files" style="display:none;" id="filesid" multiple required>
                        <div id="files_name"><br><label>{t("No Chosen Files")}</label></br></div>
                        <br></br>
                        <input type="submit" value={t("Upload Files")} style="font-size: 24px;">
                    </form>
                    
                    <script>
                        document.getElementById('filesid').addEventListener('change', function(e) {{
                            const files_name = document.getElementById('files_name');
                            if (this.files.length === 0) {{
                                files_name.innerHTML = '<br><label>{t("No Chosen Files")}</label></br>';
                            }} else {{
                                res=''
                                for (i=0;i<this.files.length;i++){{
                                    res = res + this.files[i].name + '<br>'
                                }}
                                files_name.innerHTML = res;
                            }}
                        }});
                    </script>
                </body>
                </html>
                '''
                self.wfile.write(html.encode())
            else:
                super().do_GET()
                
        def do_POST(self):
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            
            if self.path == '/':
                content_type = self.headers.get('Content-Type')
                if not content_type or 'boundary=' not in content_type:
                    self.send_error(400, t('Content-Type must be multipart/form-data'))
                    return
                
                boundary = content_type.split("boundary=")[1].strip().encode()
                boundary_sep = b'--' + boundary 
                
                success_messages = []
                error_messages = []

                try:
                    line = self.rfile.readline()
                    if boundary_sep not in line:
                        self.send_error(400, t("Content doesn't begin with boundary"))
                        return

                    while True:
                        part_headers = {}
                        while True:
                            line = self.rfile.readline()
                            if not line.strip(): break
                            
                            if line.lower().startswith(b'content-disposition'):
                                match = re.search(r'filename="([^"]+)"', line.decode('utf-8', errors='ignore'))
                                if match:
                                    part_headers['filename'] = match.group(1)

                        filename = part_headers.get('filename')
                        
                        if filename:
                            filename = os.path.basename(filename)
                            file_path = os.path.join(desktop_path, filename)
                            
                            counter = 1
                            name, ext = os.path.splitext(filename)
                            while os.path.exists(file_path):
                                filename = f"{name}_{counter}{ext}"
                                file_path = os.path.join(desktop_path, filename)
                                counter += 1

                            try:
                                with open(file_path, 'wb') as f:
                                    pre_line = self.rfile.readline()
                                    while True:
                                        line = self.rfile.readline()
                                        if boundary_sep in line:
                                            f.write(pre_line.rstrip(b'\r\n'))
                                            break
                                        else:
                                            f.write(pre_line)
                                            pre_line = line
                                success_messages.append(filename)
                            except Exception as e:
                                error_messages.append(f"{filename}: {e}")
                        if line.strip() == boundary_sep + b'--':
                            break
                            
                except Exception as e:
                    self.send_error(500, f'{t("Streaming Error:")} {e}')
                    return
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                html = f'''
                <!DOCTYPE html>
                <html>
                <head>
                <title>{t("Upload Results")}</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=2.0">
                </head>
                <body>
                    <h2>{t("Upload Results")}</h2>
                    <div class="file-list">
                        <h3>Successful Uploads:</h3>
                        {''.join(f'<p class="success">{msg}</p>' for msg in success_messages) if success_messages else ''}
                        
                        <h3>{t("Faild Uploads:")}</h3>
                        {''.join(f'<p class="error">{msg}</p>' for msg in error_messages) if error_messages else f'<p>{t("No Errors")}</p>'}
                    </div>
                    <br>
                    <a href="/">{t("Upload More Files")}</a>
                </body>
                </html>
                '''
                self.wfile.write(html.encode())
            else:
                self.send_error(404, t('Not found'))
                
    try:
        with socketserver.TCPServer(('', http_file_server_port), MultiFileUploadHandler) as httpd:
            threading.Thread(target=run_server_thread_2, args=(httpd,)).start()
            httpd.serve_forever()
    except Exception as e:
        CustomMessageBox(root,msg_type='error',title=t('Error'),message=f'{t("Fatal error")}:\n{e}\n{t("Server may already running.")}')

def run_server_thread_2(server):
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
    except:
        CustomMessageBox(root, msg_type='error', title=t('Error'),message=t('Failed to get local ip address.\nMake sure you are connected to a network.'))
        server.shutdown()
        return
    CustomMessageBox(root, title=t('Info'), message=f'{t("Server is running on")} http://{local_ip}\n{t("All uploaded files will be saved to desktop folder.")}\n{t("Click OK to close the server.")}')
    server.shutdown()

def monitor_monitors_changes():
    global old_all_monitors
    global fullscreen_ffplay
    last_screens = []
    current_screens = []
    windows = []
    while True:
        try:
            time.sleep(2)
            windows = get_windows_by_process(vmix_process_name)
            if len(windows)==0:
                if len(fullscreen_ffplay)>0:
                    for monitors_key in list(fullscreen_ffplay.keys()):
                        try:
                            os.kill(fullscreen_ffplay[monitors_key]['process'].pid,signal.SIGINT)
                            del fullscreen_ffplay[monitors_key]
                        except:
                            pass
            current_screens = get_all_screens_basic()
            if last_screens != current_screens:
                last_screens = current_screens
                all_monitors = get_all_screens_connected()
                if all_monitors != old_all_monitors:
                    old_all_monitors = copy.deepcopy(all_monitors)
            if len(fullscreen_ffplay)>0:
                print(fullscreen_ffplay)
                for monitors_key in list(fullscreen_ffplay.keys()):
                    if not any(d.get('name') == monitors_key for d in old_all_monitors):
                        if int(time.time()) - fullscreen_ffplay[monitors_key]['last_seen'] > 20:
                            try:
                                os.kill(fullscreen_ffplay[monitors_key]['process'].pid,signal.SIGINT)
                            except:
                                pass
                            del fullscreen_ffplay[monitors_key]
                            continue
                    else:
                        fullscreen_ffplay[monitors_key]['last_seen']=int(time.time())
                    if psutil.pid_exists(fullscreen_ffplay[monitors_key]['process'].pid):
                        process = psutil.Process(fullscreen_ffplay[monitors_key]['process'].pid)
                        if 'ffplay' not in process.name().lower():
                            del fullscreen_ffplay[monitors_key]
                    else:
                        del fullscreen_ffplay[monitors_key]
        except:
            pass

for key, value in options.items():
    if 'keys' not in value: continue
    for key2, value2 in value['keys'].items():
        if key2 in keys_add_to_hotkey: continue
        keyboard.add_hotkey(key2, on_key_press, args=(key2,), suppress=True)
        keys_add_to_hotkey.append(key2)
        
for registered_modifier in registered_modifiers:
    if registered_modifier in keys_add_to_hotkey: continue
    keyboard.add_hotkey(registered_modifier, on_key_modifier_press, args=(registered_modifier,), suppress=False)
    modifiers_add_to_hotkey.append(registered_modifier)

def main():
    global root
    global menu_settings
    global old_all_monitors
    global thread_monitor_ffmpeg_processes
    global thread_monitor_screens
    global virtual_audio_device_id
    load_settings_fromfile()
    check_startup()
    root = tk.Tk()
    root.withdraw()
    old_all_monitors = get_all_screens_connected()
    build_menu()
    if menu_settings['enable_auto_powerpoint_pause']:
        menu_settings['enable_auto_powerpoint_pause']=False
        on_systray_click_disable_powerpoint_play()
    if menu_settings['enable_change_layers_input_shortcuts']:
        menu_settings['enable_change_layers_input_shortcuts']=False
        on_systray_click_enable_layers()
    if menu_settings['enable_framing_layout_on_click_output_window']:
        menu_settings['enable_framing_layout_on_click_output_window']=False
        on_systray_click_enable_framing_layers()

    thread_monitor_ffmpeg_processes = threading.Thread(target=monitor_ffmpeg_processes, args=())
    thread_monitor_ffmpeg_processes.start()

    thread_monitor_screens = threading.Thread(target=monitor_monitors_changes, args=())
    thread_monitor_screens.start()
    
    if virtual_audio_device_id == 'PLEASE_INSTALL_GSTREAMER' or virtual_audio_device_id == '':
        threading.Thread(target=get_virtual_audio_device_id).start()
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        close_all_full_screens()
        close_ffmpeg_thread(False)
        os._exit(0)
        
if __name__ == '__main__':
    main()