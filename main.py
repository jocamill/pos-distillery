#  parse input string and create specific records
#  Copyright 2018 Aloft Time Productions, LLC 
#  Apache License 2.0: http://www.apache.org/licenses/LICENSE-2.0.txt


from pos_dlparser import parse_fname
from pos_dlparser import parse_mname
from pos_dlparser import parse_lname
from pos_dlparser import parse_pcode
from pos_dlparser import parse_dlexdate
from pos_dlparser import parse_dlbirthdate
from pos_dlparser import calculate_age
from pos_dlparser import parse_sex
from pos_dlparser import parse_dl
from pynput import keyboard

from datetime import datetime
from datetime import date

# setup tinyDB
from tinydb import TinyDB, Query
db = TinyDB('pos.json', sort_keys=True, indent=4, separators=(',',': '))

today = date.today()
print(today)
print('Starting applicaiton')
print()
print('To end - CTRL-C')
print()
# Manual input string for testing (would need to be populated)
#dlscan=""


# set up infinit loop

# set up blank array to store scanner info
while True:
    dlscan_array =[]

    print('Press ESC after the Scanner BEEPS!')
    print('Press ESC before the BEEP to EXIT')
    f= open("dl2020.txt","w+")
    def on_press(key):
        try: 
            k = key.char # single-char keys
            dlscan_array.append(k) # store in global variable
#           print('Key pressed: ' + k)  # debugging message  
        except: 
            k = key.name # other keys
            if key == keyboard.Key.esc: return False # stop listener
    
    lis = keyboard.Listener(on_press=on_press)
    lis.start() 
    lis.join() 

    # print Array
    print(dlscan_array)

#   test list to exit application    
    if not dlscan_array:
        print()
        print('Exiting Applicaiton - Goodbye')
        break 
    else:
        print('Processing')
        print()

    if len(dlscan_array) < 50:
        # accounts for the bad scans which typically means a short list of numbers
        print('Bad scan - do it again')
    else:     
        # convert list to one big string
        dlscan = ''.join(str(e) for e in dlscan_array)

        # convert to upper case (due to tags as all upper case in regex)
        dlscan = dlscan.upper()
        print(dlscan)

        #remove some useless pieces
        # TODO: This needs to be refined
        # NOTE: Another way to do this is to create a hash of all tags and then parse the string to create value key pairs with specific
        # NOTE: meanings. 

        dlscan = dlscan.replace("@","")
        dlscan = dlscan.replace("2ANSI","")
        dlscan = dlscan.replace("\r\n","")

        # call imported functions to parse
        fname = parse_fname(dlscan)
        # print('debug - ',fname)
        # check for intial bad parse which probably means a 2020 DL format
        
        if not fname:
            print('This may be a new 2020 DL which is not supported yet')
            print('This DL must be captured in written form')
            print()
            f.write("".join(dlscan_array))
            f.close
            print('Ready to scan another DL')
        else:    
            mname = parse_mname(dlscan)
            lname = parse_lname(dlscan)
            pcode = parse_pcode(dlscan)
            dlexdate = parse_dlexdate(dlscan)

            # determine if the license is expired
            if dlexdate > today:
                    expired_dl = False
                    print ('Expired -', expired_dl)
            else:
                    expired_dl = True
                    print ('Expired -', expired_dl)

            # parse birth date
            dlbirthdate = parse_dlbirthdate(dlscan)

            # calculate customer age
            customer_age = calculate_age(dlbirthdate)
            if customer_age >= 21:
                print('Legal Age')
                print(customer_age)
                Legal_age = True    
            else:
                print('Not Legal Age')
                print(customer_age)
                Legal_age = False

            # Determine sex
            sex = parse_sex(dlscan)

            # parse DL
            newdl = parse_dl(dlscan)

            # default testing
            # TODO:  need to be able to query database and determine the number of bottles already purchases to determine if sale is possible

            bottles = 1

            # tiny data base routine to store in pos.json file

            db.insert({'dl':newdl,'fname':fname})
            db.insert({'dl':newdl,'mname':mname})
            db.insert({'dl':newdl,'lname':lname})
            db.insert({'dl':newdl,'pcode':pcode})
            # db.insert({'dl':newdl,'exdate':dlexdate})    - date is not serializable - need to fix
            db.insert({'dl':newdl,'expired':expired_dl})
            db.insert({'dl':newdl,'age':customer_age})
            db.insert({'dl':newdl,'legal':Legal_age})
            db.insert({'dl':newdl,'sex':sex})
            db.insert({'dl':newdl,'count':bottles})

            db.all()
            f.close()