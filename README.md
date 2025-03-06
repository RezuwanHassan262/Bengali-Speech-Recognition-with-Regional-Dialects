# Bengali-Speech-Recognition-with-Regional-Dialects
A character gram modeling approach towards Bengali Speech to Text with Regional Dialects

I finetuned another OpenAI's Whisper model using another advanced checkpoint from [Kaggle](https://www.kaggle.com/competitions/ben10). I then uploaded the model weights on [Hugging Face](https://huggingface.co/Rezuwan/regional_asr_weights) and deployed the model using those weights on [HuggingFace Space](https://huggingface.co/spaces/Rezuwan/Regional_Speech_ASR). 

This later checkpoint had speech data from 12 districts, Which are shown below,

|  District  |   District  | District |  District  |  District |  District | 
|------------|-------------|----------|------------|-----------|-----------|
|   Rangpur  | Kishoreganj | Narail   | Chittagong | Narsingdi | Noakhali |
|   Tangail  |  Habiganj   | Barishal |   Sylhet   |  Sandwip  | Cumilla  |

The deployment of the model on HuggingFace Spaces can be found [here](https://huggingface.co/spaces/Rezuwan/Regional_Speech_ASR).

![ASR HF space screenshot](https://raw.githubusercontent.com/RezuwanHassan262/Bengali-Speech-Recognition-with-Regional-Dialects/main/images/hf_screenshot.jpg)
