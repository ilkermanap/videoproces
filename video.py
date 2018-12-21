import cv2
from picture import Picture


class VideoInfo:
    def __init__(self, capturer):
        self.capturer = capturer
        self.frame_width  = capturer.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.frame_height = capturer.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.frame_rate   = capturer.get(cv2.CAP_PROP_FPS) 
        self.frame_count  = capturer.get(cv2.CAP_PROP_FRAME_COUNT)

    def current_frameno(self):
        return self.capturer.get(cv2.CAP_PROP_POS_FRAMES)

    def current_msecond(self):
        return self.capturer.get(cv2.CAP_PROP_POS_MSEC)

    
class VideoFile:
    def __init__(self, fname):
        self.fname = fname
        self.capture = cv2.VideoCapture(fname)
        self.info = VideoInfo(self.capture)

    def get_frame(self):
        state, img = self.capture.read()
        
    def save_frame(self):
        """
        save current frame
        """
        frame_file_name = "%s_%d.jpg" % (self.fname, int(self.info.current_frameno()))
        print(frame_file_name)
        state, img = self.capture.read()
        if state is True: 
            cv2.imwrite(frame_file_name, img)
            return True
        return False

    def check_skin(self):
        state, img = self.capture.read()
        print(state)
        if state is True:
            p = Picture.fromarray(img)
            x = p.check_skin()
            return x
        
    def export_image(self):
        state, img = self.capture.read()
        if state is True:
            return True, Picture.fromarray(img)
        return False, None
        
    def reopen(self):
        self.capture.release()
        self.capture = None
        self.capture = cv2.VideoCapture(self.fname)
        self.info = VideoInfo(self.capture)
        
    def locate_frame(self, frame_no):
        if frame_no > self.info.frame_count:
            #eger dosya sonundan daha ileride frame istemissek, hata
            #verebilir ya da son framei getirebiliriz
            frame_no = self.info.frame_count
        current = self.info.current_frameno()
        if frame_no > current: #gidecegimiz frame ileride ise
            for i in range(int(frame_no - current)):
                self.capture.grab()
        else:  #gidecegimiz frame geride ise
            self.reopen()
            for i in range(int(frame_no)):
                self.capture.grab()
    
        
    def report(self):
        print( "Dosya   :",self.fname)
        print( "frame x :",self.info.frame_width)
        print( "frame y :",self.info.frame_height)
        print( "fps     :",self.info.frame_rate)
        print( "currentf:", self.info.current_frameno())
        
        
if __name__ == "__main__":
    v = VideoFile("test.mp4")
    v.report()
    v.locate_frame(13000)
    v.check_skin()
    



