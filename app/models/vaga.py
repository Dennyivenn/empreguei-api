# Inserir vagas com empresa_id
vaga1 = Vaga(titulo="Desenvolvedor Python", descricao="Trabalhar com APIs", empresa_id=usuario1.id, usuario_id=usuario1.id)
vaga2 = Vaga(titulo="Designer UI/UX", descricao="Design para web", empresa_id=usuario1.id, usuario_id=usuario2.id)

session.add_all([vaga1, vaga2])
session.commit()
