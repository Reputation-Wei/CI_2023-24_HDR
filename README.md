# CI_2023-24_HDR
WS_2023/24 Uni-Siegen computational imaging project HDR


# 1. Where are the main code

We have employed two methods to merge images in the dataset into an HDR file using the code from ***hdr20240203.py***.

# 2. How does the code work

  a. First of all we use the ***exifreadfile.ps1*** to read the exif file (it's stored the properties of .jpg) and store alle the data into the file named ***exif_data.json*** which is already stored in the Dataset ***HDR_TestSuite***.
  b. then open the python file the imagepathlist with the dataset ***HDR_TestSuite*** path in you computer.
  c. change the ***output_folder = r"C:\Users\admin\Desktop\hdrimages"*** with you own path, in oder to create a folder to store the .hdr files.
  d. you need to install the package ***cv2 numpy json fractions os***.

# 3. How to generate the html of hdr

  a. you should have a linux system and install pfstool, i am recommand you to install a wsl2 in windows and use the remote connection in vscode,it helps you to connect the ubuntu system.
  b. then store the ***hdrtohtml.sh*** in you compute and run it.
  c. The HTML files will be automatically stored in your specified order, facilitated by the script named ***hdrtohtml.sh***. This script likely handles the conversion of the HDR data into HTML format and organizes the resulting files according to your predefined order or criteria.

#4. When you want to get the Dataset or have any questions please contect ***xinyu.wei@student.uni-siegen.de***
  

  
 


