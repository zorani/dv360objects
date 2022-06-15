from .dv360apiconnection import DV360APIConnection


class LineItems(DV360APIConnection):
    def __init__(self):
        DV360APIConnection.__init__(self)
        self.endpoint = "v1/advertisers"

    def list_lineitems(self, advertiserId, **kwargs):
        # If a user hasn't passed in an advertiserId, they are probably expecting
        # to list insertionorders for their own advertiserId in the settings file.
        # We set that here.

        if advertiserId == None:
            advertiserId = self.advertiser_id

        params = {}
        if "pageSize" in kwargs:
            params["pageSize"] = kwargs["pageSize"]
        if "pageToken" in kwargs:
            params["pageToken"] = kwargs["pageToken"]

        path = f"{self.endpoint}/{advertiserId}/lineItems"
        return self.get_request(path, params=params)

    def get_lineitem(self, advertiserId, lineItemId, **kwargs):
        path = f"{self.endpoint}/{advertiserId}/lineItems/{lineItemId}"
        return self.get_request(path, **kwargs)
