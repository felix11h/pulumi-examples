from resources.local_file import LocalFile

LocalFile(
    resource_name="local-file-01",
    content="hello world",
    path="output/local-file-01.txt",
)

# LocalFile(
#     resource_name="local-file-02",
#     content="Exceptions are not allowed!",
#     path="output/local-file-02.txt",
# )

# LocalFile(
#     resource_name="local-file-03",
#     content="",
#     path="output/local-file-03.txt",
# )

# for i in range(10, 50):
#     LocalFile(
#         resource_name=f"local-file-{i}",
#         content=f"No. {i}",
#         path=f"output/local-file-{i}.txt",
#     )
