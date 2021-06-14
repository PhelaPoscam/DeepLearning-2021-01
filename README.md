# Using Generative Adversarial Network techniques to upscale images for Automatic License Plate Recognition
Atividade Final da disciplina como requisito para a aprovação na disciplina de Deep Learning em 2021/01.

<!-- O site está temporariamente hospedado no url a seguir: https://ledsplay.davipetris.me/ -->

## Requisitos

- `Google Collab ou JupyterNotebook`
- `Google Drive`

## Inicializando o projeto

Coloque a pasta em seu Google Drive

```bash
1)from google.colab import drive
drive.mount('/content/drive/', force_remount=True) # Monta pastas do Google Drive.

2)cd /content/drive/MyDrive/DeepLearning/SRGAN-PyTorch-master-Novo # Instalar requirements - Executar toda vez que entrar no Colab.
```

## Comandos

- `!python3 /content/drive/MyDrive/DeepLearning/SRGAN-PyTorch-master-Novo/train.py -a srgan --gpu 0 --gan-epochs 200 --psnr-epoch 200 /content/drive/MyDrive/DeepLearning/DatasetFinalPb`: Treinamento
- `!python3 test_image.py -a srgan --gpu 0 --lr /content/drive/MyDrive/DeepLearning/placaIARA01.png --model-path /content/drive/MyDrive/DeepLearning/SRGAN-PyTorch-master-Novo/weights/GAN-best.pth`: Teste

## Dependências

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


