from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext, AutoLoadResource, \
    AutoLoadAttribute, AutoLoadDetails, AutoLoadCommandContext


class {{cookiecutter.driver_name}} (ResourceDriverInterface):

    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
        """
        pass

    def initialize(self, context):
        """
        Initialize the driver session, this function is called everytime a new instance of the driver is created
        This is a good place to load and cache the driver configuration, initiate sessions etc.
        :param InitCommandContext context: the context the command runs on
        :type context: InitCommandContext
        :return:
        """
        pass
        
    # <editor-fold desc="Networking Standard Commands">
    def restore(self, context, cancellation_context, path, restore_method, configuration_type, vrf_management_name):
        """
        Restores a configuration file
        :param ResourceCommandContext context: The context object for the command with resource and reservation info
        :type context: ResourceCommandContext
        :param CancellationContext cancellation_context: Object to signal a request for cancellation. Must be enabled in drivermetadata.xml as well
        :type cancellation_context: CancellationContext
        :param str path: The path to the configuration file, including the configuration file name.
        :type path: str
        :param str restore_method: Determines whether the restore should append or override the current configuration.
        :type restore_method: str
        :param str configuration_type: Specify whether the file should update the startup or running config.
        :type configuration_type: str
        :param str vrf_management_name: Optional. Virtual routing and Forwarding management name
        :type vrf_management_name: str
        """
        pass

    def save(self, context, cancellation_context, configuration_type, folder_path, vrf_management_name):
        """
        Creates a configuration file and saves it to the provided destination
        :param ResourceCommandContext context: The context object for the command with resource and reservation info
        :type context: ResourceCommandContext
        :param CancellationContext cancellation_context: Object to signal a request for cancellation. Must be enabled in drivermetadata.xml as well
        :type cancellation_context: CancellationContext
        :param str configuration_type: Specify whether the file should update the startup or running config. Value can one
        :type configuration_type: str
        :param str folder_path: The path to the folder in which the configuration file will be saved.
        :type folder_path: str 
        :param str vrf_management_name: Optional. Virtual routing and Forwarding management name
        :type vrf_management_name: str
        :return The configuration file name.
        :rtype: str
        """
        pass

    def load_firmware(self, context, cancellation_context, file_path, remote_host):
        """
        Upload and updates firmware on the resource
        :param ResourceCommandContext context: The context object for the command with resource and reservation info
        :type context: ResourceCommandContext
        :type cancellation_context: CancellationContext
        :param str file_path: firmware file name
        :type file_path: str
        :param str remote_host: path to tftp server where firmware file is stored
        :type remote_host: str
        """
        pass

    def run_custom_command(self, context, cancellation_context, custom_command):
        """
        Executes a custom command on the device
        :param ResourceCommandContext context: The context object for the command with resource and reservation info
        :type context: ResourceCommandContext
        :param CancellationContext cancellation_context: Object to signal a request for cancellation. Must be enabled in drivermetadata.xml as well
        :type cancellation_context: CancellationContext
        :param str custom_command: The command to run. Note that commands that require a response are not supported.
        :type custom_command: str
        :return: the command result text
        :rtype: str
        """
        pass

    def run_custom_config_command(self, context, cancellation_context, custom_command):
        """
        Executes a custom command on the device in configuration mode
        :param ResourceCommandContext context: The context object for the command with resource and reservation info
        :type context: ResourceCommandContext
        :param CancellationContext cancellation_context: Object to signal a request for cancellation. Must be enabled in drivermetadata.xml as well
        :type cancellation_context: CancellationContext
        :param str custom_command: The command to run. Note that commands that require a response are not supported.
        :type custom_command: str
        :return: the command result text
        :rtype: str
        """
        pass

    def shutdown(self, context, cancellation_context):
        """
        Sends a graceful shutdown to the device
        :param ResourceCommandContext context: The context object for the command with resource and reservation info
        :type context: ResourceCommandContext
        :param CancellationContext cancellation_context: Object to signal a request for cancellation. Must be enabled in drivermetadata.xml as well
        :type cancellation_context: CancellationContext
        """
        pass

    # </editor-fold>
    
    # <editor-fold desc="Orchestration Save and Restore Standard">
    def orchestration_save(self, context, cancellation_context, mode, custom_params=None):
        """
        Saves the Shell state and returns a description of the saved artifacts and information
        This command is intended for API use only by sandbox orchestration scripts to implement
        a save and restore workflow
        :param ResourceCommandContext context: the context object containing resource and reservation info
        :type context: ResourceCommandContext
        :param CancellationContext cancellation_context: Object to signal a request for cancellation. Must be enabled in drivermetadata.xml as well
        :type cancellation_context: CancellationContext
        :param str mode: Snapshot save mode, can be one of two values 'shallow' (default) or 'deep'
        :type mode: str
        :param str custom_params: Set of custom parameters for the save operation
        :type custom_params: str
        :return: SavedResults serialized as JSON
        :rtype: OrchestrationSaveResult
        """

        # See below an example implementation, here we use jsonpickle for serialization,
        # to use this sample, you'll need to add jsonpickle to your requirements.txt file
        # The JSON schema is defined at: https://github.com/QualiSystems/sandbox_orchestration_standard/blob/master/save%20%26%20restore/saved_artifact_info.schema.json
        # You can find more information and examples examples in the spec document at https://github.com/QualiSystems/sandbox_orchestration_standard/blob/master/save%20%26%20restore/save%20%26%20restore%20standard.md
        '''
        # By convention, all dates should be UTC
        created_date = datetime.datetime.utcnow()
        nxos = AUTOMAPPER_converter.convert(context)
        nxos.model = 'aa'
        # This can be any unique identifier which can later be used to retrieve the artifact
        # such as filepath etc.

        # By convention, all dates should be UTC
        created_date = datetime.datetime.utcnow()

        # This can be any unique identifier which can later be used to retrieve the artifact
        # such as filepath etc.
        identifier = created_date.strftime('%y_%m_%d %H_%M_%S_%f')

        orchestration_saved_artifact = OrchestrationSavedArtifact('REPLACE_WITH_ARTIFACT_TYPE', identifier)

        saved_artifacts_info = OrchestrationSavedArtifactInfo(
            resource_name="some_resource",
            created_date=created_date,
            restore_rules=OrchestrationRestoreRules(requires_same_resource=True),
            saved_artifact=orchestration_saved_artifact)

        return OrchestrationSaveResult(saved_artifacts_info)
        '''
        pass

    def orchestration_restore(self, context, cancellation_context, saved_details):
        """
        Restores a saved artifact previously saved by this Shell driver using the orchestration_save function
        :param ResourceCommandContext context: The context object for the command with resource and reservation info
        :type context: ResourceCommandContext
        :param CancellationContext cancellation_context: Object to signal a request for cancellation. Must be enabled in drivermetadata.xml as well
        :type cancellation_context: CancellationContext
        :param str saved_details: A JSON string representing the state to restore including saved artifacts and info
        :type saved_details: str
        :return: None
        """
        '''
        # The saved_details JSON will be defined according to the JSON Schema and is the same object returned via the
        # orchestration save function.
        # Example input:
        # {
        #     "saved_artifact": {
        #      "artifact_type": "REPLACE_WITH_ARTIFACT_TYPE",
        #      "identifier": "16_08_09 11_21_35_657000"
        #     },
        #     "resource_name": "some_resource",
        #     "restore_rules": {
        #      "requires_same_resource": true
        #     },
        #     "created_date": "2016-08-09T11:21:35.657000"
        #    }

        # The example code below just parses and prints the saved artifact identifier
        saved_details_object = json.loads(saved_details)
        return saved_details_object[u'saved_artifact'][u'identifier']
        '''
        pass

    # </editor-fold>

    # <editor-fold desc="Connectivity Provider Interface (Optional)">

    '''
    # The ApplyConnectivityChanges function is intended to be used for using switches as connectivity providers
    # for other devices. If the Switch shell is intended to be used a DUT only there is no need to implement it

    def ApplyConnectivityChanges(self, context, request):
        """
        Configures VLANs on multiple ports or port-channels
        :param ResourceCommandContext context: The context object for the command with resource and reservation info
        :param str request: A JSON object with the list of requested connectivity changes
        :return: a json object with the list of connectivity changes which were carried out by the switch
        :rtype: str
        """

        pass

    '''

    # </editor-fold>

    # <editor-fold desc="Discovery">
    def get_inventory(self, context):
        """
        Queries the device and returns a list of sub-resources and attribute values to CloudShell
        :type context: AutoLoadCommandContext
        :rtype AutoLoadDetails
        """
        # run 'shellfoundry generate' in order to create classes that represent your data model
        resource = {{cookiecutter.model_name}}.create_from_context(context)
        resource.name = 'fill the name'

        # Add sub resources if needed
        # resource.add_sub_resource('1', sub resource)

        return resource.create_autoload_details()
    
    # </editor-fold>

    # <editor-fold desc="Health Check">

    def health_check(self,cancellation_context):
        """
        Checks if the device is up and connectable
        :type context: ResourceCommandContext
        :return: None
        :exception Exception: Raises an error if cannot connect
        """
        # run 'shellfoundry generate' in order to create classes that represent your data model
        resource = {{cookiecutter.model_name}}.create_from_context(context)
        pass

    # </editor-fold>

