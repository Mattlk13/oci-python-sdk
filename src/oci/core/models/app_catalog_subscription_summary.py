# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppCatalogSubscriptionSummary(object):
    """
    a subscription summary for a listing resource version.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppCatalogSubscriptionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param publisher_name:
            The value to assign to the publisher_name property of this AppCatalogSubscriptionSummary.
        :type publisher_name: str

        :param listing_id:
            The value to assign to the listing_id property of this AppCatalogSubscriptionSummary.
        :type listing_id: str

        :param listing_resource_version:
            The value to assign to the listing_resource_version property of this AppCatalogSubscriptionSummary.
        :type listing_resource_version: str

        :param listing_resource_id:
            The value to assign to the listing_resource_id property of this AppCatalogSubscriptionSummary.
        :type listing_resource_id: str

        :param display_name:
            The value to assign to the display_name property of this AppCatalogSubscriptionSummary.
        :type display_name: str

        :param summary:
            The value to assign to the summary property of this AppCatalogSubscriptionSummary.
        :type summary: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AppCatalogSubscriptionSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this AppCatalogSubscriptionSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'publisher_name': 'str',
            'listing_id': 'str',
            'listing_resource_version': 'str',
            'listing_resource_id': 'str',
            'display_name': 'str',
            'summary': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'publisher_name': 'publisherName',
            'listing_id': 'listingId',
            'listing_resource_version': 'listingResourceVersion',
            'listing_resource_id': 'listingResourceId',
            'display_name': 'displayName',
            'summary': 'summary',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated'
        }

        self._publisher_name = None
        self._listing_id = None
        self._listing_resource_version = None
        self._listing_resource_id = None
        self._display_name = None
        self._summary = None
        self._compartment_id = None
        self._time_created = None

    @property
    def publisher_name(self):
        """
        Gets the publisher_name of this AppCatalogSubscriptionSummary.
        Name of the publisher who published this listing.


        :return: The publisher_name of this AppCatalogSubscriptionSummary.
        :rtype: str
        """
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, publisher_name):
        """
        Sets the publisher_name of this AppCatalogSubscriptionSummary.
        Name of the publisher who published this listing.


        :param publisher_name: The publisher_name of this AppCatalogSubscriptionSummary.
        :type: str
        """
        self._publisher_name = publisher_name

    @property
    def listing_id(self):
        """
        Gets the listing_id of this AppCatalogSubscriptionSummary.
        The ocid of the listing resource.


        :return: The listing_id of this AppCatalogSubscriptionSummary.
        :rtype: str
        """
        return self._listing_id

    @listing_id.setter
    def listing_id(self, listing_id):
        """
        Sets the listing_id of this AppCatalogSubscriptionSummary.
        The ocid of the listing resource.


        :param listing_id: The listing_id of this AppCatalogSubscriptionSummary.
        :type: str
        """
        self._listing_id = listing_id

    @property
    def listing_resource_version(self):
        """
        Gets the listing_resource_version of this AppCatalogSubscriptionSummary.
        Listing resource version.


        :return: The listing_resource_version of this AppCatalogSubscriptionSummary.
        :rtype: str
        """
        return self._listing_resource_version

    @listing_resource_version.setter
    def listing_resource_version(self, listing_resource_version):
        """
        Sets the listing_resource_version of this AppCatalogSubscriptionSummary.
        Listing resource version.


        :param listing_resource_version: The listing_resource_version of this AppCatalogSubscriptionSummary.
        :type: str
        """
        self._listing_resource_version = listing_resource_version

    @property
    def listing_resource_id(self):
        """
        Gets the listing_resource_id of this AppCatalogSubscriptionSummary.
        Listing resource id.


        :return: The listing_resource_id of this AppCatalogSubscriptionSummary.
        :rtype: str
        """
        return self._listing_resource_id

    @listing_resource_id.setter
    def listing_resource_id(self, listing_resource_id):
        """
        Sets the listing_resource_id of this AppCatalogSubscriptionSummary.
        Listing resource id.


        :param listing_resource_id: The listing_resource_id of this AppCatalogSubscriptionSummary.
        :type: str
        """
        self._listing_resource_id = listing_resource_id

    @property
    def display_name(self):
        """
        Gets the display_name of this AppCatalogSubscriptionSummary.
        The display name of the listing.


        :return: The display_name of this AppCatalogSubscriptionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AppCatalogSubscriptionSummary.
        The display name of the listing.


        :param display_name: The display_name of this AppCatalogSubscriptionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def summary(self):
        """
        Gets the summary of this AppCatalogSubscriptionSummary.
        The short summary to the listing.


        :return: The summary of this AppCatalogSubscriptionSummary.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this AppCatalogSubscriptionSummary.
        The short summary to the listing.


        :param summary: The summary of this AppCatalogSubscriptionSummary.
        :type: str
        """
        self._summary = summary

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this AppCatalogSubscriptionSummary.
        The compartmentID of the subscription.


        :return: The compartment_id of this AppCatalogSubscriptionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AppCatalogSubscriptionSummary.
        The compartmentID of the subscription.


        :param compartment_id: The compartment_id of this AppCatalogSubscriptionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this AppCatalogSubscriptionSummary.
        Date and time at which the subscription was created, in RFC3339 format.
        Example: `2018-03-20T12:32:53.532Z`


        :return: The time_created of this AppCatalogSubscriptionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AppCatalogSubscriptionSummary.
        Date and time at which the subscription was created, in RFC3339 format.
        Example: `2018-03-20T12:32:53.532Z`


        :param time_created: The time_created of this AppCatalogSubscriptionSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other