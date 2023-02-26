from typing import List

from fastapi import APIRouter, Depends
from watchtower.utils.api_utils.dependencies import CommonK8sQueryParams
from watchtower.models.secrets import Repository, CreateRepository, ResponseRepository
from watchtower.kube.utils import get_kube_client, get_kube_namespace
from watchtower.kube.secrets import secret_to_model, model_to_secret

router = APIRouter(
    prefix="/repository",
    tags=["Repository"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_repositories(
    common: CommonK8sQueryParams = Depends(CommonK8sQueryParams),
) -> List[ResponseRepository]:
    client = get_kube_client()
    result = client.list_namespaced_secret(
        namespace=get_kube_namespace(),
        label_selector="watchtower/secret-type=repository",
        _continue=common.continue_token,
        limit=common.limit,
    )

    return [secret_to_model(repo, ResponseRepository) for repo in result.items]


@router.post("/")
def create_repository(repo: CreateRepository) -> ResponseRepository:
    repo_object = Repository(**repo.dict())
    secret = model_to_secret(repo_object)
    return repo
