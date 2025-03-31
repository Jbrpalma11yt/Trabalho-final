# Manual Técnico - PixeLoucura 

## 📌 Introdução
PixeLoucura é um editor de imagem que permite aos utilizadores realizar edições avançadas de forma intuitiva e eficiente. Este documento fornece informações técnicas detalhadas sobre o desenvolvimento do aplicativo, incluindo os métodos implementados, os desafios enfrentados durante a sua criação e as soluções adotadas ao longo do processo.
---

## ⚙️ Métodos Implementados  

O **PixeLoucura** foi desenvolvido utilizando a framework **Flask**, permitindo a criação de uma aplicação web para edição de imagens. Os principais métodos implementados incluem:  

### 🗂️ 1️⃣ Configuração do Ambiente e Diretórios  
O sistema define um diretório específico para o armazenamento de imagens enviadas pelos utilizadores. A configuração é realizada através da variável `UPLOAD_FOLDER`, garantindo que todas as imagens sejam armazenadas na pasta `static/uploads`. Além disso, são definidos os formatos de ficheiros suportados, como **PNG, JPG, JPEG e GIF**, através do conjunto `ALLOWED_EXTENSIONS`.  

### 📤 2️⃣ Validação e Processamento de Upload de Imagens  
A função `allowed_file(filename)` verifica se o ficheiro enviado possui uma extensão permitida, garantindo a integridade dos dados processados. No endpoint principal (`index()`), é realizada a validação e o armazenamento seguro do ficheiro utilizando `secure_filename()`, prevenindo vulnerabilidades como **path traversal attacks**.  

### 🎛️ 3️⃣ Implementação de Ajustes de Imagem  
O sistema permite ajustes de diferentes parâmetros da imagem, tais como:  
- **Brilho (`brightness`)**: Controla a intensidade da luz na imagem.  
- **Contraste (`contrast`)**: Ajusta a diferença entre áreas claras e escuras.  
- **Desfoque (`blur`)**: Aplica um efeito de suavização para reduzir detalhes.  
- **Saturação (`saturation`)**: Modifica a intensidade das cores na imagem.  
- **Tons sépia (`sepia`)**: Aplica um efeito envelhecido na fotografia.  
- **Escala de cinza (`grayscale`)**: Converte a imagem para tons de preto e branco.  

Todos esses valores são armazenados na estrutura `settings`, permitindo a recuperação e modificação das configurações conforme necessário.  

### 🌐 4️⃣ Interação com a Interface Web  
A aplicação utiliza o **Flask** para renderizar o template `index.html`, onde os utilizadores podem carregar imagens e ajustar os parâmetros visuais. O método `render_template()` recebe os valores de configuração e os repassa para o frontend, garantindo que as alterações feitas pelo utilizador sejam refletidas na interface gráfica.  

### 🚀 5️⃣ Execução da Aplicação  
O aplicativo é iniciado através do bloco `if __name__ == "__main__":`, garantindo que o servidor Flask seja executado corretamente no modo de depuração (`debug=True`), facilitando o desenvolvimento e a deteção de erros durante a execução.  

---

## 🛠️ Funcionalidades  

- 🖌️ **Edição de Imagem**: Redimensionar, cortar, ajustar cores, etc.  
- 🎨 **Filtros e Efeitos**: Aplicação de filtros pré-definidos.  
- 🔍 **Zoom e Navegação**: Ferramentas para visualização detalhada.  
- 📂 **Suporte a Formatos**: PNG, JPEG, BMP, etc.  

---


## 🛠️ Solução de Problemas
### ❌ O aplicativo não abre
- Certifique-se de que tem os requisitos mínimos.
- Tente reinstalar o aplicativo.
- Verifique se há atualizações do sistema operativo.
- Verifique que tem o  módulo **flask** instaldo no programa do Visual Code 

### 🖼️ Imagens não carregam
- Confirme se o formato da imagem é suportado.
- Verifique se o ficheiro está corrompido.

---
### 📌 Instalação do Flask  
Para garantir que o Flask esteja instalado no seu ambiente Python, utilize o seguinte comando:  

```sh
pip install flask
``` 
### 3️⃣ Usar o Python correto
Se a instalação foi feita, mas o erro persiste, pode ser que esteja a usar uma versão errada do Python. Para verificar:
```sh
python -m pip install flask
```
ou, se estiver em Windows:
```sh
py -m pip install flask
```

---
## 📞 Criadores 
- Criadores do site :Afonso Palma/  Rafael Ascençao /Rodrigo Ramos 
- Ano Ecolar : 12º
- Turma : GPSI
- Escola :Bento de Jesus Caraça Barreiro
