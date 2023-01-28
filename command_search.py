import sys
from pprint import pprint
import os



########################
#       Color
########################

#[  foreground  ]
endc="\033[0m"
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
lgray="\033[0;37m"
dgray="\033[1;30m"
lred="\033[1;31m"
lgreen="\033[1;32m"
brown="\033[1;33m"
lblue="\033[1;34m"
lpurple="\033[1;35m"
lcyan="\033[1;36m"
white="\033[1;37m"
#[  background  ]
bg_black="\033[0;40m"
bg_blue="\033[0;44m"
bg_cyan="\033[0;46m"
bg_purple="\033[0;45m"
bg_brown="\033[0;43m"
bg_lgray="\033[0;47m"
bg_dgray="\033[1;40m"
bg_lblue="\033[1;44m"
bg_lgreen="\033[1;42m"
bg_lcyan="\033[1;46m"
bg_lpurple="\033[1;45m"
bg_yellow="\033[1;43m"
bg_white="\033[1;47m"
#[  font    ]
bold="\033[1m"
dim="\033[2m"
italic="\033[3m"
underline="\033[4m"
blink="\033[5m"

###################################################
#       Classes
###################################################

class Directory:
    current = os.getcwd()

class File:
    read = 'r'
    write = 'w'
    append = 'a'
    create = 'x'
    
class Files:
    command_names = f'{Directory.current}\\names.txt'
    command_descriptions = f'{Directory.current}\\descs.txt'

###########################
#       data
###########################

commands_by_first_letter = {
    '!': ['!!'],
    '#': ['###'],
    '.': ['.'],
    'a': ['alias', 'apropos', 'apt-get', 'aptitude', 'aspell', 'awk'],
    'b': ['basename', 'bash', 'bc', 'bg', 'break', 'builtin', 'bzip2'],
    'c': ['cal','case','cat','cd','cfdisk','chgrp','chkconfig','chmod','chown','chroot','cksum','clear','cmp','comm','command','continue','cp','cron','crontab','csplit','curl','cut'],
    'd': ['date','dc','dd','ddrescue','declare','df','diff','diff3','dig','dir','dircolors','dirname','dirs','dmesg','du'],
    'e': ['echo','egrep','eject','enable','env','ethtool','eval','exec','exit','expand','expect','export','expr'],
    'f': ['false','fdformat','fdisk','fg','fgrep','file','filesyes','find','fmt','fold','for','format','free','fsck','ftp','function','fuser'],
    'g': ['gawk','getopts','grep','groupadd','groupdel','groupmod','groups','gzip'],
    'h': ['hash', 'head', 'help', 'history', 'hostname', 'htop'],
    'i': ['iconv','id','if','ifconfig','ifdown','ifup','import','install','ip'],
    'j': ['jobs', 'join'],
    'k': ['kill', 'killall'],
    'l': ['less','let','link','ln','local','locate','logname','logout','look','lpc','lpr','lprint','lprintd','lprintq','lprm','ls','lsof'],
    'm': ['make','man','mkdir','mkfifo','mkisofs','mknod','mmv','more','most','mount','mtools','mtr','mv'],
    'n': ['nc', 'netstat', 'nice', 'nl', 'nohup', 'notify', 'nslookup'],
    'o': ['op', 'open'],
    'p': ['passwd','paste','pathchk','ping','pkill','popd','pr','printcap','printenv','printf','ps','pushd','pv'],
    'q': ['quota'],
    'r': ['ram','rar','rcp','read','readarray','readonly','reboot','rename','renice','return','rev','rm','rmdir'],
    's': ['scp','screen','sdiff','sed','select','seq','set','sftp','shift','shopt','shutdown','sleep','slocate','sort','source','split','ssh','stat','strace','su','sudo','sum','suspend'],
    't': ['tail','tar','tee','test','time','timeout','times','top','touch','tput','tr','traceroute','trap','true','tsort','tty'],
    'u': ['ulimit','umask','umount','unalias','uname','unexpand','uniq','units','unrar','unset','unshar','until','uptime','useradd','userdel','usermod','users','uuencode'],
    'v': ['v', 'vdir', 'vi'],
    'w': ['wait','watch','wc','wget','whereis','which','while','who','whoami'],
    'x': ['xargs', 'xdg', 'xz'],
    'z': ['zip']
    }
