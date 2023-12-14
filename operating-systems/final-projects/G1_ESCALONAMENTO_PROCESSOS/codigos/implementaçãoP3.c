#include <Arduino.h>
#include <Arduino_FreeRTOS.h>
#include <task.h>
#include <semphr.h>
#include <queue.h>

//CONSTANTES DO PROGRAMA E O VALOR DAS SUAS PORTAS NO ARDUINO
const int ledVermelhoPin = 12;
const int ledAmareloPin = 6;
const int ledVerdePin = 13;
const int pirPin = 10;
const int botaoAzulPin = 4;
const int buzzerPin = 11;

SemaphoreHandle_t semaforoSinal;
SemaphoreHandle_t semaforoBotao;
volatile bool sistemaAtivo = true;
volatile bool sinalFechado = true;
volatile int tempoPiscarAmarelo = 8;
volatile int tempoLigarVerde = 10;
volatile int contadorInicial = 5;
volatile bool mensagemExibida = false;

QueueHandle_t fila;

//FUNÇÃO QUE ACIONA O SEMAFORO E REALIZA A CONTAGEM
void acionarSemafaro(void *pvParameters) {
  int contador = contadorInicial;
  while (contador > 0) {//SE O SINAL ESTIVER FECHADO PRINTAR SINAL FECHADO E LIGAR A LUZ
    if (sistemaAtivo && sinalFechado) {
      xSemaphoreTake(semaforoSinal, portMAX_DELAY);
      if (digitalRead(ledVermelhoPin) == HIGH) {
        Serial.println("SINAL FECHADO");
        contador--;
      }
      xSemaphoreGive(semaforoSinal);
    }
    vTaskDelay(pdMS_TO_TICKS(1000));
  }
}

void gerarSomBuzzer(int numero) { //SOLTA O SOM NO BUZZER A CADA 1 SEGUNDO
  int frequencia = 1000 + (numero * 100);//MUDA A FREQUENCIA DO SOM
  tone(buzzerPin, frequencia);
  delay(100);
  noTone(buzzerPin);
}

void pararTarefas() {
  vTaskSuspendAll();  // Suspende todas as tarefas
  sistemaAtivo = true;
  sinalFechado = true;
  mensagemExibida = false;
  digitalWrite(ledVermelhoPin, HIGH);//LED FICA VERMELHO APÓS SUSPENDER TUDO
  Serial.end();
  Serial.begin(9600);
  Serial.println("SINAL FECHADO");
  xTaskResumeAll();  // Resumo todas as tarefas
}

void reiniciarSistema() {//FUNÇÃO PARA REINICIAR O SISTEMA APÓS APERTAR O BOTÃO AZUL
  vTaskSuspendAll();  // Suspende todas as tarefas
  sistemaAtivo = true;
  sinalFechado = true;
  mensagemExibida = false;
  digitalWrite(ledVermelhoPin, HIGH);
  Serial.end();
  Serial.begin(9600);
  Serial.println("SINAL FECHADO");
  xTaskResumeAll();  // Resumo todas as tarefas
}

