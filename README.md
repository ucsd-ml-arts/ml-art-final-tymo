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

## Model/Data

Briefly describe the files that are included with your repository:
- We took a model of Nvidia's StyleGAN trained on paintings as the starting point for our transfer learning approach. This can be found [here](https://drive.google.com/uc?id=1eYHcNrI_kLRfWnC9Kb8xbak6548vTuyt).
- Our training daata consists of over 20,000 images of guitars scraped from popular websites for selling guitars, such as guitarcenter. 
The initially scraped images are 220x220, which we upscaled with upscale.py to 512x512. 
The upscaled dataset can be found [here](https://drive.google.com/file/d/1o78zBU8C7AOalezWDrZhzxm5k2OnLaeJ/view).

## Code

Your code for generating your project:
- Python: upscale.py - upscales the image set from 220x220 to 512x512.
- Python: remove220.py - removes images that are 220x220 from a directory.
- Jupyter notebooks: StyleGANGuitarGenerator.ipynb - generates guitar designs via transfer learning

## Results

Documentation of your results in an appropriate format, both links to files and a brief description of their contents:
- What you include here will very much depend on the format of your final project
  - image files (`.jpg`, `.png` or whatever else is appropriate)
  - 3d models
  - movie files (uploaded to youtube or vimeo due to github file size limits)
  - audio files
  - ... some other form

## Technical Notes

Any implementation details or notes we need to repeat your work. 
- Does this code require other pip packages, software, etc?
- Does it run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

References to any papers, techniques, repositories you used:
- Papers
- Repositories
- Blog posts