command_names_list = ['!!', '###', '.', 'alias', 'apropos', 'apt-get', 'aptitude', 'aspell', 'awk', 'basename', 'bash', 'bc', 'bg', 'break', 'builtin', 'bzip2', 'cal', 'case', 'cat', 'cd', 'cfdisk', 'chgrp', 'chkconfig', 'chmod', 'chown', 'chroot', 'cksum', 'clear', 'cmp', 'comm', 
    'command', 'continue', 'cp', 'cron', 'crontab', 'csplit', 'curl', 'cut', 'date', 'dc', 'dd', 'ddrescue', 'declare', 'df', 'diff', 'diff3', 'dig', 'dir', 'dircolors', 'dirname', 'dirs', 'dmesg', 'du', 'echo', 'egrep', 'eject', 'enable', 'env', 'ethtool', 'eval', 'exec', 'exit', 'expand', 'expect', 'export', 'expr', 'false', 'fdformat', 'fdisk', 'fg', 'fgrep', 'file', 'filesyes', 'find', 'fmt', 'fold', 'for', 'format', 'free', 'fsck', 'ftp', 'function', 'fuser', 'gawk', 'getopts', 'grep', 'groupadd', 'groupdel', 'groupmod', 'groups', 'gzip', 'hash', 'head', 'help', 'history', 'hostname', 'htop', 'iconv', 'id', 'if', 'ifconfig', 'ifdown', 'ifup', 'import', 'install', 'ip', 'jobs', 'join', 'kill', 'killall', 'less', 'let', 'link', 'ln', 'local', 'locate', 'logname', 'logout', 
    'look', 'lpc', 'lpr', 'lprint', 'lprintd', 'lprintq', 'lprm', 'ls', 'lsof', 'make', 'man', 'mkdir', 'mkfifo', 'mkisofs', 'mknod', 'mmv', 'more', 'most', 'mount', 'mtools', 'mtr', 'mv', 'nc', 'netstat', 'nice', 'nl', 'nohup', 'notify', 'nslookup', 'op', 'open', 
    'passwd', 'paste', 'pathchk', 'ping', 'pkill', 'popd', 'pr', 'printcap', 'printenv', 'printf', 'ps', 'pushd', 'pv', 'quota', 'ram', 'rar', 'rcp', 'read', 'readarray', 'readonly', 'reboot', 'rename', 'renice', 'return', 'rev', 'rm', 'rmdir', 'scp', 'screen', 'sdiff', 'sed', 'select', 'seq', 'set', 'sftp', 'shift', 'shopt', 'shutdown', 'sleep', 'slocate', 'sort', 'source', 'split', 'ssh', 'stat', 'strace', 'su', 'sudo', 'sum', 'suspend', 'tail', 'tar', 'tee', 'test', 'time', 'timeout', 'times', 'top', 'touch', 'tput', 
    'tr', 'traceroute', 'trap', 'true', 'tsort', 'tty', 'ulimit', 'umask', 'umount', 'unalias', 'uname', 'unexpand', 'uniq', 'units', 'unrar', 'unset', 'unshar', 'until', 'uptime', 'useradd', 'userdel', 'usermod', 'users', 'uuencode', 'v', 'vdir', 'vi', 'wait', 'watch', 'wc', 'wget', 'whereis', 'which', 'while', 'who', 'whoami', 'xargs', 'xdg', 'xz', 'zip']
