file_name = input("File name: ").lower().strip()
suffix = file_name.rsplit(".", 1)[1]


dict = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

if not dict.get(suffix) or not suffix:
    print("application/octet-stream")

else:
    print(dict[suffix])

