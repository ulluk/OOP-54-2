# def require_admin(func):
#     def wrapper(user):
#         if user.get("is_admin"):
#             return func(user)
#         else:
#             return print("Access denied")
#     return wrapper
#
#
# @require_admin
# def delete_user(user):
#     print(f"User {user['name']} deleted")
#
#
# delete_user({"name": "John", "is_admin": True})   # OK
# delete_user({"name": "Alice", "is_admin": False}) # Access denied



def logger(func):
    def wrapper():
        print("Вызов функции say_hello")
        func()
        print("Функция say_hello завершена")
    return wrapper


@logger
def say_hello():
    print("Hello")

say_hello()