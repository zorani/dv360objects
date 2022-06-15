from cloudapi import GoogleBaseRESTAPI
import os
from jettings import Jettings

# You need to create these json config files, and export the location as the
# following environment variables.
# export GOOGLE_APPLICATION_CREDENTIALS=/home/ubuntu/.creds/.google/360servicecreds.json
# export GOOGLE_DV360_ACCOUNT_INFO=/home/ubuntu/.creds/.google/360accountinfo.json

# See notes at the end of this file.


class DV360APIConnection(GoogleBaseRESTAPI):
    def __init__(self):
        if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
            pass
        else:
            raise Exception('"GOOGLE_APPLICATION_CREDENTIALS" ENV Variable not set.')
        if "GOOGLE_DV360_ACCOUNT_INFO" in os.environ:
            pass
        else:
            raise Exception('"GOOGLE_DV360_ACCOUNT_INFO" ENV Variable not set.')

        self.google_dv360_account_info = os.getenv("GOOGLE_DV360_ACCOUNT_INFO")
        self.jaccountinfo = Jettings(self.google_dv360_account_info)
        self.advertiser_id = self.jaccountinfo.gets(["advertiser_id"])
        self.partner_id = self.jaccountinfo.gets(["partner_id"])
        self.baseurl = self.jaccountinfo.gets(["service_endpoint"])
        self.scopelist = self.jaccountinfo.gets(["scopelist"])
        GoogleBaseRESTAPI.__init__(
            self,
            baseurl=self.baseurl,
            scopelist=self.scopelist,
            callrateperhour=700,
            geometric_delay_multiplier=2,
            maximum_geometric_delay_multiplications=5,
            maximum_failed_attempts=1,
        )


# GOOGLE AUTH CREDNETIAL FILE NOTES
# SPECIFICALLY DV360

### 360servicecreds.json Content

# You can generate this service account json file by going to https://console.developers.google.com/iam-admin/iam/ .
# It will contain your private key credentials.  Once you have followed the link, select your project, select
# "service accounts" and then create a new one.   I would select the role as "viewer".


#    {
#      "type": "service_account",
#      "project_id": <your project id>,
#      "private_key_id": <your private key id> ,
#      "private_key": <your private key> ,
#      "client_email": <your client email> ,
#      "client_id": <your client id> ,
#      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#      "token_uri": "https://oauth2.googleapis.com/token",
#      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#      "client_x509_cert_url": <your client_x509_cert_url >
#    }

### 360accountinfo.json Content

# You'll need to create this file yourself with your account details for your particular
# google api.  For the DV360 API we need the keys advertiser_id, partner_id, and
# service_endpoint.

#    {
#        "advertiser_id": <your advertisers id>,
#        "partner_id": <your partner id>,
#        "service_endpoint": "https://displayvideo.googleapis.com/v1/",
#        "scopelist" : [ "https://www.googleapis.com/auth/display-video", "https://www.googleapis.com/auth/doubleclickbidmanager"]
#    }

# DV360 API Reference

# https://developers.google.com/display-video/api/reference/rest
