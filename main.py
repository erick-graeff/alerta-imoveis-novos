from json import loads
from pathlib import Path

from requests import post

LUGARES_DISPONIVEIS = "lugares_disponiveis.csv"


class Imovel:
    def __init__(  # noqa: PLR0913
        self,
        imovel_id: str,
        endereco: str,
        bairro: str,
        quartos: int,
        banheiros: int,
        area_total: float,
        valor_considerado: float,
        situacao: str,
        foto_principal: str,
        link: str,
    ) -> None:
        self.imovel_id = imovel_id
        self.endereco = endereco
        self.bairro = bairro
        self.quartos = quartos
        self.banheiros = banheiros
        self.area_total = area_total
        self.valor_considerado = valor_considerado
        self.situacao = situacao
        self.link = link


def main() -> None:
    apolar_url = "https://uiyek91vqe.execute-api.us-east-1.amazonaws.com/prod/properties/search/main"
    body = {
        "business": "Locacao",
        "business_subfilter": "Mensal",
        "reference": "",
        "city": "Curitiba",
        "country": "Brasil",
        "district": ["Centro", "Cajuru", "Cristo Rei", "Jardim Botânico", "Jardim Das Américas", "Capão Da Imbuia"],
        "property_type": ["Apartamento", "Studio", "Kitnet"],
        "property_type_combo": [],
        "bedrooms": [],
        "garage": [],
        "bathrooms": [],
        "price_max": "R$ 1.600,00",
        "price_min": "R$ 0,00",
        "area_max": "0,00 m²",
        "area_min": "0,00 m²",
        "address": None,
        "address_number": None,
        "open_search": "",
        "in_condominium": False,
        "include_condominium_price": "true",
        "conveniences": [],
        "recreation": [],
        "facilities": [],
        "rooms": [],
        "idLoja": None,
        "mensal": None,
        "showStoreImmobiles": True,
        "order": "price_desc",
        "size": 200,
        "fields": [
            "IsFeiraoApolar",
            "IsLocacao",
            "nomeEvento",
            "tipo",
            "transacao",
            "finalidade",
            "cidade",
            "bairro",
            "referencia",
            "Quartos",
            "condominio",
            "garagem",
            "dormitorios",
            "areaterreno",
            "area_total",
            "banheiro",
            "ValorAnterior",
            "valor_considerado",
            "situacao",
            "FimPromocao",
            "foto_principal",
            "endereco",
            "linksite",
            "Selo",
            "finalidade",
            "popup_fotos",
            "descricao",
            "vlrcondominio",
            "lojacelular",
            "lojatelefone",
            "idtipomoeda",
        ],
        "price": [0, 1600],
        "area": [0, 0],
    }
    try:
        response = post(apolar_url, json=body, timeout=15)
        # with Path("initial_resp.json").open() as f:
        #     response = loads(f.read())
        print(response.text)
        # with Path(LUGARES_DISPONIVEIS).open() as f:
        #     lugares_disponiveis = f.readlines()
        # imoveis_novos = [imovel for imovel in response if imovel["referencia"] not in lugares_disponiveis]

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
