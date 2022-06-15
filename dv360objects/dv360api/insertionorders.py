from .dv360apiconnection import DV360APIConnection


class InsertionOrders(DV360APIConnection):
    def __init__(self):
        DV360APIConnection.__init__(self)
        self.endpoint = "v1/advertisers"

    def list_insertionorders(self, advertiserId, **kwargs):
        # If a user hasn't passed in an advertiserId, they are probably expecting
        # to list insertionorders for their own advertiserId in the settings file.
        # We set that here.
        if advertiserId == None:
            advertiserId = self.advertiser_id
        # pageSize=pageSize,nextPageToken=token
        # print(kwargs)
        params = {}
        if "pageSize" in kwargs:
            params["pageSize"] = kwargs["pageSize"]
        if "pageToken" in kwargs:
            params["pageToken"] = kwargs["pageToken"]
        # params = {"pageSize": pageSize}
        # print(params)
        path = f"{self.endpoint}/{advertiserId}/insertionOrders"
        return self.get_request(path, params=params)

    def get_insertionorder(self, advertiserId, insertionOrderid, **kwargs):
        path = f"{self.endpoint}/{advertiserId}/insertionOrders/{insertionOrderid}"
        return self.get_request(path, **kwargs)
