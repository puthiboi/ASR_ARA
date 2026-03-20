def srtnamefrompathname(path):
    srtname = path.split("/")
    srtname = srtname[-1][:-4] + ".srt"
    return srtname

def txtfrompathname(path):
    txtname = path.split("/")
    txtname = txtname[-1][:-4] + ".txt"
    return txtname