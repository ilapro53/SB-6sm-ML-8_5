
## Рабочая версия

## Ход работы

#### 1. Поддготовка модели:
  - Ход работы: [./local/prepare_model.ipynb](local/prepare_model.ipynb)
  - Выходные файлы:
    - [./local/server_config.json](local/server_config.json)
    - [./local/my_model.keras](local/my_model.keras)
    - `/tmp/tfsrver/models/my_model/*`
    - [./local/test_images/*](local/test_images)

#### 2. Поддготовка сервера Tensorflow Serving:
  - Ход работы: [./local/prepare_server.ipynb](local/prepare_server.ipynb)
  - Входные файлы:
    - [./local/server_config.json](local/server_config.json)
  - Выходные файлы:
    - [./local/install_server.sh](local/install_server.sh)
    - [./local/requirements.txt](local/requirements.txt)
    - [./local/start_server.sh](local/start_server.sh)
    - [./local/server.log](local/server.log)
   
#### 3. Поддготовка клиента:
  - Ход работы: [./local/build_client.ipynb](local/build_client.ipynb)
  - Входные файлы:
    - [./local/test_images/*](local/test_images)