keyword_list = [
    'eject', 'format', 'archive', 'shell', 'translate', 
    'modify', 'determine', 'operator', 'off', 'stream', 
    'display', 'exit', 'prepare', 'abort', 'convert', 
    'move', 'command', 'secure', 'measure', 'compress', 
    'schedule', 'split', 'unmount', 'dns', 'merge', 'enable', 
    'make', 'networking', 'suspend', 'do', 'change', 'send', 
    'strip', 'concatenate', 'query', 'delay', 'line', 'monitor', 
    'topological', 'data', 'find', 'environment', 'netcat', 
    'evaluate', 'declare', 'estimate', 'restore', 'wrap', 
    'user', 'uniquify', 'spell', 'clear', 'alter', 'arbitrary', 'transfer', 
    'divide', 'browse', 'expand', 'ram', 'start', 'set', 'colour', 
    'perform', 'manipulate', 'parse', 'conditionally', 'wait', 'read', 
    'resume', 'store', 'users', 'accept', 'number', 'open', 'search', 
    'mount', 'identify', 'kill', 'list', 'mark', 'shift', 'automate', 
    'partition', 'retrieve', 'process', 'redirect', 'remove', 'briefly', 
    'save', 'system', 'unpack', 'routing', 'test', 'compare', 'file', 'reverse', 
    'sort', 'mass', 'execute', 'display', 'join', 'text', 'verbosely', 'rename', 
    'comment', 'copy', 'output', 'define', 'capture', 'gnu', 'recompile', 
    'daemon', 'shutdown', 'desk', 'check', 'reboot', 'remember', 
    'interactive', 'run', 'network', 'help', 'encode', 'print', 
    'execute', 'delete', 'low-level', 'send', 'add', 
    'substitute', 'limit', 'show', 'configure', 'trace', 'printer', 
    'ethernet', 'package', 'stop', 'extract', 'reformat', 'multiplex', 'create'
    ]

