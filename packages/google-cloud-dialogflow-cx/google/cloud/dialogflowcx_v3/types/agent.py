# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.dialogflowcx_v3.types import (
    advanced_settings as gcdc_advanced_settings,
)
from google.cloud.dialogflowcx_v3.types import flow
from google.protobuf import field_mask_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "SpeechToTextSettings",
        "Agent",
        "ListAgentsRequest",
        "ListAgentsResponse",
        "GetAgentRequest",
        "CreateAgentRequest",
        "UpdateAgentRequest",
        "DeleteAgentRequest",
        "ExportAgentRequest",
        "ExportAgentResponse",
        "RestoreAgentRequest",
        "ValidateAgentRequest",
        "GetAgentValidationResultRequest",
        "AgentValidationResult",
    },
)


class SpeechToTextSettings(proto.Message):
    r"""Settings related to speech recognition.

    Attributes:
        enable_speech_adaptation (bool):
            Whether to use speech adaptation for speech
            recognition.
    """

    enable_speech_adaptation: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class Agent(proto.Message):
    r"""Agents are best described as Natural Language Understanding (NLU)
    modules that transform user requests into actionable data. You can
    include agents in your app, product, or service to determine user
    intent and respond to the user in a natural way.

    After you create an agent, you can add
    [Intents][google.cloud.dialogflow.cx.v3.Intent], [Entity
    Types][google.cloud.dialogflow.cx.v3.EntityType],
    [Flows][google.cloud.dialogflow.cx.v3.Flow],
    [Fulfillments][google.cloud.dialogflow.cx.v3.Fulfillment],
    [Webhooks][google.cloud.dialogflow.cx.v3.Webhook], and so on to
    manage the conversation flows..

    Attributes:
        name (str):
            The unique identifier of the agent. Required for the
            [Agents.UpdateAgent][google.cloud.dialogflow.cx.v3.Agents.UpdateAgent]
            method.
            [Agents.CreateAgent][google.cloud.dialogflow.cx.v3.Agents.CreateAgent]
            populates the name automatically. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
        display_name (str):
            Required. The human-readable name of the
            agent, unique within the location.
        default_language_code (str):
            Required. Immutable. The default language of the agent as a
            language tag. See `Language
            Support <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            for a list of the currently supported language codes. This
            field cannot be set by the
            [Agents.UpdateAgent][google.cloud.dialogflow.cx.v3.Agents.UpdateAgent]
            method.
        supported_language_codes (MutableSequence[str]):
            The list of all languages supported by the agent (except for
            the ``default_language_code``).
        time_zone (str):
            Required. The time zone of the agent from the `time zone
            database <https://www.iana.org/time-zones>`__, e.g.,
            America/New_York, Europe/Paris.
        description (str):
            The description of the agent. The maximum
            length is 500 characters. If exceeded, the
            request is rejected.
        avatar_uri (str):
            The URI of the agent's avatar. Avatars are used throughout
            the Dialogflow console and in the self-hosted `Web
            Demo <https://cloud.google.com/dialogflow/docs/integrations/web-demo>`__
            integration.
        speech_to_text_settings (google.cloud.dialogflowcx_v3.types.SpeechToTextSettings):
            Speech recognition related settings.
        start_flow (str):
            Immutable. Name of the start flow in this agent. A start
            flow will be automatically created when the agent is
            created, and can only be deleted by deleting the agent.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/flows/<Flow ID>``.
        security_settings (str):
            Name of the
            [SecuritySettings][google.cloud.dialogflow.cx.v3.SecuritySettings]
            reference for the agent. Format:
            ``projects/<Project ID>/locations/<Location ID>/securitySettings/<Security Settings ID>``.
        enable_stackdriver_logging (bool):
            Indicates if stackdriver logging is enabled for the agent.
            Please use
            [agent.advanced_settings][google.cloud.dialogflow.cx.v3.AdvancedSettings.LoggingSettings]
            instead.
        enable_spell_correction (bool):
            Indicates if automatic spell correction is
            enabled in detect intent requests.
        locked (bool):
            Indicates whether the agent is locked for changes. If the
            agent is locked, modifications to the agent will be rejected
            except for [RestoreAgent][].
        advanced_settings (google.cloud.dialogflowcx_v3.types.AdvancedSettings):
            Hierarchical advanced settings for this
            agent. The settings exposed at the lower level
            overrides the settings exposed at the higher
            level.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    default_language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    supported_language_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=5,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    avatar_uri: str = proto.Field(
        proto.STRING,
        number=7,
    )
    speech_to_text_settings: "SpeechToTextSettings" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="SpeechToTextSettings",
    )
    start_flow: str = proto.Field(
        proto.STRING,
        number=16,
    )
    security_settings: str = proto.Field(
        proto.STRING,
        number=17,
    )
    enable_stackdriver_logging: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    enable_spell_correction: bool = proto.Field(
        proto.BOOL,
        number=20,
    )
    locked: bool = proto.Field(
        proto.BOOL,
        number=27,
    )
    advanced_settings: gcdc_advanced_settings.AdvancedSettings = proto.Field(
        proto.MESSAGE,
        number=22,
        message=gcdc_advanced_settings.AdvancedSettings,
    )


class ListAgentsRequest(proto.Message):
    r"""The request message for
    [Agents.ListAgents][google.cloud.dialogflow.cx.v3.Agents.ListAgents].

    Attributes:
        parent (str):
            Required. The location to list all agents for. Format:
            ``projects/<Project ID>/locations/<Location ID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAgentsResponse(proto.Message):
    r"""The response message for
    [Agents.ListAgents][google.cloud.dialogflow.cx.v3.Agents.ListAgents].

    Attributes:
        agents (MutableSequence[google.cloud.dialogflowcx_v3.types.Agent]):
            The list of agents. There will be a maximum number of items
            returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    agents: MutableSequence["Agent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Agent",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAgentRequest(proto.Message):
    r"""The request message for
    [Agents.GetAgent][google.cloud.dialogflow.cx.v3.Agents.GetAgent].

    Attributes:
        name (str):
            Required. The name of the agent. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAgentRequest(proto.Message):
    r"""The request message for
    [Agents.CreateAgent][google.cloud.dialogflow.cx.v3.Agents.CreateAgent].

    Attributes:
        parent (str):
            Required. The location to create a agent for. Format:
            ``projects/<Project ID>/locations/<Location ID>``.
        agent (google.cloud.dialogflowcx_v3.types.Agent):
            Required. The agent to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    agent: "Agent" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Agent",
    )


class UpdateAgentRequest(proto.Message):
    r"""The request message for
    [Agents.UpdateAgent][google.cloud.dialogflow.cx.v3.Agents.UpdateAgent].

    Attributes:
        agent (google.cloud.dialogflowcx_v3.types.Agent):
            Required. The agent to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The mask to control which fields get updated.
            If the mask is not present, all fields will be
            updated.
    """

    agent: "Agent" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Agent",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAgentRequest(proto.Message):
    r"""The request message for
    [Agents.DeleteAgent][google.cloud.dialogflow.cx.v3.Agents.DeleteAgent].

    Attributes:
        name (str):
            Required. The name of the agent to delete. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExportAgentRequest(proto.Message):
    r"""The request message for
    [Agents.ExportAgent][google.cloud.dialogflow.cx.v3.Agents.ExportAgent].

    Attributes:
        name (str):
            Required. The name of the agent to export. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
        agent_uri (str):
            Optional. The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            export the agent to. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``. If left unspecified,
            the serialized agent is returned inline.

            Dialogflow performs a write operation for the Cloud Storage
            object on the caller's behalf, so your request
            authentication must have write permissions for the object.
            For more information, see `Dialogflow access
            control <https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage>`__.
        data_format (google.cloud.dialogflowcx_v3.types.ExportAgentRequest.DataFormat):
            Optional. The data format of the exported agent. If not
            specified, ``BLOB`` is assumed.
        environment (str):
            Optional. Environment name. If not set, draft environment is
            assumed. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID>``.
    """

    class DataFormat(proto.Enum):
        r"""Data format of the exported agent.

        Values:
            DATA_FORMAT_UNSPECIFIED (0):
                Unspecified format.
            BLOB (1):
                Agent content will be exported as raw bytes.
        """
        DATA_FORMAT_UNSPECIFIED = 0
        BLOB = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    agent_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_format: DataFormat = proto.Field(
        proto.ENUM,
        number=3,
        enum=DataFormat,
    )
    environment: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ExportAgentResponse(proto.Message):
    r"""The response message for
    [Agents.ExportAgent][google.cloud.dialogflow.cx.v3.Agents.ExportAgent].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        agent_uri (str):
            The URI to a file containing the exported agent. This field
            is populated only if ``agent_uri`` is specified in
            [ExportAgentRequest][google.cloud.dialogflow.cx.v3.ExportAgentRequest].

            This field is a member of `oneof`_ ``agent``.
        agent_content (bytes):
            Uncompressed raw byte content for agent.

            This field is a member of `oneof`_ ``agent``.
    """

    agent_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="agent",
    )
    agent_content: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="agent",
    )


