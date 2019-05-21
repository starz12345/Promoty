import os
from time import time, sleep

from InstagramAPI import InstagramAPI

if __name__ == "__main__":
    # program start time
    start_time = time()

    # username and password
    user = str(os.environ.get('INSTA_USER'))
    password = str(os.environ.get('INSTA_PASS'))

    # access api
    api = InstagramAPI(user, password)
    api.login()


    # retrieve username from account id ==> generated from https://codeofaninja.com/tools/find-instagram-user-id
    followings = [item['username'].strip() for item in api.getTotalFollowings("5998871957")]

    with open("test.txt", "w") as file:
        file.writelines("Followings \n")
        for item in followings:
            file.writelines(item + "\n")

    print('Number of Followings:', len(followings))

    # program end time
    end_time = time()
    tot_time = end_time - start_time

    #printing run time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + ":"
          + str(int((tot_time % 3600) % 60)))
