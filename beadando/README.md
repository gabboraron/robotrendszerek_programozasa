Created in Óbuda University, BioTech lab, 2022

Written by Bence Biricz, Sándor Burian, Miklós Vincze, Abdallah Benhamida, based on:
  - https://docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html
  - https://stackoverflow.com/a/45338831/7973735
  - https://scikit-image.org/docs/stable/auto_examples/filters/plot_entropy.html

 POI detection for RAMI 2022 https://metricsproject.eu/wp-content/uploads/2022/05/RAMI2022_cascade_competition_Rule_book_v1.0.pdf
 the output is in `#timestamp class instance centroid_x centroid_y` format
 also with removing comments you will be able to see the results.

Running the container: `docker run <container_name> <input_picture_name.png> <output_name.txt>`

Example: `docker run oubot_ws input.png output.txt`

Container available at: https://hub.docker.com/r/oubot/oubot_ws
