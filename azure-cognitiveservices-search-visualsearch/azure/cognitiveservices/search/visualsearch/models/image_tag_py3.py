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

from .thing import Thing


class ImageTag(Thing):
    """ImageTag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource. To use the URL,
     append query parameters as appropriate and include the
     Ocp-Apim-Subscription-Key header.
    :vartype read_link: str
    :ivar web_search_url: The URL to Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by
     this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image:
     ~azure.cognitiveservices.search.visualsearch.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item.
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar display_name: Display name for this tag. For the default tag, the
     display name is empty.
    :vartype display_name: str
    :ivar bounding_box: The bounding box for this tag. For the default tag,
     there is no bounding box.
    :vartype bounding_box:
     ~azure.cognitiveservices.search.visualsearch.models.ImageTagRegion
    :ivar actions: Actions within this tag. The order of the items denotes the
     default ranking order of these actions, with the first action being the
     most likely user intent.
    :vartype actions:
     list[~azure.cognitiveservices.search.visualsearch.models.ImageAction]
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'display_name': {'readonly': True},
        'bounding_box': {'readonly': True},
        'actions': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'bounding_box': {'key': 'boundingBox', 'type': 'ImageTagRegion'},
        'actions': {'key': 'actions', 'type': '[ImageAction]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ImageTag, self).__init__(**kwargs)
        self.display_name = None
        self.bounding_box = None
        self.actions = None
        self._type = 'ImageTag'
