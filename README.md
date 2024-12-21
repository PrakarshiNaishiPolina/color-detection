Color Detection with Bounding Box using OpenCV and Python

This Python script uses OpenCV to detect a specific color (blue in this example) in real-time from a webcam feed. A bounding box is drawn around the detected areas of the target color, making it easy to highlight and observe the regions of interest.

Key Features

Real-Time Detection: Captures frames from the webcam and processes them in real-time.
Target Color Detection: Uses the HSV color space to detect the specified color with flexible limits to handle variations in shades and lighting.
Bounding Box Highlighting: Draws a rectangle around detected areas to visually indicate the regions containing the target color.
User-Friendly Exit: Stops the webcam feed and closes all windows when the d key is pressed.
How It Works

Convert Color to HSV: The target color (blue in this case) is converted from BGR to HSV format. HSV is better suited for color detection as it separates chromatic content (hue) from intensity (value).
Define Color Range: Flexible lower and upper HSV limits are calculated to account for variations in shades and lighting.
Create Mask: A binary mask is generated where pixels matching the target color are white, and others are black.
Bounding Box Calculation: The smallest rectangle enclosing all detected regions is computed and drawn on the frame.
Display and Control: The processed frames are displayed, and the program terminates when the user presses d.
