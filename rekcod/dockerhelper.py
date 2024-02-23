import os

def clean_dangled_images():
    os.system("docker rmi -f $(docker images --filter 'dangling=true' -q --no-trunc)")


clean_dangled_images()
