## Script desenvolvido num proceso de migração do Zabbix 4.2 para o Zabbix 6 LTS

O Export inclui além dos hosts os grupos,templates, itens e triggers (não-herdadas);

Utilizei os parâmetros **selectGroups**, **selectParentTemplates**, **selectItems** e **selectTriggers** na chamada da API host.get para obter informações adicionais dos hosts, como grupos, templates, itens e triggers. Em seguida, percorro os dados exportados e os exibo no console.

<h3> Certifique-se de ter o Python e a biblioteca Requests instalados para executar o script, caso não possua:</h3>

```
pip install requests
```
