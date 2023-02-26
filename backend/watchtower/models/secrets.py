from pydantic import BaseModel, AnyUrl, Field, SecretStr, SecretBytes
from enum import Enum


class RepoType(str, Enum):
    http = "http"
    ssh = "ssh"


class RepoStatus(str, Enum):
    unknown = "unknown"
    connected = "connected"
    failed = "failed"


class CreateRepository(BaseModel):
    """
    Used by the POST endpoint to create a repository
    """

    name: str
    url: AnyUrl

    type: RepoType = RepoType.http

    username: str | None = None
    password: str | None = None


class ResponseRepository(BaseModel):
    """
    Used as the Response to any request for a repository
    """

    name: str
    url: AnyUrl

    type: RepoType = RepoType.http

    username: str | None = None
    password: SecretStr | None = None

    status: RepoStatus = RepoStatus.unknown

    class Config:
        json_encoders = {
            SecretStr: lambda v: str(v)
        }


class Repository(BaseModel):
    """
    The class used to read/write k8s secrets storing a repository object.
    Used only internally
    """

    watchtower_secret_type = "repository"

    name: str
    url: AnyUrl

    type: RepoType = RepoType.http

    username: str | None
    password: str | None

    status: RepoStatus = RepoStatus.unknown
