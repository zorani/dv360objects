from __future__ import annotations
import enum

from ..dv360api.lineitems import LineItems
from ..common.dv360exceptions import *
from ..common.utils import Utils

from dataclasses import dataclass, field

import json


class LineItemManager:
    def __init__(self):
        self.lineitemapi = LineItems()
        self.utils = Utils()

    def list_all_lineitems(self, advertiserId=None):
        # If the user does not supply an advertiserId the api call will revert to the
        # advertiserId in the config file.

        # First we build a list of line items from the api, take in to account possible pagination.

        list_of_lineitems = []
        pageSize = 100
        response = self.lineitemapi.list_lineitems(advertiserId, pageSize=pageSize)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            list_of_lineitems.extend(content["lineItems"])
        else:
            raise ErrorLineItemsNotFound()
        # print(content)
        try:
            while content["nextPageToken"]:
                token = content["nextPageToken"]
                response = self.insertionorderapi.list_insertionorders(
                    advertiserId, pageSize=pageSize, pageToken=token
                )
                if response:
                    content = json.loads(response.content.decode("utf-8"))
                    list_of_lineitems.extend(content["lineItems"])
                else:
                    raise ErrorLineItemsNotFound()
        except KeyError:
            pass

        deduped_list_of_lineitems = self.utils.deduplication_object_list(
            object_list=list_of_lineitems, object_dedupe_key="lineItemId"
        )

        # Now we build that insertion orders object list.
        list_of_lineitme_objects = []
        for lineitem in deduped_list_of_lineitems:
            newlineitem = LineItem()
            newlineitem.attributes = LineItemAttributes(**dict(lineitem))
            list_of_lineitme_objects.append(newlineitem)

        return list_of_lineitme_objects

    def get_lineitem(self, advertiserId, lineItemId):
        response = self.lineitemapi.get_lineitem(
            advertiserId=advertiserId, lineItemId=lineItemId
        )
        if response:
            content = json.loads(response.content.decode("utf-8"))
            newlineitem = LineItem()
            newlineitem.attributes = LineItemAttributes(**dict(content))
            return newlineitem
        else:
            raise ErrorLineItemsNotFound()


#    def get_insertionorder(self, advertiserId, insertionOrderId, **kwargs):
#        response = self.insertionorderapi.get_insertionorder(
#            advertiserId, insertionOrderId, **kwargs
#        )
#        newinsertionorder = InsertionOrder()
#        if response:
#            content = json.loads(response.content.decode("utf-8"))
#            newinsertionorder.attributes = InsertionOrderAttributes(**dict(content))
#        else:
#            raise ErrorInsertionOrdersNotFound()
#        return newinsertionorder


class LineItem:
    def __init__(self):
        self.attributes = LineItemAttributes()


@dataclass
class LineItemAttributes:
    name: str = None
    advertiserId: str = None
    campaignId: str = None
    insertionOrderId: str = None
    lineItemId: str = None
    displayName: str = None
    lineItemType: str = None
    entityStatus: str = None
    updateTime: str = None
    partnerCosts: object = None
    flight: object = None
    budget: object = None
    pacing: object = None
    frequencyCap: object = None
    partnerRevenueModel: object = None
    conversionCounting: object = None
    creativeIds: list = field(default_factory=list)
    bidStrategy: object = None
    integrationDetails: object = None
    inventorySourceIds: list = field(default_factory=list)
    targetingExpansion: object = None
    warningMessages: list = field(default_factory=list)
    mobileApp: object = None
    reservationType: str = None
    excludeNewExchanges: bool = None
