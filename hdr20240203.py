import cv2 as cv
import numpy as np
import json
from fractions import Fraction
import numpy as np
import os

def read_exif(json_file_path):
    with open(json_file_path, 'r',encoding='utf-16') as json_file:
        data = json.load(json_file)

    image_list_name = []
    exposure_time = []
    # 遍历图像列表
    for idx,image_tags in enumerate(data, start=1):
        #print(f"\nImage {idx}:")
        image_list_name.append(image_tags.get("SourceFile", "N/A"))
        string_variable = image_tags.get("ExposureTime", "N/A")
        f_variable = Fraction(string_variable)
        float_value = np.float32(f_variable)
        exposure_time.append(float_value)
    
    exposure_times = np.array(exposure_time,dtype=np.float32)
    img_list = [cv.imread(fn) for fn in image_list_name]
    return exposure_times,img_list
#print(exposure_times)
#print(image_list_name)

def hdrgenerate(img_list,exposure_times):
    # CRF Dev
    calibrateDebevec = cv.createCalibrateDebevec()
    responseDebevec = calibrateDebevec.process(img_list, exposure_times)
    # merge Dev
    merge_debevec = cv.createMergeDebevec()
    hdr_debevec = merge_debevec.process(img_list, exposure_times, responseDebevec)


    #CRF Robertson
    CalibrateRobertson =cv.createCalibrateRobertson()
    responseRo = CalibrateRobertson.process(img_list,exposure_times)
    # merge robortson
    merge_robertson = cv.createMergeRobertson()
    hdr_robertson = merge_robertson.process(img_list, exposure_times, responseRo)
    #生成hdr图片
    return hdr_debevec,hdr_robertson

imagepathlist=[r"C:\Users\admin\Desktop\HDR_TestSuite\chimneys",
r"C:\Users\admin\Desktop\HDR_TestSuite\dobra_tyble",
r"C:\Users\admin\Desktop\HDR_TestSuite\grzyby",
r"C:\Users\admin\Desktop\HDR_TestSuite\highgraphics05_1",
r"C:\Users\admin\Desktop\HDR_TestSuite\highgraphics05_2",
r"C:\Users\admin\Desktop\HDR_TestSuite\iona_beach_sunset",
#r"C:\Users\admin\Desktop\HDR_TestSuite\lampa_solna",
r"C:\Users\admin\Desktop\HDR_TestSuite\luxemburg_church_1",
r"C:\Users\admin\Desktop\HDR_TestSuite\luxemburg_church_2",
r"C:\Users\admin\Desktop\HDR_TestSuite\luxemburg_church_3",
#r"C:\Users\admin\Desktop\HDR_TestSuite\mpi_atrium_1",
r"C:\Users\admin\Desktop\HDR_TestSuite\mpi_office_1",
r"C:\Users\admin\Desktop\HDR_TestSuite\mpi_office_2",
r"C:\Users\admin\Desktop\HDR_TestSuite\mpi_office_3",
r"C:\Users\admin\Desktop\HDR_TestSuite\mpi_office_4",
r"C:\Users\admin\Desktop\HDR_TestSuite\nancy_cathedral_1",
r"C:\Users\admin\Desktop\HDR_TestSuite\nancy_cathedral_2",
r"C:\Users\admin\Desktop\HDR_TestSuite\nancy_cathedral_3",
r"C:\Users\admin\Desktop\HDR_TestSuite\osoyoos_1",
r"C:\Users\admin\Desktop\HDR_TestSuite\osoyoos_2",
r"C:\Users\admin\Desktop\HDR_TestSuite\saltlamp_directlight",
r"C:\Users\admin\Desktop\HDR_TestSuite\saltlamp_light",
r"C:\Users\admin\Desktop\HDR_TestSuite\saltlamp_nolight",
r"C:\Users\admin\Desktop\HDR_TestSuite\san_jose06_1",
r"C:\Users\admin\Desktop\HDR_TestSuite\san_jose06_2",
r"C:\Users\admin\Desktop\HDR_TestSuite\sardynia06",
#r"C:\Users\admin\Desktop\HDR_TestSuite\sb_drzewa",
r"C:\Users\admin\Desktop\HDR_TestSuite\seymour_park",
r"C:\Users\admin\Desktop\HDR_TestSuite\sylwester_w_dobrej_2005",
r"C:\Users\admin\Desktop\HDR_TestSuite\toys",
r"C:\Users\admin\Desktop\HDR_TestSuite\tyble",
r"C:\Users\admin\Desktop\HDR_TestSuite\ubc_library",
r"C:\Users\admin\Desktop\HDR_TestSuite\ubc_office",
r"C:\Users\admin\Desktop\HDR_TestSuite\ubc_tree",
r"C:\Users\admin\Desktop\HDR_TestSuite\usa_sunset",
r"C:\Users\admin\Desktop\HDR_TestSuite\white_page_calib",
r"C:\Users\admin\Desktop\HDR_TestSuite\winter_pine"]

picturename=['chimneys', 'dobra_tyble', 'grzyby', 'highgraphics05_1', 
 'highgraphics05_2', 'iona_beach_sunset', 
 'luxemburg_church_1', 'luxemburg_church_2', 'luxemburg_church_3', 'mpi_office_1', 'mpi_office_2', 'mpi_office_3', 
 'mpi_office_4', 'nancy_cathedral_1', 'nancy_cathedral_2', 
 'nancy_cathedral_3', 'osoyoos_1', 'osoyoos_2', 
 'saltlamp_directlight', 'saltlamp_light', 'saltlamp_nolight', 
 'san_jose06_1', 'san_jose06_2', 'sardynia06', 
 'seymour_park', 'sylwester_w_dobrej_2005', 'toys', 
 'tyble', 'ubc_library', 'ubc_office', 'ubc_tree', 'usa_sunset', 
 'white_page_calib', 'winter_pine']
#json_file_path = []
# 创建一个文件夹来保存图片
output_folder = r"C:\Users\admin\Desktop\hdrimages"
os.makedirs(output_folder, exist_ok=True)
for i,path in enumerate(imagepathlist):
    json_file_path = path + r"\exif_data.json"
    exposure_times,img_list = read_exif(json_file_path) 
    hdr_debevec,hdr_robertson = hdrgenerate(img_list,exposure_times) 
    #思考！！！！outputpath = " "
    filename = picturename[i]
    output_pathde = os.path.join(output_folder, filename+"_de.hdr")
    output_pathro = os.path.join(output_folder, filename+"_ro.hdr")
    # 保存图片
    cv.imwrite(output_pathde, hdr_debevec)
    cv.imwrite(output_pathro, hdr_robertson)


    #cv.imwrite(path+r"\picturename(i)_de.hdr",hdr_debevec)
    #cv.imwrite(path+r"\Ro.hdr",hdr_robertson)