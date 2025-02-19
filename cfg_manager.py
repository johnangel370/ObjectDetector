import yaml
from pathlib import Path

# Save configure parameters
MODEL_SETTINGS = {}
PREDICT_SETTINGS = {}
VISUAL_SETTINGS = {}

# Define keys for arg type checks
CFG_FRACTION_KEYS = "iou", "conf"  # fraction floats 0.0 - 1.0
CFG_BOOL_KEYS = (
    "save_json",
    "show",
    "save_txt",
    "save_conf",
    "save_crop",
    "save_frames",
    "show_labels",
    "show_conf",
    "show_boxes",
)
CFG_INT_KEYS = "max_det", "line_width"
CFG_FILE_KEYS = "model_path"
CFG_DIR_KEYS = "source", "destination"


# Loading configure settings from yaml
def load_yaml():
    try:
        with open('default.yaml', 'r') as file:
            config = yaml.safe_load(file)

            # checking yaml settings
            if config['model']['model_path']:
                model_file_path = config['model']['model_path']
                config['model']['model_path'] = 'ObjectDetector' / model_file_path
            args_bool, error_list = check_args(config)
            
            print(f"LOADING {colorstr('cyan', 'bold', file.name)} configurations...")

            # if configurations value is correct, save the configurations to dictionary, othrerwise print out error message
            if args_bool:
                global MODEL_SETTINGS, PREDICT_SETTINGS, VISUAL_SETTINGS
                MODEL_SETTINGS = config['model']
                PREDICT_SETTINGS = config['predict']
                VISUAL_SETTINGS = config['visual']

                print(f"Configurations loading {colorstr('green', 'bold', 'success')}!\n")
            else:
                for i in error_list:
                    print(f"⚠️  WARNING: There are {colorstr('red', 'bold', 'invalid')} arguments as the following:")
                    warn_msg(i[0], i[1])
                    print(f"Please check the {colorstr('yellow', 'bold', 'yaml')} file settings.")

    # If raise FileNotFoundError print out the error, else print other errors
    except Exception as e:
        assert type(e).__name__ == "FileNotFoundError", f"⚠️  WARNING: {type(e).__name__} is occured!"
        print(f"⚠️  WARNING: 'default.yaml' file not found in {Path.cwd()}")


# check if the yaml settings is correct
def check_args(dict) -> tuple[bool, list]:
    wrong_args_list = []
    for field in dict:
        for arg in dict[field]:
            arg_value = dict[field][arg]
            if arg in CFG_FRACTION_KEYS and arg_value != None:
                if isinstance(arg_value, float) and (0 < arg_value <= 1) == False:
                    wrong_args_list.append([arg_value, arg])
            elif arg in CFG_BOOL_KEYS and arg_value != None:
                if isinstance(arg_value, bool) == False:
                    wrong_args_list.append([arg_value, arg])
            elif arg in CFG_INT_KEYS and arg_value != None:
                if isinstance(arg_value, int) == False:
                    wrong_args_list.append([arg_value, arg])
            elif arg in CFG_FILE_KEYS and arg_value != None:
                p = Path(arg_value)
                if p.is_file() == False:
                    wrong_args_list.append([arg_value, arg])
            elif arg in CFG_DIR_KEYS and arg_value != None:
                p = Path(arg_value)
                if p.is_dir() == False:
                    wrong_args_list.append([arg_value, arg])

    if len(wrong_args_list) != 0:
        return False, wrong_args_list
    else:
        return True, wrong_args_list


# print warning messages of invalid arguments
def warn_msg(value, key):
    print(f" -- '{colorstr('red', 'bold', value)}' is not a valid YOLO argument for '{colorstr('red', 'bold', key)}'")


def colorstr(*input):
    """
    Colors a string based on the provided color and style arguments. Utilizes ANSI escape codes.
    See https://en.wikipedia.org/wiki/ANSI_escape_code for more details.

    This function can be called in two ways:
        - colorstr('color', 'style', 'your string')
        - colorstr('your string')

    In the second form, 'blue' and 'bold' will be applied by default.

    Args:
        *input (str): A sequence of strings where the first n-1 strings are color and style arguments,
                      and the last string is the one to be colored.

    Supported Colors and Styles:
        Basic Colors: 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
        Bright Colors: 'bright_black', 'bright_red', 'bright_green', 'bright_yellow',
                       'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white'
        Misc: 'end', 'bold', 'underline'

    Returns:
        (str): The input string wrapped with ANSI escape codes for the specified color and style.

    Examples:
        >>> colorstr('blue', 'bold', 'hello world')
        >>> '\033[34m\033[1mhello world\033[0m'
    """
    *args, string = input if len(input) > 1 else ("blue", "bold", input[0])  # color arguments, string
    colors = {
        "black": "\033[30m",  # basic colors
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "bright_black": "\033[90m",  # bright colors
        "bright_red": "\033[91m",
        "bright_green": "\033[92m",
        "bright_yellow": "\033[93m",
        "bright_blue": "\033[94m",
        "bright_magenta": "\033[95m",
        "bright_cyan": "\033[96m",
        "bright_white": "\033[97m",
        "end": "\033[0m",  # misc
        "bold": "\033[1m",
        "underline": "\033[4m",
    }
    return "".join(colors[x] for x in args) + f"{string}" + colors["end"]

load_yaml()


if __name__ == '__main__':
    load_yaml()
    