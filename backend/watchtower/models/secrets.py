from pydantic import BaseModel, AnyUrl, validator, ValidationError

class Repository(BaseModel):
    name: str
    url: AnyUrl

    @validator("url")
    def url_must_end_in_git(self, v):
        if not v.endswith(".git"):
            raise ValueError("Must end in .git")
        return v
