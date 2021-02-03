'''
-*- coding:utf-8 -*-
Author: 何新辰Xinchen He
Date: 2021/1/28 12:40
'''




import numpy as np


def ReadKML(kml_path):
    # Read KML file and find all coordinates, save them to lists
    with open(kml_path, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        content = []
        num = len(lines)
        for i in range(num):
            # Clean the /t at the beginning of the string
            lines[i] = lines[i].strip()
            if lines[i].startswith('<coordinates>') == True:
                # Eliminate the <coordinates>.numbers remains
                content.append(lines[i+1])
                break
            else:
                continue
    return content

def get_coordinates(content):
    polygon_num = len(content)
    polygon_dict = {} # a dict object for each polygon
    
    for i in range(polygon_num):
        # transform the list object to ndarray 
        polygon_dict[i] = np.array(content[i].split(','))
        # convert string to float
        num2 = len(polygon_dict[i])
        for j in range(num2):
            if polygon_dict[i][j].startswith('0') is True:
                polygon_dict[i][j] = polygon_dict[i][j][2:]
                
        polygon_dict[i] = polygon_dict[i][0:-1] # because the last element is empty
        polygon_dict[i] = np.array(list((map(float, polygon_dict[i]))))# convert all string to float
        
        # reshape them into two dimension array
        polygon_dict[i] = polygon_dict[i].reshape([int(num2/2), 2])
        
    return polygon_dict


if __name__ == '__main__':
    print('Author: Xinchen He; Date: 2020.1.28')
    print('------------------------------------')
    print('Affliation: Department of Civil and Environmental Engineering, University of Massachusetts, Amherst')
    print('------------------------------------')
    print("Without the original author or copyright holder's permission, it cannot be used for any activity of production")
    print('------------------------------------')
    
    input_path = input("Input the name of your kml file (including .kml). Example:Changjiang.kml:")
    content = ReadKML(input_path)
    polygon_dict = get_coordinates(content)
    out_dir = input('Input a the name of the output dir that already exists. Example: shapfiles :')
    for i in range(len(polygon_dict)):
        outpath = out_dir + '/Polygon' + str(i) + '.csv'
        np.savetxt(outpath, polygon_dict[i], delimiter=',')
