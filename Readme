## 🤖 Automação com Power Automate

Além do Analisador com Gemini AI, este projeto também inclui fluxos de automação desenvolvidos no **Microsoft Power Automate Desktop** para automatizar tarefas repetitivas no sistema PJE (Processo Judicial Eletrônico).

### 📋 Fluxos Disponíveis

#### 1. Processamento de Apelações (`apelação.txt`)
Automatiza o fluxo de trabalho para processos de Apelação no PJE:
- Leitura automática de planilha Excel com números de processos
- Navegação automatizada no sistema PJE 2G
- Pesquisa e seleção de processos na fila "Preparar relatório e voto"
- Abertura automática dos autos digitais
- Busca e processamento de documentos de Apelação

#### 2. Processamento de Agravos (`agravo.txt`)
Automatiza o fluxo de trabalho para processos de Agravo no PJE:
- Leitura automática de planilha Excel com números de processos
- Navegação automatizada no sistema PJE 2G
- Pesquisa e seleção de processos
- Tratamento de erros para processos não encontrados
- Processamento em lote

### ⚙️ Tecnologias Utilizadas

- **Microsoft Power Automate Desktop** - Plataforma de automação RPA
- **Microsoft Excel** - Armazenamento dos números de processos
- **Microsoft Edge** - Navegador automatizado
- **Excel Online Business Connector** - Integração com planilhas na nuvem

### 🚀 Como Utilizar

1. **Instalar o Power Automate Desktop**
   - Baixe em: [Power Automate Desktop](https://flow.microsoft.com/pt-br/desktop/)

2. **Importar os Fluxos**
   - Abra o Power Automate Desktop
   - Crie um novo fluxo
   - Cole o conteúdo do arquivo `.txt` correspondente

3. **Configurar a Planilha Excel**
   - Crie uma planilha com a coluna "Número do Processo"
   - Atualize o caminho do arquivo no fluxo

4. **Executar**
   - Certifique-se de estar logado no PJE
   - Execute o fluxo desejado

### 📁 Estrutura dos Arquivos

```
├── apelação.txt      # Fluxo para processamento de Apelações
├── agravo.txt        # Fluxo para processamento de Agravos
└── Processos 2024.xlsx  # Modelo de planilha (criar localmente)
```

### ⚠️ Observações Importantes

- Os fluxos foram desenvolvidos para o **PJE 2G do TRF1**
- É necessário estar autenticado no sistema antes de executar
- Ajuste os seletores de elementos caso a interface do PJE seja atualizada
- Recomenda-se testar com poucos processos antes de executar em lote

### 📊 Resultados

| Métrica | Antes | Depois |
|---------|-------|--------|
| Tempo por processo | 5-10 min | ~30 seg |
| Processos/hora | 6-12 | 100+ |
| Erros manuais | Frequentes | Raros |

---
