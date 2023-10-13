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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

from google.cloud.dataform_v1beta1 import gapic_version as package_version

import google.auth  # type: ignore
import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account # type: ignore

from google.cloud.dataform_v1beta1.types import dataform
from google.cloud.location import locations_pb2 # type: ignore
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version=package_version.__version__)


class DataformTransport(abc.ABC):
    """Abstract transport class for Dataform."""

    AUTH_SCOPES = (
        'https://www.googleapis.com/auth/cloud-platform',
    )

    DEFAULT_HOST: str = 'dataform.googleapis.com'
    def __init__(
            self, *,
            host: str = DEFAULT_HOST,
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            api_audience: Optional[str] = None,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                                credentials_file,
                                **scopes_kwargs,
                                quota_project_id=quota_project_id
                            )
        elif credentials is None:
            credentials, _ = google.auth.default(**scopes_kwargs, quota_project_id=quota_project_id)
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(api_audience if api_audience else host)

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if always_use_jwt_access and isinstance(credentials, service_account.Credentials) and hasattr(service_account.Credentials, "with_always_use_jwt_access"):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
        self._host = host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_repositories: gapic_v1.method.wrap_method(
                self.list_repositories,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_repository: gapic_v1.method.wrap_method(
                self.get_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_repository: gapic_v1.method.wrap_method(
                self.create_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_repository: gapic_v1.method.wrap_method(
                self.update_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_repository: gapic_v1.method.wrap_method(
                self.delete_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_remote_branches: gapic_v1.method.wrap_method(
                self.fetch_remote_branches,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_workspaces: gapic_v1.method.wrap_method(
                self.list_workspaces,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_workspace: gapic_v1.method.wrap_method(
                self.get_workspace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_workspace: gapic_v1.method.wrap_method(
                self.create_workspace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_workspace: gapic_v1.method.wrap_method(
                self.delete_workspace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.install_npm_packages: gapic_v1.method.wrap_method(
                self.install_npm_packages,
                default_timeout=None,
                client_info=client_info,
            ),
            self.pull_git_commits: gapic_v1.method.wrap_method(
                self.pull_git_commits,
                default_timeout=None,
                client_info=client_info,
            ),
            self.push_git_commits: gapic_v1.method.wrap_method(
                self.push_git_commits,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_file_git_statuses: gapic_v1.method.wrap_method(
                self.fetch_file_git_statuses,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_git_ahead_behind: gapic_v1.method.wrap_method(
                self.fetch_git_ahead_behind,
                default_timeout=None,
                client_info=client_info,
            ),
            self.commit_workspace_changes: gapic_v1.method.wrap_method(
                self.commit_workspace_changes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reset_workspace_changes: gapic_v1.method.wrap_method(
                self.reset_workspace_changes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_file_diff: gapic_v1.method.wrap_method(
                self.fetch_file_diff,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_directory_contents: gapic_v1.method.wrap_method(
                self.query_directory_contents,
                default_timeout=None,
                client_info=client_info,
            ),
            self.make_directory: gapic_v1.method.wrap_method(
                self.make_directory,
                default_timeout=None,
                client_info=client_info,
            ),
            self.remove_directory: gapic_v1.method.wrap_method(
                self.remove_directory,
                default_timeout=None,
                client_info=client_info,
            ),
            self.move_directory: gapic_v1.method.wrap_method(
                self.move_directory,
                default_timeout=None,
                client_info=client_info,
            ),
            self.read_file: gapic_v1.method.wrap_method(
                self.read_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.remove_file: gapic_v1.method.wrap_method(
                self.remove_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.move_file: gapic_v1.method.wrap_method(
                self.move_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.write_file: gapic_v1.method.wrap_method(
                self.write_file,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_compilation_results: gapic_v1.method.wrap_method(
                self.list_compilation_results,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_compilation_result: gapic_v1.method.wrap_method(
                self.get_compilation_result,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_compilation_result: gapic_v1.method.wrap_method(
                self.create_compilation_result,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_compilation_result_actions: gapic_v1.method.wrap_method(
                self.query_compilation_result_actions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_workflow_invocations: gapic_v1.method.wrap_method(
                self.list_workflow_invocations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_workflow_invocation: gapic_v1.method.wrap_method(
                self.get_workflow_invocation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_workflow_invocation: gapic_v1.method.wrap_method(
                self.create_workflow_invocation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_workflow_invocation: gapic_v1.method.wrap_method(
                self.delete_workflow_invocation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_workflow_invocation: gapic_v1.method.wrap_method(
                self.cancel_workflow_invocation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_workflow_invocation_actions: gapic_v1.method.wrap_method(
                self.query_workflow_invocation_actions,
                default_timeout=None,
                client_info=client_info,
            ),
         }

    def close(self):
        """Closes resources associated with the transport.

       .. warning::
            Only call this method if the transport is NOT shared
            with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def list_repositories(self) -> Callable[
            [dataform.ListRepositoriesRequest],
            Union[
                dataform.ListRepositoriesResponse,
                Awaitable[dataform.ListRepositoriesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_repository(self) -> Callable[
            [dataform.GetRepositoryRequest],
            Union[
                dataform.Repository,
                Awaitable[dataform.Repository]
            ]]:
        raise NotImplementedError()

    @property
    def create_repository(self) -> Callable[
            [dataform.CreateRepositoryRequest],
            Union[
                dataform.Repository,
                Awaitable[dataform.Repository]
            ]]:
        raise NotImplementedError()

    @property
    def update_repository(self) -> Callable[
            [dataform.UpdateRepositoryRequest],
            Union[
                dataform.Repository,
                Awaitable[dataform.Repository]
            ]]:
        raise NotImplementedError()

    @property
    def delete_repository(self) -> Callable[
            [dataform.DeleteRepositoryRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def fetch_remote_branches(self) -> Callable[
            [dataform.FetchRemoteBranchesRequest],
            Union[
                dataform.FetchRemoteBranchesResponse,
                Awaitable[dataform.FetchRemoteBranchesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_workspaces(self) -> Callable[
            [dataform.ListWorkspacesRequest],
            Union[
                dataform.ListWorkspacesResponse,
                Awaitable[dataform.ListWorkspacesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_workspace(self) -> Callable[
            [dataform.GetWorkspaceRequest],
            Union[
                dataform.Workspace,
                Awaitable[dataform.Workspace]
            ]]:
        raise NotImplementedError()

    @property
    def create_workspace(self) -> Callable[
            [dataform.CreateWorkspaceRequest],
            Union[
                dataform.Workspace,
                Awaitable[dataform.Workspace]
            ]]:
        raise NotImplementedError()

    @property
    def delete_workspace(self) -> Callable[
            [dataform.DeleteWorkspaceRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def install_npm_packages(self) -> Callable[
            [dataform.InstallNpmPackagesRequest],
            Union[
                dataform.InstallNpmPackagesResponse,
                Awaitable[dataform.InstallNpmPackagesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def pull_git_commits(self) -> Callable[
            [dataform.PullGitCommitsRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def push_git_commits(self) -> Callable[
            [dataform.PushGitCommitsRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def fetch_file_git_statuses(self) -> Callable[
            [dataform.FetchFileGitStatusesRequest],
            Union[
                dataform.FetchFileGitStatusesResponse,
                Awaitable[dataform.FetchFileGitStatusesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def fetch_git_ahead_behind(self) -> Callable[
            [dataform.FetchGitAheadBehindRequest],
            Union[
                dataform.FetchGitAheadBehindResponse,
                Awaitable[dataform.FetchGitAheadBehindResponse]
            ]]:
        raise NotImplementedError()

    @property
    def commit_workspace_changes(self) -> Callable[
            [dataform.CommitWorkspaceChangesRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def reset_workspace_changes(self) -> Callable[
            [dataform.ResetWorkspaceChangesRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def fetch_file_diff(self) -> Callable[
            [dataform.FetchFileDiffRequest],
            Union[
                dataform.FetchFileDiffResponse,
                Awaitable[dataform.FetchFileDiffResponse]
            ]]:
        raise NotImplementedError()

    @property
    def query_directory_contents(self) -> Callable[
            [dataform.QueryDirectoryContentsRequest],
            Union[
                dataform.QueryDirectoryContentsResponse,
                Awaitable[dataform.QueryDirectoryContentsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def make_directory(self) -> Callable[
            [dataform.MakeDirectoryRequest],
            Union[
                dataform.MakeDirectoryResponse,
                Awaitable[dataform.MakeDirectoryResponse]
            ]]:
        raise NotImplementedError()

    @property
    def remove_directory(self) -> Callable[
            [dataform.RemoveDirectoryRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def move_directory(self) -> Callable[
            [dataform.MoveDirectoryRequest],
            Union[
                dataform.MoveDirectoryResponse,
                Awaitable[dataform.MoveDirectoryResponse]
            ]]:
        raise NotImplementedError()

    @property
    def read_file(self) -> Callable[
            [dataform.ReadFileRequest],
            Union[
                dataform.ReadFileResponse,
                Awaitable[dataform.ReadFileResponse]
            ]]:
        raise NotImplementedError()

    @property
    def remove_file(self) -> Callable[
            [dataform.RemoveFileRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def move_file(self) -> Callable[
            [dataform.MoveFileRequest],
            Union[
                dataform.MoveFileResponse,
                Awaitable[dataform.MoveFileResponse]
            ]]:
        raise NotImplementedError()

    @property
    def write_file(self) -> Callable[
            [dataform.WriteFileRequest],
            Union[
                dataform.WriteFileResponse,
                Awaitable[dataform.WriteFileResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_compilation_results(self) -> Callable[
            [dataform.ListCompilationResultsRequest],
            Union[
                dataform.ListCompilationResultsResponse,
                Awaitable[dataform.ListCompilationResultsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_compilation_result(self) -> Callable[
            [dataform.GetCompilationResultRequest],
            Union[
                dataform.CompilationResult,
                Awaitable[dataform.CompilationResult]
            ]]:
        raise NotImplementedError()

    @property
    def create_compilation_result(self) -> Callable[
            [dataform.CreateCompilationResultRequest],
            Union[
                dataform.CompilationResult,
                Awaitable[dataform.CompilationResult]
            ]]:
        raise NotImplementedError()

    @property
    def query_compilation_result_actions(self) -> Callable[
            [dataform.QueryCompilationResultActionsRequest],
            Union[
                dataform.QueryCompilationResultActionsResponse,
                Awaitable[dataform.QueryCompilationResultActionsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_workflow_invocations(self) -> Callable[
            [dataform.ListWorkflowInvocationsRequest],
            Union[
                dataform.ListWorkflowInvocationsResponse,
                Awaitable[dataform.ListWorkflowInvocationsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_workflow_invocation(self) -> Callable[
            [dataform.GetWorkflowInvocationRequest],
            Union[
                dataform.WorkflowInvocation,
                Awaitable[dataform.WorkflowInvocation]
            ]]:
        raise NotImplementedError()

    @property
    def create_workflow_invocation(self) -> Callable[
            [dataform.CreateWorkflowInvocationRequest],
            Union[
                dataform.WorkflowInvocation,
                Awaitable[dataform.WorkflowInvocation]
            ]]:
        raise NotImplementedError()

    @property
    def delete_workflow_invocation(self) -> Callable[
            [dataform.DeleteWorkflowInvocationRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def cancel_workflow_invocation(self) -> Callable[
            [dataform.CancelWorkflowInvocationRequest],
            Union[
                empty_pb2.Empty,
                Awaitable[empty_pb2.Empty]
            ]]:
        raise NotImplementedError()

    @property
    def query_workflow_invocation_actions(self) -> Callable[
            [dataform.QueryWorkflowInvocationActionsRequest],
            Union[
                dataform.QueryWorkflowInvocationActionsResponse,
                Awaitable[dataform.QueryWorkflowInvocationActionsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_location(self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[locations_pb2.ListLocationsResponse, Awaitable[locations_pb2.ListLocationsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = (
    'DataformTransport',
)
