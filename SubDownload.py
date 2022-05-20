# TODO: FIX BUGS and write more exceptions
import praw
import requests
import cv2
import numpy as np
import os
import pickle
from os import path
from PIL import Image
from utils.create_token import create_token

POST_SEARCH_AMOUNT = 10

# Create directory if it doesn't exist to save images
def create_folder(image_path):
    CHECK_FOLDER = os.path.isdir(image_path)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(image_path)

def new_name(sub,image_path):
    s = sub
    a = 0
    while (path.exists(image_path+s + str(a) + ('.png'))):
        a += 1
    return s + str(a)



# Path to save images
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_path, "images/")
reduced_image_path = os.path.join(dir_path,"reduced_images/")
ignore_path = os.path.join(dir_path, "ignore_images/")
create_folder(image_path)
create_folder(reduced_image_path)

#Delete previous installation
for image in os.listdir(image_path):
    #print(image)
    if image.endswith('.png'):
        os.remove(image_path+image)
for image in os.listdir(reduced_image_path):
    #print(image)
    if image.endswith('.png'):
        os.remove(reduced_image_path+image)
print('Folders are clean')

    # Get token file to log into reddit.
# You must enter your....
# client_id - client secret - user_agent - username password
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
else:
    creds = create_token()
    pickle_out = open("token.pickle","wb")
    pickle.dump(creds, pickle_out)

reddit = praw.Reddit(client_id=creds['client_id'],
                    client_secret=creds['client_secret'],
                    user_agent=creds['user_agent'],
                    username=creds['username'],
                    password=creds['password'])


f_final = open("sub_list.csv", "r")
img_notfound = cv2.imread('imageNF.png')
for line in f_final:
    sub = line.strip()
    subreddit = reddit.subreddit(sub)

    print(f"Starting {sub}!")
    count = 0
    for submission in subreddit.hot(limit=POST_SEARCH_AMOUNT):
        if "jpg" in submission.url.lower() or "png" in submission.url.lower():
            try:
                resp = requests.get(submission.url.lower(), stream=True).raw
                image = np.asarray(bytearray(resp.read()), dtype="uint8")
                image = cv2.imdecode(image, cv2.IMREAD_COLOR)

                # Could do transforms on images like resize!
                compare_image = cv2.resize(image,(224,224))

                # Get all images to ignore
                for (dirpath, dirnames, filenames) in os.walk(ignore_path):
                    ignore_paths = [os.path.join(dirpath, file) for file in filenames]
                ignore_flag = False

                for ignore in ignore_paths:
                    ignore = cv2.imread(ignore)
                    difference = cv2.subtract(ignore, compare_image)
                    b, g, r = cv2.split(difference)
                    total_difference = cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)
                    if total_difference == 0:
                        ignore_flag = True

                if not ignore_flag:
                    #cv2.imwrite(f"{image_path}{sub}-{submission.id}.png", image)
                    cv2.imwrite(f"{image_path}{new_name(sub,image_path)}.png", image)
                    count += 1
                    
            except Exception as e:
                print(f"Image failed. {submission.url.lower()}")
                print(e)


#Optimize and reduce size
for image in os.listdir(image_path):
    #print(image)
    if image.endswith('.png'):
        foo = Image.open(image_path + image)
        try:
            foo.save(reduced_image_path + image, optimize=True, quality=95)
            print("success optimizing")
        except:
            print("Error for" + image)

#Delete not optimized images
for image in os.listdir(image_path):
    #print(image)
    if image.endswith('.png'):
        os.remove(image_path+image)