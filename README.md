# README #

### What is the purpose of this repository? ###

The ultimate goal is to prepare something for geometric label transfer.
Here I just want to review my understanding on Feature Matching Optical Flow and Depth estimation.

### How? ###

1. Given two successive frames of a video, depth of the first frame is estimated first (e.g. using an unsupervised method).

2. Given the camera pose and calibration (extrinsic and intrinsic matrices), and the depth of the current frame, we can warp the current image to the next frame. This transformation should result in a good warping of the annotations in the current frame to the next frame. However it might not work very well for small or dynamic objects. 

3. We use the Forward-Backward Lucas-Kanade method to find corresponding pixels in the small or dynamic objects and transfer the label with the obtained matched mask.
