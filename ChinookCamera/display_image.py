import cv2
from video_capture import VideoCaptureAsync
import time

# Specify width and height of video to be displayed
vid_w = 1280
vid_h = 720
# Initiate Video Capture object
capture = VideoCaptureAsync(src=0, width=vid_w, height=vid_h)

def display_video(duration):
    # Start video capture
    capture.start()
    time_end = time.time() + duration

    frames = 0
    # Capture for duration defined by variable 'duration'
    while time.time() <= time_end:
        ret, new_frame = capture.read()
        frames += 1
        # Create a full screen video display. Comment the following 2 lines if you have a specific dimension
        # of display window in mind and don't mind the window title bar.
        cv2.namedWindow('image',cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # Here only every 5th frame is shown on the display. Change the '5' to a value suitable to the project.
        # The higher the number, the more processing required and the slower it becomes
        if frames ==0 or frames%5 == 0:
            # This project used a Pitft screen and needed to be displayed in fullscreen.
            # The larger the frame, higher the processing and slower the program.
            # Uncomment the following line if you have a specific display window in mind.
            #frame = cv2.resize(new_frame,(640,480))
            if new_frame is not None and new_frame.size > 0:
                frame = cv2.flip(new_frame,180)
                cv2.imshow('image', frame)
            else:
                print('Frame is empty')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Stop video capture
    capture.stop()
    # Destroy all windows
    cv2.destroyAllWindows()