void controlarSemafaro(void *pvParameters) {//FUNCAO PARA CONTROLAR A COR DOS SEMAFOROS
  int valor;
  int contadorPiscadas = 0;
  while (1) {
    if (sistemaAtivo) {
      valor = digitalRead(pirPin);
      if (sinalFechado) {//SE O SINAL ESTIVER FECHADO LIGAR LUZ VERMELHA E DESLIGAR AS OUTRAS
        xSemaphoreTake(semaforoSinal, portMAX_DELAY);
        if (valor == HIGH) {
          digitalWrite(ledAmareloPin, LOW);
          digitalWrite(ledVerdePin, LOW);
          Serial.end();
          Serial.begin(9600);
          digitalWrite(ledVermelhoPin, LOW);
          xSemaphoreGive(semaforoSinal);

          digitalWrite(ledVermelhoPin, LOW);
          digitalWrite(ledAmareloPin, HIGH);

          if (!mensagemExibida) {
            gerarSomBuzzer(3);//EXIBIR MENSAGEM DE VEICULO APROXIMANDO E GERA O SOM DO BUZZER
            Serial.println("ATENÇÃO, VEÍCULO SE APROXIMANDO!");
            mensagemExibida = true;
          }
          //REALIZA A CONTAGEM REGRESSIVA DO SINAL AMARELO
          int contagemRegressivaAmarelo = tempoPiscarAmarelo;
          for (int i = 0; i < tempoPiscarAmarelo; i++) {
            digitalWrite(ledAmareloPin, !digitalRead(ledAmareloPin));
            Serial.print("Contagem Regressiva Amarela: ");
            Serial.println(contagemRegressivaAmarelo--);
            gerarSomBuzzer(contagemRegressivaAmarelo);
            vTaskDelay(pdMS_TO_TICKS(1000));
            if (digitalRead(ledAmareloPin) == HIGH) {
              contadorPiscadas++;
              if (contadorPiscadas >= 8) {//SE PISCAR 8X PRA CIMA INTERROMPE O CONTADOR
                break;
              }
            }
          }

          digitalWrite(ledAmareloPin, LOW);//DESLIGA O SINAL AMARELO
          digitalWrite(ledVerdePin, HIGH);//LIGA O SINAL VERDE
          Serial.println("SINAL ABERTO");//INFORMA QUE O SINAL ABRIU

          //CONTAGEM REGRESSIVA DO SINAL VERDE
          int contagemRegressivaVerde = tempoLigarVerde;
          for (int i = 0; i < tempoLigarVerde; i++) {
            Serial.print("Contagem Regressiva Verde: ");
            Serial.println(contagemRegressivaVerde--);
            gerarSomBuzzer(contagemRegressivaVerde);
            vTaskDelay(pdMS_TO_TICKS(1000));
          }
          //DESLIGA O SINAL VERDE E LIGA O VERMELHO
          digitalWrite(ledVerdePin, LOW);
          sinalFechado = false;
          digitalWrite(ledVermelhoPin, HIGH);
          contadorPiscadas = 0;
          mensagemExibida = false;
        }
        xSemaphoreGive(semaforoSinal);
      } else {
        digitalWrite(ledVermelhoPin, HIGH);
        sinalFechado = true;
        mensagemExibida = false;
      }
    }
    vTaskDelay(pdMS_TO_TICKS(100));
  }
}
//FUNÇÃO PARA RECEBER OS DADOS DO BOTÃO AZUL
void verificarBotaoAzul(void *pvParameters) {
  bool botaoAnterior = digitalRead(botaoAzulPin);
  while (1) {//SE FOR PRESSIONADO ENVIA PARA A FILA E DESLIGA A LUZ DO SEMAFORO ATUAL
    bool botaoAtual = digitalRead(botaoAzulPin);
    if (botaoAnterior == HIGH && botaoAtual == LOW) {
      bool botaoPressionado = true;
      xQueueSend(fila, &botaoPressionado, portMAX_DELAY);
    }
    botaoAnterior = botaoAtual;
    vTaskDelay(pdMS_TO_TICKS(100));
  }
}
//FUNÇÃO QUE REINICIA O SISTEMA PARA SEU ESTADO INICIAL
void reiniciarSistemaTask(void *pvParameters) {
  while (1) {
    bool botaoPressionado = false;
    if (xQueueReceive(fila, &botaoPressionado, portMAX_DELAY) == pdTRUE && botaoPressionado) {
      reiniciarSistema();//MANDA OS VALORES PRA FILA E REINICIA
    }
  }
}
//A MAIN DO NOSSO PROGRAMA, ONDE ARMAZENA AS VARIAVEIS USADAS
void setup() {
  Serial.begin(9600);
  pinMode(ledVermelhoPin, OUTPUT);
  pinMode(ledAmareloPin, OUTPUT);
  pinMode(ledVerdePin, OUTPUT);
  pinMode(pirPin, INPUT);
  pinMode(botaoAzulPin, INPUT_PULLUP);
  pinMode(buzzerPin, OUTPUT);

  semaforoSinal = xSemaphoreCreateMutex();
  xSemaphoreGive(semaforoSinal);
  digitalWrite(ledVermelhoPin, HIGH);

  fila = xQueueCreate(1, sizeof(bool));
//CRIAÇÃO DA FILA E DE SEU TAMANHO E CRIAR AS AÇÕES UTILIZADAS NO CÓDIGO
  xTaskCreate(acionarSemafaro, "AcionarSemafaroTask", 128, NULL, 1, NULL);
  xTaskCreate(controlarSemafaro, "ControlarSemafaroTask", 128, NULL, 2, NULL);
  xTaskCreate(verificarBotaoAzul, "VerificarBotaoAzulTask", 128, NULL, 3, NULL);
  xTaskCreate(reiniciarSistemaTask, "ReiniciarSistemaTask", 128, NULL, 4, NULL);
}

void loop() {
  // Loop vazio em sistemas FreeRTOS
}