commands_dict = {
    '!': {'!!': 'Run the last command again'},
    '#': {'###': 'Comment / Remark'},
    '.': {'.': 'Run a command script in the current shell'},
    'a': {'alias': 'Create an alias',
        'apropos': 'Search Help manual pages (man -k)',
        'apt-get': 'Search for and install software packages (Debian/Ubuntu)',
        'aptitude': 'Search for and install software packages (Debian/Ubuntu)',
        'aspell': 'Spell Checker',
        'awk': 'Find and Replace text, database sort/validate/index'},
    'b': {'basename': 'Strip directory and suffix from filenames',
        'bash': 'GNU Bourne-Again SHell',
        'bc': 'Arbitrary precision calculator language',
        'bg': 'Send to background',
        'break': 'Exit from a loop',
        'builtin': 'Run a shell builtin',
        'bzip2': 'Compress or decompress named file(s)'},
    'c': {'cal': 'Display a calendar',
        'case': 'Conditionally perform a command',
        'cat': 'Concatenate and print (display) the content of files',
        'cd': 'Change Directory',
        'cfdisk': 'Partition table manipulator for Linux',
        'chgrp': 'Change group ownership',
        'chkconfig': 'System services (runlevel)',
        'chmod': 'Change access permissions',
        'chown': 'Change file owner and group',
        'chroot': 'Run a command with a different root directory',
        'cksum': 'Print CRC checksum and byte counts',
        'clear': 'Clear terminal screen',
        'cmp': 'Compare two files',
        'comm': 'Compare two sorted files line by line',
        'command': 'Run a command â€“ ignoring shell functions',
        'continue': 'Resume the next iteration of a loop',
        'cp': 'Copy one or more files to another location',
        'cron': 'Daemon to execute scheduled commands',
        'crontab': 'Schedule a command to run at a later time',
        'csplit': 'Split a file into context-determined pieces',
        'curl': 'Transfer data from or to a server',
        'cut': 'Divide a file into several parts'},
    'd': {'date': 'Display or change the date & time',
        'dc': 'Desk Calculator',
        'dd': 'Convert and copy a file, write disk headers, boot records',
        'ddrescue': 'Data recovery tool',
        'declare': 'Declare variables and give them attributes',
        'df': 'Display free disk space',
        'diff': 'Display the differences between two files',
        'diff3': 'Show differences among three files',
        'dig': 'DNS lookup',
        'dir': 'Briefly list directory contents',
        'dircolors': 'Colour setup for `lsâ€™',
        'dirname': 'Convert a full pathname to just a path',
        'dirs': 'Display list of remembered directories',
        'dmesg': 'Print kernel & driver messages',
        'du': 'Estimate file space usage'},
    'e': {'echo': 'Display message on screen',
        'egrep': 'Search file(s) for lines that match an extended expression',
        'eject': 'Eject removable media',
        'enable': 'Enable and disable builtin shell commands',
        'env': 'Environment variables',
        'ethtool': 'Ethernet card settings',
        'eval': 'Evaluate several commands/arguments',
        'exec': 'Execute a command',
        'exit': 'Exit the shell',
        'expand': 'Convert tabs to spaces',
        'expect': 'Automate arbitrary applications accessed over a terminal',
        'export': 'Set an environment variable',
        'expr': 'Evaluate expressions'},
    'f': {'false': 'Do nothing, unsuccessfully',
        'fdformat': 'Low-level format a floppy disk',
        'fdisk': 'Partition table manipulator for Linux',
        'fg': 'Send job to foreground',
        'fgrep': 'Search file(s) for lines that match a fixed string',
        'file': 'Determine file type',
        'filesyes': 'Print a string until interrupted ',
        'find': 'Search for files that meet a desired criteria',
        'fmt': 'Reformat paragraph text',
        'fold': 'Wrap text to fit a specified width',
        'for': 'Expand words, and execute commands',
        'format': 'Format disks or tapes',
        'free': 'Display memory usage',
        'fsck': 'File system consistency check and repair',
        'ftp': 'File Transfer Protocol',
        'function': 'Define Function Macros',
        'fuser': 'Identify/kill the process that is accessing a file'},
    'g': {'gawk': 'Find and Replace text within file(s)',
        'getopts': 'Parse positional parameters',
        'grep': 'Search file(s) for lines that match a given pattern',
        'groupadd': 'Add a user security group',
        'groupdel': 'Delete a group',
        'groupmod': 'Modify a group',
        'groups': 'Print group names a user is in',
        'gzip': 'Compress or decompress named file(s)'},
    'h': {'hash': 'Remember the full pathname of a name argument',
        'head': 'Output the first part of file(s)',
        'help': 'Display help for a built-in command',
        'history': 'Command History',
        'hostname': 'Print or set system name',
        'htop': 'Interactive process viewer'},
    'i': {'iconv': 'Convert the character set of a file',
        'id': 'Print user and group idâ€™s',
        'if': 'Conditionally perform a command',
        'ifconfig': 'Configure a network interface',
        'ifdown': 'Stop a network interface',
        'ifup': 'Start a network interface up',
        'import': 'Capture an X server screen and save the image to file',
        'install': 'Copy files and set attributes',
        'ip': 'Routing, devices and tunnels'},
    'j': {'jobs': 'List active jobs', 'join': 'Join lines on a common field'},
    'k': {'kill': 'Kill a process by specifying its PID',
        'killall': 'Kill processes by name'},
    'l': {'less': 'Display output one screen at a time',
        'let': 'Perform arithmetic on shell variables',
        'link': 'Create a link to a file',
        'ln': 'Create a symbolic link to a file',
        'local': 'Create variables',
        'locate': 'Find files',
        'logname': 'Print current login name',
        'logout': 'Exit a login shell',
        'look': 'Display lines beginning with a given string',
        'lpc': 'Line printer control program',
        'lpr': 'Off line print',
        'lprint': 'Print a file',
        'lprintd': 'Abort a print job',
        'lprintq': 'List the print queue',
        'lprm': 'Remove jobs from the print queue',
        'ls': 'List information about file(s)',
        'lsof': 'List open files'},
    'm': {'make': 'Recompile a group of programs',
        'man': 'Help manual',
        'mkdir': 'Create new folder(s)',
        'mkfifo': 'Make FIFOs (named pipes)',
        'mkisofs': 'Create an hybrid ISO9660/JOLIET/HFS filesystem',
        'mknod': 'Make block or character special files',
        'mmv': 'Mass Move and rename (files)',
        'more': 'Display output one screen at a time',
        'most': 'Browse or page through a text file',
        'mount': 'Mount a file system',
        'mtools': 'Manipulate MS-DOS files',
        'mtr': 'Network diagnostics (traceroute/ping)',
        'mv': 'Move or rename files or directories'},
    'n': {'nc': 'Netcat, read and write data across networks',
        'netstat': 'Networking information',
        'nice': 'Set the priority of a command or job',
        'nl': 'Number lines and write files',
        'nohup': 'Run a command immune to hangups',
        'notify': 'send\tSend desktop notifications',
        'nslookup': 'Query Internet name servers interactively'},
    'o': {'op': 'Operator access',
        'open': 'Open a file in its default application'},
    'p': {'passwd': 'Modify a user password',
        'paste': 'Merge lines of files',
        'pathchk': 'Check file name portability',
        'ping': 'Test a network connection',
        'pkill': 'Kill processes by a full or partial name',
        'popd': 'Restore the previous value of the current directory',
        'pr': 'Prepare files for printing',
        'printcap': 'Printer capability database',
        'printenv': 'Print environment variables',
        'printf': 'Format and print data',
        'ps': 'Process status',
        'pushd': 'Save and then change the current director',
        'pv': 'Monitor the progress of data through a pipepwd\tPrint Working '
                'Directory'},
    'q': {'quota': 'Display disk usage and limitsquotacheck\tScan a file system '
                    'for disk usag'},
    'r': {'ram': 'ram disk device',
        'rar': 'Archive files with compression',
        'rcp': 'Copy files between two machines',
        'read': 'Read a line from standard input',
        'readarray': 'Read from stdin into an array variable',
        'readonly': 'Mark variables/functions as readonly',
        'reboot': 'Reboot the system',
        'rename': 'Rename files',
        'renice': 'Alter priority of running processes',
        'return': 'Exit a shell function',
        'rev': 'Reverse lines of a file',
        'rm': 'Remove files',
        'rmdir': 'Remove folder(s)rsync\tRemote file copy (Synchronize file '
                    'trees)'},
    's': {'scp': 'Secure copy (remote file copy)',
        'screen': 'Multiplex terminal, run remote shells via ssh',
        'sdiff': 'Merge two files interactively',
        'sed': 'Stream Editor',
        'select': 'Accept keyboard input',
        'seq': 'Print numeric sequences',
        'set': 'Manipulate shell variables and functions',
        'sftp': 'Secure File Transfer Program',
        'shift': 'Shift positional parameters',
        'shopt': 'Shell Options',
        'shutdown': 'Shutdown or restart linux',
        'sleep': 'Delay for a specified time',
        'slocate': 'Find files',
        'sort': 'Sort text files',
        'source': 'Run commands from a file â€˜.â€™',
        'split': 'Split a file into fixed-size pieces',
        'ssh': 'Secure Shell client (remote login program)',
        'stat': 'Display file or file system status',
        'strace': 'Trace system calls and signals',
        'su': 'Substitute user identity',
        'sudo': 'Execute a command as another user',
        'sum': 'Print a checksum for a file',
        'suspend': 'Suspend execution of this shellsync\tSynchronize data on '
                    'disk with memory'},
    't': {'tail': 'Output the last part of file',
        'tar': 'Store, list or extract files in an archive',
        'tee': 'Redirect output to multiple files',
        'test': 'Evaluate a conditional expression',
        'time': 'Measure Program running time',
        'timeout': 'Run a command with a time limit',
        'times': 'User and system times',
        'top': 'List processes running on the system',
        'touch': 'Change file timestamps',
        'tput': 'Set terminal-dependent capabilities, color, position',
        'tr': 'Translate, squeeze, and/or delete characters',
        'traceroute': 'Trace Route to Host',
        'trap': 'Run a command when a signal is set(bourne)',
        'true': 'Do nothing, successfully',
        'tsort': 'Topological sort',
        'tty': 'Print filename of terminal on stdintype\tDescribe a command'},
    'u': {'ulimit': 'Limit user resources',
        'umask': 'Users file creation mask',
        'umount': 'Unmount a device',
        'unalias': 'Remove an alias',
        'uname': 'Print system information',
        'unexpand': 'Convert spaces to tabs',
        'uniq': 'Uniquify files',
        'units': 'Convert units from one scale to another',
        'unrar': 'Extract files from a rar archive',
        'unset': 'Remove variable or function names',
        'unshar': 'Unpack shell archive scripts',
        'until': 'Execute commands (until error)',
        'uptime': 'Show uptime',
        'useradd': 'Create new user account',
        'userdel': 'Delete a user account',
        'usermod': 'Modify user account',
        'users': 'List users currently logged in',
        'uuencode': 'Encode a binary fileuudecode\tDecode a file created by '
                    'uuencode'},
    'v': {'v': 'Verbosely list directory contents (`ls -l -bâ€™)',
        'vdir': 'Verbosely list directory contents (`ls -l -bâ€™)',
        'vi': 'Text Editorvmstat\tReport virtual memory statistics'},
    'w': {'wait': 'Wait for a process to complete',
        'watch': 'Execute/display a program periodically',
        'wc': 'Print byte, word, and line counts',
        'wget': 'Retrieve web pages or files via HTTP, HTTPS or FTPwrite\tSend a message to another user',
        'whereis': 'Search the user $path, man pages and source files for a program',
        'which': 'Search the user $path for a program file',
        'while': 'Execute commands',
        'who': 'Print all usernames currently logged in',
        'whoami': 'Print the current user id and name (`id -unâ€™)'},
    'x': {'xargs': 'Execute utility, passing constructed argument list(s)',
        'xdg': 'Open a file or URL in the userâ€™s preferred application',
        'xz': 'Compress or  decompress .xz and .lzma '},
    'z': {'zip': 'Package and compress (archive) files '}}

