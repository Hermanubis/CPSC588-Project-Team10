# CPSC588-Project-Team10
Our project is a collaboration with the Yale Radiology Department to integrate generative AI into medical education, focusing on case-based learning and differential diagnosis generation. Our approach entailed developing a model that generates clinical vignettes from patient medical information and the generation of educational questions from radiology websites and patient cases. The result is a dual-component system that not only provides a model for clinical vignette generation from case files, but also a generative AI pipeline for educational content generation while offering a user-friendly interface for assisting medical researchers. Through this project, we aim to provide a solution to leverage the power of generative AI to significantly enhance educational workflows for medical researchers and educators, while providing a streamlined process for educational content generation. Code as available at \url{https://github.com/Hermanubis/CPSC588-Project-Team10}. 


## Experimental Environment Set up

We use deployment of the model hosted by HuggingFace and accessing the model through the HuggingFace API.

For using "llama2.ipynb", you need to submit a [questionaire](https://huggingface.co/meta-llama/Llama-2-7b)
Moreover, you need to create a (free) account on HuggingFace, which you can do [by following this link](https://huggingface.co/join). Then, you will need to generate an access token (so that you can call the API programmatically). To do this, [go to this page](https://huggingface.co/settings/tokens) after you have logged in; click the "New token" button, and generate a token with role "read". Once you have done this, then you will be able to view the token that you just generated.

For using the rest code, you don't need to submit any questionaire. 

## Dependency Installment

We have a "requirement.txt"

To work with the packages, you have to install them. You can do this by using the command prompt or terminal.

Type this command:

pip install -r requirements.txt