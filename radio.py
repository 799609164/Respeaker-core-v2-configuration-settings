import pyaudio 
import wave 
from datetime import datetime
import os 


WAVE_OUTPUT_FILENAME = datetime.now().strftime("%Y%m%d_%H%M") + ".wav"
SAVE_PATH = '/home/respeaker/Desktop/test/' + datetime.now().strftime("%Y%m%d") + '/'
FILE_PATH = SAVE_PATH + WAVE_OUTPUT_FILENAME
class MyRecord():
    def __init__(self):

        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16 
        self.CHANNELS = 1 
        self.RATE = 16000
        self.RECORD_SECONDS = 5 
   
    def recording(self):
        p = pyaudio.PyAudio() 
        stream = p.open(format=self.FORMAT, 
                        channels=self.CHANNELS, 
                        rate=self.RATE, 
                        input=True, 
                        frames_per_buffer=self.CHUNK) 

        print('录音中...') 

        frames = [] 

        for i in range(0, int(self.RATE /self.CHUNK * self.RECORD_SECONDS)): 
            data = stream.read(self.CHUNK) 
            frames.append(data) 
        print('录音完成！') 

        stream.stop_stream() 
        stream.close() 
        p.terminate() 

        if (os.path.exists(SAVE_PATH)):
            pass
        else:
            os.mkdir(SAVE_PATH)
            print('文件夹创建成功!!!')

        wf = wave.open(FILE_PATH, 'wb') 
        wf.setnchannels(self.CHANNELS) 
        wf.setsampwidth(2) 
        wf.setframerate(self.RATE) 
        wf.writeframes(b''.join(frames)) 
        wf.close()

        print(WAVE_OUTPUT_FILENAME,'保存成功！')

if __name__=='__main__':
    r = MyRecord()
    r.recording()