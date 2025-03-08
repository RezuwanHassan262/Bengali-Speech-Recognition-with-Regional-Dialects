# Bengali-Speech-Recognition-with-Regional-Dialects

**Regional-Speech** is an extensive **Bangla Speech Recognition Dataset** that enables benchmarking **Automatic Speech Recognition (ASR)** models under regional dialectal variations. This dataset captures spontaneous speech data from various regions across **Bangladesh**, ensuring diversity in phonetics, lexicon, and prosody. This repo has all the codes and relevant files/resources behind the development of the regional speech dataset. This is an ongoing project and this dataset checkpoint had speech data from 12 districts, Which are shown below,

---

 <h2 style=color:#fe5e21;>Project Contribution</h2>
 
- Creation of the largest ASR dataset for 12 Bangla dialects with linguist-validated annotations.
- Benchmarking study of Bangla ASR models, APIs, and foundation models on the dataset.
- An ASR model with improved accuracy for dialect-influenced speech.

---

 <h2 style=color:#fe5e21;>Dataset</h2>
 
- **100+ hours** of validated transcribed spontaneous speech
- Natural conversations covering **12 distinct dialectal regions**
- Balanced gender representation across regions
- Diverse acoustic environments (indoor/outdoor recordings)
- Transcriptions validated by native dialect speakers and linguistic experts
- Rich metadata including regional statistics and linguistic features

<img src="https://github.com/user-attachments/assets/2f64606d-ebae-4dfc-beb0-740bb2d32b82" alt="District Coverage Map" width="500"/>
<p><i>Map showing the districts covered in the Regional-Speech dataset</i></p>


|  District  |   District  | District |  District  |  District |  District | 
|------------|-------------|----------|------------|-----------|-----------|
|   Rangpur  | Kishoreganj | Narail   | Chittagong | Narsingdi | Noakhali |
|   Tangail  |  Habiganj   | Barishal |   Sylhet   |  Sandwip  | Cumilla  |



<table>
  <tr>
    <td width="50%"><img src="https://github.com/user-attachments/assets/ef286d4f-7dff-4c94-86cd-0476d2d674e9" alt="Topic Distribution" width="100%"/></td>
    <td width="50%"><img src="https://github.com/user-attachments/assets/cdf2b9df-1537-45ba-b2ae-b3b450ca3e2a" alt="Gender Distribution" width="100%"/></td>
  </tr>
  <tr>
    <td align="center"><i>Gender distribution across the dataset</i></td>
    <td align="center"><i>Topic distribution of audio recordings</i></td>
  </tr>
</table>

### Regional Speech Corpus Statistics

