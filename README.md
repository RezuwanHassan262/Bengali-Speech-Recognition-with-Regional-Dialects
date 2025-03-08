# Bengali-Speech-Recognition-with-Regional-Dialects
A character gram modeling approach towards Bengali Speech to Text with Regional Dialects

**Regional-Speech** is an extensive **Bangla Speech Recognition Dataset** that enables benchmarking **Automatic Speech Recognition (ASR)** models under regional dialectal variations. This dataset captures spontaneous speech data from various regions across **Bangladesh**, ensuring diversity in phonetics, lexicon, and prosody. This repo has all the codes and relevant files/resources behind the development of the regional speech dataset. This is an ongoing project and this dataset checkpoint had speech data from 12 districts, Which are shown below,


<img src="https://github.com/user-attachments/assets/2f64606d-ebae-4dfc-beb0-740bb2d32b82" alt="District Coverage Map" width="500"/>
<p><i>Map showing the districts covered in the Regional-Speech dataset</i></p>


|  District  |   District  | District |  District  |  District |  District | 
|------------|-------------|----------|------------|-----------|-----------|
|   Rangpur  | Kishoreganj | Narail   | Chittagong | Narsingdi | Noakhali |
|   Tangail  |  Habiganj   | Barishal |   Sylhet   |  Sandwip  | Cumilla  |

I finetuned another OpenAI's Whisper model using another advanced checkpoint from [Kaggle](https://www.kaggle.com/competitions/ben10). I then uploaded the model weights on [Hugging Face](https://huggingface.co/Rezuwan/regional_asr_weights) and deployed the model using those weights on [HuggingFace Space](https://huggingface.co/spaces/Rezuwan/Regional_Speech_ASR). 


The deployment of the model on HuggingFace Spaces can be found [here](https://huggingface.co/spaces/Rezuwan/Regional_Speech_ASR).

![ASR HF space screenshot](https://raw.githubusercontent.com/RezuwanHassan262/Bengali-Speech-Recognition-with-Regional-Dialects/main/images/hf_screenshot.jpg)


