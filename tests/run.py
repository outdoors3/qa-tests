from sys import argv

# here we will import tests

from login import login_prod, login_dev, linkedin_login_prod, linkedin_login_dev, facebook_login_prod, facebook_login_dev
from login import google_login_prod, google_login_dev
from password_recovery import password_recovery_prod
from registration import registration_prod
from registration import registration_prod_skip

from qalib import DCT_TESTS


if __name__ == "__main__":
    #for key in DCT_TESTS:
        #print(key + ":", DCT_TESTS[key])
    name_of_test = argv[1].upper()
    DCT_TESTS[name_of_test][-1]()