commands_descriptions = [
    'Run the last command again', 'Comment / Remark', 'Run a command script in the current shell', 'Create an alias', 
    'Search Help manual pages (man -k)', 'Search for and install software packages (Debian/Ubuntu)', 
    'Search for and install software packages (Debian/Ubuntu)', 'Spell Checker', 'Find and Replace text, database sort/validate/index', 
    'Strip directory and suffix from filenames', 'GNU Bourne-Again SHell', 'Arbitrary precision calculator language', 'Send to background', 
    'Exit from a loop', 'Run a shell builtin', 'Compress or decompress named file(s)', 'Display a calendar', 'Conditionally perform a command',
    'Concatenate and print (display) the content of files', 'Change Directory', 'Partition table manipulator for Linux', 'Change group ownership', 
    'System services (runlevel)', 'Change access permissions', 'Change file owner and group', 'Run a command with a different root directory', 
    'Print CRC checksum and byte counts', 'Clear terminal screen', 'Compare two files', 'Compare two sorted files line by line', 
    'Run a command â€“ ignoring shell functions', 'Resume the next iteration of a loop', 'Copy one or more files to another location', 
    'Daemon to execute scheduled commands', 'Schedule a command to run at a later time', 'Split a file into context-determined pieces', 'Transfer data from or to a server', 
    'Divide a file into several parts', 'Display or change the date & time', 'Desk Calculator', 'Convert and copy a file, write disk headers, boot records', 
    'Data recovery tool', 'Declare variables and give them attributes', 'Display free disk space', 'Display the differences between two files', 
    'Show differences among three files', 'DNS lookup', 'Briefly list directory contents', 'Colour setup for `lsâ€™', 'Convert a full pathname to just a path', 
    'Display list of remembered directories', 'Print kernel & driver messages', 'Estimate file space usage', 'Display message on screen', 
    'Search file(s) for lines that match an extended expression', 'Eject removable media', 'Enable and disable builtin shell commands', 'Environment variables', 
    'Ethernet card settings', 'Evaluate several commands/arguments', 'Execute a command', 'Exit the shell', 'Convert tabs to spaces', 
    'Automate arbitrary applications accessed over a terminal', 'Set an environment variable', 'Evaluate expressions', 'Do nothing, unsuccessfully', 
    'Low-level format a floppy disk', 'Partition table manipulator for Linux', 'Send job to foreground', 'Search file(s) for lines that match a fixed string', 
    'Determine file type', 'Print a string until interrupted ', 'Search for files that meet a desired criteria', 'Reformat paragraph text', 
    'Wrap text to fit a specified width', 'Expand words, and execute commands', 'Format disks or tapes', 'Display memory usage', 'File system consistency check and repair', 
    'File Transfer Protocol', 'Define Function Macros', 'Identify/kill the process that is accessing a file', 'Find and Replace text within file(s)', 'Parse positional parameters', 
    'Search file(s) for lines that match a given pattern', 'Add a user security group', 'Delete a group', 'Modify a group', 'Print group names a user is in', 
    'Compress or decompress named file(s)', 'Remember the full pathname of a name argument', 'Output the first part of file(s)', 'Display help for a built-in command', 
    'Command History', 'Print or set system name', 'Interactive process viewer', 'Convert the character set of a file', 'Print user and group idâ€™s', 
    'Conditionally perform a command', 'Configure a network interface', 'Stop a network interface', 'Start a network interface up', 
    'Capture an X server screen and save the image to file', 'Copy files and set attributes', 'Routing, devices and tunnels', 'List active jobs', 
    'Join lines on a common field', 'Kill a process by specifying its PID', 'Kill processes by name', 'Display output one screen at a time', 
    'Perform arithmetic on shell variables', 'Create a link to a file', 'Create a symbolic link to a file', 'Create variables', 'Find files', 
    'Print current login name', 'Exit a login shell', 'Display lines beginning with a given string', 'Line printer control program', 
    'Off line print', 'Print a file', 'Abort a print job', 'List the print queue', 'Remove jobs from the print queue', 'List information about file(s)', 
    'List open files', 'Recompile a group of programs', 'Help manual', 'Create new folder(s)', 'Make FIFOs (named pipes)', 'Create an hybrid ISO9660/JOLIET/HFS filesystem', 
    'Make block or character special files', 'Mass Move and rename (files)', 'Display output one screen at a time', 'Browse or page through a text file', 'Mount a file system', 
    'Manipulate MS-DOS files', 'Network diagnostics (traceroute/ping)', 'Move or rename files or directories', 'Netcat, read and write data across networks', 'Networking information', 
    'Set the priority of a command or job', 'Number lines and write files', 'Run a command immune to hangups', 'send\tSend desktop notifications', 'Query Internet name servers interactively', 
    'Operator access', 'Open a file in its default application', 'Modify a user password', 'Merge lines of files', 'Check file name portability', 
    'Test a network connection', 'Kill processes by a full or partial name', 'Restore the previous value of the current directory', 'Prepare files for printing', 
    'Printer capability database', 'Print environment variables', 'Format and print data', 'Process status', 'Save and then change the current director', 
    'Monitor the progress of data through a pipepwd\tPrint Working Directory', 'Display disk usage and limitsquotacheck\tScan a file system for disk usag', 
    'ram disk device', 'Archive files with compression', 'Copy files between two machines', 'Read a line from standard input', 'Read from stdin into an array variable', 
    'Mark variables/functions as readonly', 'Reboot the system', 'Rename files', 'Alter priority of running processes', 'Exit a shell function', 'Reverse lines of a file', 
    'Remove files', 'Remove folder(s)rsync\tRemote file copy (Synchronize file trees)', 'Secure copy (remote file copy)', 'Multiplex terminal, run remote shells via ssh', 
    'Merge two files interactively', 'Stream Editor', 'Accept keyboard input', 'Print numeric sequences', 'Manipulate shell variables and functions', 'Secure File Transfer Program',
    'Shift positional parameters', 'Shell Options', 'Shutdown or restart linux', 'Delay for a specified time', 'Find files', 'Sort text files', 'Run commands from a file ', 
    'Split a file into fixed-size pieces', 'Secure Shell client (remote login program)', 'Display file or file system status', 'Trace system calls and signals', 
    'Substitute user identity', 'Execute a command as another user', 'Print a checksum for a file', 'Suspend execution of this shellsync\tSynchronize data on disk with memory',
    'Output the last part of file', 'Store, list or extract files in an archive', 'Redirect output to multiple files', 'Evaluate a conditional expression', 
    'Measure Program running time', 'Run a command with a time limit', 'User and system times', 'List processes running on the system', 
    'Change file timestamps', 'Set terminal-dependent capabilities, color, position', 'Translate, squeeze, and/or delete characters', 'Trace Route to Host', 
    'Run a command when a signal is set(bourne)', 'Do nothing, successfully', 'Topological sort', 'Print filename of terminal on stdintype\tDescribe a command', 'Limit user resources', 'Users file creation mask', 'Unmount a device', 'Remove an alias', 'Print system information', 'Convert spaces to tabs', 'Uniquify files', 'Convert units from one scale to another', 'Extract files from a rar archive', 'Remove variable or function names', 'Unpack shell archive scripts', 'Execute commands (until error)', 'Show uptime', 'Create new user account', 'Delete a user account', 'Modify user account', 'List users currently logged in', 'Encode a binary fileuudecode\tDecode a file created by uuencode', 'Verbosely list directory contents (`ls -l -bâ€™)', 'Verbosely list directory contents (`ls -l -bâ€™)', 'Text Editorvmstat\tReport virtual memory statistics', 'Wait for a process to complete', 'Execute/display a program periodically', 'Print byte, word, and line counts', 'Retrieve web pages or files via HTTP, HTTPS or FTPwrite\tSend a message to another user', 'Search the user $path, man pages and source files for a program', 
    'Search the user $path for a program file', 'Execute commands', 'Print all usernames currently logged in', 'Print the current user id and name (`id -unâ€™)', 
    'Execute utility, passing constructed argument list(s)', 'Open a file or URL in the userâ€™s preferred application', 'Compress or  decompress .xz and .lzma ', 
    'Package and compress (archive) files '
    ]

