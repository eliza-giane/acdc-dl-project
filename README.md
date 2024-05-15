**This is the Automated Cardiac Disease Challenge (ACDC) Project for Deep Learning at AIT by Eliza Giane, Shirui Li, and Lydia Yang.**


This project was prompted by the challenge (found [here](https://www.creatis.insa-lyon.fr/Challenge/acdc/index.html)). The data consists of real anonymized and regulated clinical exams from the University Hospital of Dijon, and is described as follows on the challenge's website:

---
"Our dataset covers several well-defined pathologies with enough cases to (1) properly train machine learning methods and (2) clearly assess the variations of the main physiological parameters obtained from cine-MRI (in particular diastolic volume and ejection fraction)."

"The dataset is composed of 150 exams (all from different patients) divided into 5 evenly distributed subgroups (4 pathological plus 1 healthy subject groups)...Furthermore, each patient comes with the following additional information : weight, height, as well as the diastolic and systolic phase instants."

---
 The dataset to be downloaded is found [here](https://humanheart-project.creatis.insa-lyon.fr/database/#collection/637218c173e9f0047faa00fb/folder/637218e573e9f0047faa00fc).

  <!-- and the provided code for handling .nii files is found [here](https://www.creatis.insa-lyon.fr/Challenge/acdc/code/metrics_acdc.py). -->

**Any use of the ACDC database requires the following citation:**

O. Bernard, A. Lalande, C. Zotti, F. Cervenansky, et al.
"Deep Learning Techniques for Automatic MRI Cardiac Multi-structures Segmentation and Diagnosis: Is the Problem Solved ?" in IEEE Transactions on Medical Imaging, vol. 37, no. 11, pp. 2514-2525, Nov. 2018, doi: 10.1109/TMI.2018.2837502

**Running the Model**
Please downlaod the dataset at the following [link](https://humanheart-project.creatis.insa-lyon.fr/database/#collection/637218c173e9f0047faa00fb/folder/637218e573e9f0047faa00fc). Then upload the dataset to Google Drive and move it under the directory MyDrive and then rename the folder "ACDC-Challenge". Otherwise, update the variable "dataDir" with your local file path to the database folder. 

If you have not done this (please only do it once), uncomment the cell to convert the existing files into jpeg files that we will utilize later. 

Then, please run all cells afterwards to load and pre-process the data, create the model and run it on our dataset, then evaluate the results.