| District     | Total Count | Total Duration | Avg Rec. Length | WPM   | Gender Distribution (M-F-B) | OOD%  | Train Count | Train Duration | Train OOD% | Test Count | Test Duration | Test OOD% | Val Count | Val Duration | Val OOD% |
|-------------|------------|----------------|----------------|-------|----------------------------|-------|------------|----------------|------------|------------|----------------|------------|----------|--------------|----------|
| Rangpur     | 1,298      | 6:00           | 16.66          | 134.42| 19-8-0                     | 51.93 | 1,038      | 4:48           | 50.60      | 130        | 0:35           | 45.17      | 130      | 0:36         | 36.22    |
| Kishoreganj | 2,049      | 9:35           | 16.80          | 118.78| 25-18-4                    | 55.71 | 1,639      | 7:42           | 62.91      | 205        | 0:58           | 48.08      | 205      | 0:55         | 55.49    |
| Narail      | 1,859      | 8:36           | 16.80          | 136.86| 21-12-4                    | 57.23 | 1,487      | 6:52           | 56.49      | 186        | 0:51           | 44.79      | 186      | 0:53         | 43.35    |
| Chittagong  | 1,757      | 8:11           | 16.56          | 134.58| 15-22-4                    | 63.83 | 1,405      | 6:35           | 62.07      | 176        | 0:47           | 64.63      | 176      | 0:48         | 57.47    |
| Narsingdi   | 1,373      | 6:20           | 16.71          | 148.53| 9-16-1                     | 54.74 | 1,099      | 5:03           | 53.84      | 137        | 0:37           | 39.79      | 137      | 0:39         | 40.80    |
| Tangail     | 1,271      | 6:12           | 17.00          | 146.52| 18-11-7                    | 32.36 | 1,017      | 5:03           | 45.13      | 127        | 0:34           | 24.74      | 127      | 0:35         | 27.02    |
| Habiganj    | 1,170      | 5:26           | 16.99          | 123.47| 19-15-0                    | 60.82 | 936        | 4:19           | 58.06      | 117        | 0:34           | 56.65      | 117      | 0:32         | 59.34    |
| Barishal    | 1,006      | 4:45           | 17.22          | 124.57| 6-7-13                     | 53.54 | 804        | 3:47           | 50.65      | 101        | 0:29           | 48.30      | 101      | 0:29         | 47.24    |
| Sylhet      | 7,624      | 36:15          | 17.35          | 128.01| 62-30-2                    | 67.75 | 6,100      | 28:51          | 66.68      | 762        | 3:42           | 58.19      | 762      | 3:42         | 60.49    |
| Sandwip     | 1,310      | 6:02           | 16.61          | 144.26| 15-9-2                     | 63.52 | 1,048      | 4:48           | 62.69      | 131        | 0:37           | 53.48      | 131      | 0:37         | 53.48    |
| Cumilla     | 318        | 1:27           | 16.12          | 166.26| 3-2-0                      | 51.40 | 254        | 1:09           | 55.16      | 32         | 0:08           | 21.77      | 32       | 0:08         | 23.26    |
| Noakhali    | 278        | 1:16           | 16.88          | 131.95| 3-4-0                      | 49.02 | 222        | 1:00           | 48.37      | 28         | 0:08           | 43.24      | 28       | 0:07         | 40.36    |
| **TOTAL**   | **21,313** | **100:15**     | **16.84 (avg)**| **135.62**| **209-148-37**         | **76.05** | **17,049** | **80:03**    | **74.82**  | **2,132**  | **10:05**     | **62.45**  | **2,132** | **10:06**    | **62.89** |

### Notes:
- **WPM (Words per Minute):** Average speech rate.
- **OOD% (Out-of-Vocabulary Percentage):** Words not in the predefined vocabulary.
- **Train/Test/Validation splits** indicate dataset partitions.



---

<h2 style=color:#fe5e21;>Linguistic Analysis</h2>


### Dialectal Variation
The RegSpeech corpus captures significant linguistic differences across regional dialects, as demonstrated in our analysis:

<img src="https://github.com/user-attachments/assets/9210d4c7-27f8-4b21-baee-dee0d402f4fb" alt="tSNE Visualization of Dialectal Features" width="700"/>
<p><i>t-SNE plot showing distribution of speech features across 12 regional dialects</i></p>

The corpus documents systematic variations in:
- **Phonology**: Different pronunciation patterns across regions
- **Lexicon**: Region-specific vocabulary and expressions
- **Prosody**: Variations in intonation, rhythm, and stress patterns
- **Syntax**: Regional grammatical constructions

Our analysis reveals that despite geographic proximity, each dialect maintains distinctive characteristics. The t-SNE visualization demonstrates considerable overlap between dialects, suggesting shared linguistic features while maintaining regional identity.

### Acoustic Analysis
Spectral analysis reveals distinctive acoustic patterns across dialects:

<img src="https://github.com/user-attachments/assets/5210b579-588b-4edd-8cb1-c35551d138e5" alt="Long-term Average Spectrum Analysis" width="700"/>
<p><i>Long-term average spectrum (LTAS) showing acoustic differences between dialects</i></p>

### Key findings from acoustic analysis:
- Each dialect shows a unique spectral profile, particularly in the 200-800 Hz range
- Sylhet and Chittagong dialects demonstrate the most distinctive acoustic patterns
- Most dialects diverge from the OOD_Train_Set baseline, highlighting the uniqueness of regional speech
- While differences exist in frequency distribution, they maintain similar overall envelope shapes

