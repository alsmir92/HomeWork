# Логирование данных
def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Function name: {fn.__name__}")
        print(f"Function arguments: {args}, {kwargs}")
        result = fn(*args, **kwargs)
        print(f"Function result: {result}")
        return result

    return wrapper


@log_function_call
def mult(a, b):
    return a * b


print(mult(5, 2))

print('')


@log_function_call
def sum(a, b):
    return a + b


print(sum(a=40.3, b=20))

# Function name: mult
# Function arguments: (5, 2), {}
# Function result: 10
# 10

# Проверка аутентификации пользователя


def is_user_authenticated():
    return True  # /False


def check_user_authenticated(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated!")
            return fn(*args, **kwargs)
        else:
            raise Exception("User is NOT authenticated")

    return wrapper


@check_user_authenticated
def do_sensitive_job():
    # Do sime tasks only if user is authenticated
    print("Results of some sensitive tasks")


try:
    do_sensitive_job()
except Exception as e:
    print(e)

# True
# User is authenticated!
# Results of some sensitive tasks

# False
# User is NOT authenticated
