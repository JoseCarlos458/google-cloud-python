# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
from google.maps.mapsplatformdatasets import gapic_version as package_version

__version__ = package_version.__version__


from google.maps.mapsplatformdatasets_v1alpha.services.maps_platform_datasets_v1_alpha.client import MapsPlatformDatasetsV1AlphaClient
from google.maps.mapsplatformdatasets_v1alpha.services.maps_platform_datasets_v1_alpha.async_client import MapsPlatformDatasetsV1AlphaAsyncClient

from google.maps.mapsplatformdatasets_v1alpha.types.data_source import GcsSource
from google.maps.mapsplatformdatasets_v1alpha.types.data_source import LocalFileSource
from google.maps.mapsplatformdatasets_v1alpha.types.data_source import FileFormat
from google.maps.mapsplatformdatasets_v1alpha.types.dataset import Dataset
from google.maps.mapsplatformdatasets_v1alpha.types.dataset import State
from google.maps.mapsplatformdatasets_v1alpha.types.dataset import Usage
from google.maps.mapsplatformdatasets_v1alpha.types.maps_platform_datasets import CreateDatasetRequest
from google.maps.mapsplatformdatasets_v1alpha.types.maps_platform_datasets import DeleteDatasetRequest
from google.maps.mapsplatformdatasets_v1alpha.types.maps_platform_datasets import DeleteDatasetVersionRequest
from google.maps.mapsplatformdatasets_v1alpha.types.maps_platform_datasets import GetDatasetRequest
from google.maps.mapsplatformdatasets_v1alpha.types.maps_platform_datasets import ListDatasetsRequest
from google.maps.mapsplatformdatasets_v1alpha.types.maps_platform_datasets import ListDatasetsResponse
from google.maps.mapsplatformdatasets_v1alpha.types.maps_platform_datasets import ListDatasetVersionsRequest
from google.maps.mapsplatformdatasets_v1alpha.types.maps_platform_datasets import ListDatasetVersionsResponse
from google.maps.mapsplatformdatasets_v1alpha.types.maps_platform_datasets import UpdateDatasetMetadataRequest

__all__ = ('MapsPlatformDatasetsV1AlphaClient',
    'MapsPlatformDatasetsV1AlphaAsyncClient',
    'GcsSource',
    'LocalFileSource',
    'FileFormat',
    'Dataset',
    'State',
    'Usage',
    'CreateDatasetRequest',
    'DeleteDatasetRequest',
    'DeleteDatasetVersionRequest',
    'GetDatasetRequest',
    'ListDatasetsRequest',
    'ListDatasetsResponse',
    'ListDatasetVersionsRequest',
    'ListDatasetVersionsResponse',
    'UpdateDatasetMetadataRequest',
)