Our analysis revealed that while acoustic differences exist, they aren't sufficient to form distinct clusters, suggesting that vocabulary and pronunciation differences are more significant challenges for ASR systems than acoustic properties alone.
The acoustic analysis confirms that our dataset captures authentic dialectal variations while maintaining sufficient audio quality for ASR applications. This makes RegSpeech particularly valuable for developing models robust to real-world dialectal diversity.


### Key findings:
- Favorable Mean Opinion Score despite varying recording conditions
- Higher noisiness compared to studio recordings due to natural environments
- Consistent coloration characteristics across regions
- Varied loudness levels reflecting real-world recording scenarios
- Discontinuity metrics demonstrate high-quality segmentation despite spontaneous speech characteristics


---

 <h2 style=color:#fe5e21;>Audio Characteristics</h2>


### Recording Distribution
<table>
  <tr>
    <td width="50%">
      <img src="https://github.com/user-attachments/assets/3c9be96d-cee5-4635-9e7a-cdb435d82bf8" alt="Audio Length Distribution" width="100%"/>
    </td>
    <td width="50%">
      <img src="https://github.com/user-attachments/assets/9dcd470c-634c-433d-88cd-f1270624b9f2" alt="Transcript Length vs Audio Length" width="100%"/>
    </td>
  </tr>
  <tr>
    <td align="center"><i>Audio length distribution shows most recordings around 15 seconds</i></td>
    <td align="center"><i>Relationship between audio length and transcript length</i></td>
  </tr>
</table>

Most recordings in the dataset fall within the 12-18 second range, with none exceeding 30 seconds. We observe a positive correlation between audio length and transcript length, though with considerable variation reflecting differences in speaking rates across dialects.

### Quality Assessment

<table>
  <tr>
    <td width="50%">
      <img src="https://github.com/user-attachments/assets/63e3b6c4-8352-4258-bfc3-0e850e8f64df" alt="Mean Opinion Score Comparison" width="100%"/>
      <p align="center"><i>Mean Opinion Score</i></p>
    </td>
    <td width="50%">
      <img src="https://github.com/user-attachments/assets/cb7aa334-3e11-43ed-991f-267d8777ce86" alt="Discontinuity Comparison" width="100%"/>
      <p align="center"><i>Discontinuity</i></p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="https://github.com/user-attachments/assets/7e39b232-ae24-4880-a4d1-d40af4c5abc6" alt="Loudness Comparison" width="100%"/>
      <p align="center"><i>Loudness</i></p>
    </td>
    <td width="50%">
      <img src="https://github.com/user-attachments/assets/6b5667b5-f9c9-42b8-a138-63669d8e4ed5" alt="Noisiness Comparison" width="100%"/>
      <p align="center"><i>Noisiness</i></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <img src="https://github.com/user-attachments/assets/ecce6a30-971f-451c-8480-38907c917d22" alt="Coloration Comparison" width="50%"/>
      <p align="center"><i>Coloration</i></p>
    </td>
  </tr>
</table>

We conducted a comprehensive NISQA assessment to evaluate our dataset's audio quality compared to standard Bangla recordings. Key findings:

1. **Mean Opinion Score**: The Regional Speech corpus maintains comparable MOS ratings to standard recordings
2. **Discontinuity**: Similar or better discontinuity metrics, indicating high-quality segmentation
3. **Loudness**: Slightly lower values due to the use of mobile devices for recording
4. **Noisiness**: Higher noisiness levels reflecting authentic recording environments
5. **Coloration**: Comparable coloration characteristics between datasets

These metrics confirm that while our dataset captures authentic dialectal speech in natural environments, it maintains sufficient quality for ASR applications.



---

 <h2 style=color:#fe5e21;>Modeling</h2>


I finetuned another OpenAI's Whisper model using another advanced checkpoint from [Kaggle](https://www.kaggle.com/competitions/ben10) which is referred to as **PX12**. I then uploaded the model weights on [Hugging Face](https://huggingface.co/Rezuwan/regional_asr_weights) and deployed the model using those weights on [HuggingFace Space](https://huggingface.co/spaces/Rezuwan/Regional_Speech_ASR). Other team members later finetuned different models on different settings but PX12 outperformed them all. The details of the performance are shown below in the benchmarking section.