#######################################
#       Functions
#######################################

def string_to_wordlist(string: str) -> list[str]:
    retv = []
    chunks = string.split(" ")
    com = "'"
    puncts = f'{com},.!?-:;"'
    for word in chunks:
        myword = word
        for punct in puncts:
            if word.endswith(punct):
                myword = word[:-1]
                break
        retv.append(myword)
    return retv

def first(wordlist: list[str]) -> str:
    """ returns the first word of a word list """
    return wordlist[0]


def read_lines(filename: str) -> list[str]:
    """ read file path to lines """
    
    with open(filename, File.read) as rfile:
        data: str = rfile.read()
    lines: list[str] = data.split("\n")
    return lines

def make_command_map() -> dict[str:dict[str]]:
    names = read_lines(Files.command_names)
    descriptions = read_lines(Files.command_descriptions)
    fmap = {}
    for name in names:
        fmap[f'{name[0]}'] = {}
    for index, name in enumerate(names):
        try:
            fmap[f'{name[0]}'][name] = descriptions[index]
        except:
            pass 
    pprint(fmap)
    
def fix_word_length(word: str, length: int=10) -> str:
    
    myword = word
    myword_len = len(myword)
    while myword_len != length:
        myword = myword + ' '
        myword_len = len(myword)
    return myword


