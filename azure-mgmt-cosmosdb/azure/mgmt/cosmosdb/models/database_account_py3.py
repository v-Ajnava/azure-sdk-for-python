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

from .resource import Resource


class DatabaseAccount(Resource):
    """An Azure Cosmos DB database account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The unique resource identifier of the database account.
    :vartype id: str
    :ivar name: The name of the database account.
    :vartype name: str
    :ivar type: The type of Azure resource.
    :vartype type: str
    :param location: Required. The location of the resource group to which the
     resource belongs.
    :type location: str
    :param tags:
    :type tags: dict[str, str]
    :param kind: Indicates the type of database account. This can only be set
     at database account creation. Possible values include: 'GlobalDocumentDB',
     'MongoDB', 'Parse'. Default value: "GlobalDocumentDB" .
    :type kind: str or ~azure.mgmt.cosmosdb.models.DatabaseAccountKind
    :param provisioning_state:
    :type provisioning_state: str
    :ivar document_endpoint: The connection endpoint for the Cosmos DB
     database account.
    :vartype document_endpoint: str
    :ivar database_account_offer_type: The offer type for the Cosmos DB
     database account. Default value: Standard. Possible values include:
     'Standard'
    :vartype database_account_offer_type: str or
     ~azure.mgmt.cosmosdb.models.DatabaseAccountOfferType
    :param ip_range_filter: Cosmos DB Firewall Support: This value specifies
     the set of IP addresses or IP address ranges in CIDR form to be included
     as the allowed list of client IPs for a given database account. IP
     addresses/ranges must be comma separated and must not contain any spaces.
    :type ip_range_filter: str
    :param is_virtual_network_filter_enabled: Flag to indicate whether to
     enable/disable Virtual Network ACL rules.
    :type is_virtual_network_filter_enabled: bool
    :param enable_automatic_failover: Enables automatic failover of the write
     region in the rare event that the region is unavailable due to an outage.
     Automatic failover will result in a new write region for the account and
     is chosen based on the failover priorities configured for the account.
    :type enable_automatic_failover: bool
    :param consistency_policy: The consistency policy for the Cosmos DB
     database account.
    :type consistency_policy: ~azure.mgmt.cosmosdb.models.ConsistencyPolicy
    :param capabilities: List of Cosmos DB capabilities for the account
    :type capabilities: list[~azure.mgmt.cosmosdb.models.Capability]
    :ivar write_locations: An array that contains the write location for the
     Cosmos DB account.
    :vartype write_locations: list[~azure.mgmt.cosmosdb.models.Location]
    :ivar read_locations: An array that contains of the read locations enabled
     for the Cosmos DB account.
    :vartype read_locations: list[~azure.mgmt.cosmosdb.models.Location]
    :ivar failover_policies: An array that contains the regions ordered by
     their failover priorities.
    :vartype failover_policies:
     list[~azure.mgmt.cosmosdb.models.FailoverPolicy]
    :param virtual_network_rules: List of Virtual Network ACL rules configured
     for the Cosmos DB account.
    :type virtual_network_rules:
     list[~azure.mgmt.cosmosdb.models.VirtualNetworkRule]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'document_endpoint': {'readonly': True},
        'database_account_offer_type': {'readonly': True},
        'write_locations': {'readonly': True},
        'read_locations': {'readonly': True},
        'failover_policies': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'kind': {'key': 'kind', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'document_endpoint': {'key': 'properties.documentEndpoint', 'type': 'str'},
        'database_account_offer_type': {'key': 'properties.databaseAccountOfferType', 'type': 'DatabaseAccountOfferType'},
        'ip_range_filter': {'key': 'properties.ipRangeFilter', 'type': 'str'},
        'is_virtual_network_filter_enabled': {'key': 'properties.isVirtualNetworkFilterEnabled', 'type': 'bool'},
        'enable_automatic_failover': {'key': 'properties.enableAutomaticFailover', 'type': 'bool'},
        'consistency_policy': {'key': 'properties.consistencyPolicy', 'type': 'ConsistencyPolicy'},
        'capabilities': {'key': 'properties.capabilities', 'type': '[Capability]'},
        'write_locations': {'key': 'properties.writeLocations', 'type': '[Location]'},
        'read_locations': {'key': 'properties.readLocations', 'type': '[Location]'},
        'failover_policies': {'key': 'properties.failoverPolicies', 'type': '[FailoverPolicy]'},
        'virtual_network_rules': {'key': 'properties.virtualNetworkRules', 'type': '[VirtualNetworkRule]'},
    }

    def __init__(self, *, location: str, tags=None, kind="GlobalDocumentDB", provisioning_state: str=None, ip_range_filter: str=None, is_virtual_network_filter_enabled: bool=None, enable_automatic_failover: bool=None, consistency_policy=None, capabilities=None, virtual_network_rules=None, **kwargs) -> None:
        super(DatabaseAccount, self).__init__(location=location, tags=tags, **kwargs)
        self.kind = kind
        self.provisioning_state = provisioning_state
        self.document_endpoint = None
        self.database_account_offer_type = None
        self.ip_range_filter = ip_range_filter
        self.is_virtual_network_filter_enabled = is_virtual_network_filter_enabled
        self.enable_automatic_failover = enable_automatic_failover
        self.consistency_policy = consistency_policy
        self.capabilities = capabilities
        self.write_locations = None
        self.read_locations = None
        self.failover_policies = None
        self.virtual_network_rules = virtual_network_rules