---

<h2 style=color:#fe5e21;>Model Benchmarking on the Test Segments of the Dataset</h2>


### Detailed Performance Stats

<div style="overflow-x: auto;">
<table>
<tr>
<th rowspan="2">Models</th>
<th colspan="2">Rangpur</th>
<th colspan="2">Kishoreganj</th>
<th colspan="2">Narail</th>
<th colspan="2">Chittagong</th>
<th colspan="2">Narsingdi</th>
<th colspan="2">Tangail</th>
<th colspan="2">Habiganj</th>
<th colspan="2">Barishal</th>
<th colspan="2">Sylhet</th>
<th colspan="2">Sandwip</th>
<th colspan="2">Cumilla</th>
<th colspan="2">Noakhali</th>
</tr>
<tr>
<th>WER</th><th>CER</th>
<th>WER</th><th>CER</th>
<th>WER</th><th>CER</th>
<th>WER</th><th>CER</th>
<th>WER</th><th>CER</th>
<th>WER</th><th>CER</th>
<th>WER</th><th>CER</th>
<th>WER</th><th>CER</th>
<th>WER</th><th>CER</th>
<th>WER</th><th>CER</th>
<th>WER</th><th>CER</th>
<th>WER</th><th>CER</th>
</tr>
<tr>
<td><b>Google ASR</b></td>
<td>0.872</td><td>0.698</td>
<td>0.525</td><td>0.291</td>
<td>0.946</td><td>0.892</td>
<td>0.913</td><td>0.881</td>
<td>0.936</td><td>0.874</td>
<td>0.920</td><td>0.845</td>
<td>0.933</td><td>0.843</td>
<td>0.977</td><td>0.954</td>
<td>0.889</td><td>0.797</td>
<td>0.874</td><td>0.771</td>
<td>0.964</td><td>0.927</td>
<td>0.528</td><td>0.277</td>
</tr>
<tr>
<td><b>YellowKing</b></td>
<td>0.942</td><td>0.723</td>
<td>0.961</td><td>0.806</td>
<td>0.914</td><td>0.663</td>
<td>0.984</td><td>0.809</td>
<td>0.937</td><td>0.727</td>
<td>0.722</td><td>0.401</td>
<td>0.943</td><td>0.704</td>
<td>0.930</td><td>0.697</td>
<td>0.950</td><td>0.703</td>
<td>0.973</td><td>0.780</td>
<td>0.717</td><td>0.400</td>
<td>0.982</td><td>0.773</td>
</tr>
<tr>
<td><b>Hishab Conformer</b></td>
<td>0.827</td><td>0.827</td>
<td>0.900</td><td>0.631</td>
<td>0.829</td><td>0.494</td>
<td>0.974</td><td>0.660</td>
<td>1.276</td><td>0.766</td>
<td>0.931</td><td>0.588</td>
<td>0.901</td><td>0.547</td>
<td>1.038</td><td>0.691</td>
<td>0.890</td><td>0.590</td>
<td>0.533</td><td>0.252</td>
<td>0.942</td><td>0.527</td>
<td>1.210</td><td>0.760</td>
</tr>
<tr>
<td><b>Tugstugi</b></td>
<td>0.917</td><td>0.847</td>
<td>0.977</td><td>0.954</td>
<td>0.958</td><td>0.847</td>
<td>0.987</td><td>0.969</td>
<td>0.979</td><td>0.943</td>
<td>0.482</td><td>0.220</td>
<td>0.860</td><td>0.784</td>
<td>0.548</td><td>0.314</td>
<td>0.916</td><td>0.820</td>
<td>0.938</td><td>0.830</td>
<td>0.957</td><td>0.888</td>
<td>0.876</td><td>0.704</td>
</tr>
<tr>
<td><b>Wav2Vec 2 Large</b></td>
<td>0.964</td><td>0.626</td>
<td>1.031</td><td>0.744</td>
<td>0.948</td><td>0.562</td>
<td>0.989</td><td>0.659</td>
<td>0.953</td><td>0.561</td>
<td>0.805</td><td>0.332</td>
<td>1.052</td><td>0.668</td>
<td>0.960</td><td>0.612</td>
<td>1.034</td><td>0.751</td>
<td>0.995</td><td>0.716</td>
<td>0.784</td><td>0.339</td>
<td>1.020</td><td>0.780</td>
</tr>
<tr>
<td><b>W2V2LM</b></td>
<td>0.915</td><td>0.450</td>
<td>1.050</td><td>0.690</td>
<td>0.953</td><td>0.516</td>
<td>0.971</td><td>0.577</td>
<td>0.960</td><td>0.545</td>
<td>0.923</td><td>0.408</td>
<td>0.974</td><td>0.473</td>
<td>0.974</td><td>0.574</td>
<td>1.011</td><td>0.584</td>
<td>0.977</td><td>0.644</td>
<td>0.911</td><td>0.405</td>
<td>0.997</td><td>0.651</td>
</tr>
<tr>
<td><b>Whisper (Medium)</b></td>
<td>1.002</td><td>0.877</td>
<td>1.060</td><td>0.891</td>
<td>0.998</td><td>0.890</td>
<td>1.000</td><td>0.885</td>
<td>0.999</td><td>0.895</td>
<td>0.998</td><td>0.883</td>
<td>1.028</td><td>0.879</td>
<td>1.005</td><td>0.901</td>
<td>1.005</td><td>0.880</td>
<td>1.008</td><td>0.886</td>
<td>1.000</td><td>0.899</td>
<td>1.143</td><td>0.846</td>
</tr>
<tr>
<td><b>PX12</b></td>
<td>0.746</td><td>0.404</td>
<td>1.005</td><td>0.745</td>
<td>0.621</td><td>0.303</td>
<td>0.833</td><td>0.439</td>
<td>0.628</td><td>0.286</td>
<td>0.377</td><td>0.129</td>
<td>0.691</td><td>0.380</td>
<td>0.792</td><td>0.444</td>
<td>0.826</td><td>0.529</td>
<td>0.906</td><td>0.611</td>
<td>0.404</td><td>0.144</td>
<td>0.870</td><td>0.590</td>
</tr>
<tr>
<td><b>Wav2Vec 2 (Large)</b></td>
<td>1.000</td><td>0.999</td>
<td>1.000</td><td>0.998</td>
<td>1.000</td><td>0.998</td>
<td>1.000</td><td>0.999</td>
<td>1.000</td><td>0.998</td>
<td>1.000</td><td>0.999</td>
<td>1.000</td><td>0.995</td>
<td>1.000</td><td>0.999</td>
<td>1.000</td><td>0.999</td>
<td>1.000</td><td>0.998</td>
<td>1.000</td><td>0.999</td>
<td>1.000</td><td>0.996</td>
</tr>
</table>
</div>



