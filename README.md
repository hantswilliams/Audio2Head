# Audio2Head: Audio-driven One-shot Talking-head Generation with Natural Head Motion (IJCAI 2021)


## hants notes 
- updated requirements.txt file to include pytorch and ffmpeg 
- create a AWS deep learning instance with pytorch 
- once logged in, `source activate pytorch` 
- if running on aws/ec2 -> need to first then do: 
    - `sudo apt-get update` 
    - `sudo apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6` 
- then download this github project (`git clone xyz`)
- can then move the manual files/e.g., 700mb+ // the checkpoints folder 
    - `scp -r data/ nhit_pytorch:/home/ubuntu/Audio2Head/checkpoints/` 
- then run: 
    - `sudo apt install python3-pip`  # have removed toch, torchaudio, torchvision - as those are already installed 
    - `pip install -r requirements.txt` 
- can then give it a run and do: 
    - `python inference.py --audio_path demo/audio/intro.wav --img_path demo/img/trump.jpg`


#### [Paper](https://www.ijcai.org/proceedings/2021/0152.pdf) | [Demo](https://www.youtube.com/watch?v=xvcBJ29l8rA)

#### Requirements

- Python 3.6 , Pytorch >= 1.6 and ffmpeg

- Other requirements are listed in the 'requirements.txt'

  

#### Pretrained Checkpoint

Please download the pretrained checkpoint from [google-drive](https://drive.google.com/file/d/1tvI43ZIrnx9Ti2TpFiEO4dK5DOwcECD7/view?usp=sharing) and put it within the folder (`/checkpoints`).



#### Generate Demo Results

```
python inference.py --audio_path xxx.wav --img_path xxx.jpg
```

Note that the input images must keep the same height and width and the face should be appropriately cropped as in `/demo/img`.



#### License and Citation

```
@InProceedings{wang2021audio2head,
author = Suzhen Wang, Lincheng Li, Yu Ding, Changjie Fan, Xin Yu
title = {Audio2Head: Audio-driven One-shot Talking-head Generation with Natural Head Motion},
booktitle = {the 30th International Joint Conference on Artificial Intelligence (IJCAI-21)},
year = {2021},
}
```



#### Acknowledgement

This codebase is based on [First Order Motion Model](https://github.com/AliaksandrSiarohin/first-order-model), thanks for their contribution.





