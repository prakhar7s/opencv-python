import cv2
import os

# resizes the given image
def resize_img(img, resize_values):
    resized_img = cv2.resize(img, resize_values)
    return resized_img

#driver code
def main():
    # constant values
    SAMPLE_IMAGES_PATH = 'samples'
    SAMPLES_SAVED_AT = 'samples_resized'
    BASE_DIR = os.getcwd()
    RESIZE_DEFAULT = ( 100, 100)

    # import all the images
    samples = os.listdir(SAMPLE_IMAGES_PATH)

    #create folder to store resized images if not exists
    if not os.path.isdir(SAMPLES_SAVED_AT):
        os.mkdir(SAMPLES_SAVED_AT)
    
    # change dir to newly created folder before saving images
    os.chdir(SAMPLES_SAVED_AT)

    for sample in samples:
        # get the full path of current image
        img_path = os.path.join(BASE_DIR + '/' + SAMPLE_IMAGES_PATH + '/' + sample)
        
        # check whether current sample is file or not
        is_file = os.path.isfile(img_path)

        if is_file:
            # read that sample
            sample_img = cv2.imread(img_path, 1)

            # resize image
            resized_img = resize_img(sample_img, RESIZE_DEFAULT)

            # extract name of the file and save resized file by custom name 
            temp = sample.split('.')
            resize_img_name = temp[0] + '_resized.' + temp[1]

            # finally save the file
            cv2.imwrite(resize_img_name, resized_img)

            # debugging purpose
            print('{0} ---> {1}'.format(sample, SAMPLES_SAVED_AT+'/'+resize_img_name))


if __name__ == '__main__':
    main()
