from picture import Picture, Face
from video import VideoFile
import sys


surat  = Face(sys.argv[1])

vid = VideoFile(sys.argv[2])

numpics = 0
success = 0

for i in range(int(vid.info.frame_count)):
    state, pic = vid.export_image()
    pic.find_faces()
    numpics += len(pic.faces)
    if len(pic.faces) > 0:
        
        
        
        if True in surat.face_match(pic):
            success +=1
        
        print("In frame %d, found %d faces  total %d  successful %d  ratio  %f" % (i, len(pic.faces), numpics, success, ( success / (numpics  * 1.0) * 100)))
