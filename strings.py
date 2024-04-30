EMAIL_PASSWORD_EMPTY = {
    "success": False,
    "message": "Email and Password cannot be empty!",
}
INVALID_PASSWORD = {"success": False, "message": "Password is Incorrect!"}
INVALID_EMAIL = {"success": False, "message": "Email is Incorrect!"}

LOGIN_SUCCESS = {"success": True, "message": "Login Success!"}
LOGOUT_SUCCESS = {"success": True, "message": "Logout Successfully!"}
REGISTRATION_SUCCESS = {"success": True, "message": "Registered Successfully!"}
BAD_CREDENTIALS = {"success": False, "message": "Bad Credentials"}
UNAUTHORIZED = {"success": False, "message": "Unauthorized access"}

# Event Organizer data

NAME_EMPTY = {"success": False, "message": "Name is required!"}
ADDRESS_EMPTY = {"success": False, "message": "Address is required!"}
EMAIL_EMPTY = {"success": False, "message": "Email is required!"}
PASSWORD_EMPTY = {"success": False, "message": "Password is required!"}
STATUS_EMPTY = {"success": False, "message": "Status is required!"}
EMAIL_EXISTS = {"success": False, "message": "Username already exists!"}

# Events
NO_EVENTS = {"success": False, "message": "No Events at the moment"}
EVENT_DOESNT_EXIST = {"success": False, "message": "Event does not exist."}
EVENT_NAME_EMPTY = {"success": False, "message": "Event name is required!"}
EVENT_DATE_EMPTY = {"success": False, "message": "Event date is required!"}
EVENT_EXISTS = {"success": False, "message": "Event already existed!"}
EVENT_SUCESS = {"success": True, "message": "Event created sucCessfully!"}
EVENT_RETRIEVED = {"success": True, "message": "Events retrieved successfully"}

# Photographer
PHOTOGRAPHER_EXISTS = {"success": False, "message": "Photographer already registered!"}
PHOTOGRAPHER_REGISTERED_SUCCESSFULLY = {
    "success": True,
    "message": "Photographer registered sucCessfully!",
}
GET_PHOTOGRAPHERS = {"success": True, "message": "Photographers retrieved successfully"}
NO_PHOTOGRAPHERS = {
    "success": False,
    "message": "No registered photographers at the moment",
}


# Runner
FIRST_NAME_EMPTY = {"success": False, "message": "First name is required!"}
LAST_NAME_EMPTY = {"success": False, "message": "Last name is required!"}
BIB_NO_EMPTY = {"success": False, "message": "BIB Number is required!"}
RUNNER_REGISTRATION_SUCCESSFUL = {
    "success": True,
    "message": "Runner registered successfully!",
}
NO_RUNNERS = {"success": False, "message": "No Runners registered at the moment"}
NO_SINGLE_RUNNER = {"success": False, "message": "Runner doesn't exists"}

# Upload Image
NO_IMAGES_INSERTED = {"message": "No inserted images"}
IMAGE_SUCCESS = {"message": "Uploaded images successfully"}
