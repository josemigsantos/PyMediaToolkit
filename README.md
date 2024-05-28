# PyMediaToolkit

PyMediaToolkit is a comprehensive suite of Python scripts for modifying and processing multimedia files, including images, audio, and video. This project was developed as part of a Multimedia course at the University of Beira Interior.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

This project provides a variety of scripts for multimedia file manipulation, aiming to solidify knowledge in multimedia processing and Python programming.

## Features

### Image Processing

- Addition
- Subtraction
- OR operation
- AND operation
- Green color filter
- Negative filter
- Gray filter

### Audio Processing

- Cut
- Join
- Echo
- Normalize

### Video Processing

- Black and white filter

## Installation

To use PyMediaToolkit, ensure you have Python installed. You can clone this repository and install the necessary dependencies using pip.

```bash
git clone https://github.com/yourusername/PyMediaToolkit.git
cd PyMediaToolkit
pip install -r requirements.txt
```

## Usage

### Main Menu
Navigate through the main menu to access different multimedia operations.

```python

- - - - - Main Menu - - - - - - - -
1. Image Modification
2. Audio Modification
3. Video Modification
4. Exit
- - - - - - - - - - - - - - - - - -

```

### Main Menu
Navigate through the main menu to access different multimedia operations.

```python

- - - - - Main Menu - - - - - - - -
1. Image Modification
2. Audio Modification
3. Video Modification
4. Exit
- - - - - - - - - - - - - - - - - -

```

## Examples
### Image Addition
```python
from image_processing import add_images
add_images('path/to/image1.png', 'path/to/image2.png', 'path/to/output.png')
```

### Audio Cut
```python
from audio_processing import cut_audio
cut_audio('path/to/audio.mp3', start_time, end_time, 'path/to/output.mp3')
```

### Video Black and White filter
```python
from video_processing import black_and_white
black_and_white('path/to/video.mp4', 'path/to/output.mp4')
```
