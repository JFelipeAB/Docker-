from docker import DockerClient

docker_client = DockerClient(base_url='tcp://localhost:2375', version='auto')

# realizar download da imagem
docker_client.images.pull('nginx')

#docker_client.images.pull('nginx')


# Listar todas as imagens
list = docker_client.images.list(all=True)
print(list)

# 