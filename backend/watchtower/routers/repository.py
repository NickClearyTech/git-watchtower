from typing import List

from fastapi import APIRouter
from watchtower.models.secrets import Repository
from watchtower.kube.utils import get_kube_client
from watchtower.models.utils import secret_to_model

router = APIRouter(
    prefix="/repository",
    tags=["repository"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_repositories() -> List[Repository]:
    client = get_kube_client()
    result = client.list_namespaced_secret(
        namespace="watchtower",
        label_selector="watchtower/secret-type=repository",
    )
    to_return = []
    for repo in result.items:
        to_return.append(secret_to_model(repo, Repository))
    return to_return
