__version__ = 3.1
__author__ = "Dishant Gupta"

"this file is converting all the agruments in the formulae file to vectors"

import argparse
from pycvss3 import Vector

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action="version",
                        version="You are using pycvss3 {0} by {1} ".format(__version__, __author__))
    parser.add_argument("--vector", metavar="Vector mode", type=str, help="Paste the CVSS v3 vector string (without CVSS:3.0/) ")
    args = parser.parse_args()

    if args.vector:
        vector = Vector(args.vector)
        (cvss_base_value, cvss_base_risk_level) = vector.cvss_base_score()
        (cvss_temporal_value, cvss_temporal_risk_level) = vector.cvss_temporal_score()
        (cvss_environmental_value, cvss_environmental_risk_level) = vector.cvss_environmental_score()

        print ("\tCVSS 3 Base Score: %s | Rating : %s" % (cvss_base_value, cvss_base_risk_level))
        print ("\tCVSS 3 Temporal Score: %s | Rating : %s" % (cvss_temporal_value, cvss_temporal_risk_level))
        print ("\tCVSS 3 Environmental Score: %s | Rating : %s" % (cvss_environmental_value, cvss_environmental_risk_level))