from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.revendedor import Revendedor
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole


def inserir_aditivo_nutritivo() -> None:

    print('Cadastrando Aditivo Nutritivo ...\n')

    nome: str = input('Nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Fórmula quimica do Aditivo Nutritivo: ')

    data: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(data)
        session.commit()

    print('Aditivo Nutritivo cadastrado com sucesso ...')
    print(f'ID: {data.id} ...')
    print(f'Data: {data.created} ...\n')


def inserir_sabor() -> None:

    print('Cadastrando Sabor ...\n')

    nome: str = input('Nome do Sabor: ')

    data: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(data)
        session.commit()

    print('Sabor cadastrado com sucesso ...')
    print(f'ID: {data.id} ...')
    print(f'Data: {data.created} ...\n')


def inserir_tipo_embalagem() -> None:

    print('Cadastrando Tipo de Embalagem ...\n')

    nome: str = input('Nome do Tipo Embalagem: ')

    data: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(data)
        session.commit()

    print('Tipo Embalagem cadastrado com sucesso ...')
    print(f'ID: {data.id} ...')
    print(f'Data: {data.created} ...\n')


def inserir_tipo_picole() -> None:

    print('Cadastrando Tipo de Picolé ...\n')

    nome: str = input('Nome do Tipo de Picolé: ')

    data: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(data)
        session.commit()

    print('Tipo Picolé cadastrado com sucesso ...')
    print(f'ID: {data.id} ...')
    print(f'Data: {data.created} ...\n')


def inserir_ingrediente() -> None:

    print('Cadastrando Ingrediente ...\n')

    nome: str = input('Nome do Ingrediente: ')

    data: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(data)
        session.commit()

    print('Ingrediente cadastrado com sucesso ...')
    print(f'ID: {data.id} ...')
    print(f'Data: {data.created} ...\n')


def inserir_conservante() -> None:

    print('Cadastrando Conservante ...\n')

    nome: str = input('Nome do Conservante: ')
    descricao: str = input('Descrição do Conservante: ')

    data: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(data)
        session.commit()

    print('Ingrediente cadastrado com sucesso ...')
    print(f'ID: {data.id} ...')
    print(f'Data: {data.created} ...\n')


def inserir_revendedor() -> Revendedor:

    print('Cadastrando Revendedor ...\n')

    cnpj: str = input('CNPJ do Revendedor: ')
    razao_social: str = input('Razão Social: ')
    contato: str = input('Contato do Revendedor: ')

    data: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(data)
        session.commit()

    return data


if __name__ == '__main__':
    # inserir_aditivo_nutritivo()
    # inserir_sabor()
    # inserir_tipo_embalagem()
    # inserir_tipo_picole()
    # inserir_ingrediente()
    # inserir_conservante()
    print(inserir_revendedor())
