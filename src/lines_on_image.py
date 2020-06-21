# コマンドライン引数の指定　（プログラム実行時にファイル名を指定できる）
import cv2
import sys

try:
    if (len(sys.argv)!=2):
        print("引数に読み込む画像を指定する必要があります。")
        sys.exit()
    
    img = cv2.imread(sys.argv[1])

    if img is None:
        print('ファイルが読み込めません。')
        sys.exit()
    
    # 座標=(50,50)から(200,50)まで青色255で線を引く
    cv2.line(img, (50,50), (200,50), (250,0,0))

    # 座標=文字列の左下隅の座標、fontの種類=cv2.FONT_HERSHEY_SIMPLEX, フォントスケール、color(b,g,r),太さ　で文字をかく（putText）
    cv2.putText(img, 'Hello OpenCV', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50,60,80),2)

    cv2.imwrite('./tmp3/LineOnImage.jpg',img)

except:
    print("Erro:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
