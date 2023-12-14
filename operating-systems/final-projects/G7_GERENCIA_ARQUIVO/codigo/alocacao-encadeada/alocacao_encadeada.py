class Node:
    def __init__(self, index):
        self.index = index
        self.next = None
        self.allocated = False  # Flag para marcar se o bloco está alocado


class AlocacaoEncadeada:
    def __init__(self, disk_space):
        self.disk_space = disk_space
        self.disk = [Node(i) for i in range(disk_space)]  # Lista de Nodes representando o disco
        for i in range(disk_space - 1):
            self.disk[i].next = self.disk[i + 1]  # Configura os ponteiros para os próximos blocos livres

        self.free_head = self.disk[0]  # O primeiro bloco livre é o início da lista encadeada de blocos livres
        self.allocated_blocks = {}  # Dicionário para armazenar os blocos alocados

    def allocate_file(self, file_name, file_size):
        if file_size > self.disk_space:
            return False  # O arquivo é maior do que o espaço total do disco

        current_block = self.free_head
        previous_block = None
        blocks_allocated = 0
        allocated_indices = []

        while current_block or previous_block:
            if blocks_allocated == file_size:
                # Espaço suficiente encontrado para alocar o arquivo
                for index in allocated_indices:
                    self.disk[index].allocated = True  # Marca os blocos como alocados
                self.allocated_blocks[file_name] = allocated_indices

                if previous_block:
                    previous_block.next = current_block  # Remove os blocos alocados da lista encadeada de livres
                else:
                    self.free_head = current_block.next

                return True
            if current_block is not None:
                if not current_block.allocated:
                # Se o bloco já estiver alocado, reinicia a contagem de blocos
                #blocks_allocated = 0
                #allocated_indices = []
                    allocated_indices.append(current_block.index)
                    blocks_allocated += 1 
                previous_block = current_block
                current_block = current_block.next
            else:
                return False# Não há espaço contíguo suficiente para alocar o arquivo
        return False 

    def deallocate_blocks(self, file_name):
        if file_name in self.allocated_blocks:
            indices = self.allocated_blocks[file_name]
            for index in indices:
                self.disk[index].allocated = False  # Marca os blocos como livres novamente

            last_free_block = self.disk[indices[-1]]
            self.free_head = self.disk[indices[0]]

            del self.allocated_blocks[file_name]  # Remove o arquivo do dicionário de blocos alocados
            return True  # Blocos desalocados com sucesso
        else:
            return False  # Arquivo não encontrado ou não está alocado

    def display_disk_allocation(self):
        current_block = self.disk[0]
        while current_block:
            if current_block.allocated:
                print(f"Bloco {current_block.index}: Alocado")
            else:
                print(f"Bloco {current_block.index}: Livre")
            current_block = current_block.next
        print("-------------------------")
        for file_name, indices in self.allocated_blocks.items():
            for index in indices:
                print(f"Bloco {index}: Alocado para '{file_name}'")