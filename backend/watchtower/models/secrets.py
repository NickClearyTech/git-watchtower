from pydantic import BaseModel, AnyUrl, validator, Field


class CreateRepository(BaseModel):
    name: str
    url: AnyUrl

    username: str | None = None
    password: str | None = Field(exclude=True)

    @validator("url")
    def url_must_end_in_git(cls, v):
        if not v.endswith(".git"):
            raise ValueError("Must end in .git")
        return v


class Repository(BaseModel):
    name: str
    url: AnyUrl

    username: str | None
    password: str | None = Field(exclude=True)

    valid: bool | None = Field(default=False)

    @validator("url")
    def url_must_end_in_git(cls, v):
        if not v.endswith(".git"):
            raise ValueError("Must end in .git")
        return v
