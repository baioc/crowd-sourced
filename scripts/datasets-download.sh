#!/bin/sh
pip install gdown
pip install pandas

# kitti semantics (autonomous driving)
<<<<<<< HEAD
gdown https://drive.google.com/u/0/uc?id=1nj0lZwTd8uK71ulZngAY3gcugeMXTIWO&export=download && pid=$!
wait $pid
# tweets
gdown https://drive.google.com/u/0/uc?id=1DWscOPs1Wi4-y98q6FASUFRjOaO0ggZU&export=download && pid=$!
wait $pid
=======
gdown https://drive.google.com/u/0/uc?id=1nj0lZwTd8uK71ulZngAY3gcugeMXTIWO&export=download &
# tweets
gdown https://drive.google.com/u/0/uc?id=1DWscOPs1Wi4-y98q6FASUFRjOaO0ggZU&export=download
>>>>>>> datasets-2

# unsplash nature
python py_scripts/unsplash_download.py