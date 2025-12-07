import sys

filename = input("File name: ")
filename = filename.strip().lower()
ext = filename.rsplit(".")
if len(ext) < 2:
    print("application/octet-stream")
    sys.exit()
match ext[-1]:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
