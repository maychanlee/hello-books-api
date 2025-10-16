# from flask import Blueprint
# hello_world_bp = Blueprint("hello_world", __name__)

# # @blueprint_name.get("/endpoint/path/here")
# # def endpoint_name():
# #     my_beautiful_response_body = "Hello, World!"
# #     return my_beautiful_response_body

# @hello_world_bp.get("/")
# def say_hello_world():
#     return "Hello, World!"

# @hello_world_bp.get("/hello/JSON")
# def say_hello_json():
#     return {
#         "name": "Godzilla",
#         "message": "RAWRRRRR!",
#         "hobbies": ["eating cities", "fighting giant monsters", "swimming"],
#     }

# @hello_world_bp.get("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"] + new_hobby
#     return response_body