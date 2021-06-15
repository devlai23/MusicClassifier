# Imports
import numpy as np
import pandas as pd
import librosa

# File Imports
from Song import Song

from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('features_3_sec.csv')
df2 = pd.read_csv('features_30_sec.csv')

labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

df = df.drop('perceptr_var', axis=1).drop('perceptr_mean', axis=1)
df2 = df2.drop('perceptr_var', axis=1).drop('perceptr_mean', axis=1)

y = df['label']
X = df.drop('label', axis = 1).drop('filename', axis=1).drop('length', axis=1)

y2 = df2['label']
X2 = df2.drop('label', axis = 1).drop('filename', axis=1).drop('length', axis=1)

# Scale the features
cols = X.columns
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(X)

X = pd.DataFrame(np_scaled, columns = cols)

cols = X2.columns
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(X2)
X2 = pd.DataFrame(np_scaled, columns = cols)

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.1 , random_state = 42, stratify = y)
X2_train, X2_test, y2_train, y2_test = train_test_split (X2, y2, test_size = 0.1 , random_state = 42, stratify = y2)

neighbors = range(5, 20)
test_accuracy = np.empty(len(neighbors))
highest_score = 0
highest_i = 0
best_knn = 0
confus_mat = 0

for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors = k)

    # Fit the classifier to the training data
    knn.fit(X, y)

    #Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X2_test, y2_test)
    if test_accuracy[i] > highest_score:
        highest_score = test_accuracy[i]
        highest_i = k
        best_knn = knn
        
        preds = knn.predict(X_test)
        confus_mat = confusion_matrix(y_test, preds) 

knn = best_knn

def get_input_from_file(fname):
    # Extract  features
    x, fs = librosa.load(fname)

    # 'chroma_stft'
    chroma_stft = librosa.feature.chroma_stft(x, fs)
    chroma_stft_mean = np.mean(chroma_stft)
    chroma_stft_var = np.var(chroma_stft)

    # 'rms'
    rms = librosa.feature.rms(x)
    rms_mean = np.mean(rms)
    rms_var = np.var(rms)

    # 'spectral_centroid'
    spectral_centroid = librosa.feature.spectral_centroid(x, fs)
    spectral_centroid_mean = np.mean(spectral_centroid)
    spectral_centroid_var = np.var(spectral_centroid)

    # 'spectral_bandwidth'
    spectral_bandwidth = librosa.feature.spectral_bandwidth(x, fs)
    spectral_bandwidth_mean = np.mean(spectral_bandwidth)
    spectral_bandwidth_var = np.var(spectral_bandwidth)

    # 'rolloff'
    rolloff = librosa.feature.spectral_rolloff(x, fs)
    rolloff_mean = np.mean(rolloff)
    rolloff_var = np.var(rolloff)

    # 'zero_crossing_rate'
    zero_crossing_rate = librosa.feature.zero_crossing_rate(x)
    zero_crossing_rate_mean = np.mean(zero_crossing_rate)
    zero_crossing_rate_var = np.var(zero_crossing_rate)

    # 'harmony'
    # harmony = librosa.feature.tonnetz(x, fs)
    harmony = librosa.effects.harmonic(x)
    harmony_mean = np.mean(harmony)
    harmony_var = np.var(harmony)

    # Ignoring the perceptr input because I can't figure out what feature it is/how to get it
    # spect = librosa.feature.melspectrogram(x, fs)
    # freqs = librosa.fft_frequencies(fs)
    # # 'perceptr'
    # perceptr = librosa.perceptual_weighting(spect, freqs)
    # perceptr_mean = np.mean(perceptr)
    # perceptr_var = np.var(perceptr)

    # 'tempo'
    tempo = librosa.beat.tempo(x, fs)[0]

    # Find mfccs:
    # mean
    # var(iance)
    mfccs = librosa.feature.mfcc(x, sr=fs)

    inp = np.array([chroma_stft_mean, chroma_stft_var, 
                    rms_mean, rms_var, 
                    spectral_centroid_mean, spectral_centroid_var, 
                    spectral_bandwidth_mean, spectral_bandwidth_var, 
                    rolloff_mean, rolloff_var, 
                    zero_crossing_rate_mean, zero_crossing_rate_var, 
                    harmony_mean, harmony_var, 
                    tempo, 
                    np.mean(mfccs[0]), np.var(mfccs[0]),
                    np.mean(mfccs[1]), np.var(mfccs[1]),
                    np.mean(mfccs[2]), np.var(mfccs[2]),
                    np.mean(mfccs[3]), np.var(mfccs[3]),
                    np.mean(mfccs[4]), np.var(mfccs[4]),
                    np.mean(mfccs[5]), np.var(mfccs[5]),
                    np.mean(mfccs[6]), np.var(mfccs[6]),
                    np.mean(mfccs[7]), np.var(mfccs[7]),
                    np.mean(mfccs[8]), np.var(mfccs[8]),
                    np.mean(mfccs[9]), np.var(mfccs[9]),
                    np.mean(mfccs[10]), np.var(mfccs[10]),
                    np.mean(mfccs[11]), np.var(mfccs[11]),
                    np.mean(mfccs[12]), np.var(mfccs[12]),
                    np.mean(mfccs[13]), np.var(mfccs[13]),
                    np.mean(mfccs[14]), np.var(mfccs[14]),
                    np.mean(mfccs[15]), np.var(mfccs[15]),
                    np.mean(mfccs[16]), np.var(mfccs[16]),
                    np.mean(mfccs[17]), np.var(mfccs[17]),
                    np.mean(mfccs[18]), np.var(mfccs[18]),
                    np.mean(mfccs[19]), np.var(mfccs[19])
                    ])
    
    # Scale the data
    inp = min_max_scaler.transform(inp.reshape(1, -1))

    return inp.reshape(1, -1)

class GenreClassifier:
    def __init__(self):
        self.network = best_knn

    def predict(self, file):
        inp = get_input_from_file(file)
        result = self.network.predict(inp)
        s = Song(result[0])
        return s