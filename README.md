# Using Generative Adversarial Network techniques to upscale images for Automatic License Plate Recognition
Requirement for approval in the Deep Learning course from PPGI/UFES 2021/01.

## Requirements

- `Google Collab or JupyterNotebook` (Collab prefered for GPU training)
- `Google Drive`

## Initializing the project

Put the folder 'FOLDER' in your Google Drive

```bash
1)from google.colab import drive
drive.mount('/content/drive/', force_remount=True) # Mount Google Drive folders.

2)cd /content/drive/MyDrive/FOLDER # Install requirements - Run every time you enter Colab.
```

## Commands for SRGAN

- `!python3 /content/drive/MyDrive/FOLDER/train.py -a srgan --gpu 0 --gan-epochs 200 --psnr-epoch 200 /content/drive/MyDrive/FOLDER/DatasetFinalPb`: Training with 200 epochs
- In train.py `base_image = transforms.ToTensor()(Image.open(os.path.join("assets", "baseimage.png")))`: Change this line to the image that you want to upscale
- `!python3 /content/drive/MyDrive/FOLDER/test_image.py -a srgan --gpu 0 --lr /content/drive/MyDrive/FOLDER/PLACADETESTE.png --model-path/content/drive/MyDrive/PASTA/weights/GAN-best.pth`: Testing using the last/best GAN values.

## Dependencies for SRGAN

`requirements.txt`

```python
opencv-python>=4.5.2.52
torchvision>=0.9.1+cu111
Pillow>=8.2.0
numpy>=1.19.5
torch>=1.8.1+cu111
tqdm>=4.60.0
scipy>=1.6.3
prettytable>=2.1.0
thop>=0.0.31.post2005241907
setuptools>=56.2.0
tensorboardX>=2.2
lpips>=0.1.3
albumentations
easyocr
pytesseract
imutils
```

## REFERENCES

[SRGAN](https://github.com/Lornatang/SRGAN-PyTorch)


