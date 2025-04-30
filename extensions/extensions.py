file_name = input("File name: ").lower()
suffix = file_name.split(".")[1]

dict = {
    "gif": "image/gif",
    "jpg": "image/jpg",
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

