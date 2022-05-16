import pulumi


def import_module_read_config():
    print("imported module reports: ", pulumi.Config("example").require(key="value"))