def get_letters() -> list[str]:
    
    return list(commands_dict.keys())


def subdict_items(letter: str) -> tuple[list[str], list[str]]:
    
    mydict = commands_dict[letter]
    return list(mydict.keys()), list(mydict.values())


def sub_lists() -> tuple[list[str], list[str]]:
    
    all_names = []
    all_values = []
    for letter in get_letters():
        names, values = subdict_items(letter)
        for name in names:all_names.append(name)
        for value in values:all_values.append(value)
    return all_names, all_values


def print_all():

    for letter in get_letters():
        
        print(f'[ {letter} ]')
        mynames, myvalues = subdict_items(letter=letter)
        
        for index, name in enumerate(mynames):
            myname = fix_word_length(name)
            print(f'\t{myname}\t\t{myvalues[index]}')


def first_words_desc() -> list[str]:
    first_word_list = []
    for des in commands_descriptions:
        wl = string_to_wordlist(des)
        first_word_list.append(first(wl).lower())
    return first_word_list

def search_commands(name: str):
    values = commands_dict.values()
    found = False
    for value in values:
        try:
            mydict = value[name]
            print(name)
            print(value[name])
            found = True
        except:
            pass
    if not found:
        for index, desc in enumerate(commands_descriptions):
            wl = string_to_wordlist(desc)
            name_list = list(set([name.lower(), name.upper(), name.capitalize()]))
            for xname in name_list:
                if xname in wl:
                    print(f'[ {command_names_list[index]} ]')
                    print(f'\t\t{desc}')
            


if __name__ == '__main__':
    
    args = sys.argv[1:]
    if args == [] or args == None:
        print_all()
    else:
        for arg in args:
            search_commands(arg)
    