class RestoreAgentRequest(proto.Message):
    r"""The request message for
    [Agents.RestoreAgent][google.cloud.dialogflow.cx.v3.Agents.RestoreAgent].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the agent to restore into. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
        agent_uri (str):
            The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            restore agent from. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``.

            Dialogflow performs a read operation for the Cloud Storage
            object on the caller's behalf, so your request
            authentication must have read permissions for the object.
            For more information, see `Dialogflow access
            control <https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage>`__.

            This field is a member of `oneof`_ ``agent``.
        agent_content (bytes):
            Uncompressed raw byte content for agent.

            This field is a member of `oneof`_ ``agent``.
        restore_option (google.cloud.dialogflowcx_v3.types.RestoreAgentRequest.RestoreOption):
            Agent restore mode. If not specified, ``KEEP`` is assumed.
    """

    class RestoreOption(proto.Enum):
        r"""Restore option.

        Values:
            RESTORE_OPTION_UNSPECIFIED (0):
                Unspecified. Treated as KEEP.
            KEEP (1):
                Always respect the settings from the exported
                agent file. It may cause a restoration failure
                if some settings (e.g. model type) are not
                supported in the target agent.
            FALLBACK (2):
                Fallback to default settings if some settings
                are not supported in the target agent.
        """
        RESTORE_OPTION_UNSPECIFIED = 0
        KEEP = 1
        FALLBACK = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    agent_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="agent",
    )
    agent_content: bytes = proto.Field(
        proto.BYTES,
        number=3,
        oneof="agent",
    )
    restore_option: RestoreOption = proto.Field(
        proto.ENUM,
        number=5,
        enum=RestoreOption,
    )


class ValidateAgentRequest(proto.Message):
    r"""The request message for
    [Agents.ValidateAgent][google.cloud.dialogflow.cx.v3.Agents.ValidateAgent].

    Attributes:
        name (str):
            Required. The agent to validate. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>``.
        language_code (str):
            If not specified, the agent's default
            language is used.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAgentValidationResultRequest(proto.Message):
    r"""The request message for
    [Agents.GetAgentValidationResult][google.cloud.dialogflow.cx.v3.Agents.GetAgentValidationResult].

    Attributes:
        name (str):
            Required. The agent name. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/validationResult``.
        language_code (str):
            If not specified, the agent's default
            language is used.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AgentValidationResult(proto.Message):
    r"""The response message for
    [Agents.GetAgentValidationResult][google.cloud.dialogflow.cx.v3.Agents.GetAgentValidationResult].

    Attributes:
        name (str):
            The unique identifier of the agent validation result.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/validationResult``.
        flow_validation_results (MutableSequence[google.cloud.dialogflowcx_v3.types.FlowValidationResult]):
            Contains all flow validation results.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    flow_validation_results: MutableSequence[
        flow.FlowValidationResult
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=flow.FlowValidationResult,
    )


__all__ = tuple(sorted(__protobuf__.manifest))