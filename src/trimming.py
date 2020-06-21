# トリミングといってもサイズをスライスして切ってるだけ...
import cv2

try:
    # 画像の読み込み
    img = cv2.imread('./tmp/lena.jpg')

    if img is None:
        print('読み込みできませんでした')
        import sys
        sys.exit()


    height = img.shape[0]
    width = img.shape[1]

    # 切り取り
    dst = img[250:height, 250:width]
    cv2.imwrite('./tmp6/trimming.jpg',dst)

except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))