# Bengali-Speech-Recognition-with-Regional-Dialects

**Regional-Speech** is an extensive **Bangla Speech Recognition Dataset** that enables benchmarking **Automatic Speech Recognition (ASR)** models under regional dialectal variations. This dataset captures spontaneous speech data from various regions across **Bangladesh**, ensuring diversity in phonetics, lexicon, and prosody. This repo has all the codes and relevant files/resources behind the development of the regional speech dataset. This is an ongoing project and this dataset checkpoint had speech data from 12 districts, Which are shown below,

 <h2 style=color:#fe5e21;>Project Contribution</h2>
 
- Creation of the largest ASR dataset for 12 Bangla dialects with linguist-validated annotations.
- Benchmarking study of Bangla ASR models, APIs, and foundation models on the dataset.
- An ASR model with improved accuracy for dialect-influenced speech.

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

### Key findings:
- Favorable Mean Opinion Score despite varying recording conditions
- Higher noisiness compared to studio recordings due to natural environments
- Consistent coloration characteristics across regions
- Varied loudness levels reflecting real-world recording scenarios
- Discontinuity metrics demonstrate high-quality segmentation despite spontaneous speech characteristics

The acoustic analysis confirms that our dataset captures authentic dialectal variations while maintaining sufficient audio quality for ASR applications. This makes RegSpeech particularly valuable for developing models robust to real-world dialectal diversity.
---














I finetuned another OpenAI's Whisper model using another advanced checkpoint from [Kaggle](https://www.kaggle.com/competitions/ben10). I then uploaded the model weights on [Hugging Face](https://huggingface.co/Rezuwan/regional_asr_weights) and deployed the model using those weights on [HuggingFace Space](https://huggingface.co/spaces/Rezuwan/Regional_Speech_ASR). 


The deployment of the model on HuggingFace Spaces can be found [here](https://huggingface.co/spaces/Rezuwan/Regional_Speech_ASR).

![ASR HF space screenshot](https://raw.githubusercontent.com/RezuwanHassan262/Bengali-Speech-Recognition-with-Regional-Dialects/main/images/hf_screenshot.jpg)


