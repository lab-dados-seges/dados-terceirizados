## Histórico de terceirizados (2010 a 2024)

### Introdução

Aqui vamos analisar o histórico dos dados de terceirizados do governo federal. Com a contribuição da CGU, conseguimos os dados desde 2010, o que nos 14 anos de informações sobre os terceirizados que foram contratados no administração pública federal. 

É importante mencionar que, como são os órgãos que encaminham as informações para a CGU, não há dados de todos os órgãos. Há três informações validadas pela CGU antes da publicação na página de Dados Abertos: CBO (Classificação Brasileira de Ocupações) a partir de 2018; CPF e CNPJ da empresa contratada pelo órgão para a terceirização. Portanto, há margem para erros e todas as análises aqui discutidas devem ser lidas de maneira crítica. 

Para verificar o tratamento feito para construir as análises aqui listadas, [visualize o notebook com os códigos](https://nbviewer.org/github/lab-dados-seges/dados-terceirizados/blob/main/analises/historico_terceirizados.ipynb).

### Terceirizados no governo federal

Para verificar a quantidade de terceirizados por ano na administração pública federal, vamos utilizar a variável ano de carga. Isso significa que foi o ano em que o órgão submeteu a informação daquele terceirizado. Vejamos a distribuição do quantitativo total:

![Gráfico de terceirizados por ano](../analises/graficos/quantidade_terceirizados_por_ano.png)
<p style="text-align: center; font-size: 0.9em; color: gray;">
Gráfico 1 – Quantitativo total de terceirizados de 2010 a 2024.
</p>

É possível perceber uma flutuação significativa de 2010 a 2017. Em 2018, houve uma redução de 33,7% de terceirizados ao comparar com 2017. Em 2019 há o maior pico de contratação, totalizando 274.696 terceirizados. A partir de 2010 há uma certa constância no número de entradas de terceirizados. As flutuações até 2017 podem estar ligadas à organização internada dos órgãos para submeter os dados exigidos pela CGU. Em 2019 há mudança de governo e um significativo aumento de terceirizados.

A seguir, veremos um gráfico com os orgãos com as maiores quantidades de terceirizados por ano. Para melhor visualização, escolhemos os top 3:

![Gráfico de terceirizados por ano](../analises/graficos/top3_orgaos_qtd_terceirizados_ano.png)
<p style="text-align: center; font-size: 0.9em; color: gray;">
Gráfico 2 – Top 3 órgãos com o maior quantitativo total de terceirizados entre 2010 e 2024.
</p>

Dez órgãos aparecem no gráfico: MEC (Ministério da Educação, MINC (Ministério da Cultura), MPS (Ministério da Previdência Social), MS (Ministério da Saúde), MT (Ministério dos Transportes), MF (Ministério da Fazenda), MDS (Ministério do Desenvolvimento Social), ME (Ministério da Economia), MJSP (Ministério da Justiça e Segurança Pública) e MTP (Ministério do Trabalho e Previdência Social).

Claramente vemos que o MEC é o órgão que acumula o maior quantitativo de terceirizados desde 2010.