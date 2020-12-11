import getpass


class ArgsHelper(object):

    @staticmethod
    def check_arg(arg_name, arg_string, default=None, is_password=False):
        if arg_name is None:
            if is_password:
                arg_name = getpass.getpass("Please enter %s: " % arg_string)
            else:
                arg_name = input("Please enter %s: " % arg_string) or default
            if arg_name is None:
                print("No %s was not specified. Exiting..." % arg_string)
                exit(1)
        return arg_name
