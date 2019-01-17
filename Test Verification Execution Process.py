import subprocess

def processExists(processname):
    tlcall = 'TASKLIST', '/FI', 'imagename eq %s' % processname
    
    tlproc = subprocess.Popen(tlcall, shell=True, stdout=subprocess.PIPE)
    
    tlout = tlproc.communicate()[0].strip().split('\r\n')

    if len(tlout) > 1 and processname in tlout[-1]:
        print('process "%s" is running!' % processname)
        return True
    else:
        print('process "%s" is NOT running!' % processname)
        return False
