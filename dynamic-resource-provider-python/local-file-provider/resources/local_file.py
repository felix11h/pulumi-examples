import os
import time
from pathlib import Path
from typing import Any, Optional
from uuid import uuid4

import pulumi
from pulumi import Input, Output
from pulumi.dynamic import CreateResult, DiffResult, ReadResult, Resource, ResourceProvider, UpdateResult


class LocalFileResourceProvider(ResourceProvider):

    def _write_content(self, file_path, content):
        if "exception" in content.lower():
            raise Exception("File content can not contain 'exception'")
        Path(file_path).write_text(content)

    def create(self, props: Any) -> CreateResult:
        print("CREATE has been called")
        time.sleep(5)
        self._write_content(props["path"], props["content"])
        return CreateResult(id_=uuid4().hex, outs=props)

    def delete(self, _id: str, _props: Any) -> None:
        print("DELETE has been called")
        time.sleep(5)
        os.remove(_props["path"])

    def diff(self, _id: str, _olds: Any, _news: Any) -> DiffResult:
        print("DIFF has been called")
        # print("_id", _id)
        # print("_olds", _olds)
        # print("_news", _news)
        return DiffResult(
            changes=_olds != _news,
            replaces=["path"] if _olds["path"] != _news["path"] else [],
            delete_before_replace=True,
        )

    def update(self, _id: str, _olds: Any, _news: Any) -> UpdateResult:
        print("UPDATE has been called")
        time.sleep(5)
        self._write_content(_news["path"], _news["content"])
        return UpdateResult(outs={**_news})

    def read(self, id_: str, props: Any):
        print("READ has been called")
        print(f"{props=}")
        return ReadResult(id_, outs={**props, "content": Path(props["path"]).read_text()})


class LocalFile(Resource):
    content: Output[str]
    path: Output[str]

    def __init__(
            self,
            resource_name: str,
            content: Input[str],
            path: Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
    ):
        super().__init__(
            LocalFileResourceProvider(),
            name=resource_name,
            props={"content": content, "path": path},
            opts=opts,
        )
