from __future__ import annotations
import enum

from ..dv360api.advertisers import Advertisers
from ..common.dv360exceptions import *

from dataclasses import dataclass, field

import json

# https://developers.google.com/display-video/api/reference/rest/v1/advertisers


class AdvertiserManager:
    def __init__(self):
        self.advertiserapi = Advertisers()

    def list_advertisers(self):
        list_of_advertisers = []
        response = self.advertiserapi.list_advertisers()
        if response:
            content = json.loads(response.content.decode("utf-8"))
            advertiser_data = list(content["advertisers"])
            # if "advertisers" in content:
            #    print("TRUEEEE")
            # else:
            #    print("FALSE")
            for advertiser in advertiser_data:
                newadvertiser = Advertiser()
                newadvertiser.attributes = AdvertiserAttributes(**dict(advertiser))
                newadvertiser.audit = self.get_advertiser_audit(
                    newadvertiser.attributes.advertiserId
                )
                list_of_advertisers.append(newadvertiser)
        else:
            raise ErrorAdvertisersNotFound()
        return list_of_advertisers

    def get_advertiser(self, advertiserId):
        response = self.advertiserapi.get_advertiser(advertiserId)
        newadvertiser = Advertiser()
        if response:
            content = json.loads(response.content.decode("utf-8"))
            newadvertiser.attributes = AdvertiserAttributes(**dict(content))
            newadvertiser.audit = self.get_advertiser_audit(advertiserId)
        else:
            raise ErrorAdvertisersNotFound()
        return newadvertiser

    def get_advertiser_audit(self, advertiserId):
        response = self.advertiserapi.audit_advertiser(advertiserId)
        if response:
            content = json.loads(response.content.decode("utf-8"))
            advertiserauditattributes = AdvertiserAuditAttributes(**dict(content))
            return advertiserauditattributes
        else:
            raise ErrorAdvertisersAuditNotFound()


class Advertiser:
    def __init__(self):
        self.attributes = AdvertiserAttributes()
        self.audit = AdvertiserAuditAttributes()


@dataclass
class AdvertiserAttributes:
    name: str = None
    advertiserId: str = None
    partnerId: str = None
    displayName: str = None
    entityStatus: str = None
    updateTime: str = None
    generalConfig: object = None
    adServerConfig: object = None
    creativeConfig: object = None
    dataAccessConfig: object = None
    integrationDetails: object = None
    servingConfig: object = None
    prismaEnabled: bool = None


@dataclass
class AdvertiserAuditAttributes:
    usedLineItemsCount: str = None
    usedInsertionOrdersCount: str = None
    usedCampaignsCount: str = None
    channelsCount: str = None
    negativelyTargetedChannelsCount: str = None
    negativeKeywordListsCount: str = None
    adGroupCriteriaCount: str = None
    campaignCriteriaCount: str = None


##generalConfig
# @dataclass
# class GeneralConfigAttributes:
#     domainUrl: str = None
#     timeZone: str = None
#     currencyCode: str = None


# class GeneralConfig:
#     def __init__(self):
#         self.attributes = GeneralConfigAttributes()


# ##adServerConfig
# @dataclass
# class ThirdPartyOnlyConfigAttributes:
#     pixelOrderIdReportingEnabled: bool = None


# class ThirdPartyOnlyConfig:
#     def __init__(self):
#         self.attributes = ThirdPartyOnlyConfigAttributes()


# class CmHybridConfigAttributes:
#     cmAccountId: str = None
#     cmFloodlightConfigId: str = None
#     cmSyncableSiteIds: list = field(default_factory=list)
#     dv360ToCmDataSharingEnabled: bool = None
#     dv360ToCmCostReportingEnabled: bool = None
#     cmFloodlightLinkingAuthorized: bool = None


# class CmHybridConfig:
#     def __init__(self):
#         self.attributes = CmHybridConfigAttributes()


# class AdserverConfig:
#     def __init__(self):
#         self.thirdpartyonlyconfig = ThirdPartyOnlyConfig()
#         self.CmHybridConfig = CmHybridConfig()


# ##creativeConfig
# @dataclass
# class CreativeConfigAttributes:
#     iasClientId: str = None
#     obaComplianceDisabled: bool = None
#     dynamicCreativeEnabled: bool = None
#     videoCreativeDataSharingAuthorized: bool = None


# class CreativeConfig:
#     def __init__(self):
#         self.attributes = CreativeConfigAttributes()


# ##dataAccessConfig


# @dataclass
# class DataAccessConfigAttributes:
#     sdfConfig: object = None


# class DataAccessConfig:
#     def __init__(self):
#         self.attributes = DataAccessConfigAttributes()


# # integrationDetails
# @dataclass
# class IntegrationDetailsAttributes:
#     integrationCode: str = None
#     details: str = None


# class IntegrationDetails:
#     def __init__(self):
#         self.attributes = IntegrationDetailsAttributes()
