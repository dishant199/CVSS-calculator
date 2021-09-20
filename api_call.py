__version__ = 3.1
__author__ = "Dishant gupta"
"""
this file is used to enter the values of all the vectors in the respective format and display the calculated score
"""
from pycvss3 import Vector

cvss3_vector =  "AV:N/AC:H/PR:H/UI:R/S:U/C:H/I:N/A:H/E:H/RL:W/RC:U/CR:L/IR:H/AR:M/MAV:H/MAC:H/MPR:N/MUI:N/MS:C/MC:N/MI:H/MA:L"
cvss3 = Vector(cvss3_vector)
cvss_base_value = cvss3.cvss_base_score()
cvss_temporal_value = cvss3.cvss_temporal_score()
cvss_environmental_value = cvss3.cvss_environmental_score() 
print ("CVSS v3 vector:", cvss3_vector)
print ("\tCVSS v3 Base Score:", cvss_base_value)
print ("\tCVSS v3 Temporal Score:", cvss_temporal_value)
print ("\tCVSS v3 Environmental Score:", cvss_environmental_value)



OUTPUT:
  CVSS v3 vector: AV:N/AC:H/PR:H/UI:R/S:U/C:H/I:N/A:H/E:H/RL:W/RC:U/CR:L/IR:H/AR:M/MAV:H/MAC:H/MPR:N/MUI:N/MS:C/MC:N/MI:H/MA:L
	CVSS v3 Base Score: (5.7, 'Medium')
	CVSS v3 Temporal Score: (5.1, 'Medium')
	CVSS v3 Environmental Score: (8.4, 'High')
