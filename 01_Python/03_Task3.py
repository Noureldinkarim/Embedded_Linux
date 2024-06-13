import os


env_vars = ['PATH','USER']


def get_env_variable(var_name):
    return os.getenv(var_name)


for var in env_vars:
    value = get_env_variable(var)
    if value is None:
        print("variable is not set")
    else:
        print(f"Variable = {value}")