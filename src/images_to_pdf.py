import os
import shutil
from PIL import Image
import datetime

input_dir = "C:/dev/CAP/Q_pdf/input"
output_dir = "C:/dev/CAP/Q_pdf/output"
output_file= "scan.pdf" 

def generate_pdf():
    imagesRGB=[]
    entries=os.listdir(input_dir)
    for entry in entries:
        print(entry)
        image = Image.open(input_dir+"/"+entry)
        imageRGB = image.convert('RGB')
        imagesRGB.append(imageRGB)
    firstImageRGB = imagesRGB.pop(0) 
    firstImageRGB.save(output_dir+"/"+output_file,save_all=True, append_images=imagesRGB)

def main():
    # init output dirctory
    try:
        shutil.rmtree(output_dir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir(output_dir)
    start_time = datetime.datetime.now()
    print(start_time)
    generate_pdf();
    end_time = datetime.datetime.now()
    print("------------------------------")
    print("Started at : " + str(start_time))
    print("Ended   at : " + str(end_time))

if __name__ == '__main__':
    main()