from typing import List

from fastapi import APIRouter, Depends
from watchtower.utils.api_utils.dependencies import CommonK8sQueryParams
from watchtower.models.secrets import Repository, CreateRepository
from watchtower.kube.utils import get_kube_client, get_kube_namespace
from watchtower.models.utils import secret_to_model

router = APIRouter(
    prefix="/repository",
    tags=["Repository"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_repositories(
    common: CommonK8sQueryParams = Depends(CommonK8sQueryParams),
) -> List[Repository]:
    client = get_kube_client()
    result = client.list_namespaced_secret(
        namespace=get_kube_namespace(),
        label_selector="watchtower/secret-type=repository",
        _continue=common.continue_token,
        limit=common.limit,
    )
    to_return = []
    for repo in result.items:
        to_return.append(secret_to_model(repo, Repository))

    thingy = CreateRepository(name="Hello there", url="https://amazon.com")
    return to_return


@router.post("/")
def create_repository(repo: CreateRepository):
    return repo
