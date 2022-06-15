from .dv360apiconnection import DV360APIConnection


class Advertisers(DV360APIConnection):
    def __init__(self):
        DV360APIConnection.__init__(self)
        self.endpoint = "v1/advertisers"

    def list_advertisers(self, **kwargs):
        path = f"{self.endpoint}"
        return self.get_request(path, params={"partnerId": self.partner_id}, **kwargs)

    def get_advertiser(self, advertiserId, **kwargs):
        path = f"{self.endpoint}/{advertiserId}"
        return self.get_request(path, **kwargs)

    def audit_advertiser(self, advertiserId, **kwargs):
        path = f"{self.endpoint}/{advertiserId}:audit"
        return self.get_request(path, **kwargs)
