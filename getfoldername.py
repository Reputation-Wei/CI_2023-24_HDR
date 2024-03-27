
'''
import os

folder_path = r'C:/Users/admin/Desktop/HDR_TestSuite'

file_names = os.listdir(folder_path)

for file_name in file_names:
    print(file_name)
'''
'''''
import os

folder_path = r'C:/Users/admin/Desktop/HDR_TestSuite'
file_paths = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path)]

for file_path in file_paths:
    print(file_path)





import os

folder_path = r'C:/Users/admin/Desktop/HDR_TestSuite'
output_file = r'C:/Users/admin/Desktop/HDR_TestSuite/file_paths.txt'

file_paths = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path)]
print(file_paths)
with open(output_file, 'w') as file:
    for file_path in file_paths:
        file.write(file_path + '\n')

'''''

import os

#for file_path in file_paths:
#    print(file_path)


def get_subdirectories(folder_path):
    # 获取指定文件夹中的所有子文件夹名字
    subdirectories = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
    return subdirectories


folder_path = r'C:/Users/admin/Desktop/HDR_TestSuite'
file_paths = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path)]
print(file_paths)
# 指定文件夹路径
#folder_path = r'C:/Users/admin/Desktop/HDR_TestSuite'

# 获取所有子文件夹名字
subdirectories = get_subdirectories(folder_path)

# 输出子文件夹名字
print("Subdirectories in", folder_path, "are:", subdirectories)

['chimneys', 'dobra_tyble', 'grzyby', 'highgraphics05_1', 'highgraphics05_2', 'iona_beach_sunset', 'lampa_solna', 'luxemburg_church_1', 'luxemburg_church_2', 'luxemburg_church_3', 'mpi_atrium_1', 'mpi_office_1', 'mpi_office_2', 'mpi_office_3', 'mpi_office_4', 'nancy_cathedral_1', 'nancy_cathedral_2', 'nancy_cathedral_3', 'osoyoos_1', 'osoyoos_2', 'saltlamp_directlight', 'saltlamp_light', 'saltlamp_nolight', 'san_jose06_1', 'san_jose06_2', 'sardynia06', 'sb_drzewa', 'seymour_park', 'sylwester_w_dobrej_2005', 'toys', 'tyble', 'ubc_library', 'ubc_office', 'ubc_tree', 'usa_sunset', 'white_page_calib', 'winter_pine']