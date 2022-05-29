
# from constant import SUPERVISER_CREDENTIALS
import sys


def check_credentials(argv):
    from constant import SUPERVISER_CREDENTIALS
    if len(sys.argv) > 2:
        # for i in range(len(SUPERVISER_CREDENTIALS)):
        username_check = bool(SUPERVISER_CREDENTIALS[0]['username'] == sys.argv[1])
        password_check = bool( SUPERVISER_CREDENTIALS[0]['password'] == sys.argv[2])

    return username_check and password_check
