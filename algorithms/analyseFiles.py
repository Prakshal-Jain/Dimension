import os
from shutil import copyfile

def analyser(path, targetDirectory, username):
    extensions = ['.3gp', '.aa', '.aac', '.aax', '.act', '.aiff', '.alac', '.amr', '.ape', '.au', '.awb', '.dss', '.flac', '.gsm', '.m4a', '.m4b', '.m4p', '.mp3', '.mpc', '.ogg, .oga, .mogg', '.opus', '.ra, .rm', '.raw', '.rf64', '.sln', '.tta', '.voc', '.vox', '.wav', '.wma', '.wv', '.webm', '.8svx', '.cda']
    get_user = username.split("@")[0]
    locus = os.path.join(targetDirectory, get_user)
    os.mkdir(locus) if not os.path.isdir(locus) else None
    aud_files = [f for f in os.listdir(path) if os.path.splitext(f)[1] in extensions]
    for files in aud_files:
        extension = os.path.splitext(files)[-1][1:]
        newLocus = os.path.join(targetDirectory, extension)
        if(not os.path.isdir(newLocus)):
            os.mkdir(newLocus)
        copyfile(os.path.join(path, files), "./")