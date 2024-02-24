import os


class Dockerhelper:
    def create_dcoker_file(self,path):
        with open(os.path.join(path,"Dockerfile"),"w") as f:
            f.write("# Docker file content")
            print("Docker file created successfully")