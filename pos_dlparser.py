#  parse input string and create specific records
#  Copyright 2018 Aloft Time Productions, LLC 
#  Apache License 2.0: http://www.apache.org/licenses/LICENSE-2.0.txt

#  main functions to parse DL string
#  
import re
from datetime import datetime
from datetime import date


# Discussion:   How to parse?   Are the fields always in the same order?  I am going to make that assumption - the fields are in the same order
  
# TODO:
# These functions need to be expanded to support the new DLs being issues. The parsing strings are weak and need to check for null values
# There may have to be multiple test to look for each tag and the provide conditional parse.


#  following are DL fields tags to help parse the dl string { reference only}

driverLicenseFields = {
                  'DAA':  'Full Name' ,
		  'DAB': 'Last Name' ,
		  'DAB': 'Family Name' ,
		  'DAC': 'First Name' ,
		  'DAC': 'Given Name' ,
		  'DAD': 'Middle Name or Initial' ,
		  'DAD': 'Middle Name' ,
		  'DAE': 'Name Suffix' ,
		  'DAF': 'Name Prefix' ,
		  'DAG': 'Mailing Street Address1' ,
		  'DAH': 'Mailing Street Address2' ,
		  'DAI': 'Mailing City' ,
		  'DAJ': 'Mailing Jurisdiction Code' ,
		  'DAK': 'Mailing Postal Code' ,
		  'DAL': 'Residence Street Address1' ,
		  'DAM': 'Residence Street Address2' ,
		  'DAN': 'Residence City' ,
		  'DAO': 'Residence Jurisdiction Code' ,
		  'DAP': 'Residence Postal Code' ,
		  'DAQ': 'License or ID Number' ,
		  'DAR': 'License Classification Code' ,
		  'DAS': 'License Restriction Code' ,
		  'DAT': 'License Endorsements Code' ,
		  'DAU': 'Height in FT_IN' ,
		  'DAV': 'Height in CM' ,
		  'DAW': 'Weight in LBS' ,
		  'DAX': 'Weight in KG' ,
		  'DAY': 'Eye Color' ,
		  'DAZ': 'Hair Color' ,
		  'DBA': 'License Expiration Date' ,
		  'DBB': 'Date of Birth' ,
		  'DBC': 'Sex' ,
		  'DBD': 'License or ID Document Issue Date' ,
		  'DBE': 'Issue Timestamp' ,
		  'DBF': 'Number of Duplicates' ,
		  'DBG': 'Medical Indicator Codes', 
		  'DBH': 'Organ Donor' ,
		  'DBI': 'Non-Resident Indicator' ,
		  'DBJ': 'Unique Customer Identifier' ,
		  'DBK': 'Social Security Number' ,
		  'DBL': 'Date Of Birth' ,
		  'DBM': 'Social Security Number' ,
		  'DBN': 'Full Name' ,
		  'DBO': 'Last Name' ,
		  'DBO': 'Family Name' ,
		  'DBP': 'First Name' ,
		  'DBP': 'Given Name' ,
		  'DBQ': 'Middle Name' ,
		  'DBQ': 'Middle Name or Initial' ,
		  'DBR': 'Suffix' ,
		  'DBS': 'Prefix' ,
		  'DCA': 'Virginia Specific Class' ,
		  'DCB': 'Virginia Specific Restrictions' ,
		  'DCD': 'Virginia Specific Endorsements' ,
		  'DCE': 'Physical Description Weight Range' ,
		  'DCF': 'Document Discriminator' ,
		  'DCG': 'Country territory of issuance' ,
		  'DCH': 'Federal Commercial Vehicle Codes' , 
		  'DCI': 'Place of birth' ,
		  'DCJ': 'Audit information' ,
		  'DCK': 'Inventory Control Number' ,
		  'DCL': 'Race Ethnicity' ,
		  'DCM': 'Standard vehicle classification' ,
		  'DCN': 'Standard endorsement code' ,
		  'DCO': 'Standard restriction code' ,
		  'DCP': 'Jurisdiction specific vehicle classification description' ,
		  'DCQ': 'Jurisdiction-specific' ,
		  'DCR': 'Jurisdiction specific restriction code description' ,
		  'DCS': 'Family Name', 
		  'DCS': 'Last Name' ,
		  'DCT': 'Given Name' ,
		  'DCT': 'First Name' ,
		  'DCU': 'Suffix' ,
		  'DDA': 'Compliance Type' ,
		  'DDB': 'Card Revision Date' ,
		  'DDC': 'HazMat Endorsement Expiry Date' ,
		  'DDD': 'Limited Duration Document Indicator' ,
		  'DDE': 'Family Name Truncation' ,
		  'DDF': 'First Names Truncation' ,
		  'DDG': 'Middle Names Truncation' ,
		  'DDH': 'Under 18 Until' ,
		  'DDI': 'Under 19 Until' ,
		  'DDJ': 'Under 21 Until' ,
		  'DDK': 'Organ Donor Indicator' ,
		  'DDL': 'Veteran Indicator' ,
		  'PAA': 'Permit Classification Code' ,
		  'PAB': 'Permit Expiration Date' ,
		  'PAC': 'Permit Identifier' ,
		  'PAD': 'Permit IssueDate' ,
		  'PAE': 'Permit Restriction Code' ,
		  'PAF': 'Permit Endorsement Code' ,
		  'ZVA': 'Court Restriction Code' ,
}



