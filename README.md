<table align="center"><tr><td align="center" width="9999">

<img src="https://cdn.leroymerlin.com.br/categories/aspirador_de_po_56af_300x300.jpeg" align="center" width="170" alt="Project icon">

# Joguinho do aspirador de pó

*Faça o maradona limpar a poeira*

</td></tr>

</table>    

<div align="center">

> [![Version badge](https://img.shields.io/badge/version-0.1.0-silver.svg)]()

</div>

Este joguinho simples foi feito como exercício de prática com base na disciplina de introdução à inteligência artificial.

O programa é escrito em **python3** portanto para sua execução é necessário que você possua o python instalado.

Se você é usuário Unix (linux/Mac) execute o programa com:

```
$ make run
```

Se você é usuário Windows execute o programa com:

```
> python3 main.py
```

A interface de texto lhe pedirá para inserir um número de fase. A fase será gerada com base neste número.

A fase é um tabuleiro 5x5 composto por `0`s, `1`s e uma letra `M`.

`0`: São posições LIMPAS.
`1`: São posições SUJAS.
`M`: É a posição do aspirador de pó (Maradona).

```
Choose a stage by inserting any number:
>	1
Map of stage 1:
	      N

	[ 0 0 1 0 1 ]
	[ 1 1 1 0 0 ]
	[ 1 0 1 1 0 ]
	[ 1 1 0 0 1 ]
	[ 0 0 0 M 1 ]

	      S
-------------------------------
```

Então a interface de texto perguntará se jogo é manual ou automático:

```
Choose mode:
1 - Manual
2 - Autopilot
>
```

Se a entrada for `manual` (`1`) você poderá controlar o aspirador de pó, inserindo comandos de movimento como `up`, `down`, `left` e `right`. Ao fazer isso o maradona se movimentará no tabuleiro. Ao mover o maradona par auma posição que contém um número `1` o aspirador irá limpar aquela posição. O jogo acaba quando o tabuleiro todo for limpo.

```
what you gonna do?
up down left right exit
up
	      N

	[ 0 0 1 0 1 ]
	[ 1 1 1 0 0 ]
	[ 1 0 1 1 0 ]
	[ 1 1 0 M 1 ]
	[ 0 0 0 0 1 ]

	      S
-------------------------------
{'up': 1, 'down': 0, 'left': 0, 'right': 1}
Steps taken:  1
There are still dirty to clean.
what you gonna do?
up down left right exit
```

O objetivo do jogo é limpar o tabuleiro com a menor quantidade de passos (`steps`) possíveis.

Se você escolher a opção `auto` (`2`) o computador jogará sozinho tentando limpar o tabuleiro na menor quantidade de passos possível.