# README #

### What is the purpose of this repository? ###

The ultimate goal is to prepare something for geometric label transfer.
Here I just want to review my understanding on Feature Matching Optical Flow and Depth estimation.

### How? ###

1. Given two successive frames of a video, depth of the first frame is estimated first (e.g. using an unsupervised method).

2. Given the camera pose and calibration (extrinsic and intrinsic matrices), and the depth of the current frame, we can warp the current image to the next frame. This transformation should result in a good warping of the annotations in the current frame to the next frame. However it might not work very well for small or dynamic objects.

Note that once you estimate the disparity d using a unsupervised method, you can estimate the depth by D=B.d/f, where B is baseline (the distance between two camera centers in the stereo configuration) and f is focal length of the cameras.
Here since we know the baseline between the stereo cameras, we can do this. If we are in a one-camera setting, then depth from disparity can not be computed this way.
Once depth is computed, you can project it onto the next frame using the camera pose of the next frame.

3. We use the Forward-Backward Lucas-Kanade method to find corresponding pixels in the small or dynamic objects and transfer the label with the obtained matched mask.
