# JogoDaForca
Jogo da forca (hangman) implementado em Python junto com uma base de dados de palavras em CSV.

```Center
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
   ========
```

## Como jogar
Coloque o arquivo *forca_palavras.csv* na mesma pasta do script (do Jupyter Notebook) em python *JogoDaForca.ipynb*. Com isso, o algoritmo irá escolher aleatoriamente uma das palavras na base e sua categoria, que será utilizada como dica para direcionar as adivinhações. 
* Quantidade de erros permitida = 7
* Permite chutar uma palavra ou letra
* Todas as acentuações foram eliminadas
* Somente letras minúsculas

## Versão Bot de Telegram
Aproveitando o mesmo código, é possível criar um bot de telegram para jogar. Para isso, siga o [tutorial anterior](https://github.com/luiseduardobr1/TelegramBOT) para criar um bot e receber um TOKEN e, então, basta utilizar o código do arquivo *jogodaforcaTelegramBot.py*. 

### Como jogar na versão do Telegram
No telegram, o bot não pode iniciar uma conversa, então, você precisa ativá-lo com o comando **/forca**. Após isso, ele responderá com uma palavra a ser adivinhada e uma dica. Para começar os chutes digite **/forca a** (para chutar apenas uma única letra *a*) ou **/forca abelha** (para chutar uma palavra toda que no exemplo é a palavra *abelha*). As regras são as mesmas da versão de computador. 

Como exemplo de funcionamento, segue a figura:

![image](https://user-images.githubusercontent.com/56649205/81187247-2b200900-8f8a-11ea-8d10-f9501344003b.png)
