import sys

# import requests

print(sys.version)
print(sys.executable)


def greet(who):
    new_func()
    greeting = f"hello,{who}"
    return greeting


def new_func():
    return """
    jjjjjj
    """


# r = requests.get("https://coreyms.com")

print(greet("YJ"))
# print(r.status_code)

name = input("your name?")

print("Hello,", name)
