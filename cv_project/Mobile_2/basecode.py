import cv2


def main():

    print("Press 1 for pre-recorded videos, 2 for live stream: ")
    option = int(input())

    if option == 1:
        # Record video
        windowName = "Sample Feed from Camera 1"
        cv2.namedWindow(windowName)

        capture1 = cv2.VideoCapture("http://10.130.144.76:8080/video")  # laptop's camera
        capture2 = cv2.VideoCapture("http://10.130.144.76:8080/video")   # sample code for mobile camera video capture using IP camera

        # define size for recorded video frame for video 1
        width1 = int(capture1.get(3))
        height1 = int(capture1.get(4))
        size1 = (width1, height1)

        # frame of size is being created and stored in .avi file
        optputFile1 = cv2.VideoWriter(
            'Stream1Recording.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size1)

        # check if feed exists or not for camera 1
        if capture1.isOpened():
            ret1, frame1 = capture1.read()
        else:
            ret1 = False

        while ret1:
            ret1, frame1 = capture1.read()
            # sample feed display from camera 1
            cv2.imshow(windowName, frame1)

            # saves the frame from camera 1
            optputFile1.write(frame1)

            # escape key (27) to exit
            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        optputFile1.release()
        cv2.destroyAllWindows()

    elif option == 2:
        # live stream
        windowName1 = "Live Stream Camera 1"
        cv2.namedWindow(windowName1)

        capture1 = cv2.VideoCapture("http://10.130.149.13:8080/video")  # laptop's camera

        if capture1.isOpened():  # check if feed exists or not for camera 1
            ret1, frame1 = capture1.read()
        else:
            ret1 = False

        while ret1:  # and ret2 and ret3:
            ret1, frame1 = capture1.read()
            cv2.imshow(windowName1, frame1)

            if cv2.waitKey(1) == 27:
                break

        capture1.release()
        cv2.destroyAllWindows()

    else:
        print("Invalid option entered. Exiting...")


main()
