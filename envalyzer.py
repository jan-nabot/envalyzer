from os import listdir
listofpids = []
commswithenvslist = []

def main():
    directorylisting = listdir('/proc/')
    for potentialpid in directorylisting:
        try: # find numerical directories in /proc/ VFS
            assert int(potentialpid)
            listofpids.append(potentialpid)
        except ValueError:
            pass

    for pid in listofpids: # do something to list of pids found
        with open('/proc/' + pid + '/cmdline') as procnamelookup: # get pid initiating command
            initialcommand = procnamelookup.readline()[:-1].replace('\x00', ' ')
        with open('/proc/' + pid + '/environ') as procinitialenvs: # get pid initial env vars
            itsenvs = str(procinitialenvs.readline()).replace('\x00', '    ')
        commswithenvslist.append([pid, initialcommand, itsenvs])

    if __name__ == '__main__':
        for pidinfo in commswithenvslist: # present command and its envs
            if len(pidinfo[2]) < 3: # suppress if no envs related
                pass 
            else:
                print('PID: ', pidinfo[0], ' ( ', pidinfo[1], ' ):', '\n', pidinfo[2], '\n')
    else:
        return commswithenvslist
            
main() # Print environment variables of Linux processes. Run with privileges.
