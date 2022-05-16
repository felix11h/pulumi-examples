import os
from uuid import uuid4

import pulumi
from resources.local_module import import_module_read_config
from resources.local_provider import ConfigRequestTest

print("__main__.py reports: ", pulumi.Config("example").require(key="value"))

import_module_read_config()

if os.environ.get("USE_PROVIDER"):
    ConfigRequestTest(name=uuid4().hex)


