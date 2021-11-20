from docker import DockerClient
import docker

def menu():
    print('''
        MENU:

        [1] - Listar Imagens
        [2] - Baixar uma Imagem
        [3] - Apagar Imagem
        [4] - Apagar todas as imagens Imagens
        [5] - Quit
        '''
    )
    return int(input('Escolha uma opção: '))
    
resp = menu()
while (resp != 5):
    if(resp == 1):
        docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')
        list = docker_client.images.list(all=True) 
        print (list)
    if(resp == 2):
        repository = str(input('Digite o repositório da imagem: '))
        name = str(input('Digite o nome da imagem: '))

        docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')
        docker_client.images.pull(repository, name)
        print ('Imagem criada com sucesso! ')

    if(resp == 3):
        name = str(input('Digite o nome da imagem que deseja excluir: '))
        docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')
        docker_client.images.remove(name)
        print ('Imagem excluída com sucesso! ')


    if(resp == 4):    
        docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')
        r = str ('Deseja realmente excluir todas as imagens? ')
        lista = docker_client.images.list(all=True)  
        for image in lista:
            docker_client.images.remove(image)
    resp = menu() 
print ('Programa Finalizado')