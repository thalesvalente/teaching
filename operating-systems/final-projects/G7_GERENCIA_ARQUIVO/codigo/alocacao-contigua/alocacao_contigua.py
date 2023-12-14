class AlocacaoContigua:
    def __init__(self, disk_space):
        self.disk_space = disk_space
        self.disk = [0] * disk_space  # Representação do disco como uma lista de 0s (espaços vazios)
        self.allocated_blocks = {}  # Dicionário para armazenar os blocos alocados

    def allocate_first_fit(self, file_name, file_size):
        start = -1
        count = 0
        for i, block in enumerate(self.disk):
            if block == 0:  # Verifica se o bloco está livre
                if start == -1:
                    start = i  # Marca o início do bloco livre
                count += 1  # Incrementa o contador de blocos livres
                if count == file_size:
                    for j in range(start, start + file_size):
                        self.disk[j] = 1  # Marca os blocos como alocados
                    self.allocated_blocks[file_name] = {'start': start, 'size': file_size}
                    return True  # Arquivo alocado com sucesso
            else:
                start = -1
                count = 0

        return False  # Não há espaço suficiente para alocar o arquivo
    
    def allocate_best_fit(self, file_name, file_size):
        indice_start = -1  # Índice de início da alocação
        best_fit_size = self.disk_space + 1  # Inicializando com um tamanho maior que o espaço disponível

        current_start = -1  # Início do bloco atualmente verificado
        current_size = 0  # Tamanho do bloco atual

        # Percorre os blocos do disco
        for i, block in enumerate(self.disk):
            if block == 0:  # Verifica se o bloco está livre
                if current_start == -1:
                    current_start = i  # Marca o início do bloco livre
                current_size += 1  # Incrementa o tamanho do bloco livre

                # Modificação na condição para encontrar o melhor encaixe
                if current_size >= file_size and current_size < best_fit_size:
                    if (i + file_size >= len(self.disk) or self.disk[i + file_size] == 1):
                        indice_start = current_start
                        best_fit_size = current_size  # Atualiza o melhor tamanho encontrado

            else:  # Se o bloco não estiver livre, reinicia a busca
                current_start = -1
                current_size = 0

        # Se houver espaço para alocar o arquivo
        if indice_start != -1:
            # Marca os blocos como alocados
            for i in range(indice_start, indice_start + file_size):
                self.disk[i] = 1
            # Registra a alocação na estrutura de dados
            self.allocated_blocks[file_name] = {'start': indice_start, 'size': file_size}
            return True  # Arquivo alocado com sucesso

        return False  # Não há espaço suficiente para alocar o arquivo


    
    def allocate_worst_fit(self, file_name, file_size):
        indice_start = -1  # Índice de início da alocação
        worst_fit_size = 0  # Inicialização do pior tamanho para comparação
    
        current_start = -1  # Início do bloco atualmente verificado
        current_size = 0  # Tamanho do bloco atual
    
        # Percorre os blocos do disco
        for i, block in enumerate(self.disk):
            if block == 0:  # Verifica se o bloco está livre
                if current_start == -1:
                    current_start = i  # Marca o início do bloco livre
                current_size += 1  # Incrementa o tamanho do bloco livre
    
                # Verifica se o tamanho atual é maior que o pior tamanho anterior
                # E se o espaço pode acomodar o arquivo ou já está ocupado adiante
                if current_size >= file_size and current_size > worst_fit_size and (i + file_size >= len(self.disk) or self.disk[i + file_size] == 1):
                    indice_start = current_start
                    worst_fit_size = current_size  # Atualiza o pior tamanho encontrado
    
            else:  # Se o bloco não estiver livre, reinicia a busca
                current_start = -1
                current_size = 0
    
        # Se houver espaço para alocar o arquivo
        if indice_start != -1:
            # Marca os blocos como alocados
            for i in range(indice_start, indice_start + file_size):
                self.disk[i] = 1
            # Registra a alocação na estrutura de dados
            self.allocated_blocks[file_name] = {'start': indice_start, 'size': file_size}
            return True  # Arquivo alocado com sucesso
    
        return False  # Não há espaço suficiente para alocar o arquivo

            
    def deallocate_blocks(self, file_name):
        if file_name in self.allocated_blocks:
            start = self.allocated_blocks[file_name]['start']
            size = self.allocated_blocks[file_name]['size']
            for i in range(start, start + size):
                self.disk[i] = 0  # Marca os blocos como desalocados
            del self.allocated_blocks[file_name]  # Remove o arquivo do dicionário de blocos alocados
            return True  # Blocos desalocados com sucesso
        else:
            return False  # Arquivo não encontrado ou não está alocado
    
    def display_disk_allocation(self):
        for i in range(self.disk_space):
            if self.disk[i] == 0:
                print(f"Bloco {i}: Livre")
            else:
                allocated_file = None
                for file_name, data in self.allocated_blocks.items():
                    start = data['start']
                    size = data['size']
                    if i in range(start, start + size):
                        allocated_file = file_name
                        break

                if allocated_file:
                    print(f"Bloco {i}: Alocado para '{allocated_file}'")
                else:
                    print(f"Bloco {i}: Alocado para um arquivo desconhecido (Possivel inconsistência)")