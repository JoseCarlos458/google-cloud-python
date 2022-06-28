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
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateRestorePlan
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-gke-backup


# [START gkebackup_v1_generated_BackupForGKE_UpdateRestorePlan_async]
from google.cloud import gke_backup_v1


async def sample_update_restore_plan():
    # Create a client
    client = gke_backup_v1.BackupForGKEAsyncClient()

    # Initialize request argument(s)
    restore_plan = gke_backup_v1.RestorePlan()
    restore_plan.backup_plan = "backup_plan_value"
    restore_plan.cluster = "cluster_value"
    restore_plan.restore_config.all_namespaces = True

    request = gke_backup_v1.UpdateRestorePlanRequest(
        restore_plan=restore_plan,
    )

    # Make the request
    operation = client.update_restore_plan(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)

# [END gkebackup_v1_generated_BackupForGKE_UpdateRestorePlan_async]
