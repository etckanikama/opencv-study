"""
閾値（すれしょるど）処理を行うプログラム
"""
import cv2
import numpy as np

try:
    # BGRで画像の読み込み
    img = cv2.imread('./tmp/sky.jpg')

    if img is None:
        print('読み込みできませんでした')
        import sys
        sys.exit()
    # convert bgr to hsb
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,100,100])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask_inverse = cv2.inRange(img_hsv, lower_blue, upper_blue)

    # inverse mask to get parts that are not blue
    mask = cv2.bitwise_not(mask_inverse)

    # convert single channel mask back into 3 channels
    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)


    # perform bitwise and on mask to obtain cut-out image that is not blue
    masked_upstate = cv2.bitwise_and(img, mask_rgb)

        # replace the cut-out parts with white
    masked_replace_white = cv2.addWeighted(masked_upstate, 1, \
                                        cv2.cvtColor(mask_inverse, cv2.COLOR_GRAY2RGB), 1, 0)


    cv2.imwrite('./tmp8/mask_white.jpg',masked_replace_white)







except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))


