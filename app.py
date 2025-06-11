import requests

def converter_moeda():
    try:
        moeda_origem = input("Digite a moeda de origem (ex: BRL): ").upper()
        moeda_destino = input("Digite a moeda de destino (ex: USD): ").upper()
        valor_str = input(
            f"Digite o valor em {moeda_origem} a ser convertido: ")

        valor = float(valor_str.replace(',', '.'))

        url = f"https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/{moeda_origem}"

        url_demo = f"https://open.er-api.com/v6/latest/{moeda_origem}"

        print("\nBuscando as taxas de câmbio mais recentes...")
        response = requests.get(url_demo)
        response.raise_for_status()

        dados = response.json()

        if dados["result"] == "success":
            if moeda_destino in dados["rates"]:
                taxa_conversao = dados["rates"][moeda_destino]
                valor_convertido = valor * taxa_conversao
                print("\n -Resultado da Conversão-")
                print(
                    f"Taxa de câmbio: 1 {moeda_origem} = {taxa_conversao} {moeda_destino}")
                print(
                    f"Valor convertido: {valor_convertido:.2f} {moeda_destino}")
                print("----------------------------")
            else:
                print(
                    f"Erro: A moeda de destino '{moeda_destino}' não foi encontrada.")
        else:
            print("Erro ao obter as taxas de câmbio.")

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão com a API: {e}")
    except ValueError:
        print("Erro: O valor digitado não é um número válido.")
    except KeyError:
        print(
            f"Erro: A moeda de origem '{moeda_origem}' pode ser inválida ou não suportada pela API.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == '__main__':
    converter_moeda()

