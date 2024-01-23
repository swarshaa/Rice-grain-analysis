# Rice-grain-analysis
 
Rice Quality Detection Using Computer Vision This repository contains Python code for detecting the quality of rice using computer vision techniques. The program captures images from the camera, processes them, and analyzes the rice grains' quality based on their aspect ratios.

Description The script utilizes OpenCV library functions to perform the following tasks:

Access the camera and capture frames for a specific duration. Process the captured frames to identify rice grains. Analyze the aspect ratios of the rice grains to determine quality. Display processed images showcasing various stages of image transformation. Features Camera interface to capture live images for quality analysis. Image processing techniques like thresholding, filtering, erosion, dilation, and edge detection. Aspect ratio analysis to classify rice grains as broken or good quality. Visualization of different stages of image processing. Requirements Python 3.x OpenCV (cv2) NumPy Matplotlib Usage Clone the repository:

bash Copy code git clone https://github.com/swarshaa/Rice-grain-analysis.git Install the required dependencies:

bash Copy code pip install -r requirements.txt Run the Python script:

bash Copy code python rice_quality_detection.py Follow on-screen instructions to interact with the camera interface. Press 'q' to exit.

Results Upon execution, the program displays processed images showing the original image, binary image, filtered image, eroded image, dilated image, and edge-detected image. It also provides information about the total number of rice grains, broken rice grains, whole rice grains, and the percentage of whole rice grains.
