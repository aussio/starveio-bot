### Getting Started

Run the following commands to install the requirements:

```
# Install the package manager we need
https://conda.io/docs/install/quick.html#os-x-miniconda-install

# Create virtual environment
conda create --name=starveio3.5 python=3.5

# Source new virtual environment
source activate starveio3.5

# Install OpenCV
# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html
conda install -c menpo opencv3

# Install the rest of our requirements
pip install -r requirements.txt
```

... I may have forgotten some. I think that's it. :)

### How to Run:

```
python bot.py
```
