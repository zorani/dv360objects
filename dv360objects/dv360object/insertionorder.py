from __future__ import annotations
import enum

from ..dv360api.insertionorders import InsertionOrders
from ..common.dv360exceptions import *
from ..common.utils import Utils

from dataclasses import dataclass, field

import json

# https://developers.google.com/display-video/api/reference/rest/v1/advertisers.insertionOrders/


class InsertionOrderManager:
    def __init__(self):
        self.insertionorderapi = InsertionOrders()
        self.utils = Utils()

    #'nextPageToken'

    def list_all_insertionorders(self, advertiserId=None):
        # If the user does not supply an advertiserId the api call will revert to the
        # advertiserId in the config file.

        # First we build a list of insertion orders from the api, take in to account possible pagination.

        list_of_insertionsorders = []
        pageSize = 100
        response = self.insertionorderapi.list_insertionorders(
            advertiserId, pageSize=pageSize
        )
        content = json.loads(response.content.decode("utf-8"))
        list_of_insertionsorders.extend(content["insertionOrders"])

        try:
            while content["nextPageToken"]:
                token = content["nextPageToken"]
                response = self.insertionorderapi.list_insertionorders(
                    advertiserId, pageSize=pageSize, pageToken=token
                )
                content = json.loads(response.content.decode("utf-8"))
                list_of_insertionsorders.extend(content["insertionOrders"])
        except KeyError:
            pass

        deduped_list_of_insertionorders_objects = self.utils.deduplication_object_list(
            object_list=list_of_insertionsorders, object_dedupe_key="insertionOrderId"
        )

        # Now we build that insertion orders object list.
        list_of_insertionorders_objects = []
        for insertionorder in deduped_list_of_insertionorders_objects:
            newinsertionorder = InsertionOrder()
            newinsertionorder.attributes = InsertionOrderAttributes(
                **dict(insertionorder)
            )
            list_of_insertionorders_objects.append(newinsertionorder)

        return list_of_insertionorders_objects

    def get_insertionorder(self, advertiserId, insertionOrderId, **kwargs):
        response = self.insertionorderapi.get_insertionorder(
            advertiserId, insertionOrderId, **kwargs
        )
        newinsertionorder = InsertionOrder()
        if response:
            content = json.loads(response.content.decode("utf-8"))
            newinsertionorder.attributes = InsertionOrderAttributes(**dict(content))
        else:
            raise ErrorInsertionOrdersNotFound()
        return newinsertionorder


class InsertionOrder:
    def __init__(self):
        self.attributes = InsertionOrderAttributes()


@dataclass
class InsertionOrderAttributes:
    name: str = None
    advertiserId: str = None
    campaignId: str = None
    insertionOrderId: str = None
    displayName: str = None
    insertionOrderType: str = None
    entityStatus: str = None
    updateTime: str = None
    partnerCosts: object = None
    pacing: object = None
    frequencyCap: object = None
    integrationDetails: object = None
    performanceGoal: object = None
    budget: object = None
    bidStrategy: object = None
    reservationType: str = None
    billableOutcome: str = None
