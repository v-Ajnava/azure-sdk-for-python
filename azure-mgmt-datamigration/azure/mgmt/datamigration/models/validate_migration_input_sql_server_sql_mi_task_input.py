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


class ValidateMigrationInputSqlServerSqlMITaskInput(Model):
    """Input for task that validates migration input for SQL to Azure SQL Managed
    Instance.

    All required parameters must be populated in order to send to Azure.

    :param target_connection_info: Required. Information for connecting to
     target
    :type target_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param selected_databases: Required. Databases to migrate
    :type selected_databases:
     list[~azure.mgmt.datamigration.models.MigrateSqlServerSqlMIDatabaseInput]
    :param backup_file_share: Backup file share information for all selected
     databases.
    :type backup_file_share: ~azure.mgmt.datamigration.models.FileShare
    :param backup_blob_share: Required. SAS URI of Azure Storage Account
     Container to be used for storing backup files.
    :type backup_blob_share: ~azure.mgmt.datamigration.models.BlobShare
    """

    _validation = {
        'target_connection_info': {'required': True},
        'selected_databases': {'required': True},
        'backup_blob_share': {'required': True},
    }

    _attribute_map = {
        'target_connection_info': {'key': 'targetConnectionInfo', 'type': 'SqlConnectionInfo'},
        'selected_databases': {'key': 'selectedDatabases', 'type': '[MigrateSqlServerSqlMIDatabaseInput]'},
        'backup_file_share': {'key': 'backupFileShare', 'type': 'FileShare'},
        'backup_blob_share': {'key': 'backupBlobShare', 'type': 'BlobShare'},
    }

    def __init__(self, **kwargs):
        super(ValidateMigrationInputSqlServerSqlMITaskInput, self).__init__(**kwargs)
        self.target_connection_info = kwargs.get('target_connection_info', None)
        self.selected_databases = kwargs.get('selected_databases', None)
        self.backup_file_share = kwargs.get('backup_file_share', None)
        self.backup_blob_share = kwargs.get('backup_blob_share', None)