### Key Performance Insights

1. **Best Overall Model**: PX12 achieved the lowest error rates (WER: 0.725, CER: 0.417), showing particular strength with Tangail, Cumilla, and Narsingdi dialects.

2. **Regional Variations**: Performance varied significantly across regions:
   - Tangail dialect was generally easier to recognize across models
   - Sylhet, Kishoreganj, and Chittagong dialects presented more challenges

3. **Error Pattern Analysis**: 
   - Character-level errors were consistently lower than word-level errors
   - Models struggled most with dialectal vocabulary and word boundaries
   - Commercial systems (Google ASR) performed well on some dialects but struggled with regional expressions


### Notes:
- **WER (Word Error Rate)** measures the percentage of words incorrectly transcribed.
- **CER (Character Error Rate)** measures the percentage of characters incorrectly transcribed.
- **Lower WER/CER values indicate better ASR model performance.**


---

<h2 style=color:#fe5e21;>Model Deployment</h2>

I uploaded the PX12 model weights on [Hugging Face](https://huggingface.co/Rezuwan/regional_asr_weights) and deployed the model using those weights on [HuggingFace Space](https://huggingface.co/spaces/Rezuwan/Regional_Speech_ASR).

![ASR HF space screenshot](https://raw.githubusercontent.com/RezuwanHassan262/Bengali-Speech-Recognition-with-Regional-Dialects/main/images/hf_screenshot.jpg)