def parse_dl(dlscan):
#       parses out DL #
        try:
                # DAQ3		 
                # DAR
                p = re.compile(r'DAQ\w+DAR')
                dl = p.search(dlscan)
                dl = dl.group()
                dl = dl.replace('DAQ','')
                dl = dl.replace('DAR','')
                print(dl)
                return dl
        except ArithmeticError:
                print('Error',dl)

def parse_lname(dlscan):
#       parses out last name
        try:
                # DAB  		#Last name 
                # DAC  		#First Name 
                p = re.compile(r'DAB\w+DAC')
                lname = p.search(dlscan)
                lname = lname.group()
                lname = lname.replace('DAB','')
                lname = lname.replace('DAC','')
                print(lname)
                return lname
        except AttributeError:
                print('Error', lname)

def parse_fname(dlscan):
#       parses out first name
        try: 
                # DAC     	First Name 
                # DAD 		Middle name
                p = re.compile(r'DAC\w+DAD')
                fname = p.search(dlscan)
                fname = fname.group()
                fname = fname.replace('DAC','')
                fname = fname.replace('DAD','')
                print(fname)
                return fname
        except AttributeError:
                print('Error', fname)

def parse_mname(dlscan):
#       parses out the middle name        
        try:
                # DAD     	Middle name 
                # DAE 		name suffix
                p = re.compile(r'DAD\w+DAE')
                mname = p.search(dlscan)
                mname = mname.group()
                mname = mname.replace('DAD','')
                mname = mname.replace('DAE','')
                print(mname)
                return mname
        except AttributeError:
                print('Error', mname)

def parse_pcode(dlscan):
#       parses out postal code        
        try:
                # DAP     	 Residence postal code
                # DAQ 		
                p = re.compile(r'DAP\w+-\w+DAQ')
                pcode = p.search(dlscan)
                pcode = pcode.group()
                pcode = pcode.replace('DAP','')
                pcode = pcode.replace('DAQ','')
                print(pcode)
                return pcode
        except AttributeError:
                print('Error', pcode)

def calculate_age(dlbirthdate):
        today = date.today()
        return today.year - dlbirthdate.year - ((today.month, today.day) < (dlbirthdate.month, dlbirthdate.day))

def parse_dlexdate(dlscan):
        try:
            # DBA       # Expire - CALCULATE1
            # DBB	    # DOB - CALCULATE2  (STORE AGE)
                p = re.compile(r'DBA\w+-\w+-\w+DBB')
                dlexdate = p.search(dlscan)
                dlexdate = dlexdate.group()
                dlexdate = dlexdate.replace('DBA','')
                dlexdate = dlexdate.replace('DBB','')
                dlexdate = datetime.strptime(dlexdate, '%m-%d-%Y').date()
                print(dlexdate)    
                return dlexdate
        except AttributeError:
                print('Error', dlexdate)

def parse_dlbirthdate(dlscan):
        try:
                # DBB	    # DOB - CALCULATE2  (STORE AGE)
                # DBC	    # Sex - STORE
                p = re.compile(r'DBB\w+-\w+-\w+DBC')
                dlbirthdate = p.search(dlscan)
                dlbirthdate = dlbirthdate.group()
                dlbirthdate = dlbirthdate.replace('DBB','')
                dlbirthdate = dlbirthdate.replace('DBC','')
                dlbirthdate = datetime.strptime(dlbirthdate, '%m-%d-%Y').date()
                print(dlbirthdate)
                return dlbirthdate
        except AttributeError:
                print('Error', dlbirthdate)

def parse_sex(dlscan):
        try: 
                # DBC    # Sex - STORE
                # DBD    # issue date - NO CAPTURE
                p = re.compile(r'DBC\w+DBD')
                sex = p.search(dlscan)
                sex = sex.group()
                sex = sex.replace('DBC','')
                sex = sex.replace('DBD','')
                print(sex)
                return sex
        except AttributeError:
                print('Error', sex)


