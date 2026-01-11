user = input("status: ")
def check_admin(func):
    def wrapper(*args, **kwargs):
        if user == "admin":
            func(*args, **kwargs)
        else:
            print(f"user is not admin but he is {user}")
        return None
    return wrapper
@check_admin 
def delete_system() -> None: #clears the screen using the os system
    print("deleting system")
intent = input("would u like to delete the system")
if intent=="yes":
    delete_system()
else:
    print("have a nice day!")