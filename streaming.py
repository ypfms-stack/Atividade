class User:
    def __init__(self, nome, email, senha, cartao):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cartao = cartao
#instanciando
user1 = User("yasmin", "yayah14f@gmail.com", 231202, 1111)
user2 = User("Poliana", "hehe@email", 1234, 6464)
user3 = User("Joyce", "wiiill@email", 5678, 6767)

class Filme:
    def __init__(self, titulo, genero, classificacao, nota, duracao):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.nota = nota
        self.duracao = duracao
#instanciando

filme1 = Filme("IT: A Coisa", "terror", 16, 8.5, 125)
filme2 = Filme("The Turning", "Terror/Drama", 14, 3.5, 154)
filme3 = Filme("Given Movie 3: Umi E", 16, 7.5, 140)

    
class Serie:
    def __init__(self, titulo, genero, classificacao, temporadas, episodios):
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.temporadas = temporadas
        self.episodios = episodios
#instanciando
serie1 = Serie("Owari no Seraph", "Fantasia&Anime", 2015, 2, 24)
serie2 = Serie("Given", "Drama&Anime", 2016, 1, 11)
serie3 = Serie("Julie and the Phantoms", "musical", "L", 1, 9)


        