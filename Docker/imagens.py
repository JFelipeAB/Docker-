from docker import DockerClient
import docker



 
    

def criar(image, tag):
    docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')
    docker_client.images.pull(image,tag)

def apagar(id):
    docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')
    docker_client.images.get(id).remove()
    
def apagarTodos():
    docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')
    for image in listar():
        docker_client.images.remove(image)
#resp = ''   
def menu():
    print('''
        MENU:

        [1] - Listar Imagens
        [2] - Baixar uma Imagem
        [3] - Apagar Imagem
        [4] - Apagar todas as imagens Imagens
        '''
    )
    return int(input('Escolha uma opção: '))
    
resp = menu()

if(resp == 1):
    docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')
    list = docker_client.images.list(all=True) 
    print (list)
if(resp == 2):
    tag = str(input('Digite o nome da imagem: '))
    docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')
    docker_client.images.pull(tag)
    print ('Imagem criada com sucesso! ')

if(resp == 3):
    name = str(input('Digite o nome da imagem que deseja excluir: '))
    docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')
    docker_client.images.remove(name)
    print ('Imagem excluída com sucesso! ')


if(resp == 4):    
    docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')
    lista = docker_client.images.list(all=True)  
    for image in lista:
        docker_client.images.remove(image)

print ('Programa Finalizado')