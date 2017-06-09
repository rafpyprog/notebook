import os

'''
Desktop Entry specification (DES):
https://standards.freedesktop.org/desktop-entry-spec/latest/

Both the KDE and GNOME desktop environments have adopted a similar format for
"desktop entries", or configuration files describing how a particular program
is to be launched.

$XDG_DATA_HOME defines the base directory relative  to  which  user  specific
data files should be stored. If $XDG_DATA_HOME is either not set or  empty, a
default equal to $HOME/.local/share should be used. '''

XDG_DATA_HOME = os.getenv('XDG_DATA_HOME', None)

if XDG_DATA_HOME in [None, ""]:
    HOME = os.getenv('HOME')
    XDG_DATA_HOME = os.path.join(HOME, '.local', 'share')

''' According to the Desktop File specifications .desktop files are Searched
for in "XDG_DATA_DIRS/file-manager/actions" directories. Check if the path
exists on XGD_DATA_HOME. '''

ACTIONS_FOLDER = os.path.join(XDG_DATA_HOME, 'file-manager', 'actions')
if os.path.exists(ACTIONS_FOLDER) and os.access(ACTIONS_FOLDER, os.W_OK):
    #CHECK WRITE ACESS
    has_write_permission = os.access(ACTIONS_FOLDER, os.W_OK)
    if has_write_permission:
        # CREATE THE .DESKTOP FILE
    else:
        # go for DATA DIRS
else:
    '''If, when attempting to write  a  file, the  destination  directory  is
    non-existant an attempt should be made to create it with permission 0700.
    If the destination directory exists  already the permissions  should  not
    be changed. '''
    try:
        os.makedirs(ACTIONS_FOLDER, mode=0o700)
    except PermissionError:
        'try the datadirs'








''' Desktop entry files should have the .desktop extension '''
desktop_file = 'open-with-jupyter.desktop'  # Desktop entry files are encoded in UTF-8

'''
Such file should be installed to $datadir/subdir/filename with $datadir
defaulting to /usr/share. '''
datadir = '/usr/share/file-manager/actions'


'''If, when attempting to write a file, the destination directory is
non-existant an attempt should be made to create it with permission 0700.
If the destination directory exists already the permissions should not
be changed.
'''
if os.path.exists(datadir) is False:
    try:
        os.makedirs(datadir, mode=0o700)
    except PermissionError:
        ''' According to the Desktop File specifications .desktop files are
        searched  for  in "XDG_DATA_DIRS/file-manager/actions" directories,
        as defined in freedesktop.org XDG specifications. Try using the
        XDG DATA DIRS'''
        data_dirs_environ_name = 'XDG_DATA_DIRS'
        if data_dirs_environ_name in os.environ:
            xdg_data_dirs = os.environ['XDG_DATA_DIRS'].split(':')
            for data_dir in xdg_data_dirs:
                x = os.path.exists(data_dir)
                print(x)
        else:
            # we cant create shortcuts
            pass






desktop_entry = {
    '[Desktop Entry]': {
        'Type': 'Action',
        'TargetLocation': 'true',
        'Name': 'Open with Jupyter',
        'Name[pt]': 'Abrir no Jupyter',
        'Name[es]': 'Abrin en Jupyter',
        'Profiles': 'open-jupyter'
        }
    }

command_line = '''gnome-terminal --working-directory %%f -e "jupyter notebook"'''

action = {
    '[X-Action-Profile open-jupyter]': {
        'Name': 'open-jupyter'
        'Exec': command_line
        }
    }


'''

base_dir = 'XDG_DATA_DIRS'
