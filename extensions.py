extensions = (".gif", ".jpg", "jpeg", ".png", ".pdf", ".txt", ".zip")

file = input("File name: ")
for extension in extensions:
    if file.endswith(extensions):
        if file.endswith(extension):
            print(f"image/{extension.strip('.')}")
    else:
        print("application/octet-stream")

