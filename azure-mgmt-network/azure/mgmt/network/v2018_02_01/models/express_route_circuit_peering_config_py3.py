# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExpressRouteCircuitPeeringConfig(Model):
    """Specifies the peering configuration.

    :param advertised_public_prefixes: The reference of
     AdvertisedPublicPrefixes.
    :type advertised_public_prefixes: list[str]
    :param advertised_communities: The communities of bgp peering. Spepcified
     for microsoft peering
    :type advertised_communities: list[str]
    :param advertised_public_prefixes_state: AdvertisedPublicPrefixState of
     the Peering resource. Possible values are 'NotConfigured', 'Configuring',
     'Configured', and 'ValidationNeeded'. Possible values include:
     'NotConfigured', 'Configuring', 'Configured', 'ValidationNeeded'
    :type advertised_public_prefixes_state: str or
     ~azure.mgmt.network.v2018_02_01.models.ExpressRouteCircuitPeeringAdvertisedPublicPrefixState
    :param legacy_mode: The legacy mode of the peering.
    :type legacy_mode: int
    :param customer_asn: The CustomerASN of the peering.
    :type customer_asn: int
    :param routing_registry_name: The RoutingRegistryName of the
     configuration.
    :type routing_registry_name: str
    """

    _attribute_map = {
        'advertised_public_prefixes': {'key': 'advertisedPublicPrefixes', 'type': '[str]'},
        'advertised_communities': {'key': 'advertisedCommunities', 'type': '[str]'},
        'advertised_public_prefixes_state': {'key': 'advertisedPublicPrefixesState', 'type': 'str'},
        'legacy_mode': {'key': 'legacyMode', 'type': 'int'},
        'customer_asn': {'key': 'customerASN', 'type': 'int'},
        'routing_registry_name': {'key': 'routingRegistryName', 'type': 'str'},
    }

    def __init__(self, *, advertised_public_prefixes=None, advertised_communities=None, advertised_public_prefixes_state=None, legacy_mode: int=None, customer_asn: int=None, routing_registry_name: str=None, **kwargs) -> None:
        super(ExpressRouteCircuitPeeringConfig, self).__init__(**kwargs)
        self.advertised_public_prefixes = advertised_public_prefixes
        self.advertised_communities = advertised_communities
        self.advertised_public_prefixes_state = advertised_public_prefixes_state
        self.legacy_mode = legacy_mode
        self.customer_asn = customer_asn
        self.routing_registry_name = routing_registry_name
