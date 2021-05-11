import time
from typing import Any, Optional
from uuid import uuid4

import pulumi
from pulumi import Output
from pulumi.dynamic import CreateResult, Resource, ResourceProvider


class RandomOutputProvider(ResourceProvider):

    def create(self, props: Any) -> CreateResult:
        time.sleep(1)
        return CreateResult(id_=uuid4().hex, outs=props | {"property": uuid4().hex[:4]})


class RandomOutput(Resource):
    property: Output[str]

    def __init__(
            self,
            resource_name: str,
            opts: Optional[pulumi.ResourceOptions] = None,
    ):
        super().__init__(
            RandomOutputProvider(),
            name=resource_name,
            props={"property": None},
            opts=opts,
        )


class InputReaderProvider(ResourceProvider):

    def create(self, props: Any) -> CreateResult:
        print(props["comment"], "\n>>> ", f"{props['input']}", "\n---")
        time.sleep(1)
        return CreateResult(id_=uuid4().hex, outs=props)


class InputReader(Resource):

    def __init__(
            self,
            resource_name: str,
            input_str: Output[str],
            comment: str,
            opts: Optional[pulumi.ResourceOptions] = None,
    ):
        super().__init__(
            InputReaderProvider(),
            name=resource_name,
            props={"input": input_str, "comment": comment},
            opts=opts,
        )
