# coding:utf-8
from fileinput import filename
import os, cv2, sys


def take_photo():
    # 提醒用户操作字典
    print("*********************************************")
    print("*  热键(请在摄像头的窗口使用)：             *")
    print("*  z: 拍摄图片                              *")
    print("*  q: 退出                                  *")
    print("*********************************************")

    # 创建/使用local_photo文件夹
    class_name = "res"
    if (os.path.exists("res")):
        pass
    else:
        os.mkdir(class_name)

    # 设置特定值

    index = 'takephoto'
    cap = cv2.VideoCapture(0)

    while True:
        # 读入每一帧
        ret, frame = cap.read()

        cv2.imshow("capture", frame)

        # 存储
        input = cv2.waitKey(1) & 0xFF
        # 拍照
        if input == ord('z'):
            cv2.imwrite(
                "%s/%s.jpeg" % (class_name, index),
                cv2.resize(frame, (600, 480), interpolation=cv2.INTER_AREA))
            break

        # 退出
        if input == ord('q'):

            # 关闭窗口
            cap.release()
            cv2.destroyAllWindows()
            sys.exit()


def cut_photo():
    
    path_red = '/home/ubuntu/catkin_ws/src/mycobot_ros/mycobot_ai/res/red'
    for i, j, k in os.walk(path_red):
        file_len_red = len(k)

    path_gray = '/home/ubuntu/catkin_ws/src/mycobot_ros/mycobot_ai/res/gray'
    for i, j, k in os.walk(path_gray):
        file_len_gray = len(k)

    path_green = '/home/ubuntu/catkin_ws/src/mycobot_ros/mycobot_ai/res/green'
    for i, j, k in os.walk(path_green):
        file_len_green = len(k)

    path_blue = '/home/ubuntu/catkin_ws/src/mycobot_ros/mycobot_ai/res/blue'
    for i, j, k in os.walk(path_blue):
        file_len_blue = len(k)
    print("请截取要识别的部分")
    # root = tk.Tk()
    # root.withdraw()
    # temp1=filedialog.askopenfilename(parent=root)   #rgb
    # temp2=Image.open(temp1,mode='r')
    # temp2= cv.cvtColor(np.asarray(temp2),cv.COLOR_RGB2BGR)
    # cut = np.array(temp2)

    cut = cv2.imread(r"res/takephoto.jpeg")

    cv2.imshow('original', cut)
    # C:\Users\Elephant\Desktop\pymycobot+opencv\local_photo/takephoto.jpeg

    # 选择ROI
    roi = cv2.selectROI(windowName="original",
                        img=cut,
                        showCrosshair=False,
                        fromCenter=False)
    x, y, w, h = roi
    print(roi)

    kw = input("请输入保存图片文件夹名称('red','gray','blue','green'）:")
    # print(kw)

    # 显示ROI并保存图片
    if roi != (0, 0, 0, 0):
        
        crop = cut[y:y + h, x:x + w]
        cv2.imshow('crop', crop)
        # 选择红桶文件夹
        if kw == 'red':
            cv2.imwrite('/home/ubuntu/catkin_ws/src/mycobot_ros/mycobot_ai/res/red/goal{}.jpeg'.format(str(file_len_red + 1)),crop)
            print('Saved')
        # 选择灰桶文件夹
        elif kw == 'gray':
            cv2.imwrite('/home/ubuntu/catkin_ws/src/mycobot_ros/mycobot_ai/res/gray/goal{}.jpeg'.format(str(file_len_gray+1)),crop)
            print('Saved')
        # 选择绿桶文件夹
        elif kw == 'green':
            cv2.imwrite('/home/ubuntu/catkin_ws/src/mycobot_ros/mycobot_ai/res/green/goal{}.jpeg'.format(str(file_len_green+1)),crop)
            print('Saved')
        # 选择蓝桶文件夹
        elif kw == 'blue':
            cv2.imwrite('/home/ubuntu/catkin_ws/src/mycobot_ros/mycobot_ai/res/blue/goal{}.jpeg'.format(str(file_len_blue+1)),crop)
            print('Saved')

    # 退出
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    take_photo()
    cut_photo()
