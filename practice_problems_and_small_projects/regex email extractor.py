# we need to extract out the emails from the internet page content.
# press "control+A" for selecting all the content in web page. Save it in a file or as string in Python file.
# Using regex expressions, extract emails from it. Write the emails to the file.


# solution:-

# import re
# s = """
# Alliance University 360 degree vertual tour
# International Collaborations
# News & Events
# Media Presence
# Blog
# Insights
# Research
# Conferences
# Webinars
# Careers
# Library
# Login
# Contact Us
# APPLY ONLINE
# Alliance University
# ● COVID-19 UPDATES
# ABOUT

# ACADEMICS
# ADMISSIONS
# PROGRAMMES
# CAMPUS LIFE
# PLACEMENTS
# Enquire Now
# Contact Us
# Alliance University
# Central Campus
# Chikkahagade Cross, Chandapura - Anekal Main Road, Anekal, Bengaluru – 562 106, Karnataka, India.

# Get Route Map

# Phone : +91 80 4619 9000 / 9100 / +91 80 4129 9200

# Fax : +91 80 4619 9099

# E-mail : enquiry@alliance.edu.in

# City Campus 1
# 19th Cross, 7th Main, BTM 2nd Stage, N.S. Palya, Bengaluru – 560 076, Karnataka, India.
#
# Get Route Map
#
# Phone : +91 80 26786020 / 21 / +91 80 26789749
#
# Office of Admissions
# UG

# +91 96200 09825
#
# +91 91084 42143
#
# PG
#
# +91 98860 02500
#
# +91 99002 29974
#
# City Campus 2
# 2nd Cross, 36th Main, Dollars Scheme, BTM 1st Stage, Bengaluru – 560 068, Karnataka, India
#
# Get Route Map
#
# Phone : +91 80 26681444 / 4372
#
# Fax : +91 80 26782048
#
# Enquiry
# Feedback

# Select Institute Applying For
# Enter Full Name
# Enter Email Address
# Enter Mobile Number
# Enter State
# Enter City
#
# Select Course
# Type Your Enquiry Here
# By clicking Submit, you agree to our Terms & Conditions, Privacy Policy and Disclaimer, including our Cookie Use.
#
# Vice-Chancellor
# Dr. Anubha Singh

# Phone : +91 80 4619 9100 / +91 80 4129 9200
#
# E-mail : vc@alliance.edu.in
#
# Registrar
# Dr. Nivedita Mishra
#
# Phone : +91 80 4619 9100 / +91 80 4129 9200
#
# E-mail : registrar@alliance.edu.in
#
# Admissions
# Phone : +91 80 4619 9010

# E-mail : admissions@alliance.edu.in
#
# Placements
# Phone : +91 80 4619 9113
#
# E-mail : placement@alliance.edu.in
#
# International Affairs
# Phone : +91 80 4619 9000 / 9100
#
# E-mail : oia@alliance.edu.in
#
# Human Resources Department
# Phone : +91 80 4619 9083

# E-mail : hrd@alliance.edu.in
#
# Student Verification
# Office of Registrar (Examination & Evaluation)
# Phone : +91 80 4619 9100 / +91 80 4129 9200
#
# E-mail : edu.verify@alliance.edu.in
#
# ABOUT
# The UniversityRanking & Accolades
# IMPORTANT LINKS
# ResultsAACSBIACBENIRF - ManagementNIRF - EngineeringNIRF - 2021Student LoginFaculty & Staff LoginRoute Map
# SCHOOLS
# Alliance School of BusinessAlliance College of Engineering & DesignAlliance School of LawAlliance Ascent College
# DownloadsWebmailContact UsStudent VerificationAnti-Ragging Policy
# PROGRAMMES
# UndergraduatePostgraduateDoctoralExecutive Education
# OTHERS
# SitemapDisclaimerPrivacy PolicyTerms & Conditions
# ADMISSIONS
# Admission ProcessCourse & Fee StructurePayment OptionsUniversity Brochures
# Helpline
# 080 4619 9000 / 9100 / 080 4129 9200


# FOLLOW US
     

# Alliance University
#
# Designed and Developed by Sterco Digitex
#
#
# Hey! I am Niaa... Your Admission Assistant.

# """


# mail = re.findall(r"[0-9a-zA-Z._+%]+[@][0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+", s)  # [] means pattern is grouped.
# here findall() function gives all the matches which we are defining in the pattern.
# "+" means one or more occurrence. If we want to get from 0 to 9, we write as 0-9.
# We write a-z for searching a to z. We write A-Z for searching A to Z.
# print(mail)  # we get the result in list format, we get the mail ids in the above string.

# ---------------------*-------------------------*------------------------*-------------------------*--------------

# we see another example of findall() function in a different way.

# import re
# st = "Hello my Number is 123456789 and my friend's number is 987654321"
# A sample regular expression to find digits.
# regex = "\d+"  # \d finds 0 to 9 digits, "+" gives matches with one or more than one occurrence.

# regex is the variable in which we have defined our required string pattern.

# match = re.findall(regex, st)  # takes two arguments, one is pattern and other is string.
# print(match)  # we get the result     ['123456789', '987654321']

# -----------------------*-------------------------*----------------------*---------------------------*------------
