# Simulação de dispositivos MQTT (Publisher)
----
##### ALYSSON C. C. CORDEIRO
##### Engenheiro da Computação - Instituto de Tecnologia e Liderança (INTELI)

---

# Simulador de Dispositivos IoT com MQTT - Agora com Testes Automatizados

## Objetivo 
Este projeto tem como objetivo implementar testes automatizados para validar um simulador de dispositivos IoT, desenvolvido como parte de uma atividade anterior. Os testes foram implementados utilizando os conceitos de TDD (Desenvolvimento Orientado a Testes) apresentados durante a semana.

## Enunciado
A implementação visa reproduzir o comportamento de dispositivos de detecção de gases, gerando mensagens MQTT com base em dados simulados. O enunciado orienta a reprodução fiel da taxa de comunicação, unidades de medida e faixa de valores das medições. Agora são os testes que estão no arquivo "sub.py".

## Aspectos Abordados nos Testes:

1. **Recebimento:**
    
    Garante que os dados enviados pelo simulador são recebidos pelo broker.

2. **Validação dos Dados:** 

    Garante que os dados enviados pelo simulador chegam sem alterações.


3. **Confirmação da Taxa de Disparo:**

    Garante que o simulador atende às especificações de taxa de disparo de mensagens dentro de uma margem de erro razoável.

##  Padrão de qualidade segundo a ponderada:

- Testes bem definidos e que passam consistentemente.
- Pelo menos **UM** teste é definido para validar o perfil de QoS (Qualidade de Serviço) definido em tempo de execução para o simulador.



## Quais tecnologias utilizadas?
- Python
- Paho MQTT Library
- Mosquitto
- unittest (python)

## Dados Tirados daqui:
[https://datasheetspdf.com/pdf/1350171/SGX/MiCS-6814/1]

## como ficou a estrutura:

- **pub.py:** Código do simulador responsável por publicar mensagens no tópico ***"sensor/gases"***. Além disso, a adição de controle de taxa de disparo por meio de time.sleep.

-**sub.py:** Código de teste do simulador que aborda os aspectos mencionados acima. Os testes Implementados de acorddo com o padrão de qualidade da ponderada:

1. Recebimento de dados.
2. Validação dos dados.
3. Confirmação da taxa de disparo.


## Como Executar o Código?

1. **Instalação de Dependências:**
   Certifique-se de ter o Python instalado. Em seguida, instale as dependências usando o seguinte comando:
   ```bash
   pip install paho-mqtt
2. Baixe e instale o Mosquitto [https://mosquitto.org/download/]

3. Vai no reposítório 
    ```bash
    cd dispositivos_MQTT_Publisher
4. Execute em um terminal:
    ```bash
    mosquitto -c mosquitto.conf
5. execute em outro terminal:
    ```bash
    python pub.py
6. execute o terceiro  terminal:
    ```bash
    python sub.py
    ```

## Demostração:
[https://drive.google.com/file/d/1uouRK40V18SWjsDEY4oRbwHI75numTSl/view?usp=sharing]
