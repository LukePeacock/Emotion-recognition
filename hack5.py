"""\
------------------------------------------------------------
USE: python <PROGNAME> (options)
OPTIONS:
    -h : print this help message
    -e : number of emotions to detect
    -t : time per emotion
------------------------------------------------------------\
"""

#===============================================
from __future__ import print_function
import sys, getopt, hashlib

#from real_time_video import start_stream

#========================================
# Command Line Processing
class CommandLine:
    def __init__(self):
        opts, args = getopt.getopt(sys.argv[1:], 'he:t:')
        opts = dict(opts)
        self.exit = True

        if '-h' in opts:
            self.printHelp()
            return
  
        if len(args) > 0:
            print("*** ERROR: no arg files - only options! ***", file=sys.stderr)
            self.printHelp()
            return
        
        ## check if emotion number option is included
        if '-e' in opts:
            if isinstance(int(opts['-e']), int):
                self.emo_number = opts['-e']
            else:
                warning = (
                    "*** ERROR: emotion number (opt: -e LABEL)! ***\n"
                    " -- value (%s) not recognised!\n"
                    " -- must be an integer"
                    ) % (opts['-e'])
                print(warning, file=sys.stderr)
                self.printHelp()
                return
        else:
            self.emo_number = 5

        ## check if emotion duration option is included
        if '-t' in opts:
            if isinstance(float(opts['-t']), float):
                self.emo_duration = opts['-t']
            else:
                warning = (
                    "*** ERROR: emotion duration (opt: -t LABEL!) ***\n"
                    " -- value (%s) not recognised!\n"
                    " -- must be a float"
                    ) % (opts['-t'])
                print(warning, file=sys.stderr)
                self.printHelp()
                return
        else:
            self.emo_duration = 1
    
        self.exit = False
    
    def printHelp(self):
        progname = sys.argv[0]
        progname = progname.split('/')[-1]
        help = __doc__.replace('<PROGNAME>', progname, 1)
        print(help, file=sys.stderr)

## Encryption function using SHA-2 256 bit hashing
def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
    
## Turn emotions array into password by hashing each individually
## then concat them into a string and hash that then return
def create_password(emotions, emo_num, emo_dur):
    password = ""

    for item in emotions:
        password+= encrypt_string(item)
    password += encrypt_string(emo_num)
    password += encrypt_string(emo_dur)
    newpass = encrypt_string(password)
    return newpass

if __name__ == '__main__':
    config = CommandLine()
    if config.exit:
        sys.exit(0)
    emo_num = config.emo_number
    emo_dur = config.emo_duration
    print(str(emo_num) + ":" + str(emo_dur))
    
    
    # Test emotion array
    emos = ['happy', 'sad', 'happy']
    password = create_password(emos, str(emo_num), str(emo_dur))
    print(password)



#emos = (start_stream(3,50))
