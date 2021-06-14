# Using Generative Adversarial Network techniquesto upscale images for Automatic License PlateRecognition
Atividade Final da disciplina como requisito para a aprovação na disciplina de Deep Learning em 2021/01.

<!-- O site está temporariamente hospedado no url a seguir: https://ledsplay.davipetris.me/ -->

## Requisitos

- `Google Collab ou JupyterNotebook`
- `Google Drive`

## Inicializando o projeto

Coloque a pasta em seu Google Drive

```bash
from google.colab import drive
drive.mount('/content/drive/', force_remount=True) # Monta pastas do Google Drive.
cd /content/drive/MyDrive/DeepLearning/SRGAN-PyTorch-master-Novo # Instalar requirements - Executar toda vez que entrar no Colab.
```

## Comandos

- `./run`: Executa comandos dentro do container da aplicação
- `make help`: Mostra a explicação dos comandos executados com `make`

## Dependências

O Docker **não atualiza** mudanças de dependencias instaladas pelo `pip`. Caso queira adicionar uma nova dependência, adicione o nome da biblioteca nova no arquivo `requirements.txt`

```python
Django>=3.0,<4.0
psycopg2-binary>=2.8
django-seed
django-filter==2.4.0
django-cpf==0.1.0
django-phonenumber-field[phonenumbers]==5.0.0
```

Digite o comando a seguir para buildar a nova imagem e inicializar a aplicação atualizada:

```bash
make build up
```
