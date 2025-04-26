def parse_input(user_input):
    if not user_input:
        print("Input cannot be empty. Please enter a command.")
        return "", []
    cmd, *args = user_input.split()
    return cmd.lower(), args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner