import sys
import subprocess

def main():
    # Test if there is at least one server to connect to
    if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '?' or sys.argv[1] == '/?' or sys.argv[1] == 'help':
        print usage()
    else:
        # Get sys.argv starting at position [1] to avoid rdp sys.argv[0]
        # which is the script name itself
        servers = sys.argv[1:]
    
        # Iterate over the args (e.g. servers name) and call them one by
        # one in a different mstsc.exe process
        for server in servers:
            rdp = 'mstsc /v:' + server
            subprocess.Popen(rdp)
            
def usage():
    print 'Remote Control Utility for Windows. RC.PY, v 0.1'
    print 'Info: Simply call one mstsc.exe process per server name entered to enable multiple connections at once.'
    print '>>> Usage: '
    print ">>> to print this help: 'rc -h' or 'rc ?' or 'rc /?' or 'rc help'"
    print '>>> to connect: rc server_name-1 [server_name-2 server_name-3 ... server_name-n]'
    print '>>> example: rc dc1 exchange2k7 appserver'
    
if __name__ == '__main__':
    main()
