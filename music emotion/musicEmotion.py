from sys import pycache_prefix
import tensorflow as tf
import pydub
import wave
import scipy as sp
import matplotlib.pyplot as plt

mmodel=tf.keras.models.load_model('music_emotion.h5')

mdic={0:"Happy", 1:"Sad", 2:"Neutral", 3:"Happy"}
def mpredict(filepath:str):
    if ".mp3" in filepath:
        pydub.AudioSegment.from_mp3(filepath).export(filepath.replace('32kps/', 'wav/').replace('.mp3', '.wav'), format="wav")
        print(filepath)
    if ".wav" in filepath:
        wo = wave.open(filepath, 'rb' )
        chunk = 65536
        data = sp.fromstring(wo.readframes(chunk), sp.int16)
        srate = wo.getframerate()
        nFFT = 1024
        window = sp.hamming(nFFT)

        fig, ax = plt.subplots(1)
        fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
        ax.set_axis_off()
        Pxx, freq, bins, im = ax.specgram(data,
                                        NFFT=nFFT,
                                        Fs=srate,
                                        noverlap=512,
                                        window=window)
        plt.savefig(filepath.replace('wav', 'png'))
        plt.close(fig)



