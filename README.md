# Final Project

Tyler Farnan, tfarnan@ucsd.edu
Mo Rahman m2rahman@ucsd.edu

## Abstract Proposal

Wouldn't it be cool to generate guitar styles that don't yet exist? 
Taking inspiration from state of the art GAN results like https://thispersondoesnotexist.com/, we created a basic implementation of GuitarGAN to create images of new guitar shapes and designs.  
Our creative goal is to produce photo realistic guitar images that are able to be produced in real life. 
For the final project we will improve the resolution of our model by: 

1) Expanding the dataset

2) Implement transfer learning on a pre-trained state-of-the-art StyleGAN, built by Nvidia. 

3) Implement a super-resolution model. 
We will present a brief visual presentation on various models' ability to produce real guitar images.

## Project Report

The link to our report can be found [here](https://docs.google.com/document/d/1dDCi19-xLcYT7hmHqI1JnoV5mDxdI6bjvoTEdLlQsa8/edit?usp=sharing).

The report can also be found in the root directory as FinalReport.pdf.

## Model/Data

Model:
- We took a model of Nvidia's StyleGAN trained on paintings as the starting point for our transfer learning approach. 
- This can be found [here](https://drive.google.com/uc?id=1eYHcNrI_kLRfWnC9Kb8xbak6548vTuyt).

Data:
- Our training data consists of over 20,000 images of guitars scraped from popular websites for selling guitars, such as guitarcenter. 
- The initially scraped images are 220x220, which we upscaled with upscale.py to 512x512. 
- The upscaled dataset can be found [here](https://drive.google.com/file/d/1o78zBU8C7AOalezWDrZhzxm5k2OnLaeJ/view).

## Code

The StyleGAN and relevant files can be found in the root directory, other files in OtherTechniques directory:
- Python: upscale.py - upscales the image set from 220x220 to 512x512.
- Python: remove220.py - removes images that are 220x220 from a directory.
- Jupyter Notebook: StyleGANGuitarGenerator.ipynb - generates guitar designs via transfer learning
- Jupyter Notebook: OtherTechniques/Guitar_DCGAN.ipynb - Generated guitars via Deep Convolutional GAN
- Jupyter Notebook: OtherTechniques/style_transfer_keras.ipynb - Generate style transfers applied onto guitars
- Python: OtherTechniques/srgan.py - Uses super resolution to (poorly) upscale guitars

## Results

All results can be found in the Results directory:
- StyleGAN/StyleGANGuitars.png - Results of StyleGAN transfer learning method trained on set of 1,361 images
- DCGAN/DCGAN3k.png - Results of DCGAN trained on set of 3,000 images
- DCGAN/DCGAN20k.png - Results of DCGAN trained on set of 20,000 images
- StyleTransfer/StyleResult1.jpg - Result of style transfer taking the style of one guitar and placing on another
- StyleTransfer/StyleResult2.jpg - Result of style transfer taking the style of an album cover and placing a guitar
- SuperResolution/SuperResAfter.png - Result of implementing super resolution model onto guitar from dataset
- TCGAN/TCGANResult.jpg - (Unintentional) Results of TCGAN

## Technical Notes

To work through the StyleGAN notebook, the code needs to run on Google CoLab.
Other files can work directly through datahub.

## Reference

Blog posts and repositories used:
- Repositories: [Super Resoluton](https://github.com/tensorlayer/srgan), [Transfer Learning](https://github.com/ak9250/stylegan-art)
- Blog posts: [Making Anime Faces with StyleGAN](https://www.gwern.net/Faces#transfer-learning)
