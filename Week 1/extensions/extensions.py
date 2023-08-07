def main():
    # Ask for filename
    user_input = input("File name: ")

    # Pass filename to function to get the filetype
    get_file_type(user_input)


def get_file_extension(fn):
    # First remove any whitespace from the filename and lowercase
    fn = fn.strip().lower()
    # Get a sub string of the last 5 characters
    sub_fn = fn[-5:]
    # Split the substring on the dot
    result = sub_fn.split('.')
    # Return extension or Err on failure
    if len(result) > 1:
        return result[1]
    else:
        return "Err"


def get_file_type(fn):
    #get a cleaned extension from the filename
    extension = get_file_extension(fn)

    # Find the file type using a match statement
    match extension:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
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

main()