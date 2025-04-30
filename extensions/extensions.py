file_name = input("File name: ").lower().strip()
suffix = file_name.rsplit(".", 1)

if len(suffix) > 1:
    suffix = suffix[1]
else:
    print("application/octet-stream")


dict = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

if not dict.get(suffix):
    print("application/octet-stream")

else:
    print(dict[suffix])

