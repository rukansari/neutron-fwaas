# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2012 OpenStack Foundation.
# All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from quantum.api import extensions
from quantum.api.v2 import attributes


# The service will return the vif type for the specific port.
VIF_TYPE = 'binding:vif_type'
# In some cases different implementations may be run on different hosts.
# The host on which the port will be allocated.
HOST_ID = 'binding:host_id'
# The profile will be a dictionary that enables the application running
# on the specific host to pass and receive vif port specific information to
# the plugin.
PROFILE = 'binding:profile'
# The capabilities will be a dictionary that enables pass information about
# functionalies quantum provides. The following value should be provided.
#  - port_filter : Boolean value indicating Quantum provides port filtering
#                  features such as security group and anti MAC/IP spoofing
CAPABILITIES = 'binding:capabilities'
CAP_PORT_FILTER = 'port_filter'

VIF_TYPE_UNBOUND = 'unbound'
VIF_TYPE_BINDING_FAILED = 'binding_failed'
VIF_TYPE_OVS = 'ovs'
VIF_TYPE_IVS = 'ivs'
VIF_TYPE_BRIDGE = 'bridge'
VIF_TYPE_802_QBG = '802.1qbg'
VIF_TYPE_802_QBH = '802.1qbh'
VIF_TYPE_HYPERV = 'hyperv'
VIF_TYPE_OTHER = 'other'

EXTENDED_ATTRIBUTES_2_0 = {
    'ports': {
        VIF_TYPE: {'allow_post': False, 'allow_put': False,
                   'default': attributes.ATTR_NOT_SPECIFIED,
                   'enforce_policy': True,
                   'is_visible': True},
        HOST_ID: {'allow_post': True, 'allow_put': True,
                  'default': attributes.ATTR_NOT_SPECIFIED,
                  'is_visible': True,
                  'enforce_policy': True},
        PROFILE: {'allow_post': True, 'allow_put': True,
                  'default': attributes.ATTR_NOT_SPECIFIED,
                  'enforce_policy': True,
                  'validate': {'type:dict': None},
                  'is_visible': True},
        CAPABILITIES: {'allow_post': False, 'allow_put': False,
                       'default': attributes.ATTR_NOT_SPECIFIED,
                       'enforce_policy': True,
                       'is_visible': True},
    }
}


class Portbindings(extensions.ExtensionDescriptor):
    """Extension class supporting port bindings.

    This class is used by quantum's extension framework to make
    metadata about the port bindings available to external applications.

    With admin rights one will be able to update and read the values.
    """

    @classmethod
    def get_name(cls):
        return "Port Binding"

    @classmethod
    def get_alias(cls):
        return "binding"

    @classmethod
    def get_description(cls):
        return "Expose port bindings of a virtual port to external application"

    @classmethod
    def get_namespace(cls):
        return "http://docs.openstack.org/ext/binding/api/v1.0"

    @classmethod
    def get_updated(cls):
        return "2012-11-14T10:00:00-00:00"

    def get_extended_resources(self, version):
        if version == "2.0":
            return EXTENDED_ATTRIBUTES_2_0
        else:
            return {}