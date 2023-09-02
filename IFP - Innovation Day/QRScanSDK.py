from dbr import *
from time import sleep
import math



class Point :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
    
    def midpoint(self,other) :
        return Point((self.x+other.x)/2, (self.y+other.y)/2)

    def distance(self, other) :

        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __lt__(self, other) :
        return self.x < other.x

    def __gt__(self, other) :
        return self.x > other.x
    
def QRScan(product,image_name) :
        
        print(" Scan Function Started ........")

    
    # set license
        BarcodeReader.init_license("t0072oQAAAK29s8QVQiRQwDjZDQIOvIewCfBwhNmgHXuC4LJxeirJEIAJyXS3Nmo6j/AveR4yAMhs1hkzM+rAcsNoeH9h8FbPHSJA")

        # initialize barcode reader
        reader = BarcodeReader.get_instance()

        # Get runtime settings
        settings = reader.get_runtime_settings()
        settings.barcode_format_ids = EnumBarcodeFormat.BF_ALL
        settings.barcode_format_ids_2 = EnumBarcodeFormat_2.BF2_POSTALCODE | EnumBarcodeFormat_2.BF2_DOTCODE
        settings.barcode_complement_modes[0] = EnumBarcodeComplementMode.BCM_GENERAL
        settings.grayscale_transformation_modes[0] = EnumGrayscaleTransformationMode.GTM_ORIGINAL
        settings.grayscale_transformation_modes[1] = EnumGrayscaleTransformationMode.GTM_INVERTED
        settings.deformation_resisting_modes[0] = EnumDeformationResistingMode.DRM_BROAD_WARP
        settings.deformation_resisting_modes[1] = EnumDeformationResistingMode.DRM_LOCAL_REFERENCE
        settings.deformation_resisting_modes[2] = EnumDeformationResistingMode.DRM_DEWRINKLE
        settings.scale_up_modes[0] = EnumScaleUpMode.SUM_LINEAR_INTERPOLATION
        settings.image_preprocessing_modes[0] = EnumImagePreprocessingMode.IPM_GRAY_EQUALIZE
        settings.image_preprocessing_modes[1] = EnumImagePreprocessingMode.IPM_GRAY_SMOOTH
        settings.image_preprocessing_modes[2] = EnumImagePreprocessingMode.IPM_SHARPEN_SMOOTH
        settings.image_preprocessing_modes[3] = EnumImagePreprocessingMode.IPM_MORPHOLOGY
        settings.excepted_barcodes_count = 8
        reader.update_runtime_settings(settings)
        reader.set_mode_argument("ScaleUpModes", 0, "AcuteAngleWithXThreshold", "0")
        reader.set_mode_argument("ScaleUpModes", 0, "ModuleSizeThreshold", "3")
        reader.set_mode_argument("ScaleUpModes", 0, "TargetModuleSize", "8")
        reader.set_mode_argument("ImagePreprocessingModes", 0, "Sensitivity", "9")
        reader.set_mode_argument("ImagePreprocessingModes", 1, "SmoothBlockSizeX", "10")
        reader.set_mode_argument("ImagePreprocessingModes", 1, "SmoothBlockSizeY", "10")
        reader.set_mode_argument("ImagePreprocessingModes", 2, "SharpenBlockSizeX", "5")
        reader.set_mode_argument("ImagePreprocessingModes", 2, "SharpenBlockSizeY", "5")
        reader.set_mode_argument("ImagePreprocessingModes", 3, "MorphOperation", "Close")
        reader.set_mode_argument("ImagePreprocessingModes", 3, "MorphOperationKernelSizeX", "7")
        reader.set_mode_argument("ImagePreprocessingModes", 3, "MorphOperationKernelSizeY", "7")

        # print(reader.getParameters())

        # Set runtime settings
        # ret = reader.setParameters(settings)
        # print(ret)

        # decodeFile()
        results = reader.decode_file("images\{}".format(image_name))
        # print('Elapsed time: ' + str(elapsed_time) + 'ms')


        
        QR_Codes = {} 
        QR_count = 1
        for result in results:
            print(result.barcode_format_string, QR_count)
            print(result.barcode_text)
            
            resPoints = result.localization_result.localization_points
            resPoint1 = resPoints[0]
            resPoint3 = resPoints[2]
            print(resPoint1, resPoint3)
            print('-----------------------------------')

            mydata = result.barcode_text
            if mydata not in QR_Codes and mydata != product :
                point1 = Point(resPoint1[0], resPoint1[1])
                point2 = Point(resPoint3[0], resPoint3[0])
                QR_Codes[mydata] = point1.midpoint(point2)
            
            if mydata == product :
                point1 = Point(resPoint1[0], resPoint1[1])
                point2 = Point(resPoint3[0], resPoint3[0])

                Product_point =  point1.midpoint(point2)
            QR_count += 1


        distance_list = [QR_Codes[x].distance(Product_point) for x in QR_Codes if x in ['1','2','3','4'] and QR_Codes[x] < Product_point]


        least_distance = min(distance_list)

        for i in QR_Codes :

            if least_distance == QR_Codes[i].distance(Product_point) and i in ['1','2','3','4'] :
                print(f'{product} => position:',i)
                position = i
                break
        print("Scan Function Finished ....")
        
        return position


# QRScan('Dolo 650', 'PRoducts0.png')
    
    