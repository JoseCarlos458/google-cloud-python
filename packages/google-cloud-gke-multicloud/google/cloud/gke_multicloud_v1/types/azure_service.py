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
import proto  # type: ignore

from google.cloud.gke_multicloud_v1.types import azure_resources
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.gkemulticloud.v1",
    manifest={
        "CreateAzureClusterRequest",
        "UpdateAzureClusterRequest",
        "GetAzureClusterRequest",
        "ListAzureClustersRequest",
        "ListAzureClustersResponse",
        "DeleteAzureClusterRequest",
        "CreateAzureNodePoolRequest",
        "UpdateAzureNodePoolRequest",
        "GetAzureNodePoolRequest",
        "ListAzureNodePoolsRequest",
        "ListAzureNodePoolsResponse",
        "DeleteAzureNodePoolRequest",
        "GetAzureServerConfigRequest",
        "CreateAzureClientRequest",
        "GetAzureClientRequest",
        "ListAzureClientsRequest",
        "ListAzureClientsResponse",
        "DeleteAzureClientRequest",
        "GenerateAzureAccessTokenRequest",
        "GenerateAzureAccessTokenResponse",
    },
)


class CreateAzureClusterRequest(proto.Message):
    r"""Request message for ``AzureClusters.CreateAzureCluster`` method.

    Attributes:
        parent (str):
            Required. The parent location where this
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource will be created.

            Location names are formatted as
            ``projects/<project-id>/locations/<region>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        azure_cluster (google.cloud.gke_multicloud_v1.types.AzureCluster):
            Required. The specification of the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            to create.
        azure_cluster_id (str):
            Required. A client provided ID the resource. Must be unique
            within the parent resource.

            The provided ID will be part of the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource name formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

            Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
            than 40 characters.
        validate_only (bool):
            If set, only validate the request, but do not
            actually create the cluster.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    azure_cluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=azure_resources.AzureCluster,
    )
    azure_cluster_id = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateAzureClusterRequest(proto.Message):
    r"""Request message for ``AzureClusters.UpdateAzureCluster`` method.

    Attributes:
        azure_cluster (google.cloud.gke_multicloud_v1.types.AzureCluster):
            Required. The
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource to update.
        validate_only (bool):
            If set, only validate the request, but do not
            actually update the cluster.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. The elements of the repeated
            paths field can only include these fields from
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]:

            -  ``description``.
            -  ``annotations``.
            -  ``azureClient``.
            -  ``control_plane.version``.
            -  ``control_plane.vm_size``.
            -  ``authorization.admin_users``.
            -  ``control_plane.root_volume.size_gib``.
            -  ``logging_config``
    """

    azure_cluster = proto.Field(
        proto.MESSAGE,
        number=1,
        message=azure_resources.AzureCluster,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=2,
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class GetAzureClusterRequest(proto.Message):
    r"""Request message for ``AzureClusters.GetAzureCluster`` method.

    Attributes:
        name (str):
            Required. The name of the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource to describe.

            ``AzureCluster`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on GCP resource names.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAzureClustersRequest(proto.Message):
    r"""Request message for ``AzureClusters.ListAzureClusters`` method.

    Attributes:
        parent (str):
            Required. The parent location which owns this collection of
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resources.

            Location names are formatted as
            ``projects/<project-id>/locations/<region>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on GCP resource names.
        page_size (int):
            The maximum number of items to return.

            If not specified, a default value of 50 will be used by the
            service. Regardless of the pageSize value, the response can
            include a partial list and a caller should only rely on
            response's
            [nextPageToken][google.cloud.gkemulticloud.v1.ListAzureClustersResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            The ``nextPageToken`` value returned from a previous
            [azureClusters.list][google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClusters]
            request, if any.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAzureClustersResponse(proto.Message):
    r"""Response message for ``AzureClusters.ListAzureClusters`` method.

    Attributes:
        azure_clusters (Sequence[google.cloud.gke_multicloud_v1.types.AzureCluster]):
            A list of
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resources in the specified GCP project and region region.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    azure_clusters = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=azure_resources.AzureCluster,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAzureClusterRequest(proto.Message):
    r"""Request message for ``Clusters.DeleteAzureCluster`` method.

    Attributes:
        name (str):
            Required. The resource name the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            to delete.

            ``AzureCluster`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on GCP resource names.
        allow_missing (bool):
            If set to true, and the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource is not found, the request will succeed but no
            action will be taken on the server and a completed
            [Operation][google.longrunning.Operation] will be returned.

            Useful for idempotent deletion.
        validate_only (bool):
            If set, only validate the request, but do not
            actually delete the resource.
        etag (str):
            The current etag of the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster].

            Allows clients to perform deletions through optimistic
            concurrency control.

            If the provided etag does not match the current etag of the
            cluster, the request will fail and an ABORTED error will be
            returned.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing = proto.Field(
        proto.BOOL,
        number=2,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag = proto.Field(
        proto.STRING,
        number=4,
    )


class CreateAzureNodePoolRequest(proto.Message):
    r"""Response message for ``AzureClusters.CreateAzureNodePool`` method.

    Attributes:
        parent (str):
            Required. The
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource where this node pool will be created.

            Location names are formatted as
            ``projects/<project-id>/locations/<region>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        azure_node_pool (google.cloud.gke_multicloud_v1.types.AzureNodePool):
            Required. The specification of the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            to create.
        azure_node_pool_id (str):
            Required. A client provided ID the resource. Must be unique
            within the parent resource.

            The provided ID will be part of the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resource name formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>/azureNodePools/<node-pool-id>``.

            Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
            than 40 characters.
        validate_only (bool):
            If set, only validate the request, but do not
            actually create the node pool.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    azure_node_pool = proto.Field(
        proto.MESSAGE,
        number=2,
        message=azure_resources.AzureNodePool,
    )
    azure_node_pool_id = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateAzureNodePoolRequest(proto.Message):
    r"""Request message for ``AzureClusters.UpdateAzureNodePool`` method.

    Attributes:
        azure_node_pool (google.cloud.gke_multicloud_v1.types.AzureNodePool):
            Required. The
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resource to update.
        validate_only (bool):
            If set, only validate the request, but don't
            actually update the node pool.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. The elements of the repeated
            paths field can only include these fields from
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]:

            \*. ``annotations``.

            -  ``version``.
            -  ``autoscaling.min_node_count``.
            -  ``autoscaling.max_node_count``.
            -  ``config.vm_size``.
    """

    azure_node_pool = proto.Field(
        proto.MESSAGE,
        number=1,
        message=azure_resources.AzureNodePool,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=2,
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class GetAzureNodePoolRequest(proto.Message):
    r"""Request message for ``AzureClusters.GetAzureNodePool`` method.

    Attributes:
        name (str):
            Required. The name of the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resource to describe.

            ``AzureNodePool`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>/azureNodePools/<node-pool-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAzureNodePoolsRequest(proto.Message):
    r"""Request message for ``AzureClusters.ListAzureNodePools`` method.

    Attributes:
        parent (str):
            Required. The parent ``AzureCluster`` which owns this
            collection of
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resources.

            ``AzureCluster`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        page_size (int):
            The maximum number of items to return.

            If not specified, a default value of 50 will be used by the
            service. Regardless of the pageSize value, the response can
            include a partial list and a caller should only rely on
            response's
            [nextPageToken][google.cloud.gkemulticloud.v1.ListAzureNodePoolsResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            The ``nextPageToken`` value returned from a previous
            [azureNodePools.list][google.cloud.gkemulticloud.v1.AzureClusters.ListAzureNodePools]
            request, if any.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAzureNodePoolsResponse(proto.Message):
    r"""Response message for ``AzureClusters.ListAzureNodePools`` method.

    Attributes:
        azure_node_pools (Sequence[google.cloud.gke_multicloud_v1.types.AzureNodePool]):
            A list of
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resources in the specified ``AzureCluster``.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    azure_node_pools = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=azure_resources.AzureNodePool,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAzureNodePoolRequest(proto.Message):
    r"""Delete message for ``AzureClusters.DeleteNodePool`` method.

    Attributes:
        name (str):
            Required. The resource name the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            to delete.

            ``AzureNodePool`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureClusters/<cluster-id>/azureNodePools/<node-pool-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        validate_only (bool):
            If set, only validate the request, but do not
            actually delete the node pool.
        allow_missing (bool):
            If set to true, and the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool]
            resource is not found, the request will succeed but no
            action will be taken on the server and a completed
            [Operation][google.longrunning.Operation] will be returned.

            Useful for idempotent deletion.
        etag (str):
            The current ETag of the
            [AzureNodePool][google.cloud.gkemulticloud.v1.AzureNodePool].

            Allows clients to perform deletions through optimistic
            concurrency control.

            If the provided ETag does not match the current etag of the
            node pool, the request will fail and an ABORTED error will
            be returned.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=2,
    )
    allow_missing = proto.Field(
        proto.BOOL,
        number=3,
    )
    etag = proto.Field(
        proto.STRING,
        number=4,
    )


class GetAzureServerConfigRequest(proto.Message):
    r"""GetAzureServerConfigRequest gets the server config of GKE
    cluster on Azure.

    Attributes:
        name (str):
            Required. The name of the
            [AzureServerConfig][google.cloud.gkemulticloud.v1.AzureServerConfig]
            resource to describe.

            ``AzureServerConfig`` names are formatted as
            ``projects/<project-id>/locations/<region>/azureServerConfig``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAzureClientRequest(proto.Message):
    r"""Request message for ``AzureClusters.CreateAzureClient`` method.

    Attributes:
        parent (str):
            Required. The parent location where this
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            resource will be created.

            Location names are formatted as
            ``projects/<project-id>/locations/<region>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        azure_client (google.cloud.gke_multicloud_v1.types.AzureClient):
            Required. The specification of the
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient] to
            create.
        azure_client_id (str):
            Required. A client provided ID the resource. Must be unique
            within the parent resource.

            The provided ID will be part of the
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            resource name formatted as
            ``projects/<project-id>/locations/<region>/azureClients/<client-id>``.

            Valid characters are ``/[a-z][0-9]-/``. Cannot be longer
            than 40 characters.
        validate_only (bool):
            If set, only validate the request, but do not
            actually create the client.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    azure_client = proto.Field(
        proto.MESSAGE,
        number=2,
        message=azure_resources.AzureClient,
    )
    azure_client_id = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetAzureClientRequest(proto.Message):
    r"""Request message for ``AzureClusters.GetAzureClient`` method.

    Attributes:
        name (str):
            Required. The name of the
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            resource to describe.

            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            names are formatted as
            ``projects/<project-id>/locations/<region>/azureClients/<client-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAzureClientsRequest(proto.Message):
    r"""Request message for ``AzureClusters.ListAzureClients`` method.

    Attributes:
        parent (str):
            Required. The parent location which owns this collection of
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            resources.

            Location names are formatted as
            ``projects/<project-id>/locations/<region>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on GCP resource names.
        page_size (int):
            The maximum number of items to return.

            If not specified, a default value of 50 will be used by the
            service. Regardless of the pageSize value, the response can
            include a partial list and a caller should only rely on
            response's
            [nextPageToken][google.cloud.gkemulticloud.v1.ListAzureClientsResponse.next_page_token]
            to determine if there are more instances left to be queried.
        page_token (str):
            The ``nextPageToken`` value returned from a previous
            [azureClients.list][google.cloud.gkemulticloud.v1.AzureClusters.ListAzureClients]
            request, if any.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAzureClientsResponse(proto.Message):
    r"""Response message for ``AzureClusters.ListAzureClients`` method.

    Attributes:
        azure_clients (Sequence[google.cloud.gke_multicloud_v1.types.AzureClient]):
            A list of
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            resources in the specified Google Cloud project and region
            region.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    azure_clients = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=azure_resources.AzureClient,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAzureClientRequest(proto.Message):
    r"""Request message for ``AzureClusters.DeleteAzureClient`` method.

    Attributes:
        name (str):
            Required. The resource name the
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient] to
            delete.

            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            names are formatted as
            ``projects/<project-id>/locations/<region>/azureClients/<client-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
        allow_missing (bool):
            If set to true, and the
            [AzureClient][google.cloud.gkemulticloud.v1.AzureClient]
            resource is not found, the request will succeed but no
            action will be taken on the server and a completed
            [Operation][google.longrunning.Operation] will be returned.

            Useful for idempotent deletion.
        validate_only (bool):
            If set, only validate the request, but do not
            actually delete the resource.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing = proto.Field(
        proto.BOOL,
        number=2,
    )
    validate_only = proto.Field(
        proto.BOOL,
        number=3,
    )


class GenerateAzureAccessTokenRequest(proto.Message):
    r"""Request message for ``AzureClusters.GenerateAzureAccessToken``
    method.

    Attributes:
        azure_cluster (str):
            Required. The name of the
            [AzureCluster][google.cloud.gkemulticloud.v1.AzureCluster]
            resource to authenticate to.

            ``AzureCluster`` names are formatted as
            ``projects/<project-id>/locations/<region>/AzureClusters/<cluster-id>``.

            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names>`__
            for more details on Google Cloud resource names.
    """

    azure_cluster = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateAzureAccessTokenResponse(proto.Message):
    r"""Response message for ``AzureClusters.GenerateAzureAccessToken``
    method.

    Attributes:
        access_token (str):
            Output only. Access token to authenticate to
            k8s api-server.
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp at which the token
            will expire.
    """

    access_token = proto.Field(
        proto.STRING,
        number=1,
    )
    expiration_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
